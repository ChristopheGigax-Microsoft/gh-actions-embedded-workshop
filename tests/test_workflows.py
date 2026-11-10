from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


class DemoWorkflowTests(unittest.TestCase):
    def test_active_build_selects_real_source_for_every_build_and_package(self):
        build = (WORKFLOWS / "firmware-build.yml").read_text(encoding="utf-8")
        self.assertNotIn("path/to/your/project", build)
        for preset in ("host", "arm", "host-quality"):
            self.assertIn(f"cmake --preset {preset} -S samples/reference-firmware", build)
        package_commands = [line.strip() for line in build.splitlines()
                            if "scripts/package_firmware.py" in line]
        self.assertEqual(len(package_commands), 2)
        for command in package_commands:
            self.assertIn("--source samples/reference-firmware", command)
        self.assertEqual(build.count("--no-tests=error"), 2)
        for suffix in ("elf", "bin", "map"):
            self.assertIn(f"test -s build/arm/monitor.{suffix}", build)
        self.assertIn("python3 -m unittest discover -s tests -v", build)

    def test_ci_covers_demo_changes_and_default_branch(self):
        caller = (WORKFLOWS / "ci.yml").read_text(encoding="utf-8")
        self.assertNotIn("path/to/your/project", caller)
        self.assertIn("branches: ['main', 'workshop/**']", caller)
        for path in ("samples/reference-firmware/**", "scripts/**", "tests/**",
                     ".github/workflows/**", "examples/**", "site/**", "README.md"):
            self.assertEqual(caller.count(f"'{path}'"), 2)
        self.assertIn("workflow_dispatch:", caller)
        self.assertIn("uses: ./.github/workflows/firmware-build.yml", caller)

    def test_optional_modules_remain_independent_and_off_by_default(self):
        for name in ("ci.yml", "firmware-build.yml", "release.yml"):
            text = (WORKFLOWS / name).read_text(encoding="utf-8")
            for option in ("quality", "sbom"):
                declaration = re.search(
                    rf"^      {option}:\n(?P<body>(?:        .*\n)+)", text, re.MULTILINE,
                )
                self.assertIsNotNone(declaration, f"{name}: missing {option} input")
                self.assertIn("type: boolean", declaration["body"])
                self.assertIn("default: false", declaration["body"])
        build = (WORKFLOWS / "firmware-build.yml").read_text(encoding="utf-8")
        self.assertIn("if: inputs.quality", build)
        self.assertIn("if: inputs.sbom", build)
        self.assertIn('--fail-under-line 80', build)
        self.assertIn("--flash 16384 --ram 4096", build)
        self.assertLess(build.index("Optional quality gates"), build.index("Upload firmware only"))
        upload = build[build.index("      - name: Upload firmware only"):]
        self.assertNotIn("if: always()", upload)
        self.assertIn("if-no-files-found: error", upload)

    def test_release_consumes_same_run_artifact_with_write_only_in_publisher(self):
        release = (WORKFLOWS / "release.yml").read_text(encoding="utf-8")
        self.assertIn("uses: ./.github/workflows/firmware-build.yml", release)
        self.assertIn("needs: validate", release)
        self.assertIn("name: firmware-${{ github.sha }}", release)
        self.assertIn("--verify release-assets", release)
        self.assertIn('manifest["commit"] != head', release)
        self.assertIn("--verify-tag --prerelease", release)
        self.assertEqual(release.count("contents: write"), 1)
        self.assertIn("contents: write", release.split("  publish:", 1)[1])
