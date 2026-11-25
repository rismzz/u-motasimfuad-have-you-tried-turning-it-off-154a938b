#!/usr/bin/env python3
"""Have You Tried Turning It Off? — the hopeless support agent gives up.

The joke: the most famous tech-support line in the world, delivered by
an agent who has said it for six years and never once heard "yes".
The twist is the solidarity at the end — the router and the agent have
both stopped hoping. The customer is desperate, the agent is hopeless,
and the device is a silent third party in the same failed relationship.
The line works because it confesses what every support script hides:
the agent no longer believes in the fix either. It stays under the
200-character cap with room to spare, and it is one sentence of setup
plus one sentence of surrender.
"""

import os
from pathlib import Path

LINE = "Have you tried turning it off and on again? In six years nobody has ever said yes, and the router and I have stopped hoping."

MAX_CHARS = 199


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
