"""One Line, One Laugh — emit the entry line to /output/entry.txt.

Reads the single funny line from entry.txt next to this script, checks it
is one line of 1-140 characters, and writes it to the grader's output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        raw = f.read()
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    if len(lines) != 1:
        print("entry.txt must hold exactly one non-empty line, found %d"
              % len(lines), file=sys.stderr)
        return 1
    line = lines[0].strip()
    if any(ord(ch) < 32 for ch in line):
        print("entry line holds control characters", file=sys.stderr)
        return 1
    if len(line) > 140:
        print("entry line is %d chars, over the 140 limit" % len(line),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
