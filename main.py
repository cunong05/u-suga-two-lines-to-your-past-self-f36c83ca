#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line entry text to /output/entry.txt, byte-exact,
with no trailing newline. Standard library only, no network.
"""

import hashlib
import os

ENTRY = (
    "Dear past me: yes, that 2 a.m. code ships to production, "
    "and no, the tests will not save you.\n"
    "Buy the bigger hard drive. Future you is out of space and out of excuses."
)


def save_entry() -> str:
    """Write ENTRY to /output/entry.txt and return its sha256 hex digest."""
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return path


def verify_entry(path: str) -> str:
    """Read the file back and compare byte-for-byte with ENTRY.

    Raises SystemExit on any mismatch (including a trailing newline).
    Returns the sha256 hex digest of the bytes on disk.
    """
    with open(path, "rb") as f:
        data = f.read()
    expected = ENTRY.encode("utf-8")
    if data != expected:
        raise SystemExit(
            f"read-back mismatch: wrote {len(expected)} bytes, "
            f"read back {len(data)} bytes"
        )
    if data.endswith(b"\n"):
        raise SystemExit("read-back mismatch: trailing newline present")
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    path = save_entry()
    digest = verify_entry(path)
    print(f"wrote {path}")
    print("sha256:", digest)


if __name__ == "__main__":
    main()
