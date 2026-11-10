"""Optional reference size gate. Adapt size utility/sections/budgets to your target."""

import argparse
import json
from pathlib import Path
import subprocess


def parse_size(output):
    rows = output.strip().splitlines()
    if len(rows) != 2:
        raise ValueError(f"Expected GNU size header and one image row, got: {output}")
    fields = rows[1].split()
    text, data, bss = map(int, fields[:3])
    if min(text, data, bss) < 0:
        raise ValueError("Negative section size")
    return {"text": text, "data": data, "bss": bss, "flash": text + data, "ram": data + bss}


def within_budget(report, flash, ram):
    if flash < 0 or ram < 0:
        raise ValueError("Budgets must be non-negative byte counts")
    return report["flash"] <= flash and report["ram"] <= ram


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("elf", type=Path)
    parser.add_argument("--flash", type=int, required=True)
    parser.add_argument("--ram", type=int, required=True)
    parser.add_argument("--size-tool", default="arm-none-eabi-size")
    args = parser.parse_args()
    output = subprocess.check_output([args.size_tool, str(args.elf)], text=True)
    report = parse_size(output)
    print(json.dumps({**report, "flash_limit": args.flash, "ram_limit": args.ram}, indent=2))
    if not within_budget(report, args.flash, args.ram):
        raise SystemExit("Firmware size gate FAILED: one or more byte budgets exceeded")


if __name__ == "__main__":
    main()
