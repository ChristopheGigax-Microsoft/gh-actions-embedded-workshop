# From Commit to Firmware

An English, hands-on embedded CI/CD workshop with GitHub Actions. The mandatory
learning path supports a facilitated session of **at least two hours**, excluding
preflight and the optional quality/SBOM modules.

## Customer workshop

Open [site/index.html](site/index.html). The workshop uses the customer's **existing
GitHub repository and development environment**. It does not require adopting the
sample project, Codespaces, or a new build system.

[Complete workflow examples and supporting scripts](site/workflow-examples.html)
are embedded directly in the static workshop, so participants do not need access
to this source repository to read or copy them.

Lab 1 produces verified command notes in OneNote or another approved location;
no new script or build configuration is required. Subsequent labs include their
completed code directly in their checkpoints, with copy buttons.
The [last lab](site/labs/07-versioned-releases.html#solution) adds the complete
release workflow and release-specific verification references, reusing rather
than repeating the CI/build workflows from earlier labs. Its integration contract
explains the required package artifact and inputs, including the core-only route.
Participants do not need to navigate to a separate solution page.

Labs 1-5 and 7 present the customer purpose, activities and completion requirements
outside the solution checkpoint. Worked commands, YAML and reference material
stay inside it. Labs 4, 5 and 7 each group their supporting files into one large
reference-ideas accordion within that solution area, introduced as examples for
a separate simple C project using CMake and ARM GCC.

Lab 4 uses a build/test/artifact-only checkpoint from `examples/workflows`;
it does not introduce quality or SBOM inputs or steps. Later labs extend it,
and the final combined customer templates remain under `examples/workflows`.

**Adapt to your target project:** CMake and Arm GNU are reference examples. For
every build example, use the compiler/version, architecture, SDK, CPU/ABI flags,
startup files, linker script, presets, runner, and output paths appropriate to your
target. Host tests use a host compiler, not the device cross-compiler.

**Set your project path:** replace `path/to/your/project` in workflow commands,
source path filters and helper configuration with your existing project's path
relative to the repository root. Do not create the literal placeholder directory.
For a root-level project, use `.` in commands and `**` for the workflow source path
filter. Also adapt include/source subdirectories, presets and output paths.

The required exercise changes one **test expectation**, observes failed CI, then
restores the original expectation. It does not introduce defects in production
firmware. Additional quality gates and SBOM generation are independent opt-ins
before the versioned release. Builds and tests remain required.

## Reference project and workflows

[The reference C project](samples/reference-firmware/README.md) accompanies the
examples; workshop participants use their existing project and environment.
The three active workflow files are ready to build **this repository's**
`samples/reference-firmware` project on GitHub-hosted Ubuntu runners:

- `.github/workflows/ci.yml`: PR, `main`, and `workshop/**` branch checks,
  plus manual options.
- `.github/workflows/firmware-build.yml`: reusable build/test, optional quality
  gates, optional SBOM, and checksummed firmware packaging. Also runs the
  workshop's Python regression checks.
- `.github/workflows/release.yml`: validate a `workshop-vMAJOR.MINOR.PATCH` tag and
  publish that run's verified firmware package. Releases are marked prereleases.

After committing and pushing these files to your repository, open **Actions >
Firmware CI > Run workflow** and select `main`. Leave both options off for the
core demo, or independently enable `quality` (warnings, analysis, 80% line
coverage, size budgets) and `sbom` (validated SPDX source inventory). No device
or repository secrets are required; Actions must be enabled.

A successful run provides `firmware-<commit SHA>` containing `monitor.elf`,
`monitor.bin`, `monitor.map`, `manifest.json`, and `SHA256SUMS`, plus
`sbom.spdx.json` when selected. The separate `diagnostics-<commit SHA>` artifact
retains test and coverage reports, including available reports on failure.
Selected gate failures prevent firmware upload and release publication.

For the red-to-green demo, change only `EXPECTED_MIDPOINT_MC` in
`samples/reference-firmware/tests/test_monitor.c` from `50000` to `50001` on an
approved `workshop/**` branch, observe failed CI, then restore `50000`.
For delivery, create and push a new `workshop-vMAJOR.MINOR.PATCH` tag on the
desired commit. The release workflow rebuilds and checks that tagged source
and publishes its same-run package as a prerelease, never flashing hardware.
To select optional gates for a release, dispatch **Firmware release** against
an existing matching tag; it will refuse to overwrite an existing release.
Tag-push releases use the core checks with optional modules off.

Customer-facing snippets still use `path/to/your/project`: their final caller
and reusable-build templates are `examples/workflows/04-full-ci.yml` and
`examples/workflows/04-full-build.yml`. They are embedded in the site instead of
the repository-specific active workflows. Customers must adapt paths, toolchains
and tag patterns and review existing automation before use. Do not copy workflow
files over existing customer files without review.

## Static hosting

Upload the **contents of `site`** to VibeHub manually. All assets and navigation
are relative, and essential content works without JavaScript. No build step,
backend, CDN, tracking, website workflow, GitHub Pages workflow, or VibeHub
integration is included. VibeHub-specific hosting compatibility is not verified
until its hosting contract is available.

For a local preview, from this repository root run `python -m http.server 8000`
and visit `http://localhost:8000/site/`. This serves static files only.

## Local checks

`python -m unittest discover -s tests -v` checks package integrity, SBOM semantics,
site links, and workshop scope without creating a website workflow. See the
reference project README for native/Arm builds and the test-only failure exercise.
Do not treat these local checks as evidence of a hosted Actions run or real
hardware validation.
