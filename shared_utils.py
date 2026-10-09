"""Shared utilities for AWS Lambda functions using a Lambda Layer."""

from datetime import datetime, timezone
import json
import requests


def standard_response(status_code: int, data: dict, message: str | None = None) -> dict:
    """Build a consistent API-style response."""
    body = {
        "data": data,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    if message:
        body["message"] = message

    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False, default=str),
    }


def validate_request(data: dict, required_fields: list[str]) -> tuple[bool, str | None]:
    """Check whether required fields exist and are not None."""
    missing_fields = [
        field for field in required_fields
        if field not in data or data[field] is None
    ]

    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"

    return True, None


def log_event(level: str, message: str, **context) -> None:
    """Write a JSON log record that can be queried in CloudWatch Logs."""
    record = {
        "level": level.upper(),
        "message": message,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **context,
    }

    print(json.dumps(record, ensure_ascii=False))


def requests_version() -> str:
    """Return the version of requests provided by the Layer."""
    return requests.__version__
