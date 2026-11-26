"""One-star review of the Moon.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no time, no randomness, no network.
"""

import os

ENTRY = "One star. Rises late, floods my bedroom, then vanishes for a week like it owes me rent. Would not orbit again."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
    # The file is written with no trailing newline, so its contents are
    # exactly the 110-character review above.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate is 1-120"
    assert ENTRY.strip() == ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
