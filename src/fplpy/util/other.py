from typing import Any


def filter_dict(data: dict[str, Any], allowed_keys: list[str]) -> dict[str, Any]:
    """Filter the dictionary to only include allowed keys."""
    return {key: data[key] for key in allowed_keys if key in data}
