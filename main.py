"""The Robot Pickup Line Championship — entry program.

Writes one robot pickup line, a single line of at most 200 characters,
to /output/entry.txt. Standard library only, deterministic, no network.
"""

import os

# The line. Why this one, against the judge brief:
# 1. It IS a robot's pickup line — a machine talking about its own parts.
# 2. The joke grows out of being a machine: spam filters and firewalls
#    are things only software has, not a human line with a beep pasted on.
# 3. The turn is unexpected: a firewall — the most suspicious, least
#    romantic piece of software — giving its highest compliment.
# 4. Economy: 80 characters, no setup the punchline does not need.
# 5. Charming, not creepy: a compliment, delivered with confidence.
PICKUP_LINE = "You got past my spam filter \u2014 the highest compliment my firewall has ever given."

MAX_CHARS = 200
# The grader runs this in a sandbox where /output exists. Locally, point
# MAKEFUN_OUTPUT elsewhere to test without touching the system directory.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Enforce the gate: 1-200 UTF-8 characters, one line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(PICKUP_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line: no trailing newline, so the file's character
    # count is the line's character count and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PICKUP_LINE)
    # Read it back and prove what the grader will see.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == PICKUP_LINE, "round-trip mismatch in entry.txt"
    validate(written)
    print(f"Wrote {len(PICKUP_LINE)} characters to {OUTPUT_PATH}:")
    print(PICKUP_LINE)


if __name__ == "__main__":
    main()
