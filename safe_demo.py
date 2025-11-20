"""
Safe demo for educational purposes. This module simulates key events
and demonstrates handling without capturing real user input.
Do NOT attempt to attach real device hooks or import `pynput` here.
"""

from typing import List


def get_simulated_events() -> List[str]:
    """Return a short list of simulated key events."""
    return ["a", "b", "[space]", "[enter]", "[esc]"]


def print_simulated_events() -> List[str]:
    """Print and return simulated events so tests can inspect them."""
    events = get_simulated_events()
    for e in events:
        print(f"Simulated event: {e}")
    return events


if __name__ == "__main__":
    print("Running safe simulated demo (no real input is recorded).")
    print_simulated_events()
