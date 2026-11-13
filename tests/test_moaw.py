from pathlib import Path
import re
import unittest
from urllib.parse import parse_qs, unquote, urljoin, urlsplit

from test_site import Page

ROOT = Path(__file__).resolve().parents[1]
MOAW = ROOT / "moaw"
PAGES = [
    "index.html", "prerequisites.html",
    "labs/01-local-build.html", "labs/02-first-pipeline.html",
    "labs/03-tests-and-debugging.html", "labs/04-arm-firmware.html",
    "labs/05-quality-gates-optional.html", "labs/06-sbom-optional.html",
    "labs/07-versioned-releases.html", "deployment-concepts.html",
    "troubleshooting.html", "workflow-examples.html", "solutions.html",
    "extensions.html", "instructor.html",
]


def parse_section(markdown):
    prose, blocks, details = [], [], []
    fence = None
    source = None
    lines = []
    block_details = ()
    for line in markdown.splitlines(keepends=True):
        if fence:
            if line.strip() == fence:
                blocks.append({"source": source, "text": "".join(lines),
                               "details": block_details})
                fence, source, lines = None, None, []
            else:
                lines.append(line)
            continue
        marker = re.fullmatch(r"<!-- source: (.+) -->\n?", line)
        if marker:
            source = marker[1]
            continue
        opening = re.fullmatch(r"(`{3,})[a-z]*\n?", line)
        if opening:
            fence = opening[1]
            block_details = tuple(details)
            continue
        if re.fullmatch(r"<details(?: open)?>\n?", line):
            details.append(len(details))
        elif line.strip() == "</details>":
            details.pop()
        prose.append(line)
    if fence or details or source:
        raise ValueError("Unclosed code/accordion or orphaned source marker")
    return "".join(prose), blocks


def resolve_route(link, route=None):
    return re.sub(r"\$\$route:([^$\n]+)\$\$", lambda match: route or match[1], link)


def rendered_code(text):
    return text.replace(r"\assets/", "assets/")


class MoawTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.markdown = (MOAW / "workshop.md").read_text(encoding="utf-8")
        _, cls.metadata, body = cls.markdown.split("---\n", 2)
        cls.sections = re.split(r"\n\n---\n\n", body.strip())
        cls.parsed = [parse_section(section + "\n") for section in cls.sections]
        cls.pages = []
        for name in PAGES:
            page = Page()
            page.feed((ROOT / "site" / name).read_text(encoding="utf-8"))
            cls.pages.append(page)

    def test_metadata_and_sections_are_valid_for_direct_moaw_loading(self):
        for name in ("type", "title", "description", "level", "duration_minutes", "tags"):
            self.assertRegex(self.metadata, rf"(?m)^{name}: \S.+$")
        self.assertRegex(self.metadata, r"(?m)^published: true$")
        self.assertRegex(self.metadata, r"(?m)^type: workshop$")
        self.assertRegex(self.metadata, r"(?m)^level: (beginner|intermediate|advanced)$")
        self.assertRegex(self.metadata, r"(?m)^duration_minutes: [1-9]\d*$")
        for name in ("authors", "contacts"):
            self.assertRegex(self.metadata, rf"(?m)^{name}:\n(?:  - \S.+\n)+")
        titles = self.metadata.split("sections_title:\n", 1)[1].splitlines()
        self.assertEqual(len(titles), len(PAGES))
        self.assertEqual(len(self.sections), len(PAGES))
        for step, (prose, _) in enumerate(self.parsed):
            with self.subTest(step=step):
                self.assertEqual(len(re.findall(r"^# .+", prose, re.MULTILINE)), 1)

    def test_every_original_code_block_is_preserved_in_its_section(self):
        for step, page in enumerate(self.pages):
            _, blocks = self.parsed[step]
            with self.subTest(page=PAGES[step]):
                self.assertEqual(
                    [rendered_code(block["text"]).rstrip("\n") for block in blocks],
                    [block["text"].rstrip("\n") for block in page.code_blocks],
                )
                self.assertEqual(
                    [block["source"] for block in blocks],
                    [block["source"] for block in page.code_blocks],
                )
                for block in blocks:
                    if block["source"]:
                        source = (ROOT / block["source"]).resolve()
                        self.assertTrue(source.is_relative_to(ROOT))
                        self.assertNotRegex(block["text"], r"(?<!\\)assets/")
                        self.assertEqual(
                            rendered_code(block["text"]), source.read_text(encoding="utf-8"),
                        )

    def test_internal_links_resolve_to_existing_steps_and_explicit_anchors(self):
        all_links = 0
        for step, (prose, _) in enumerate(self.parsed):
            ids = re.findall(r'<a id="([^"]+)"></a>', prose)
            self.assertEqual(len(ids), len(set(ids)))
            for link in re.findall(r"\]\(([^)]+)\)", prose):
                all_links += 1
                with self.subTest(step=step, link=link):
                    url = urlsplit(link)
                    if url.scheme:
                        self.assertEqual(url.scheme, "https")
                        continue
                    if url.path.startswith(("assets/", "./assets/")):
                        destination = (MOAW / unquote(url.path)).resolve()
                        self.assertTrue(destination.is_relative_to(MOAW.resolve()))
                        self.assertTrue(destination.is_file())
                        continue
                    for base, route in (
                        ("http://localhost:4444/", "workshop/workshop.md"),
                        ("https://microsoft.github.io/moaw/", None),
                    ):
                        resolved = urlsplit(urljoin(base, resolve_route(link, route)))
                        expected_route = route or (
                            "workshop/gh:christophegigax-microsoft/"
                            "gh-actions-embedded-workshop/main/moaw/"
                        )
                        self.assertEqual(
                            unquote(resolved.path),
                            urlsplit(base).path + expected_route,
                        )
                        params = parse_qs(resolved.query)
                        self.assertEqual(params["vars"], [f"route:{expected_route}"])
                    target = int(params["step"][0])
                    self.assertGreaterEqual(target, 0)
                    self.assertLess(target, len(self.sections))
                    if url.fragment:
                        self.assertIn(f'<a id="{url.fragment}"></a>', self.parsed[target][0])
        self.assertGreater(all_links, 40)

    def test_original_solution_and_reference_accordion_structure_is_preserved(self):
        for step in range(2, 9):
            prose, blocks = self.parsed[step]
            page = self.pages[step]
            with self.subTest(lab=PAGES[step]):
                self.assertEqual(prose.count("<summary>Solution and recovery checkpoint</summary>"), 1)
                self.assertEqual(prose.count("<details"), len(page.details))
                for block, original in zip(blocks, page.code_blocks):
                    self.assertEqual(len(block["details"]), len(original["details"]))
                for original in page.details:
                    self.assertIn(original["summary"], prose)
                if step != 7:
                    self.assertTrue(all(block["details"] for block in blocks))
                    for expected in ("## Purpose", "Customer activities", "**Done when"):
                        self.assertIn(expected, prose)

    def test_core_route_skips_independent_optional_modules(self):
        target = self.parsed[5][0]
        self.assertRegex(target, r"\[Core route: continue to releases\]\([^\n]+\?step=8&")
        for step in (6, 7):
            prose = self.parsed[step][0]
            self.assertIn("Optional", prose)
            self.assertIn("?step=8&", prose)
        self.assertIn("?step=9&", self.parsed[8][0])
        self.assertIn("temporary incorrect expected value", self.parsed[1][0])

    def test_customer_boundaries_and_hosting_are_not_misrepresented(self):
        introduction = self.parsed[0][0]
        self.assertIn("existing customer project", introduction)
        self.assertIn("Publishing a package is not device deployment", introduction)
        self.assertIn("original correct expectation", self.parsed[4][0])
        self.assertIn("Host tests need a host compiler", self.parsed[10][0])
        for prose, _ in self.parsed:
            self.assertNotIn("VibeHub", prose)
            self.assertNotIn("Mark this lab completed", prose)
            self.assertNotRegex(prose, r"<(?:script|link)\b")
            for link in re.findall(r"\]\(([^)]+)\)", prose):
                if not urlsplit(link).scheme:
                    self.assertNotIn(".html", link)
            for admonition in re.finditer(
                r'<div class="(?:warning|task|important)">\n\n(.*?)\n\n</div>',
                prose, re.DOTALL,
            ):
                self.assertTrue(all(line.startswith(">") for line in admonition[1].splitlines()))
        self.assertIn("does not implement", self.parsed[10][0])
        self.assertIn("not access control", self.parsed[14][0])

    def test_moaw_changes_trigger_existing_ci_without_a_deployment_workflow(self):
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertEqual(ci.count("'moaw/**'"), 2)
        self.assertIn("uses: ./.github/workflows/firmware-build.yml", ci)
        self.assertEqual(
            {path.name for path in (ROOT / ".github" / "workflows").glob("*.yml")},
            {"ci.yml", "firmware-build.yml", "release.yml"},
        )


if __name__ == "__main__":
    unittest.main()
