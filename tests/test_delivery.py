import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_size import parse_size, within_budget
from package_firmware import make_sbom, require_passing_tests, verify_package
from validate_sbom import check_identity


class SizeTests(unittest.TestCase):
    def test_exact_budget_passes_and_one_byte_over_fails(self):
        report = parse_size("text data bss dec hex filename\n100 20 30 150 96 image.elf\n")
        self.assertEqual((report["flash"], report["ram"]), (120, 50))
        self.assertTrue(within_budget(report, 120, 50))
        self.assertFalse(within_budget(report, 119, 50))
        self.assertFalse(within_budget(report, 120, 49))

    def test_malformed_report_and_negative_budget_fail(self):
        with self.assertRaises(ValueError):
            parse_size("no report")
        with self.assertRaises(ValueError):
            within_budget({"flash": 0, "ram": 0}, -1, 0)


class TestEvidenceTests(unittest.TestCase):
    def check_report(self, text):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tests.xml"
            path.write_text(text, encoding="utf-8")
            require_passing_tests(path)

    def test_executed_pass_is_required(self):
        self.check_report('<testsuite tests="1" failures="0" errors="0" skipped="0"/>')

    def test_empty_failed_and_skipped_reports_block_packaging(self):
        for attributes in ('tests="0"', 'tests="1" failures="1"',
                           'tests="1" errors="1"', 'tests="1" skipped="1"'):
            with self.subTest(attributes=attributes), self.assertRaises(ValueError):
                self.check_report(f"<testsuite {attributes}/>")


@patch("package_firmware.SOURCE", Path(__file__).resolve().parents[1] / "samples" / "reference-firmware")
class InventoryTests(unittest.TestCase):
    def test_explicit_source_overrides_customer_placeholder(self):
        source = Path(__file__).resolve().parents[1] / "samples" / "reference-firmware"
        with patch("package_firmware.SOURCE", source / "missing"):
            document = make_sbom("a" * 40, "b" * 64, "2026-01-01T00:00:00Z", source)
        check_identity(document, "a" * 40, "b" * 64)
        self.assertEqual(document["files"][0]["checksums"][0]["checksumValue"],
                         hashlib.sha256((source / "src/monitor.c").read_bytes()).hexdigest())

    def test_identity_relationships_and_unknown_licenses(self):
        document = make_sbom("a" * 40, "b" * 64, "2026-01-01T00:00:00Z")
        check_identity(document, "a" * 40, "b" * 64)
        self.assertEqual(document["packages"][0]["licenseDeclared"], "NOASSERTION")
        self.assertEqual(len(document["files"]), 5)

    def test_wrong_commit_elf_and_relationship_are_rejected(self):
        document = make_sbom("a" * 40, "b" * 64, "2026-01-01T00:00:00Z")
        with self.assertRaises(ValueError):
            check_identity(document, "c" * 40, "b" * 64)
        with self.assertRaises(ValueError):
            check_identity(document, "a" * 40, "c" * 64)
        invalid = copy.deepcopy(document)
        invalid["relationships"][0]["relatedSpdxElement"] = "SPDXRef-Unknown"
        with self.assertRaises(ValueError):
            check_identity(invalid, "a" * 40, "b" * 64)


@patch("package_firmware.SOURCE", Path(__file__).resolve().parents[1] / "samples" / "reference-firmware")
class PackageTests(unittest.TestCase):
    def make_package(self, directory, sbom):
        firmware = {}
        for name in ("monitor.elf", "monitor.bin", "monitor.map"):
            (directory / name).write_bytes(name.encode())
            firmware[name] = hashlib.sha256(name.encode()).hexdigest()
        manifest = {"commit": "a" * 40, "dirty": False, "sbom": sbom, "firmware": firmware}
        (directory / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        if sbom:
            document = make_sbom(manifest["commit"], firmware["monitor.elf"], "2026-01-01T00:00:00Z")
            (directory / "sbom.spdx.json").write_text(json.dumps(document), encoding="utf-8")
        lines = [f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
                 for path in sorted(directory.iterdir())]
        (directory / "SHA256SUMS").write_text("".join(lines), encoding="ascii")

    def test_package_with_and_without_sbom(self):
        for sbom in (False, True):
            with self.subTest(sbom=sbom), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                self.make_package(directory, sbom)
                self.assertEqual(verify_package(directory)["sbom"], sbom)

    def test_corruption_missing_inventory_and_unexpected_file_fail(self):
        for failure in ("corrupt", "missing", "extra"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                self.make_package(directory, False)
                if failure == "corrupt":
                    (directory / "monitor.bin").write_bytes(b"corrupted")
                elif failure == "missing":
                    (directory / "SHA256SUMS").write_text("", encoding="ascii")
                else:
                    (directory / "unexpected.txt").write_text("not a release asset")
                with self.assertRaises(ValueError):
                    verify_package(directory)
