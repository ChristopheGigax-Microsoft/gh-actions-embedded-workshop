"""Package already-built reference firmware; optional SBOM before publication."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
# REQUIRED: set this to your project path and adapt INVENTORY to its actual sources.
SOURCE = ROOT / "path/to/your/project"
INVENTORY = (
    "src/monitor.c",
    "include/monitor.h",
    "platform/main.c",
    "platform/startup.S",
    "platform/memory.ld",
)


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def require_passing_tests(path):
    tree = ET.parse(path)
    suites = list(tree.getroot().iter("testsuite"))
    if not suites or sum(int(suite.get("tests", "0")) for suite in suites) < 1:
        raise ValueError("No executed tests in report")
    if any(int(suite.get(field, "0")) for suite in suites for field in ("failures", "errors", "skipped")):
        raise ValueError("Failed, errored or skipped tests prevent firmware packaging")


def make_sbom(commit, elf_sha, created):
    files = []
    for number, name in enumerate(INVENTORY, 1):
        files.append({
            "SPDXID": f"SPDXRef-File-{number}",
            "fileName": f"./{name}",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256(SOURCE / name)},
                {"algorithm": "SHA1", "checksumValue": hashlib.sha1((SOURCE / name).read_bytes()).hexdigest()},
            ],
            "licenseConcluded": "NOASSERTION",
            "copyrightText": "NOASSERTION",
        })
    return {
        "spdxVersion": "SPDX-2.3",
        "dataLicense": "CC0-1.0",
        "SPDXID": "SPDXRef-DOCUMENT",
        "name": "workshop-monitor-firmware",
        "documentNamespace": f"https://spdx.org/spdxdocs/workshop-monitor-{commit}-{elf_sha}",
        "creationInfo": {"creators": ["Tool: workshop-fixture-sbom-1.0"], "created": created},
        "documentDescribes": ["SPDXRef-Firmware"],
        "packages": [{
            "SPDXID": "SPDXRef-Firmware",
            "name": "workshop-monitor",
            "versionInfo": commit,
            "downloadLocation": "NOASSERTION",
            "filesAnalyzed": True,
            "packageVerificationCode": {
                "packageVerificationCodeValue": hashlib.sha1(
                    "".join(sorted(hashlib.sha1((SOURCE / name).read_bytes()).hexdigest()
                                   for name in INVENTORY)).encode("ascii")
                ).hexdigest()
            },
            "checksums": [{"algorithm": "SHA256", "checksumValue": elf_sha}],
            "licenseConcluded": "NOASSERTION",
            "licenseDeclared": "NOASSERTION",
            "copyrightText": "NOASSERTION",
            "comment": "Reference source inventory only. No external runtime libraries linked (-nostdlib). "
                       "Build tools are recorded separately in manifest.json. "
                       "Not a general customer dependency scanner or vulnerability assessment.",
        }],
        "files": files,
        "relationships": [
            {"spdxElementId": "SPDXRef-DOCUMENT", "relationshipType": "DESCRIBES",
             "relatedSpdxElement": "SPDXRef-Firmware"},
            *({"spdxElementId": "SPDXRef-Firmware", "relationshipType": "CONTAINS",
               "relatedSpdxElement": item["SPDXID"]} for item in files),
        ],
    }


def verify_package(directory):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    entries = {}
    for line in (directory / "SHA256SUMS").read_text(encoding="ascii").splitlines():
        digest, name = line.split("  ", 1)
        if name in entries or Path(name).name != name or "/" in name or "\\" in name:
            raise ValueError("Invalid or duplicate checksum filename")
        entries[name] = digest
    expected_files = {"monitor.elf", "monitor.bin", "monitor.map", "manifest.json"}
    if manifest["sbom"]:
        expected_files.add("sbom.spdx.json")
    if set(entries) != expected_files:
        raise ValueError("Checksum inventory does not match selected package contents")
    actual_files = {item.name for item in directory.iterdir()}
    if actual_files != expected_files | {"SHA256SUMS"}:
        raise ValueError("Package contains missing or unexpected files")
    for name, digest in entries.items():
        if sha256(directory / name) != digest:
            raise ValueError(f"Checksum mismatch: {name}")
    for name, digest in manifest["firmware"].items():
        if entries.get(name) != digest:
            raise ValueError(f"Manifest identity mismatch: {name}")
    if manifest["sbom"]:
        from validate_sbom import check_identity
        check_identity(json.loads((directory / "sbom.spdx.json").read_text(encoding="utf-8")),
                       manifest["commit"], manifest["firmware"]["monitor.elf"])
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sbom", action="store_true")
    parser.add_argument("--test-report", type=Path, default=ROOT / "build/host/test-results.xml")
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify:
        manifest = verify_package(args.verify)
        print(f"Verified package for {manifest['commit']}")
        return
    require_passing_tests(args.test_report)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True).strip())
    created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with tempfile.TemporaryDirectory() as temporary:
        staging = Path(temporary)
        firmware = {}
        for name in ("monitor.elf", "monitor.bin", "monitor.map"):
            shutil.copyfile(ROOT / "build/arm" / name, staging / name)
            firmware[name] = sha256(staging / name)
        compiler = subprocess.check_output(["arm-none-eabi-gcc", "--version"], text=True).splitlines()[0]
        cmake = subprocess.check_output(["cmake", "--version"], text=True).splitlines()[0]
        manifest = {
            "commit": commit, "dirty": dirty, "created": created,
            "target": "reference-cortex-m3-not-hardware-validated",
            "toolchain": compiler, "cmake": cmake,
            "sbom": args.sbom, "firmware": firmware,
            "test_report_sha256": sha256(args.test_report),
        }
        (staging / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        if args.sbom:
            from validate_sbom import check_identity, validate
            sbom_path = staging / "sbom.spdx.json"
            sbom_path.write_text(json.dumps(make_sbom(commit, firmware["monitor.elf"], created), indent=2) + "\n",
                                 encoding="utf-8")
            check_identity(validate(sbom_path), commit, firmware["monitor.elf"])
        sums = "".join(f"{sha256(path)}  {path.name}\n" for path in sorted(staging.iterdir()))
        (staging / "SHA256SUMS").write_text(sums, encoding="ascii")
        verify_package(staging)
        destination = ROOT / "dist/firmware"
        destination.mkdir(parents=True, exist_ok=True)
        allowed = {"monitor.elf", "monitor.bin", "monitor.map", "manifest.json", "sbom.spdx.json", "SHA256SUMS"}
        if any(path.name not in allowed or not path.is_file() for path in destination.iterdir()):
            raise ValueError(f"Refusing to overwrite unexpected contents of {destination}")
        for name in allowed:
            target = destination / name
            if target.is_file():
                target.unlink()
        for path in staging.iterdir():
            shutil.copyfile(path, destination / path.name)
    print(f"Verified firmware package: {destination}; dirty source: {dirty}")


if __name__ == "__main__":
    main()
