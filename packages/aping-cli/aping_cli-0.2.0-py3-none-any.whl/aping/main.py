import argparse
import sys
import time
from dataclasses import dataclass
from typing import Dict, List, NoReturn, Optional, Union

from prometheus_client import start_http_server

from .ping import PingError, ping

DEFAULT_PING_TIMEOUT_SECONDS = 2
DEFAULT_PROMETHEUS_METRICS_SERVER_PORT = 8000


def format_response_time(response_time: Union[float, None], timeout: int) -> str:
    if response_time is None:
        return f">{timeout}s"
    else:
        ms = round(response_time * 1000, 2)
        return f"{ms:0.2f}ms"


@dataclass(frozen=True)
class Input:
    targets: Dict[str, str]
    timeout: int
    port: int


def parse_args(cli_args: Optional[List[str]] = None) -> Input:
    p = argparse.ArgumentParser(
        description="Ping multiple targets and export results as Prometheus metrics.",
    )
    p.add_argument(
        "targets",
        nargs="+",
        metavar="target",
        help="A target to ping, in the form 'name=ip_address' (e.g., 'google-dns=8.8.8.8')",
    )
    p.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=DEFAULT_PING_TIMEOUT_SECONDS,
        help=f"Maximum ping-completion time in seconds (default: {DEFAULT_PING_TIMEOUT_SECONDS})",
    )
    p.add_argument(
        "-p",
        "--port",
        type=int,
        default=DEFAULT_PROMETHEUS_METRICS_SERVER_PORT,
        help=f"Prometheus metric server port (default: {DEFAULT_PROMETHEUS_METRICS_SERVER_PORT})",
    )
    args = p.parse_args(args=cli_args)

    targets = {}
    for s in args.targets:
        try:
            name, address = s.split("=", 1)
        except ValueError:
            print(
                (
                    f"ERROR: Invalid target: {s!r}. "
                    "Targets must be given in the form 'name=ip_address' (e.g., 'google-dns=8.8.8.8')"
                ),
                file=sys.stderr,
            )
            exit(1)
        targets[name.strip()] = address.strip()

    return Input(targets, args.timeout, args.port)


def main() -> NoReturn:
    args = parse_args()

    start_http_server(args.port)
    print(f"Prometheus metrics server available at http://127.0.0.1:{args.port}", flush=True)

    while True:
        try:
            response_time_by_full_name = ping(args.targets, args.timeout)
        except PingError as e:
            print(f"ERROR: {e}", file=sys.stderr, flush=True)
        else:
            details = [
                f"{full_name}: {format_response_time(response_time_by_full_name[full_name], args.timeout)}"
                for full_name in sorted(response_time_by_full_name.keys())
            ]
            print(", ".join(details), flush=True)

        time.sleep(1)


if __name__ == "__main__":
    main()
