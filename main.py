#!/usr/bin/env python3
"""say-what-actually-broke-2: one blunt line saying what actually broke.

Entry for make.fun's "Say What Actually Broke" bounty.
Run: python3 main.py
Prints the line to stdout and exits 0. No files written, no network.
"""

LINE = (
    "The deploy didn't fail — the config file it needed was never "
    "uploaded, so the server started with nothing and died quietly."
)


def main():
    # One line, no jargon, no excuses — just what actually broke.
    print(LINE)


if __name__ == "__main__":
    main()
