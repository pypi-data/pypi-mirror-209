import socket
import subprocess
from contextlib import closing
from typing import Dict, List

from dstack.core.job import Job
from dstack.utils.common import PathLike


def get_free_port() -> int:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def allocate_local_ports(jobs: List[Job]) -> Dict[int, int]:
    ports = {}
    for job in jobs:
        ws_logs_port = int(job.env.get("WS_LOGS_PORT"))
        if ws_logs_port:
            ports[ws_logs_port] = get_free_port()
        for app_spec in job.app_specs or []:
            port = job.ports[app_spec.port_index]
            ports[port] = get_free_port()
    return ports


def make_ssh_tunnel_args(
    ssh_key: PathLike, hostname: str, ports: Dict[int, int], backend_type: str
) -> List[str]:
    username = "root"
    if backend_type == "azure":
        # root login is disabled on azure
        # TODO: use non-root for all backends
        username = "ubuntu"
    args = [
        "ssh",
        "-o",
        "StrictHostKeyChecking=no",
        "-o",
        "UserKnownHostsFile=/dev/null",
        "-i",
        str(ssh_key),
        f"{username}@{hostname}",
        "-N",
        "-f",
    ]
    for port_remote, local_port in ports.items():
        args.extend(["-L", f"{local_port}:{hostname}:{port_remote}"])
    return args


def run_ssh_tunnel(
    ssh_key: PathLike, hostname: str, ports: Dict[int, int], backend_type: str
) -> bool:
    args = make_ssh_tunnel_args(ssh_key, hostname, ports, backend_type)
    return (
        subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    )
