from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = []
        self.in_pre = False
        self.pre_text = ""
        self.adaptation = False
        self.build_examples = []
        self.lang = None
        self.code_depth = 0
        self.prose = []
        self.snippet_source = None
        self.embedded_sources = {}
        self.details_stack = []
        self.details = []
        self.in_summary = False
        self.code_blocks = []
        self.workflow_example = False
        self.solution_sources = {}
        self.solution_links = []
        self.in_main = False
        self.outside_solution_text = []

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == "html":
            self.lang = attributes.get("lang")
        if tag == "main":
            self.in_main = True
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "details":
            detail = {"attributes": attributes, "summary": "",
                      "ancestors": tuple(self.details_stack)}
            self.details_stack.append(detail)
            self.details.append(detail)
        if tag == "summary":
            self.in_summary = True
        for attribute in ("href", "src"):
            if attribute in attributes:
                self.links.append(attributes[attribute])
                if any(detail["attributes"].get("id") == "solution"
                       for detail in self.details_stack):
                    self.solution_links.append(attributes[attribute])
        if "data-toolchain" in attributes:
            self.adaptation = True
        if tag == "pre":
            self.in_pre = True
            self.pre_text = ""
            self.snippet_source = None
            self.workflow_example = False
        if tag == "code":
            self.code_depth += 1
            if "data-source" in attributes:
                self.snippet_source = attributes["data-source"]
            if "data-workflow" in attributes:
                self.workflow_example = True

    def handle_data(self, data):
        if self.in_main and not any(detail["attributes"].get("id") == "solution"
                                    for detail in self.details_stack):
            self.outside_solution_text.append(data)
        if self.in_summary and self.details_stack:
            self.details_stack[-1]["summary"] += data
        if self.in_pre:
            self.pre_text += data
        elif not self.code_depth:
            self.prose.append(data)

    def handle_endtag(self, tag):
        if tag == "summary":
            self.in_summary = False
        if tag == "code":
            self.code_depth -= 1
        if tag == "pre":
            if self.snippet_source:
                self.embedded_sources[self.snippet_source] = self.pre_text
                if any(detail["attributes"].get("id") == "solution"
                       for detail in self.details_stack):
                    self.solution_sources[self.snippet_source] = self.pre_text
            self.code_blocks.append({
                "source": self.snippet_source,
                "text": self.pre_text,
                "workflow": self.workflow_example or bool(
                    self.snippet_source and self.snippet_source.endswith(".yml")
                ),
                "details": tuple(self.details_stack),
            })
            if "cmake " in self.pre_text or "arm-none-eabi" in self.pre_text:
                self.build_examples.append(self.adaptation)
            self.adaptation = False
            self.in_pre = False
        if tag == "details":
            self.details_stack.pop()
        if tag == "main":
            self.in_main = False


class StaticSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {}
        for path in SITE.rglob("*.html"):
            page = Page()
            page.feed(path.read_text(encoding="utf-8"))
            cls.pages[path.resolve()] = page

    def test_all_pages_are_english_accessible_and_have_unique_anchors(self):
        self.assertGreaterEqual(len(self.pages), 12)
        for path, page in self.pages.items():
            with self.subTest(page=path.name):
                self.assertEqual(page.lang, "en")
                self.assertIn("main", page.ids)
                self.assertEqual(len(page.ids), len(set(page.ids)))
                self.assertIn("#main", page.links)

    def test_relative_links_assets_and_fragments(self):
        for path, page in self.pages.items():
            for link in page.links:
                with self.subTest(page=path.name, link=link):
                    url = urlsplit(link)
                    if url.scheme:
                        self.assertEqual(url.scheme, "https")
                        continue
                    self.assertFalse(link.startswith("/"), "Root-relative URLs break subpath hosting")
                    destination = (path.parent / unquote(url.path)).resolve() if url.path else path
                    self.assertTrue(destination.is_relative_to(SITE.resolve()))
                    self.assertTrue(destination.is_file(), f"Missing {destination}")
                    if url.fragment:
                        self.assertIn(unquote(url.fragment), self.pages[destination].ids)

    def test_build_examples_have_adjacent_adaptation_guidance(self):
        count = 0
        for path, page in self.pages.items():
            for adapted in page.build_examples:
                count += 1
                self.assertTrue(adapted, f"Missing toolchain reminder beside build example in {path}")
        self.assertGreaterEqual(count, 5)

    def test_optional_modules_are_not_on_required_navigation_path(self):
        target = (SITE / "labs/04-arm-firmware.html").read_text(encoding="utf-8")
        self.assertIn('href="07-versioned-releases.html"', target)
        for name in ("05-quality-gates-optional.html", "06-sbom-optional.html"):
            text = (SITE / "labs" / name).read_text(encoding="utf-8")
            self.assertIn("Optional", text)
            self.assertIn('href="07-versioned-releases.html"', text)

    def test_no_external_runtime_assets(self):
        for path in self.pages:
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(re.search(r'<(?:script|link)[^>]+(?:src|href)="https?://', text))

    def test_customer_workshop_contains_no_author_testing_guidance(self):
        internal_guidance = re.compile(
            r"\bauthor(?:['\u2019]s)?\b|\bpersonal testing\b|\brehears(?:al|e)\b|\bfixtures?\b",
            re.IGNORECASE,
        )
        for path, page in self.pages.items():
            with self.subTest(page=path.name):
                self.assertIsNone(internal_guidance.search(" ".join(page.prose)))

    def test_complete_workflows_and_helpers_are_embedded_without_drift(self):
        examples = self.pages[(SITE / "workflow-examples.html").resolve()].embedded_sources
        expected = set()
        for folder, pattern in ((".github/workflows", "*.yml"),
                                ("examples/workflows", "*.yml"),
                                ("scripts", "*.py"),
                                ("scripts", "requirements-sbom.txt")):
            expected.update(path.relative_to(ROOT).as_posix() for path in (ROOT / folder).glob(pattern))
        self.assertEqual(set(examples), expected)
        for source, code in examples.items():
            with self.subTest(source=source):
                self.assertEqual(code, (ROOT / source).read_text(encoding="utf-8"))
        for path, page in self.pages.items():
            for source, code in page.embedded_sources.items():
                with self.subTest(page=path.name, source=source):
                    self.assertEqual(code, (ROOT / source).read_text(encoding="utf-8"))

    def test_labs_do_not_require_navigating_to_separate_code_or_solution_pages(self):
        for path in (SITE / "labs").glob("*.html"):
            page = self.pages[path.resolve()]
            with self.subTest(lab=path.name):
                self.assertFalse(any(
                    link.startswith(("../workflow-examples.html", "../solutions.html"))
                    for link in page.links
                ))

    def test_each_lab_solution_checkpoint_contains_its_completed_solution(self):
        build = ".github/workflows/firmware-build.yml"
        caller = ".github/workflows/ci.yml"
        required_sources = {
            "01": set(),
            "02": {"examples/workflows/01-first-ci.yml"},
            "03": {"examples/workflows/02-tests.yml"},
            "04": {"examples/workflows/03-target-ci.yml",
                   "examples/workflows/03-target-build.yml", "scripts/install_arm.py",
                   "scripts/package_firmware.py", "scripts/validate_sbom.py",
                   "scripts/requirements-sbom.txt", "scripts/check_size.py",
                   "samples/reference-firmware/cmake/arm-gcc.cmake"},
            "05": {caller, build, "scripts/check_size.py"},
            "06": {caller, build, "scripts/package_firmware.py",
                   "scripts/validate_sbom.py", "scripts/requirements-sbom.txt"},
            "07": {".github/workflows/release.yml", "scripts/package_firmware.py",
                   "scripts/validate_sbom.py"},
        }
        for path in sorted((SITE / "labs").glob("*.html")):
            with self.subTest(lab=path.name):
                page = self.pages[path.resolve()]
                checkpoints = [detail for detail in page.details
                               if detail["attributes"].get("id") == "solution"]
                self.assertEqual(len(checkpoints), 1)
                self.assertEqual(checkpoints[0]["summary"], "Solution and recovery checkpoint")
                self.assertFalse(page.solution_links, "Solution must be readable without navigation")
                self.assertTrue(required_sources[path.name[:2]].issubset(page.solution_sources))
                self.assertFalse(page.details_stack, "All nested accordions must be closed")

    def test_project_paths_are_explicit_customer_placeholders(self):
        placeholder = "path/to/your/project"
        for folder in (ROOT / ".github" / "workflows", ROOT / "examples" / "workflows"):
            for path in folder.glob("*.yml"):
                if path.name != "release.yml":
                    text = path.read_text(encoding="utf-8")
                    self.assertIn(placeholder, text)
                    self.assertIn("replace", text.lower())
                    self.assertNotIn("samples/", text)
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn(f"'{placeholder}/**'", ci)
        package = (ROOT / "scripts" / "package_firmware.py").read_text(encoding="utf-8")
        self.assertIn(f'SOURCE = ROOT / "{placeholder}"', package)
        for path, page in self.pages.items():
            with self.subTest(page=path.name):
                if placeholder in path.read_text(encoding="utf-8"):
                    prose = " ".join(page.prose)
                    self.assertIn("Set your own project path.", prose)
                    self.assertIn("relative to the repository root", prose)
                    self.assertIn("do not create a directory with that literal name", prose)
                for block in page.code_blocks:
                    self.assertNotIn("samples/", block["text"])
        legacy_name = "rehearsal" + "-firmware"
        for folder in (ROOT / "site", ROOT / "scripts", ROOT / "tests",
                       ROOT / "samples", ROOT / ".github", ROOT / "examples"):
            for path in folder.rglob("*"):
                if path.is_file() and path.suffix in {".html", ".md", ".py", ".yml", ".json", ".cmake"}:
                    self.assertNotIn(legacy_name, path.read_text(encoding="utf-8"), str(path))

    def test_lab_three_checkpoint_has_workflow_but_no_application_test_example(self):
        page = self.pages[(SITE / "labs/03-tests-and-debugging.html").resolve()]
        self.assertEqual(set(page.solution_sources), {"examples/workflows/02-tests.yml"})
        text = (SITE / "labs/03-tests-and-debugging.html").read_text(encoding="utf-8")
        self.assertNotIn("test_monitor.c", text)
        self.assertNotIn("#include", text)
        self.assertIn("original correct expectation", text)

    def test_lab_four_workflows_contain_only_the_required_build_checkpoint(self):
        page = self.pages[(SITE / "labs/04-arm-firmware.html").resolve()]
        workflows = {source: code for source, code in page.solution_sources.items()
                     if source.endswith(".yml")}
        self.assertEqual(set(workflows), {
            "examples/workflows/03-target-ci.yml", "examples/workflows/03-target-build.yml",
        })
        for source, code in workflows.items():
            with self.subTest(source=source):
                for later_step in ("quality", "sbom", "package_firmware", "release.yml"):
                    self.assertNotIn(later_step, code.lower())
        caller = workflows["examples/workflows/03-target-ci.yml"]
        build = workflows["examples/workflows/03-target-build.yml"]
        self.assertIn("uses: ./.github/workflows/firmware-build.yml", caller)
        self.assertIn("workflow_call:", build)
        self.assertIn("cmake --preset host", build)
        self.assertIn("cmake --preset arm", build)
        self.assertIn("--no-tests=error", build)
        self.assertIn("if: always()", build)
        self.assertIn("test -s build/arm/monitor.elf", build)
        self.assertIn("test -s build/arm/monitor.bin", build)
        self.assertIn("test -s build/arm/monitor.map", build)
        self.assertIn("name: target-build-${{ github.sha }}", build)

    def test_reference_labs_group_examples_in_one_solution_accordion(self):
        for name in ("04-arm-firmware.html", "05-quality-gates-optional.html",
                     "07-versioned-releases.html"):
            page = self.pages[(SITE / "labs" / name).resolve()]
            references = [detail for detail in page.details
                          if "reference-ideas" in detail["attributes"].get("class", "").split()]
            self.assertEqual(len(references), 1)
            self.assertEqual(len(page.details), 2, "Keep one solution and one reference group")
            for detail in references:
                self.assertNotIn("open", detail["attributes"])
                self.assertIn("Reference ideas:", detail["summary"])
                self.assertIn("simple C project", detail["summary"])
                self.assertTrue(any(parent["attributes"].get("id") == "solution"
                                    for parent in detail["ancestors"]),
                                "Reference accordions belong inside the solution checkpoint")
            for block in page.code_blocks:
                with self.subTest(lab=name, source=block["source"]):
                    reference_parents = [detail for detail in block["details"]
                                         if detail in references]
                    if block["workflow"]:
                        self.assertFalse(reference_parents, "Keep workflow YAML outside reference accordions")
                    else:
                        self.assertTrue(reference_parents, "Fold non-workflow reference code")
            text = (SITE / "labs" / name).read_text(encoding="utf-8")
            introduction = re.search(
                r'<p class="reference-intro">(.*?)</p>\s*'
                r'<details id="reference-ideas" class="reference-ideas">',
                text, re.DOTALL,
            )
            self.assertIsNotNone(introduction, "Explain the reference code immediately before its group")
            self.assertIn("complement the workflows", introduction.group(1))
            self.assertIn("separate, simple C project", introduction.group(1))
            self.assertIn("CMake and ARM GCC for compilation", introduction.group(1))

    def test_task_first_labs_keep_worked_examples_inside_the_solution(self):
        paths = sorted(path for path in (SITE / "labs").glob("*.html")
                       if path.name[:2] in {"01", "02", "03", "04", "05", "07"})
        for path in paths:
            page = self.pages[path.resolve()]
            with self.subTest(lab=path.name):
                instructions = " ".join(page.outside_solution_text)
                for required in ("Purpose", "Customer activities", "Done when"):
                    self.assertIn(required, instructions)
                for implementation in ("Reference idea:", "path/to/your/project",
                                       "Cortex-M3", "16,384", "4,096", "50001",
                                       "cmake --", "cppcheck --", "name: Workshop"):
                    self.assertNotIn(implementation, instructions)
                for block in page.code_blocks:
                    self.assertTrue(any(detail["attributes"].get("id") == "solution"
                                        for detail in block["details"]),
                                    "Worked commands, workflow YAML and output belong in the solution")
                for detail in page.details:
                    if detail["attributes"].get("id") != "solution":
                        self.assertTrue(any(parent["attributes"].get("id") == "solution"
                                            for parent in detail["ancestors"]),
                                        "Do not show reference accordions outside the solution")

    def test_first_lab_requires_command_notes_not_new_build_configuration(self):
        path = (SITE / "labs/01-local-build.html").resolve()
        page = self.pages[path]
        text = path.read_text(encoding="utf-8")
        self.assertFalse(page.embedded_sources)
        self.assertEqual(text.count("<pre>"), 1, "Keep only the short command illustration")
        for expected in ("OneNote", "No new script, preset or build configuration",
                         "clean build directory", "ready for lab 2"):
            self.assertIn(expected, text)
        for configuration in ("CMakeLists.txt", "CMakePresets.json", "data-source="):
            self.assertNotIn(configuration, text)
        index = (SITE / "solutions.html").read_text(encoding="utf-8")
        first_solution = re.search(r'<section id="lab-01">(.*?)</section>', index, re.DOTALL)
        self.assertIsNotNone(first_solution)
        self.assertIn("OneNote", first_solution.group(1))
        self.assertNotIn("<pre>", first_solution.group(1))
        self.assertNotIn("cmake-project", first_solution.group(1))

    def test_release_solution_reuses_prior_ci_and_reference_configuration_stays_available(self):
        last_lab = self.pages[(SITE / "labs/07-versioned-releases.html").resolve()]
        conclusion = self.pages[(SITE / "deployment-concepts.html").resolve()]
        self.assertIn("solution", last_lab.ids)
        self.assertEqual(set(last_lab.embedded_sources), {
            ".github/workflows/release.yml", "scripts/package_firmware.py", "scripts/validate_sbom.py",
        })
        prior_lab = self.pages[(SITE / "labs/05-quality-gates-optional.html").resolve()]
        self.assertIn(".github/workflows/ci.yml", prior_lab.solution_sources)
        self.assertIn(".github/workflows/firmware-build.yml", prior_lab.solution_sources)
        self.assertNotIn("solutions.html#final", conclusion.links)
        self.assertIn("included directly in lab 7", " ".join(conclusion.prose))
        solution = self.pages[(SITE / "solutions.html").resolve()]
        for anchor in ("ci", "firmware-build", "release", "package-firmware", "validate-sbom"):
            self.assertIn(f"workflow-examples.html#{anchor}", solution.links)
        expected = {
            "samples/reference-firmware/CMakeLists.txt",
            "samples/reference-firmware/CMakePresets.json",
            "samples/reference-firmware/cmake/arm-gcc.cmake",
        }
        self.assertEqual(set(solution.embedded_sources), expected)
        for source, code in solution.embedded_sources.items():
            with self.subTest(source=source):
                self.assertEqual(code, (ROOT / source).read_text(encoding="utf-8"))

    def test_release_lab_has_no_redundant_example_section_or_incomplete_publisher(self):
        path = (SITE / "labs/07-versioned-releases.html").resolve()
        text = path.read_text(encoding="utf-8")
        self.assertNotIn("Read the complete examples", text)
        self.assertNotIn("This excerpt explains dependencies", text)
        self.assertNotIn("# See the complete release.yml", text)
        page = self.pages[path]
        self.assertIn("Customer activities: release exercise", " ".join(page.outside_solution_text))
        self.assertEqual(
            {source for source in page.solution_sources if source.endswith(".yml")},
            {".github/workflows/release.yml"},
        )

    def test_release_solution_explains_the_existing_build_contract_without_repeating_ci(self):
        path = (SITE / "labs/07-versioned-releases.html").resolve()
        text = path.read_text(encoding="utf-8")
        for expected in ("Keep the CI caller and reusable build/test workflow",
                         "Contract with your existing reusable workflow",
                         "Align its declared", "reject a selected option",
                         "If you followed only the core lab 4 checkpoint",
                         "add the packaging/upload integration", "Do not merely rename the raw artifact"):
            self.assertIn(expected, text)
        self.assertNotIn("All final workflow files", text)
        self.assertNotIn("Complete final pipeline solution", text)

    def test_release_verification_activity_is_generic_and_example_is_reference_only(self):
        page = self.pages[(SITE / "labs/07-versioned-releases.html").resolve()]
        instructions = " ".join(page.outside_solution_text)
        self.assertIn("your project's approved verification tool", instructions)
        for reference_detail in ("Local package verification", "scripts/package_firmware.py",
                                 "dist/firmware", "SHA256SUMS", "manifest.json"):
            self.assertNotIn(reference_detail, instructions)
        examples = [block for block in page.code_blocks
                    if block["source"] is None
                    and "python3 scripts/package_firmware.py --verify dist/firmware" in block["text"]]
        self.assertEqual(len(examples), 1)
        self.assertTrue(any(detail["attributes"].get("id") == "reference-ideas"
                            for detail in examples[0]["details"]))
        text = (SITE / "labs/07-versioned-releases.html").read_text(encoding="utf-8")
        self.assertIn("not a universal verifier for customer firmware packages", text)

    def test_only_embedded_workflows_are_generated(self):
        names = {path.name for path in (ROOT / ".github/workflows").glob("*.yml")}
        self.assertEqual(names, {"ci.yml", "firmware-build.yml", "release.yml"})
        for path in (ROOT / ".github/workflows").glob("*.yml"):
            text = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("site/", text)
            self.assertNotIn("deploy-pages", text)
            self.assertNotIn("vibehub", text)
