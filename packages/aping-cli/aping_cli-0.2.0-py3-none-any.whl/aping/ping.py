from typing import Dict, List, Optional

from multiping import MultiPing
from prometheus_client import Gauge

PING_LATENCY_SECONDS = Gauge("ping_latency_seconds", "Latency (gauge)", ["target"])


class PingError(Exception):
    pass


def ping(target_by_name: Dict[str, str], timeout: int) -> Dict[str, Optional[float]]:
    name_by_target = {target: name for name, target in target_by_name.items()}
    targets = sorted(target_by_name.values())

    res = _multi_ping(targets, timeout_seconds=timeout)

    res_by_full_name = {f"{name_by_target[target]} ({target})": response_time for target, response_time in res.items()}
    for full_name, response_time in res_by_full_name.items():
        value = response_time or timeout
        PING_LATENCY_SECONDS.labels(full_name).set(value)

    return res_by_full_name


def _multi_ping(targets: List[str], timeout_seconds: int = 1) -> Dict[str, Optional[float]]:
    try:
        mp = MultiPing(targets)
    except Exception as e:
        raise PingError(f"Something went wrong while trying to ping: {e}") from e

    resolved_targets = mp._dest_addrs
    target_by_resolved_target = dict(zip(resolved_targets, targets))

    try:
        mp.send()
        responses, no_responses = mp.receive(timeout_seconds)
    except Exception as e:
        raise PingError(f"Something went wrong while trying to ping: {e}") from e

    res = {
        target_by_resolved_target[resolved_target]: response_time_seconds
        for resolved_target, response_time_seconds in responses.items()
    }

    for resolved_target in no_responses:
        target_by_resolved_target[resolved_target] = None

    return res
