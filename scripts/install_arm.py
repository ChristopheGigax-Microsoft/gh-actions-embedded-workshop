"""Install the reference compiler locally; customers must adapt to their target."""

import hashlib
import os
from pathlib import Path
import platform
import sys
import tarfile
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "15.2.1-1.1"
ARCHIVES = {
    ("Linux", "x86_64"): (
        "linux-x64.tar.gz",
        "da6a49ad4003944b823c6c93702a8787c922ab34bd7e918ec0eaf6933a9b1ff6",
    ),
    ("Windows", "AMD64"): (
        "win32-x64.zip",
        "bae6a3d1667697ce750c3b13d6d26d80973ecedc2cc87bf04869e83447fd93ea",
    ),
}


def main():
    key = (platform.system(), platform.machine())
    if key not in ARCHIVES:
        sys.exit(f"Unsupported reference host {key}; install your approved target compiler manually.")
    suffix, digest = ARCHIVES[key]
    name = f"xpack-arm-none-eabi-gcc-{VERSION}-{suffix}"
    url = f"https://github.com/xpack-dev-tools/arm-none-eabi-gcc-xpack/releases/download/v{VERSION}/{name}"
    tools = ROOT / ".tools"
    tools.mkdir(exist_ok=True)
    destination = tools / f"xpack-arm-none-eabi-gcc-{VERSION}"
    if destination.exists():
        sys.exit(f"{destination} already exists. Reuse it, or remove that specific installation before reinstalling.")
    with tempfile.TemporaryDirectory() as temporary:
        archive = Path(temporary) / name
        urllib.request.urlretrieve(url, archive)
        with archive.open("rb") as stream:
            actual = hashlib.file_digest(stream, "sha256").hexdigest()
        if actual != digest:
            sys.exit(f"Compiler checksum mismatch: expected {digest}, got {actual}")
        if suffix.endswith(".zip"):
            with zipfile.ZipFile(archive) as package:
                for member in package.infolist():
                    resolved = (tools / member.filename).resolve()
                    if not resolved.is_relative_to(tools.resolve()):
                        sys.exit("Unsafe archive member")
                package.extractall(tools)
        else:
            with tarfile.open(archive) as package:
                package.extractall(tools, filter="data")
    compiler = destination / "bin" / ("arm-none-eabi-gcc.exe" if os.name == "nt" else "arm-none-eabi-gcc")
    if not compiler.is_file():
        sys.exit(f"Compiler missing after extraction: {compiler}")
    print(compiler.parent)


if __name__ == "__main__":
    main()
