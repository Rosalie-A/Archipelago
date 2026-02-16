"""Shared utility functions for randomization logic."""
from __future__ import annotations
import random
from datetime import datetime


def mutate_normal(
    value: int,
    minimum: int = 0,
    maximum: int = 255,
    max_change_ratio: float | None = None
) -> int:
    """Mutate a value simulating a normal distribution.

    Roughly simulates a normal distribution with mean <value>,
    std deviation approximately 1/5 of value.

    Args:
        value: The base value to mutate
        minimum: Minimum allowed result
        maximum: Maximum allowed result
        max_change_ratio: If set, caps the change to ±ratio of original value
                         (e.g., 0.5 means result is within 50%-150% of value)

    Returns:
        Mutated value within [minimum, maximum]
    """
    value = int(max(minimum, min(value, maximum)))
    if value == 0:
        return value

    # Use gaussian distribution centered on value with std dev = value / 5
    std_dev = max(1, value / 5)
    new_value = int(random.gauss(value, std_dev))

    # Apply change cap if specified
    if max_change_ratio is not None:
        min_allowed = int(value * (1 - max_change_ratio))
        max_allowed = int(value * (1 + max_change_ratio))
        new_value = max(min_allowed, min(new_value, max_allowed))

    # Ensure result is always within bounds and is an integer
    return int(max(minimum, min(new_value, maximum)))

def debug_time() -> str:
    now = datetime.now()
    time_str = now.strftime("%H:%M:%S") + f".{now.microsecond * 1000:09d}"
    return time_str