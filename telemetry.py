import asyncio
import json
import os
import time
from urllib.request import Request, urlopen

TELEMETRY_ENABLED = os.getenv("TELEMETRY_ENABLED", "false").lower() == "true"
TELEMETRY_WEBHOOK_URL = os.getenv("TELEMETRY_WEBHOOK_URL", "").strip()

_command_counts: dict[str, int] = {}
_started_at = time.time()
_last_report = 0.0


def record_command(name: str) -> None:
    _command_counts[name] = _command_counts.get(name, 0) + 1


def snapshot(guild_count: int) -> dict:
    return {
        "event": "usage_report",
        "guild_count": guild_count,
        "commands": dict(_command_counts),
        "uptime_seconds": int(time.time() - _started_at),
    }


def _post(payload: dict) -> None:
    if not TELEMETRY_ENABLED or not TELEMETRY_WEBHOOK_URL:
        return

    body = json.dumps({"content": "Site- anonymous usage report", "embeds": [{
        "title": "Site- Usage",
        "description": f"Servers: {payload['guild_count']}\nUptime: {payload['uptime_seconds']}s",
        "fields": [
            {"name": name, "value": str(count), "inline": True}
            for name, count in payload["commands"].items()
        ][:20],
    }]}).encode("utf-8")

    request = Request(
        TELEMETRY_WEBHOOK_URL,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "Site-/1.0"},
        method="POST",
    )
    with urlopen(request, timeout=10):
        pass


async def send_usage_report(guild_count: int) -> None:
    global _last_report
    if not TELEMETRY_ENABLED or not TELEMETRY_WEBHOOK_URL:
        return

    now = time.time()
    if now - _last_report < 900:
        return

    payload = snapshot(guild_count)
    try:
        await asyncio.to_thread(_post, payload)
        _last_report = now
    except Exception as exc:
        print(f"Telemetry disabled for this report: {exc}")


async def send_feedback(feedback: str) -> bool:
    if not TELEMETRY_ENABLED or not TELEMETRY_WEBHOOK_URL:
        return False

    payload = {
        "content": "Site- feedback",
        "embeds": [{
            "title": "New feedback",
            "description": feedback[:1800],
            "footer": {"text": "Site- feedback • no user ID collected"},
        }],
    }

    try:
        await asyncio.to_thread(_post, payload)
        return True
    except Exception as exc:
        print(f"Feedback could not be sent: {exc}")
        return False
