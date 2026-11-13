---
published: true
type: workshop
title: From Commit to Firmware
short_title: Commit to Firmware
description: Build and verify an embedded CI/CD pipeline with GitHub Actions in your existing customer project.
level: intermediate
authors:
  - ChristopheGigax-Microsoft
contacts:
  - https://github.com/ChristopheGigax-Microsoft
duration_minutes: 150
tags: github actions, embedded, firmware, ci/cd, testing, delivery
navigation_levels: 2
navigation_numbering: false
sections_title:
  - "Introduction"
  - "Customer preflight"
  - "Lab 1: Repeatable build"
  - "Lab 2: First CI workflow"
  - "Lab 3: Test-only red to green"
  - "Lab 4: Target firmware"
  - "Lab 5: Optional quality gates"
  - "Lab 6: Optional SBOM"
  - "Lab 7: Versioned delivery"
  - "Discussion: Release to device"
  - "Troubleshooting"
  - "Complete workflow examples"
  - "Solution reference"
  - "Optional extensions"
  - "Facilitator guide"
---

<a id="step-0-main"></a>

Embedded engineering / GitHub Actions

# From Commit to Firmware

**Your code. Your target. A repeatable pipeline.**

Build a firmware delivery pipeline around your existing customer project. Automate builds and tests, follow a failure back to its cause, and publish firmware you can trace to the exact source commit.

- **English**
- **At least 2 hours of core activities**
- **No hardware required**
- **Existing customer environment**

 [Start with customer preflight]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=1&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) 

<div class="warning">

> **CMake and Arm are reference examples, not required customer targets.**
>
> For every compilation example, adapt the toolchain to your targeted project: compiler/version, architecture, SDK, CPU/ABI flags, startup code, linker script, presets, runner, and output paths. Native tests need a host compiler. You do not have to migrate your project to CMake.

</div>

## What you will leave with

A build/test workflow in your own repository, actual target firmware artifacts, a diagnosed red-to-green CI run, and a versioned release with checksums and source/toolchain identity. Optionally add quality gates and a software bill of materials (SBOM) before release.

This is **continuous integration and continuous delivery**. Publishing a package is not device deployment. Real flashing, OTA, and hardware validation are discussed separately.

<a id="step-0-journey"></a>

## The learning journey

Complete preflight before the facilitated session. Follow labs 1-4 and 7 plus the deployment discussion for the mandatory route. The facilitator guide provides a core activity budget of 150 minutes, excluding the independent optional labs.

01 / REQUIRED

### [Make the build repeatable]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=2&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Map your project's real build commands, dependencies, and target configuration.

02 / REQUIRED

### [Your first CI workflow]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=3&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Move the reproducible build onto an approved runner and inspect the evidence.

03 / REQUIRED

### [See red. Diagnose. Restore green.]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=4&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Change only a test expectation, observe the failed assertion, then restore it.

04 / REQUIRED

### [Build target firmware]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Separate host tests from target compilation and identify genuine firmware outputs.

05 / OPTIONAL

### [Add quality gates]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=6&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Warnings, analysis, coverage, and a size budget. Existing customer gates stay intact.

06 / OPTIONAL

### [Generate an SBOM]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Create a scoped, machine-readable inventory before publishing the firmware.

07 / REQUIRED

### [Deliver a versioned release]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Promote the exact validated package, not an arbitrary rebuild or latest artifact.

DISCUSSION

### [From release to device]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=9&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Understand the missing evidence: HIL, compatibility, health checks, and recovery.

## Work in your existing project

Use your existing GitHub repository and approved environment. Map the reference instructions to your tools; do not copy sample paths blindly. Keep your source and reports inside approved customer infrastructure.

## Working example files

[Read and copy the complete workflow examples directly in this workshop]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$): first build, tests, CI caller, reusable firmware build, and versioned release. All supporting scripts are included on the same page. You do not need access to the workshop repository. These examples automate firmware only.

[Complete workflow examples]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) · [Lab solutions]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) · [Final pipeline solution]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-final) · [Optional advanced topics]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=13&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-1-main"></a>

Before the workshop

# Bring your project, not a new platform.

The workshop starts with code already in your customer's GitHub repository and a working customer development environment. Resolve these prerequisites before the session.

## Access and safety agreement

- Permission to create an approved workshop branch/PR and edit workflow files in the existing repository.
- Actions enabled, an approved runner, and an allowed-actions list compatible with the reviewed examples.
- Compiler/SDK access, required licenses, dependency/network access, and a runner OS that can build the real target.
- Approval for the **required test-only intentional failure**: one editable deterministic test, a temporary incorrect expected value, and an isolated red CI run.
- Review existing push, PR, tag, release, and downstream deployment triggers. Agree a workshop namespace that cannot publish production firmware or flash a device.
- Agree where diagnostic reports and binaries can be retained. Do not copy customer source or reports into the public workshop repository.
- For the release lab, permission to create an approved workshop tag and GitHub prerelease. If customer policy forbids publication, record the limitation before the session and demonstrate packaging without claiming release completion.

## Fill in the adaptation map

| Integration point | Reference | Record for your project |
| --- | --- | --- |
| Source/build entry | `path/to/your/project` placeholder and reference CMake presets | Your repository-relative source directory and existing configure/build commands |
| Host tests | CTest/native compiler | Executable test command, deterministic test, report path |
| Target toolchain | Arm GNU/Cortex-M3 | Compiler/version, target/ABI, SDK, startup, linker map |
| Runner | Hosted Ubuntu reference | Approved labels/OS, network and licensing constraints |
| Outputs | ELF/BIN/map | Actual target files and packaging location |
| Optional gates | GCC/cppcheck/gcovr/size | Selected modules, supported tools, agreed thresholds |
| Optional SBOM | Scoped SPDX inventory | Approved generator and component inventory scope |
| Delivery | Workshop-only version tags | Non-production namespace and release policy |

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. Use `.` for a root-level project in commands and `**` for its workflow source path filter. Also adapt include/source subdirectories, presets and output paths.

</div>

<div class="warning">

> **Adapt to your target project.**
>
> CMake is a build-system reference, not a universal toolchain. Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner, and paths for your actual target. Host tests use a host compiler. Do not migrate build systems just to follow this workshop.

</div>

## Evidence to bring

Run a clean build and the chosen tests in your current environment. Record tool versions and the output locations. A native test runner must not attempt to execute a device ELF directly. Missing testability or noninteractive build access is a preflight gap, not something to hide with a passing placeholder job.

## Optional modules are not prerequisites

Quality gates and SBOM generation are independently optional. You need their tools only if you choose them. Existing customer-required checks must remain required. No physical board, paid environment approvals, Codespaces, or external code-upload service is required for the core.

<div class="important">

> **Ready to start?**
>
> You have a baseline passing build/test, the adaptation map, approved runner access, the test-only exercise agreement, and safe branch/tag boundaries.

</div>

[Home]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: repeatable build →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=2&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-2-main"></a>

01 / Required / Build foundation

# Make the build repeatable.

Find and verify your existing build and test commands, then note them in OneNote or another approved place for lab 2.

## Purpose

Establish a repeatable local baseline so that the next lab can automate your actual project without guessing how it builds or tests.

## Starting checkpoint

Preflight is complete. You are on an approved workshop branch in the customer repository, with a working baseline and no production deployment trigger attached.

## Customer activities: inspect before you automate

1. Locate the build entry point, dependency setup, and outputs. Which steps depend on your workstation state?
2. Identify host-test and target configurations. Record the compiler and target used by each.
3. Find the project's existing presets or equivalent scripts. Prefer those over duplicating IDE settings in YAML.
4. Record a clean output directory and exact tool versions. Avoid using artifacts left behind by a previous build.

## Write your command notes

Use OneNote, a text file or another customer-approved location. No new script, preset or build configuration is required for this lab. Keep using the project's existing build system.

- The working directory and environment/dependency setup commands, including compiler/SDK versions.
- The exact configure, build and test commands, in execution order.
- The configuration used by each command: native host tests or target firmware.
- The build output, firmware artifact and test-report locations.

Verify the commands from a clean build directory, then keep these notes for lab 2. Do not delete existing customer-owned outputs indiscriminately or commit generated directories or local SDK licenses.

<div class="task">

> **Customer activity: clean-room explanation**
>
> In pairs, explain how a new approved runner would obtain each dependency and execute the same build. Identify at least one hidden workstation dependency and decide where its setup belongs.

</div>

## Discuss the evidence

- What would change if the runner has no access to the vendor SDK?
- Does the build require a GUI, interactive license prompt, or network share?
- Are host tests actually running application logic, or only compiling it?

<a id="step-2-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Your verified command notes

The solution is your own short set of notes: environment setup, configure/build/test commands, host or target configuration, and output/report paths. OneNote is enough; there is no configuration file to create or copy for this checkpoint. In lab 2, you will translate these verified commands into workflow steps.

### Optional command illustration

<div class="warning">

> **Adapt to your target project before running.**
>
> CMake and the following paths are references. Replace the toolchain/compiler, SDK, CPU/ABI flags, startup/linker configuration, presets, and output paths to fit your targeted project. For this native example, choose a host compiler. Changing toolchains requires a fresh build directory.

</div>

```bash
# Illustrative native commands: use your project's existing configuration.
cmake -S . -B build/workshop-host
cmake --build build/workshop-host
ctest --test-dir build/workshop-host --output-on-failure --output-junit test-results.xml
```

The first command configures; the second compiles/links; the third executes tests. CMake does not select the correct hardware target by itself. With a different build system, substitute your existing configure/build/test commands; no migration is required.

A clean build succeeds and at least one real test executes and passes. If changing the compiler leaves stale CMake state, use a separate clean output directory rather than deleting customer-owned files indiscriminately. If no tests execute, fix test discovery before treating the checkpoint as complete.

</details>

<div class="important">

> **Done when**
>
> Your recorded commands produce a clean successful build, your chosen test executes and passes, and the output/report locations are known. Keep your notes and report inside the customer environment, ready for lab 2.

</div>

[← Preflight]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=1&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: first pipeline →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=3&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-3-main"></a>

02 / Required / Continuous integration

# Move the build into CI.

Run your verified local build on an approved GitHub Actions runner and make its result visible during code review.

## Purpose

Turn the command notes from lab 1 into a repeatable CI check for the intended commit, while preserving existing customer checks and production behavior.

## Starting checkpoint

Lab 1's command map is working. Review existing customer workflows before adding a new file. Preserve existing mandatory checks and production behavior.

## Customer activities: automate your baseline

1. Choose an approved workflow path and runner that can access your project's compiler, dependencies and licenses.
2. Create or extend a workflow to check out the intended commit, prepare the environment and execute the build commands recorded in lab 1.
3. Configure an approved trigger for your workshop branch. If you choose manual dispatch, verify that the workflow is available on the default branch; otherwise use approved scoped push/PR events.
4. Use your actual source and output paths, and compare the runner's configuration with the successful local baseline.
5. Connect the workflow to the workshop PR without changing organization protection rules or production tag triggers.

<div class="task">

> **Customer activity: read the run**
>
> 1. Trigger the workflow on your workshop change and open its Actions run.
> 2. Locate the runner OS, compiler setup, source checkout, and build step.
> 3. Compare actual commands and paths to the successful local baseline.
> 4. Open the workshop PR and find its check status. Determine which existing checks still apply.

</div>

## Permissions and trust

Start with a read-only token. Pin reviewed action revisions, not a moving branch. Never run untrusted pull-request code on a device-connected self-hosted runner. An environment approval does not make a persistent runner isolated.

<a id="step-3-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed first-build workflow

Save or merge this checkpoint into an approved workflow path in your existing repository. It starts with a manual event; add approved workshop-branch push/PR triggers as described in the exercise. Provisioning and build commands must match your environment.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

GitHub exposes a manual workflow in the Actions UI after the workflow exists on the default branch. For a workshop-branch-only file, add approved scoped push/PR events and push a commit to trigger it instead of assuming the Run workflow button will exist.

#### `.github/workflows/01-first-ci.yml`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: examples/workflows/01-first-ci.yml -->
```yaml
# Teaching checkpoint; copy/adapt into your CUSTOMER repository after reviewing existing workflows.
# Adapt CMake compiler/SDK, presets, runner and paths to your target project.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
name: Workshop first build
on:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  build:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13
      - name: Reference native build - adapt host compiler and CMake paths
        env:
          CC: gcc-13
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
```

### Recovery and expected result

A successful run checks out the expected commit, installs/locates the approved compiler, and invokes the recorded project build. Runner setup failure is not a firmware regression. If a workflow never starts, compare the event, branch, path filters, and default-branch dispatch rule before changing code.

</details>

<div class="important">

> **Done when**
>
> The customer project's build passes in Actions and the PR exposes meaningful status. Record the run/commit identity; a green check from a different commit is not your evidence.

</div>

[← Repeatable build]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=2&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: red to green →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=4&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-4-main"></a>

03 / Required / Diagnose the evidence

# Make a test fail. Then restore it.

This is a required customer exercise, not a demonstration-only slide. Change only a test expectation on the workshop branch. Production firmware logic stays unchanged.

## Purpose

Prove that CI executes your actual tests, reports an assertion failure as a failed run, and retains enough evidence to diagnose it. Then restore the original passing behavior without weakening the test.

## Starting checkpoint

A build and a suitable deterministic test pass. Customer approval covers an intentionally red intermediate commit. The branch/PR is isolated from production delivery. Record the test's original assertion before editing it.

## Customer activities: prepare the evidence

1. Extend your workflow to run the real test command recorded in lab 1 after the build succeeds.
2. Make the diagnostic report available even when tests fail, without changing the failed run's overall result.
3. Verify that native tests use the host compiler and that the runner does not attempt to execute a device binary.

## Customer activities: run the required experiment

1. **Baseline:** run the test successfully and note its name, run, and commit.
2. **Test-only edit:** choose a deterministic assertion from your project and make one expectation deliberately incorrect for the unchanged correct application behavior.
3. **Observe red:** commit/push the approved test-only change and inspect the PR run. Confirm the test actually executes and fails with an expected/actual mismatch.
4. **Explain it:** find the test name and mismatch in logs/report. Distinguish an assertion failure from a compilation, network, license, or runner failure.
5. **Restore:** return the exact original correct expectation, commit/push the restoration, and confirm the test executes and passes.
6. **Review:** inspect the final diff. No intentional failing assertion or manufactured production-code defect may remain before merge/release.

<div class="warning">

> **Do not manufacture green.**
>
> No skipped/disabled tests, weakened assertions, `continue-on-error`, ignored exit codes, or production-code changes to satisfy the incorrect expectation. A forced shell failure or broken compilation does not complete this exercise.

</div>

<div class="task">

> **Customer activity: explain the boundary**
>
> What would happen if a failed test job had a successful report-upload step? Why must artifact retention not change the overall failing result? Later, inspect the release job's dependencies and confirm it cannot publish when this test fails.

</div>

<a id="step-4-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed test workflow

The final workflow runs your existing tests and retains diagnostics without masking failures. Restore the original correct expectation in your own test after observing the intentional failure; no application test implementation is supplied or required here.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

#### `.github/workflows/02-tests.yml`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: examples/workflows/02-tests.yml -->
```yaml
# Teaching checkpoint; adapt existing customer workflows rather than overwriting them.
# Adapt CMake toolchain/presets/paths; native tests need a host compiler.
name: Workshop build and tests
on:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13
      - name: Native build and real tests - adapt toolchain to your project
        env:
          CC: gcc-13
        run: |
          # REQUIRED: replace this placeholder with your repository-relative project path.
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --output-junit test-results.xml
      - if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: workshop-test-report
          path: build/host/test-results.xml
          if-no-files-found: warn
```

### Recovery and expected result

Two runs are required: an executed assertion fails for the intended wrong expectation, then the restored assertion executes and passes. Restore your test's original correct expectation, not the implementation. If no tests are discovered, stop and fix test registration; a “no tests found” success is not validation.

</details>

<div class="important">

> **Done when**
>
> You can show the failed assertion, retained diagnostics, passing restoration, and a clean final test diff. Keep the red intermediate commit as history on the approved branch according to customer policy.

</div>

[← First pipeline]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=3&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: target firmware →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-5-main"></a>

04 / Required / Target compilation

# Build firmware, not a renamed host binary.

Host tests and target compilation answer different questions. Keep both configurations visible and build your actual customer's target.

## Purpose

Add a real target build to CI while keeping host tests as separate evidence. Identify the exact firmware outputs that later delivery steps should consume; compilation alone does not prove that firmware boots or behaves correctly on hardware.

## Starting checkpoint

The required red-to-green exercise is complete and all tests are restored. You have the project's approved target compiler, SDK/license setup, linker/startup configuration, and output paths.

## Customer activities: build your actual target

1. Record your target's compiler/version, board or architecture, SDK, CPU/ABI/FPU settings, startup/runtime and linker memory layout. Identify how they differ from the host-test configuration.
2. Extend the workflow to provision the approved target tools and execute your existing target build noninteractively, using a separate build directory from native tests.
3. Keep the required host tests in the pipeline and ensure target-build failures also fail the run.
4. Identify the firmware, debug information and memory-layout outputs needed by your project's delivery process. Record their exact paths and formats.
5. Retain the intended target artifacts only after the required checks pass. Avoid broad globs that could include unrelated or sensitive files.

<div class="task">

> **Customer activity: artifact inspection**
>
> 1. Locate your real target outputs after the clean build.
> 2. Confirm the reported machine/architecture using the customer's approved inspection tool.
> 3. Find the linker entry point and memory regions. Explain how they differ from the host-test configuration.
> 4. Record exactly which output files the delivery package needs. Avoid broad globs that include secrets or license files.

</div>

A memory report and enforced size budget are available in the optional quality module. They are not required to complete the core.

<a id="step-5-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed target-build pipeline

This checkpoint contains required host tests, target compilation and artifact retention only. The caller and reusable workflow have no quality or SBOM inputs or steps. Labs 5 and 6 introduce those independent optional extensions; lab 7 adds the final packaging/release flow. Save or merge the two files below into the indicated workflow paths. The artifact from this checkpoint contains target outputs, not a versioned release package.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

#### `.github/workflows/ci.yml`

<!-- source: examples/workflows/03-target-ci.yml -->
```yaml
# Lab 4 checkpoint: save or merge as .github/workflows/ci.yml.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# If the project is at the repository root, use '**' for its path filter.
name: Firmware CI
on:
  pull_request:
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  push:
    branches: ['workshop/**']
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
```

#### `.github/workflows/firmware-build.yml`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: examples/workflows/03-target-build.yml -->
```yaml
# Lab 4 checkpoint: save or merge as .github/workflows/firmware-build.yml.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# Adapt compiler/SDK, presets, runner and source/build/artifact paths to your target.
name: Reusable firmware build
on:
  workflow_call:

permissions:
  contents: read

jobs:
  firmware:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Install reference host tools
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13 python3
      - name: Install verified reference target compiler
        run: |
          python3 scripts/install_arm.py
          echo "$GITHUB_WORKSPACE/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin" >> "$GITHUB_PATH"
      - name: Native configure, build and test
        env:
          CC: gcc-13
        # Host tests use a host compiler; adapt this CMake setup to your project.
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --no-tests=error --output-junit test-results.xml
      - name: Target firmware
        # Adapt Arm GCC, SDK, CPU/ABI, startup and linker configuration to your target.
        run: |
          cmake --preset arm -S path/to/your/project
          cmake --build build/arm
      - name: Verify the expected target outputs
        # Replace these filenames and formats with your project's actual outputs.
        run: |
          test -s build/arm/monitor.elf
          test -s build/arm/monitor.bin
          test -s build/arm/monitor.map
      - name: Retain diagnostic reports, including on failure
        if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: diagnostics-${{ github.sha }}
          path: |
            build/host/test-results.xml
            build/host/Testing/Temporary/LastTest.log
          if-no-files-found: warn
          retention-days: 7
      - name: Upload target outputs after required checks pass
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: target-build-${{ github.sha }}
          path: |
            build/arm/monitor.elf
            build/arm/monitor.bin
            build/arm/monitor.map
          if-no-files-found: error
          retention-days: 7
```

These scripts and build-configuration examples complement the workflows for a separate, simple C project using CMake and ARM GCC for compilation. Use them as reference ideas and adapt them to your existing project.

<a id="step-5-reference-ideas"></a>

<details>
<summary>Reference ideas: supporting files for a simple C project</summary>

For lab 4, only the native/target build configuration and compiler helper are needed. The other helpers below support later quality, SBOM and release exercises; they are not steps in this lab's workflow.

#### Target-build commands

<div class="warning">

> **Always adapt the Arm/CMake toolchain to your targeted project.**
>
> Arm GNU is the reference, not a requirement. Replace compiler/version, board/architecture, SDK/sysroot, CPU/ABI/FPU flags, startup/runtime, linker script/memory map, presets, runner setup, artifact paths, and inspection tools as applicable. A non-Arm customer must use their own target toolchain. Use a separate build directory from native tests.

</div>

```
# Reference commands: adapt the target toolchain, source paths and presets.
python3 scripts/install_arm.py
export PATH="$PWD/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin:$PATH"
cmake --preset arm -S path/to/your/project
cmake --build build/arm
```

These are POSIX shell commands for the reference Linux runner. Keep using your existing environment and equivalent shell commands. The installer verifies the reference archive digest before extracting locally.

In this separate C project, the toolchain file selects the cross-compiler, the target sets Cortex-M3 flags, and startup and linker files supply initialization and memory placement. Adapt all these pieces to your target, not simply the compiler name.

The reference outputs are an ELF with target sections and symbols, a BIN for a target-specific flashing procedure, and a linker map for section/symbol placement. A BIN alone does not specify a flash address, and none of these outputs proves hardware validation.

#### `CMakeLists.txt`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: samples/reference-firmware/CMakeLists.txt -->
```cmake
cmake_minimum_required(VERSION 3.25)
project(workshop_monitor VERSION 1.0.0 LANGUAGES C)

option(BUILD_FIRMWARE "Build the reference Arm image instead of host tests" OFF)
option(QUALITY_GATES "Enable extra warnings and native coverage" OFF)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_library(monitor STATIC src/monitor.c)
target_include_directories(monitor PUBLIC include)

if(QUALITY_GATES)
  if(NOT CMAKE_C_COMPILER_ID STREQUAL "GNU")
    message(FATAL_ERROR "The reference quality preset requires native GCC/gcov; adapt it for your compiler.")
  endif()
  target_compile_options(monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  if(NOT BUILD_FIRMWARE)
    target_compile_options(monitor PUBLIC --coverage -O0 -g)
    target_link_options(monitor PUBLIC --coverage)
  endif()
endif()

if(BUILD_FIRMWARE)
  enable_language(ASM)
  add_executable(firmware platform/startup.S platform/main.c)
  target_link_libraries(firmware PRIVATE monitor)
  target_compile_options(monitor PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_compile_options(firmware PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_link_options(firmware PRIVATE
    -mcpu=cortex-m3 -mthumb -nostdlib
    "-T${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld"
    "-Wl,-Map=${CMAKE_BINARY_DIR}/monitor.map"
    -Wl,--gc-sections -Wl,--build-id=none)
  set_target_properties(firmware PROPERTIES OUTPUT_NAME monitor SUFFIX .elf
    LINK_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld")
  add_custom_command(TARGET firmware POST_BUILD
    COMMAND "${CMAKE_OBJCOPY}" -O binary "$<TARGET_FILE:firmware>" "${CMAKE_BINARY_DIR}/monitor.bin"
    COMMAND "${CMAKE_SIZE}" "$<TARGET_FILE:firmware>"
    BYPRODUCTS "${CMAKE_BINARY_DIR}/monitor.bin"
    VERBATIM)
else()
  enable_testing()
  add_executable(test_monitor tests/test_monitor.c)
  target_link_libraries(test_monitor PRIVATE monitor)
  if(QUALITY_GATES)
    target_compile_options(test_monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  endif()
  add_test(NAME monitor_logic COMMAND test_monitor)
endif()
```

#### `CMakePresets.json`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: samples/reference-firmware/CMakePresets.json -->
```json
{
  "version": 6,
  "configurePresets": [
    {
      "name": "host",
      "displayName": "Native tests - adapt host compiler to your environment",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/../../build/host",
      "cacheVariables": { "CMAKE_BUILD_TYPE": "Debug" }
    },
    {
      "name": "host-quality",
      "inherits": "host",
      "displayName": "Optional native GCC quality gates",
      "binaryDir": "${sourceDir}/../../build/quality",
      "cacheVariables": { "QUALITY_GATES": "ON" }
    },
    {
      "name": "arm",
      "displayName": "Sample Cortex-M3 only - adapt toolchain to your target project",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/../../build/arm",
      "toolchainFile": "${sourceDir}/cmake/arm-gcc.cmake",
      "cacheVariables": { "CMAKE_BUILD_TYPE": "MinSizeRel", "BUILD_FIRMWARE": "ON" }
    }
  ]
}
```

#### `cmake/arm-gcc.cmake`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: samples/reference-firmware/cmake/arm-gcc.cmake -->
```cmake
# Reference only: adapt compiler/SDK, CPU/ABI, startup and linker map to your target.
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
find_program(CMAKE_C_COMPILER arm-none-eabi-gcc REQUIRED)
find_program(CMAKE_ASM_COMPILER arm-none-eabi-gcc REQUIRED)
find_program(CMAKE_OBJCOPY arm-none-eabi-objcopy REQUIRED)
find_program(CMAKE_SIZE arm-none-eabi-size REQUIRED)
```

#### `scripts/install_arm.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/install_arm.py -->
```python
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
```

#### `scripts/check_size.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/check_size.py -->
```python
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
```

#### `scripts/package_firmware.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/package_firmware.py -->
```python
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


def make_sbom(commit, elf_sha, created, source=None):
    source = SOURCE if source is None else source
    files = []
    for number, name in enumerate(INVENTORY, 1):
        files.append({
            "SPDXID": f"SPDXRef-File-{number}",
            "fileName": f"./{name}",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256(source / name)},
                {"algorithm": "SHA1", "checksumValue": hashlib.sha1((source / name).read_bytes()).hexdigest()},
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
                    "".join(sorted(hashlib.sha1((source / name).read_bytes()).hexdigest()
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
    parser.add_argument("--source", type=Path, default=SOURCE,
                        help="Reference source directory for the optional SBOM inventory")
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
            source = (ROOT / args.source).resolve()
            sbom_path.write_text(json.dumps(make_sbom(commit, firmware["monitor.elf"], created, source), indent=2) + "\n",
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
```

#### `scripts/validate_sbom.py`

<!-- source: scripts/validate_sbom.py -->
```python
"""Validate SPDX 2.3 JSON with a pinned official schema and fixture semantics."""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

SCHEMA_URL = (
    "https://raw.githubusercontent.com/spdx/spdx-spec/"
    "aadf3b0b8dbbabdb4d880b0fc714255fea436ff7/schemas/spdx-schema.json"
)
SCHEMA_SHA256 = "239208b7ac287b3cf5d9a9af23f9d69863971102a5e1587a27a398b43490b89b"


def check_identity(document, commit, elf_sha):
    package = document["packages"][0]
    if package["versionInfo"] != commit:
        raise ValueError("SBOM source commit does not match manifest")
    expected = {"algorithm": "SHA256", "checksumValue": elf_sha}
    if expected not in package["checksums"]:
        raise ValueError("SBOM firmware hash does not match manifest")
    if not document["files"]:
        raise ValueError("SBOM contains no source inventory")
    identifiers = {document["SPDXID"]}
    identifiers.update(item["SPDXID"] for item in document["packages"])
    identifiers.update(item["SPDXID"] for item in document["files"])
    if len(identifiers) != 1 + len(document["packages"]) + len(document["files"]):
        raise ValueError("SBOM SPDX identifiers must be unique")
    for relation in document["relationships"]:
        if relation["spdxElementId"] not in identifiers or relation["relatedSpdxElement"] not in identifiers:
            raise ValueError("SBOM relationship references a missing element")


def validate(path):
    import jsonschema

    document = json.loads(path.read_text(encoding="utf-8"))
    with urllib.request.urlopen(SCHEMA_URL, timeout=60) as response:
        schema_bytes = response.read()
    if hashlib.sha256(schema_bytes).hexdigest() != SCHEMA_SHA256:
        raise ValueError("Official SPDX schema checksum mismatch")
    jsonschema.Draft7Validator(json.loads(schema_bytes)).validate(document)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sbom", type=Path)
    args = parser.parse_args()
    validate(args.sbom)
    print("SPDX 2.3 JSON schema validation passed")


if __name__ == "__main__":
    main()
```

#### `scripts/requirements-sbom.txt`

<!-- source: scripts/requirements-sbom.txt -->
```
# Optional official SPDX JSON-schema validation.
jsonschema==4.23.0
```

</details>

### Recovery and expected result

The reference output names are `build/arm/monitor.elf`, `monitor.bin`, and `monitor.map`. Your project may produce different formats. If architecture/SDK/linking is wrong, adapt the toolchain to the actual targeted project and configure in a fresh build directory; do not reuse cached native compiler settings.

</details>

<div class="important">

> **Done when**
>
> Your customer's approved compiler produces genuine target artifacts alongside passing host tests. State explicitly: no device boot, peripheral, timing, power-failure, or safety behavior has been validated.

</div>

## Choose your next step

[Core route: continue to releases]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

Or take [optional quality gates]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=6&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) and/or [optional SBOM generation]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) first. They are independent.

[← Red to green]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=4&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next required lab: release →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-6-main"></a>

05 / Optional / Before release

# Add useful quality gates.

Choose this module only when its tools and thresholds fit your customer project. Builds and tests remain required whether or not you take this module.

## Purpose

Add meaningful, measurable checks before firmware delivery. Select only tools and thresholds that fit your project, without weakening existing required checks or claiming that a metric proves hardware correctness.

[Skip directly to release]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) or [take SBOM generation independently]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$).

## Starting checkpoint

Lab 4 is complete. Agree supported analysis tools and meaningful thresholds with the customer. Preserve all pre-existing mandatory checks; “optional” describes adding this workshop module, not permission to disable customer policy.

## Customer activities: select and integrate a gate

1. Choose one or more applicable checks: compiler warnings, static analysis, host-test coverage or firmware size. Confirm that your approved tools support the actual project and toolchain.
2. Record the measured source or artifact scope, metric, threshold and reason for that threshold. For size, account for the actual memory layout and any stack, heap or bootloader reservations.
3. Integrate the selected checks into your pipeline before packaging/publication, while retaining the required builds, tests and existing customer gates.
4. Run the workflow with the quality module selected independently of the optional SBOM module. Retain the diagnostics and confirm which checks actually executed.
5. Review failure propagation: a selected gate failure must fail the run and prevent delivery. Do not ignore exit codes, lower a valid threshold just to pass, or report an unselected check as successful.

<div class="task">

> **Customer activity: defend a threshold**
>
> Choose one applicable gate and explain its metric, relevant source scope, threshold, and failure evidence. Review how its diagnostics identify issues; do not introduce defects in production code to manufacture analyzer failures.

</div>

<a id="step-6-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed optional quality-gate configuration

The completed caller and reusable workflow expose the quality option. For this exercise, manually dispatch Firmware CI with quality enabled; leave SBOM disabled unless selected independently. The reference defaults remain off. The complete size helper is included; the other build/package helpers from lab 4 are unchanged. Existing customer checks remain required.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

#### `.github/workflows/ci.yml`

<!-- source: examples/workflows/04-full-ci.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# If the project is at the repository root, use '**' for its path filter.
name: Firmware CI
on:
  pull_request:
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  push:
    branches: ['workshop/**']
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  workflow_dispatch:
    inputs:
      quality:
        description: Enable optional quality gates
        type: boolean
        default: false
      sbom:
        description: Generate an optional pre-release SPDX SBOM
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: ${{ inputs.quality == true }}
      sbom: ${{ inputs.sbom == true }}
```

#### `.github/workflows/firmware-build.yml`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: examples/workflows/04-full-build.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# Adapt presets, include/source directories, output paths and tools to that project.
name: Reusable firmware build
on:
  workflow_call:
    inputs:
      quality:
        type: boolean
        default: false
      sbom:
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  firmware:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Install reference host tools
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13 python3-venv
      - name: Install verified reference target compiler
        run: |
          python3 scripts/install_arm.py
          echo "$GITHUB_WORKSPACE/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin" >> "$GITHUB_PATH"
      - name: Native configure, build and test
        env:
          CC: gcc-13
        # Adapt this CMake setup to your project; host tests require a host compiler.
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --output-junit test-results.xml
      - name: Target firmware
        # Adapt the Arm/CMake toolchain, SDK, CPU/ABI, startup, linker map and paths to your target project.
        run: |
          cmake --preset arm -S path/to/your/project
          cmake --build build/arm
      - name: Optional quality gates
        if: inputs.quality
        env:
          CC: gcc-13
        # Adapt host coverage and target size tools to the project's actual toolchains.
        run: |
          sudo apt-get install -y cppcheck gcovr
          cmake --preset host-quality -S path/to/your/project
          cmake --build build/quality
          ctest --test-dir build/quality --output-on-failure --output-junit test-results.xml
          cppcheck --enable=warning,style,performance,portability --error-exitcode=1 --inline-suppr --std=c11 -I path/to/your/project/include path/to/your/project/src
          gcovr --root . --filter path/to/your/project/src/ --object-directory build/quality --gcov-executable gcov-13 --xml-pretty --output build/quality/coverage.xml --fail-under-line 80
          python3 scripts/check_size.py build/arm/monitor.elf --flash 16384 --ram 4096
      - name: Optional SBOM validator dependency
        if: inputs.sbom
        run: |
          python3 -m venv .venv
          .venv/bin/python -m pip install -r scripts/requirements-sbom.txt
      - name: Package exact built firmware, optionally generating SBOM
        env:
          SBOM: ${{ inputs.sbom }}
        run: |
          if [ "$SBOM" = "true" ]; then
            .venv/bin/python scripts/package_firmware.py --sbom
          else
            python3 scripts/package_firmware.py
          fi
      - name: Retain diagnostic reports, including on failure
        if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: diagnostics-${{ github.sha }}
          path: |
            build/host/test-results.xml
            build/host/Testing/Temporary/LastTest.log
            build/quality/test-results.xml
            build/quality/coverage.xml
          if-no-files-found: warn
          retention-days: 7
      - name: Upload firmware only after all selected checks pass
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: firmware-${{ github.sha }}
          path: dist/firmware/
          if-no-files-found: error
          retention-days: 7
```

These scripts and build-configuration examples complement the workflows for a separate, simple C project using CMake and ARM GCC for compilation. Use them as reference ideas and adapt them to your existing project.

<a id="step-6-reference-ideas"></a>

<details>
<summary>Reference ideas: supporting files for a simple C project</summary>

#### Quality-check commands

The example combines native warnings/coverage, static analysis with project-specific include paths, and a target-size budget. Coverage measures executed source lines, not assertion quality or target timing. Size metrics require separate reasoning about stack, heap, alignment and reserved regions.

<div class="warning">

> **Adapt these CMake/Arm examples to your targeted project.**
>
> The quality preset requires native GCC/gcov; change the compiler/coverage integration for your host tools. For target size, use your compiler utilities, architecture/ABI, linker layout and actual firmware paths. Adapt SDK, presets and startup configuration as applicable; do not copy this sample target unchanged.

</div>

```
# Reference Ubuntu tools: cppcheck, gcovr, GCC/gcov 13.
export CC=gcc-13
cmake --preset host-quality -S path/to/your/project
cmake --build build/quality
ctest --test-dir build/quality --output-on-failure --output-junit test-results.xml
cppcheck --enable=warning,style,performance,portability --error-exitcode=1 --inline-suppr --std=c11 -I path/to/your/project/include path/to/your/project/src
gcovr --root . --filter path/to/your/project/src/ --object-directory build/quality --gcov-executable gcov-13 --xml-pretty --output build/quality/coverage.xml --fail-under-line 80
python3 scripts/check_size.py build/arm/monitor.elf --flash 16384 --ram 4096
```

The reference size check computes flash as `.text + .data` and RAM as `.data + .bss`. The optional example limits are 16,384 and 4,096 bytes. Equality passes; exceeding either fails. These are teaching budgets, not the physical device capacity or a stack-safety certificate. Choose metrics and thresholds appropriate to your target.

#### `scripts/check_size.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/check_size.py -->
```python
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
```

</details>

### Recovery and expected result

Successful integration means meaningful checks run, diagnostics survive failure, and selected gate failures block delivery. Unsupported optional tools can be left unselected with an explicit scope note. They must not be reported as passed. Restore an incorrectly configured check rather than lowering a valid threshold merely to make CI green.

</details>

<div class="important">

> **Done when selected**
>
> The chosen tools produce reviewable reports and enforce agreed thresholds. If skipped, the required build/test/release path still works unchanged.

</div>

[← Target firmware]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Optional: SBOM →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next required lab: release →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-7-main"></a>

06 / Optional / Before release

# Know what you are delivering.

Generate a software bill of materials before the versioned release. This module is independent of quality gates: choose either, both, or neither.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

[Skip to versioned release]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$).

## Starting checkpoint

Passing required tests and actual target outputs already exist. Select an approved SBOM generator that understands your project's dependency/build information, inventory scope, and customer data rules.

## Define the inventory honestly

An SBOM is a machine-readable component inventory. It is not a vulnerability scan, digital signature, provenance attestation, or completeness guarantee. A scan of a source directory alone does not establish which libraries are actually linked into firmware.

- Identify the application, linked libraries, and relevant vendor/RTOS components where your tools can establish them.
- Distinguish firmware components from build-only tools such as the compiler and generator.
- Document unresolved versions, unknown licenses, and undiscovered/proprietary components rather than inventing answers.
- Select an accepted output format: SPDX JSON or CycloneDX JSON, with an explicit schema version.

## Reference example: scoped SPDX 2.3 JSON

The example generator inventories an explicit list of application/header/startup/linker files with hashes, records the ELF checksum and source commit, and declares unknown licenses `NOASSERTION`. It does not discover external dependencies and must not be used unchanged to describe your firmware. Use approved dependency-aware tooling for your project's SDKs, RTOSes, vendor libraries, and other linked components, and document the resulting inventory scope.

The complete package/SBOM generator, validator and optional requirements file are included in the solution checkpoint below. Copy them into the indicated paths in your own repository only after adapting their paths and inventory, or substitute approved project tooling.

```bash
# Use the same already-built firmware and passing test report.
python3 -m pip install -r scripts/requirements-sbom.txt
python3 scripts/package_firmware.py --sbom
python3 scripts/validate_sbom.py dist/firmware/sbom.spdx.json
```

The validator checks the official SPDX 2.3 JSON schema pinned to an immutable specification commit and checksum. Packaging additionally checks source/ELF identity and internal relationships. Schema validity alone does not prove the inventory is complete.

## Associate it with the release

1. Generate the inventory from the same commit/build inputs as the target firmware, before publishing.
2. Record generator/version, source commit, inventory scope, and firmware checksum.
3. Validate the document format and verify the source/package association.
4. Include `sbom.spdx.json` as a release asset and in the delivery bundle's checksums.

```
jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: false
      sbom: true
```

If the selected generator or validation fails, this configured run must not publish. If the module is deliberately disabled, the release must not depend on a missing SBOM artifact or claim that one was generated.

The full CI caller and reusable firmware-build implementation are also included in this lab's solution checkpoint.

<div class="task">

> **Customer activity: inventory review**
>
> Choose a known firmware dependency and find its name/version/license evidence in your generator's output. Explain what you would do if it were missing. Review whether customer policy permits storing the inventory with release assets; do not upload source to an external analysis service without approval.

</div>

<a id="step-7-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed optional SBOM configuration

Manually dispatch Firmware CI with SBOM enabled; quality is independently selectable. The complete generation, validation and package code is below. Replace the fixed reference inventory with your approved component-aware tooling and actual project scope. The compiler setup from lab 4 is unchanged. SBOM failures block this configured run; skipping SBOM leaves its tools and artifacts unnecessary.

#### `.github/workflows/ci.yml`

<!-- source: examples/workflows/04-full-ci.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# If the project is at the repository root, use '**' for its path filter.
name: Firmware CI
on:
  pull_request:
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  push:
    branches: ['workshop/**']
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  workflow_dispatch:
    inputs:
      quality:
        description: Enable optional quality gates
        type: boolean
        default: false
      sbom:
        description: Generate an optional pre-release SPDX SBOM
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: ${{ inputs.quality == true }}
      sbom: ${{ inputs.sbom == true }}
```

#### `.github/workflows/firmware-build.yml`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: examples/workflows/04-full-build.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# Adapt presets, include/source directories, output paths and tools to that project.
name: Reusable firmware build
on:
  workflow_call:
    inputs:
      quality:
        type: boolean
        default: false
      sbom:
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  firmware:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Install reference host tools
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13 python3-venv
      - name: Install verified reference target compiler
        run: |
          python3 scripts/install_arm.py
          echo "$GITHUB_WORKSPACE/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin" >> "$GITHUB_PATH"
      - name: Native configure, build and test
        env:
          CC: gcc-13
        # Adapt this CMake setup to your project; host tests require a host compiler.
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --output-junit test-results.xml
      - name: Target firmware
        # Adapt the Arm/CMake toolchain, SDK, CPU/ABI, startup, linker map and paths to your target project.
        run: |
          cmake --preset arm -S path/to/your/project
          cmake --build build/arm
      - name: Optional quality gates
        if: inputs.quality
        env:
          CC: gcc-13
        # Adapt host coverage and target size tools to the project's actual toolchains.
        run: |
          sudo apt-get install -y cppcheck gcovr
          cmake --preset host-quality -S path/to/your/project
          cmake --build build/quality
          ctest --test-dir build/quality --output-on-failure --output-junit test-results.xml
          cppcheck --enable=warning,style,performance,portability --error-exitcode=1 --inline-suppr --std=c11 -I path/to/your/project/include path/to/your/project/src
          gcovr --root . --filter path/to/your/project/src/ --object-directory build/quality --gcov-executable gcov-13 --xml-pretty --output build/quality/coverage.xml --fail-under-line 80
          python3 scripts/check_size.py build/arm/monitor.elf --flash 16384 --ram 4096
      - name: Optional SBOM validator dependency
        if: inputs.sbom
        run: |
          python3 -m venv .venv
          .venv/bin/python -m pip install -r scripts/requirements-sbom.txt
      - name: Package exact built firmware, optionally generating SBOM
        env:
          SBOM: ${{ inputs.sbom }}
        run: |
          if [ "$SBOM" = "true" ]; then
            .venv/bin/python scripts/package_firmware.py --sbom
          else
            python3 scripts/package_firmware.py
          fi
      - name: Retain diagnostic reports, including on failure
        if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: diagnostics-${{ github.sha }}
          path: |
            build/host/test-results.xml
            build/host/Testing/Temporary/LastTest.log
            build/quality/test-results.xml
            build/quality/coverage.xml
          if-no-files-found: warn
          retention-days: 7
      - name: Upload firmware only after all selected checks pass
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: firmware-${{ github.sha }}
          path: dist/firmware/
          if-no-files-found: error
          retention-days: 7
```

#### `scripts/package_firmware.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/package_firmware.py -->
```python
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


def make_sbom(commit, elf_sha, created, source=None):
    source = SOURCE if source is None else source
    files = []
    for number, name in enumerate(INVENTORY, 1):
        files.append({
            "SPDXID": f"SPDXRef-File-{number}",
            "fileName": f"./{name}",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256(source / name)},
                {"algorithm": "SHA1", "checksumValue": hashlib.sha1((source / name).read_bytes()).hexdigest()},
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
                    "".join(sorted(hashlib.sha1((source / name).read_bytes()).hexdigest()
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
    parser.add_argument("--source", type=Path, default=SOURCE,
                        help="Reference source directory for the optional SBOM inventory")
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
            source = (ROOT / args.source).resolve()
            sbom_path.write_text(json.dumps(make_sbom(commit, firmware["monitor.elf"], created, source), indent=2) + "\n",
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
```

#### `scripts/validate_sbom.py`

<!-- source: scripts/validate_sbom.py -->
```python
"""Validate SPDX 2.3 JSON with a pinned official schema and fixture semantics."""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

SCHEMA_URL = (
    "https://raw.githubusercontent.com/spdx/spdx-spec/"
    "aadf3b0b8dbbabdb4d880b0fc714255fea436ff7/schemas/spdx-schema.json"
)
SCHEMA_SHA256 = "239208b7ac287b3cf5d9a9af23f9d69863971102a5e1587a27a398b43490b89b"


def check_identity(document, commit, elf_sha):
    package = document["packages"][0]
    if package["versionInfo"] != commit:
        raise ValueError("SBOM source commit does not match manifest")
    expected = {"algorithm": "SHA256", "checksumValue": elf_sha}
    if expected not in package["checksums"]:
        raise ValueError("SBOM firmware hash does not match manifest")
    if not document["files"]:
        raise ValueError("SBOM contains no source inventory")
    identifiers = {document["SPDXID"]}
    identifiers.update(item["SPDXID"] for item in document["packages"])
    identifiers.update(item["SPDXID"] for item in document["files"])
    if len(identifiers) != 1 + len(document["packages"]) + len(document["files"]):
        raise ValueError("SBOM SPDX identifiers must be unique")
    for relation in document["relationships"]:
        if relation["spdxElementId"] not in identifiers or relation["relatedSpdxElement"] not in identifiers:
            raise ValueError("SBOM relationship references a missing element")


def validate(path):
    import jsonschema

    document = json.loads(path.read_text(encoding="utf-8"))
    with urllib.request.urlopen(SCHEMA_URL, timeout=60) as response:
        schema_bytes = response.read()
    if hashlib.sha256(schema_bytes).hexdigest() != SCHEMA_SHA256:
        raise ValueError("Official SPDX schema checksum mismatch")
    jsonschema.Draft7Validator(json.loads(schema_bytes)).validate(document)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sbom", type=Path)
    args = parser.parse_args()
    validate(args.sbom)
    print("SPDX 2.3 JSON schema validation passed")


if __name__ == "__main__":
    main()
```

#### `scripts/requirements-sbom.txt`

<!-- source: scripts/requirements-sbom.txt -->
```
# Optional official SPDX JSON-schema validation.
jsonschema==4.23.0
```

### Recovery and expected result

A useful result is a schema-valid inventory tied to the actual release inputs, with explicit limitations. In the reference SPDX document, `SPDXRef-Firmware` carries the ELF SHA-256 and source commit; source-file records connect through `CONTAINS` relationships. A wrong firmware hash or malformed document must fail validation, not be silently omitted.

</details>

<div class="important">

> **Done when selected**
>
> The SBOM is validated, associated with the firmware commit/hash, and staged for the same release. You can explain both what it inventories and what it does not prove.

</div>

[← Target firmware]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: versioned release →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-8-main"></a>

07 / Required / Continuous delivery

# Release the package you validated.

A release should answer: which source, which compiler, which binary, and which evidence? Do not rebuild after validation or promote an arbitrary “latest” artifact.

## Purpose

Deliver a versioned package of your validated firmware with traceable source, build and test evidence. Verify the release assets using your project's approved tools and formats, without treating publication as device deployment or hardware validation.

## Starting checkpoint

Required builds/tests pass and the test-only exercise is fully restored. Optional quality gates and SBOM generation have been selected or explicitly skipped. Customer-approved tag/release permissions and non-production trigger boundaries are confirmed.

## Customer activities: release exercise

<div class="task">

> 1. Inspect the existing customer tag/release/deployment triggers with the facilitator. Use a namespace that cannot invoke production automation.
> 2. Define the package contents, versioning policy and source/build metadata for your own project. Use the actual target artifacts and do not rebuild them after validation.
> 3. Reuse the build/test workflow from the previous labs. Extend its packaging and artifact-output interface where needed so the release can consume the validated package; do not recreate the CI workflow.
> 4. Review and merge the appropriate workflow changes under customer policy; verify the restored test diff before tagging. Confirm the selected optional checks and release trigger before starting the run.
> 5. Create and push an approved workshop tag only when authorized. Observe the validation and publisher jobs for the same commit and workflow run.
> 6. Download the release assets inside the approved environment. Use your project's approved verification tool to check their integrity and confirm that the package metadata identifies the intended source commit, target and compiler.
> 7. If SBOM is enabled, inspect its firmware hash/commit association. If disabled, verify no missing-SBOM dependency blocks release.
> 8. Explain what would prevent publication if lab 3's assertion failed again. Inspect the publisher's dependencies and normal step failure propagation rather than masking failures.

</div>

If customer policy prohibits release publication, use customer-approved packaging and verification tools locally and record that the hosted publication checkpoint was not performed. Do not bypass policy to claim completion.

<a id="step-8-solution"></a>

<details>
<summary>Solution and recovery checkpoint</summary>

### Completed release workflow

The new workflow in this checkpoint is `.github/workflows/release.yml`. Keep the CI caller and reusable build/test workflow created in the previous labs; they are not repeated here. Adapt their release interface only where the contract below requires it. Required tests must pass and the original test expectation must be restored. Quality and SBOM remain independent opt-ins. Review existing tag/deployment triggers and customer release policy before publishing.

The reusable workflow runs required tests and target compilation, then any selected optional modules, then packages the exact outputs. The publisher depends on validation and only receives write permission in its own job.

### Contract with your existing reusable workflow

- The release calls your existing `.github/workflows/firmware-build.yml` for the tagged commit, not a separate CI run.
- Align its declared `workflow_call` inputs with the release caller's `quality` and `sbom` booleans. Keep skipped modules disabled, and reject a selected option if its checks are not implemented rather than reporting it as passed.
- After required and selected checks succeed, the reusable workflow must package the already-built outputs and upload `firmware-<source SHA>` in that same run. The reference package contains firmware outputs, `manifest.json` and `SHA256SUMS`, plus the SBOM only when selected.
- If you followed only the core lab 4 checkpoint, its `target-build-<source SHA>` artifact contains raw outputs, not this release package. Keep its build/test steps, add the packaging/upload integration and align the inputs before using the release workflow. Do not merely rename the raw artifact or duplicate the CI pipeline.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

### How the reference release workflow connects the checks

1. Validate an existing tag matches the safe reference pattern `workshop-vMAJOR.MINOR.PATCH`. A branch dispatch is rejected.
2. Check out that tag's commit and run the same required builds/tests, plus selected optional modules. The tag is revalidated rather than borrowing a green result from another commit.
3. Create ELF/BIN/map, `manifest.json`, and `SHA256SUMS`; add the validated SBOM when enabled.
4. Upload the immutable run artifact named `firmware-<source SHA>`.
5. Download that named artifact **from this same workflow run**, verify all checksums, and compare the manifest's clean source identity to the checked-out tag commit.
6. Create a workshop prerelease. Do not overwrite an existing release or silently replace its assets.

The reference's tag-push path uses both optional modules off. To select them for a release, dispatch **Firmware release** against an existing matching tag with the desired boolean inputs. Manual dispatch requires the workflow on the default branch. Avoid racing an automatic tag release: choose the exercise route before creating the tag, or adapt the caller's fixed options before the tag is created. Existing releases are never clobbered.

#### `.github/workflows/release.yml`

<!-- source: .github/workflows/release.yml -->
```yaml
name: Firmware release
on:
  push:
    tags: ['workshop-v*']
  workflow_dispatch:
    inputs:
      quality:
        description: Enable optional quality gates
        type: boolean
        default: false
      sbom:
        description: Generate optional SBOM before publishing
        type: boolean
        default: false

permissions:
  contents: read

concurrency:
  group: firmware-release-${{ github.ref }}
  cancel-in-progress: false

jobs:
  tag:
    runs-on: ubuntu-24.04
    timeout-minutes: 5
    steps:
      - name: Require an existing workshop version tag
        env:
          REF_TYPE: ${{ github.ref_type }}
          REF_NAME: ${{ github.ref_name }}
        run: |
          python3 - <<'PY'
          import os, re
          if os.environ["REF_TYPE"] != "tag" or not re.fullmatch(r"workshop-v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", os.environ["REF_NAME"]):
              raise SystemExit("Select an existing workshop-vMAJOR.MINOR.PATCH tag, not a branch.")
          PY
  validate:
    needs: tag
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: ${{ inputs.quality == true }}
      sbom: ${{ inputs.sbom == true }}
  publish:
    needs: validate
    runs-on: ubuntu-24.04
    timeout-minutes: 10
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - uses: actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093 # v4
        with:
          name: firmware-${{ github.sha }}
          path: release-assets
      - name: Verify package identity and checksums without rebuilding
        run: |
          python3 scripts/package_firmware.py --verify release-assets
          python3 - <<'PY'
          import json, os, subprocess
          from pathlib import Path
          manifest = json.loads(Path("release-\assets/manifest.json").read_text())
          head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
          if manifest["dirty"] or manifest["commit"] != head:
              raise SystemExit("Release package is dirty or does not match the tagged commit.")
          PY
      - name: Publish immutable workshop prerelease
        env:
          GH_TOKEN: ${{ github.token }}
          GH_REPO: ${{ github.repository }}
          TAG: ${{ github.ref_name }}
        run: |
          gh release create "$TAG" release-\assets/* --verify-tag --prerelease --title "$TAG" --notes "Workshop firmware delivery only. Not hardware-validated or deployed. Checksums and source/toolchain identity are included."
```

These release-verification scripts complement the workflows for a separate, simple C project using CMake and ARM GCC for compilation. Use them as reference ideas and adapt them to your existing project; the compiler setup, size checks and build configuration remain in the earlier labs.

<a id="step-8-reference-ideas"></a>

<details>
<summary>Reference ideas: supporting files for a simple C project</summary>

#### Local package verification for the reference C project

This command uses the reference package format and Python helper below. It checks that example's expected files, checksums and metadata; it is not a universal verifier for customer firmware packages. Use your own project's approved verification tool, or adapt the helper and paths to your package.

```
# No compilation or publication occurs in this verification command.
python3 scripts/package_firmware.py --verify dist/firmware
```

#### `scripts/package_firmware.py`

<div class="warning">

> **Adapt the toolchain to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/artifact paths as applicable. Native tests use a host compiler. Arm and the sample paths are references, not required customer settings.

</div>

<!-- source: scripts/package_firmware.py -->
```python
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


def make_sbom(commit, elf_sha, created, source=None):
    source = SOURCE if source is None else source
    files = []
    for number, name in enumerate(INVENTORY, 1):
        files.append({
            "SPDXID": f"SPDXRef-File-{number}",
            "fileName": f"./{name}",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256(source / name)},
                {"algorithm": "SHA1", "checksumValue": hashlib.sha1((source / name).read_bytes()).hexdigest()},
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
                    "".join(sorted(hashlib.sha1((source / name).read_bytes()).hexdigest()
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
    parser.add_argument("--source", type=Path, default=SOURCE,
                        help="Reference source directory for the optional SBOM inventory")
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
            source = (ROOT / args.source).resolve()
            sbom_path.write_text(json.dumps(make_sbom(commit, firmware["monitor.elf"], created, source), indent=2) + "\n",
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
```

#### `scripts/validate_sbom.py`

<!-- source: scripts/validate_sbom.py -->
```python
"""Validate SPDX 2.3 JSON with a pinned official schema and fixture semantics."""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

SCHEMA_URL = (
    "https://raw.githubusercontent.com/spdx/spdx-spec/"
    "aadf3b0b8dbbabdb4d880b0fc714255fea436ff7/schemas/spdx-schema.json"
)
SCHEMA_SHA256 = "239208b7ac287b3cf5d9a9af23f9d69863971102a5e1587a27a398b43490b89b"


def check_identity(document, commit, elf_sha):
    package = document["packages"][0]
    if package["versionInfo"] != commit:
        raise ValueError("SBOM source commit does not match manifest")
    expected = {"algorithm": "SHA256", "checksumValue": elf_sha}
    if expected not in package["checksums"]:
        raise ValueError("SBOM firmware hash does not match manifest")
    if not document["files"]:
        raise ValueError("SBOM contains no source inventory")
    identifiers = {document["SPDXID"]}
    identifiers.update(item["SPDXID"] for item in document["packages"])
    identifiers.update(item["SPDXID"] for item in document["files"])
    if len(identifiers) != 1 + len(document["packages"]) + len(document["files"]):
        raise ValueError("SBOM SPDX identifiers must be unique")
    for relation in document["relationships"]:
        if relation["spdxElementId"] not in identifiers or relation["relatedSpdxElement"] not in identifiers:
            raise ValueError("SBOM relationship references a missing element")


def validate(path):
    import jsonschema

    document = json.loads(path.read_text(encoding="utf-8"))
    with urllib.request.urlopen(SCHEMA_URL, timeout=60) as response:
        schema_bytes = response.read()
    if hashlib.sha256(schema_bytes).hexdigest() != SCHEMA_SHA256:
        raise ValueError("Official SPDX schema checksum mismatch")
    jsonschema.Draft7Validator(json.loads(schema_bytes)).validate(document)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sbom", type=Path)
    args = parser.parse_args()
    validate(args.sbom)
    print("SPDX 2.3 JSON schema validation passed")


if __name__ == "__main__":
    main()
```

</details>

### Recovery and expected result

Correct assets have matching checksums and source identity, and selected checks succeeded before publication. A dirty source manifest, wrong commit, corrupt/missing file, invalid tag, or existing release must stop the relevant operation. Checksums detect changes; they are not signatures or proof of a trusted producer.

</details>

<div class="important">

> **Done when**
>
> You have an approved versioned firmware release with traceable assets, or an explicitly recorded publishing restriction. You have not flashed, deployed, or hardware-validated a device.

</div>

[← Target firmware]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Next: from release to device →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=9&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-9-main"></a>

Required discussion / No device operation

# A release is not a deployed device.

Your pipeline has delivered a package. It has not demonstrated bootability, peripheral correctness, real-time behavior, or safe recovery on physical hardware.

| Evidence | What it supports | What it does not prove |
| --- | --- | --- |
| Host unit tests | Logic for the tested host inputs/assertions | Interrupts, peripherals, device compiler behavior |
| Target build/link | Compilation and section placement for that configuration | Boot, electrical behavior, timing |
| Optional static/coverage/size checks | Defined diagnostics and measured thresholds | Complete correctness or stack safety |
| Optional SBOM | A documented component inventory | Vulnerability clearance or completeness without scope evidence |
| Release checksums | Downloaded bytes match recorded digests | Trusted origin or compatible/safe deployment |

## Where HIL belongs

An approved trusted-source job can request an isolated hardware lane after software checks. It must identify the exact device, serialize access, flash a compatible package, reset it, collect bounded serial/assertion results, and retain logs even on failure. Define timeouts and a recovery procedure before unattended operation.

<div class="warning">

> **Protect the runner and device network.**
>
> Do not execute untrusted PR code on a persistent self-hosted runner connected to hardware. Prefer isolated, controlled infrastructure for trusted refs. An environment approval alone does not isolate a compromised runner. Feature availability depends on the customer's GitHub plan and repository visibility.

</div>

## Safe deployment is target-specific

1. Verify hardware revision, bootloader compatibility, image layout, authenticity, and customer policy.
2. Select the exact validated package; do not rebuild or select an ambiguous latest version.
3. Require the applicable approval and service/maintenance conditions.
4. Use a bootloader/update mechanism that can tolerate interrupted updates.
5. Observe post-update boot/health criteria. Roll back only if the device architecture and policy actually support it.

<div class="task">

> **Customer discussion: review a deployment incident**
>
> A checksum matches, but the device never boots. Which assumptions might be wrong? Consider board revision, memory layout, ABI, startup, bootloader, power interruption, and peripheral initialization. Identify which additional test could supply evidence for each assumption.

</div>

## Core workshop completion

You can explain the customer build/test pipeline, show the required test-only failure/restoration, identify target artifacts and source identity, and distinguish delivery from deployment. Optional labs do not determine core completion. A blocked customer publication step must remain explicitly documented.

The release workflow and release-verification references are included directly in lab 7's solution checkpoint. It reuses the CI/build workflows from the earlier labs rather than repeating them. No separate solution page is needed.

[Explore optional next topics]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=13&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) or [return to the learning journey]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$).

## Authoritative references

- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [Deployments, environments, and feature constraints](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)

[← Versioned release]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Optional extensions →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=13&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-10-main"></a>

Recovery guide

# Diagnose the layer that failed.

Keep the original error and source commit. Do not turn a failure into success by suppressing the evidence.

<details open>
<summary>Workflow does not start / no Run workflow button</summary>

Check branch/path filters and Actions policy. Manual dispatch requires the workflow on the default branch; a new workshop-branch workflow may need an approved push/PR event first. Reusable workflows need a caller and `workflow_call`, not their own manual button.

</details>

<details>
<summary>CMake uses the wrong compiler or cannot find the SDK</summary>

**Adapt the toolchain to your targeted project:** verify compiler/version, SDK/sysroot, CPU/ABI/FPU flags, startup files, linker map, presets, runner PATH and license access. Use a new build directory when changing toolchains. Host tests need a host compiler; the sample Arm toolchain is not universal. Do not delete customer-owned directories blindly.

</details>

<details>
<summary>Target ELF cannot execute on the runner</summary>

The device executable is not a host test. Use a native test build, or a separately supported emulator/HIL setup. Do not relabel an unexecuted target build as a passed test. Adapt CMake/toolchain configuration to distinguish host and actual target outputs.

</details>

<details>
<summary>CTest says no tests found</summary>

Check test registration, build directory and command mapping. “No tests found” is not passing test evidence. The reference package script rejects an empty test report. Restore actual test execution before continuing.

</details>

<details>
<summary>The required intentional failure failed for the wrong reason</summary>

A compile/license/network error is not the expected test assertion. Return to the recorded baseline, confirm the test executes, and change only its expectation. Restore the exact original assertion afterward; do not change production firmware logic, skip the test, or mask its exit code.

</details>

<details>
<summary>Report missing after a failed test</summary>

Use an always-run artifact step and the actual report path. Inspect test runner output to confirm it wrote a file. Artifact retention must not erase the test failure. Do not upload broad workspace globs containing customer secrets.

</details>

<details>
<summary>Optional coverage or size tool fails</summary>

When selected, the module must fail visibly. Check the matching host compiler/gcov versions, supported source scope, and target size utility/sections. **Adapt the CMake/Arm toolchain and reporting to your targeted project.** If not selected, the core must have no dependency on its report. Preserve customer-required checks.

</details>

<details>
<summary>SBOM validation or inventory is incomplete</summary>

Check schema version, required fields, commit/firmware hashes, generator scope, and network access to the pinned schema. Document unknown components/licenses rather than inventing them. A valid schema is not inventory completeness. If SBOM is selected, validation failure blocks publication.

</details>

<details>
<summary>Release fails or has the wrong artifact</summary>

Select an existing safe workshop version tag, not a branch. Ensure the named artifact is from the same run/source SHA, not another CI run. Compare manifest identity and checksums. Existing releases are intentionally not overwritten; do not force-update production tags. The publisher needs customer-approved write permission.

</details>

<details>
<summary>MOAW navigation or code-copy buttons unavailable</summary>

MOAW uses JavaScript to render the workshop and navigate between steps. If it cannot load, check browser scripting and network access with the facilitator. The source Markdown remains readable on GitHub, and the original static HTML edition remains available separately. If only the copy button is unavailable, select the code and copy it manually. This edition does not implement the original site's browser-local completion tracking; do not treat navigation or copied code as completion evidence.

</details>

## Recovery checkpoints

Use the embedded [first-build]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-first-build) and [test checkpoints]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-tests) to compare structure, not to overwrite customer automation. The complete [CI]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci), [reusable build]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build), and [release examples]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-release), plus all [supporting scripts]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-supporting-files), are available in this workshop without source-repository access. After a failure, retain its run/commit/test identity and restore only the deliberate workshop change.

[Workshop home]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Revisit preflight]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=1&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-11-main"></a>

Copyable reference / No workshop repository access needed

# Complete examples, right here.

Read and copy the full workflow examples directly from this workshop. All supporting scripts used by these examples are included below. No access to the workshop's source repository is required.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

Create or merge these files in **your own existing project**, using the destination paths shown. Review existing workflows before editing; do not overwrite customer automation. Copy buttons are a convenience: without JavaScript, select the code and copy it manually.

<div class="warning">

> **Reference code must be adapted, not adopted blindly.**
>
> The source placeholder `path/to/your/project` must point to your existing project. The `build/host` and `build/arm` output paths and preset names are references too. The supporting scripts are ideas from a separate, simple C project: adapt their output paths, target description and fixed source inventory, or substitute approved customer tooling. In particular, do not use the example SBOM inventory unchanged for your project.

</div>

[1. First build]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-first-build)[2. Tests]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-tests)[3. Lab 4 checkpoint]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-target-build-checkpoint)[4. Final CI caller]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci)[5. Final reusable build]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build)[6. Release]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-release)[Supporting scripts]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-supporting-files)

<a id="step-11-first-build"></a>

## 1. First-build checkpoint

Save as an approved file such as `.github/workflows/workshop-first-build.yml`. Start here in [lab 2]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=3&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$). Manual dispatch requires the workflow on the default branch; otherwise use approved workshop-branch push/PR triggers.

<div class="warning">

> **Adapt the CMake/toolchain to your targeted project.**
>
> Choose your runner, compiler/version, SDK and source/build paths. Host builds use a host compiler. For target compilation, adapt CPU/ABI flags, startup, linker map and presets too.

</div>

<!-- source: examples/workflows/01-first-ci.yml -->
```yaml
# Teaching checkpoint; copy/adapt into your CUSTOMER repository after reviewing existing workflows.
# Adapt CMake compiler/SDK, presets, runner and paths to your target project.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
name: Workshop first build
on:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  build:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13
      - name: Reference native build - adapt host compiler and CMake paths
        env:
          CC: gcc-13
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
```

<a id="step-11-tests"></a>

## 2. Build-and-test checkpoint

Save as an approved file such as `.github/workflows/workshop-tests.yml`. Use this checkpoint in [lab 3]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=4&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$); keep the intended assertion failure visible while retaining its report.

<div class="warning">

> **Adapt these CMake commands to your project's toolchain.**
>
> Use your actual host compiler, presets, paths, test command and report location. Keep target compiler/SDK, architecture/ABI, startup and linker configuration separate from native test execution.

</div>

<!-- source: examples/workflows/02-tests.yml -->
```yaml
# Teaching checkpoint; adapt existing customer workflows rather than overwriting them.
# Adapt CMake toolchain/presets/paths; native tests need a host compiler.
name: Workshop build and tests
on:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13
      - name: Native build and real tests - adapt toolchain to your project
        env:
          CC: gcc-13
        run: |
          # REQUIRED: replace this placeholder with your repository-relative project path.
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --output-junit test-results.xml
      - if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: workshop-test-report
          path: build/host/test-results.xml
          if-no-files-found: warn
```

<a id="step-11-target-build-checkpoint"></a>

## 3. Lab 4 target-build checkpoint

These two files implement required host tests, target compilation and artifact retention only. They do not include optional quality or SBOM inputs or steps, packaging, or release publication. Save or merge them into the destination paths shown below. Later labs extend this checkpoint; the final combined workflows follow it in this reference library.

### `.github/workflows/ci.yml`

<!-- source: examples/workflows/03-target-ci.yml -->
```yaml
# Lab 4 checkpoint: save or merge as .github/workflows/ci.yml.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# If the project is at the repository root, use '**' for its path filter.
name: Firmware CI
on:
  pull_request:
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  push:
    branches: ['workshop/**']
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
```

### `.github/workflows/firmware-build.yml`

<div class="warning">

> **Adapt the CMake/ARM GCC setup to your targeted project.**
>
> Change compiler/version, SDK, target CPU/ABI flags, startup and linker configuration, presets, runner and source/build/artifact paths. Native tests need a host compiler. The target compiler helper is only a reference.

</div>

<!-- source: examples/workflows/03-target-build.yml -->
```yaml
# Lab 4 checkpoint: save or merge as .github/workflows/firmware-build.yml.
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# Adapt compiler/SDK, presets, runner and source/build/artifact paths to your target.
name: Reusable firmware build
on:
  workflow_call:

permissions:
  contents: read

jobs:
  firmware:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Install reference host tools
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13 python3
      - name: Install verified reference target compiler
        run: |
          python3 scripts/install_arm.py
          echo "$GITHUB_WORKSPACE/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin" >> "$GITHUB_PATH"
      - name: Native configure, build and test
        env:
          CC: gcc-13
        # Host tests use a host compiler; adapt this CMake setup to your project.
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --no-tests=error --output-junit test-results.xml
      - name: Target firmware
        # Adapt Arm GCC, SDK, CPU/ABI, startup and linker configuration to your target.
        run: |
          cmake --preset arm -S path/to/your/project
          cmake --build build/arm
      - name: Verify the expected target outputs
        # Replace these filenames and formats with your project's actual outputs.
        run: |
          test -s build/arm/monitor.elf
          test -s build/arm/monitor.bin
          test -s build/arm/monitor.map
      - name: Retain diagnostic reports, including on failure
        if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: diagnostics-${{ github.sha }}
          path: |
            build/host/test-results.xml
            build/host/Testing/Temporary/LastTest.log
          if-no-files-found: warn
          retention-days: 7
      - name: Upload target outputs after required checks pass
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: target-build-${{ github.sha }}
          path: |
            build/arm/monitor.elf
            build/arm/monitor.bin
            build/arm/monitor.map
          if-no-files-found: error
          retention-days: 7
```

<a id="step-11-ci"></a>

## 4. Final CI caller

Save as `.github/workflows/ci.yml`, or merge into the existing caller. Copy the [reusable workflow]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build) into the same customer repository too. Adapt branch and path filters to the customer's existing project.

<!-- source: examples/workflows/04-full-ci.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# If the project is at the repository root, use '**' for its path filter.
name: Firmware CI
on:
  pull_request:
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  push:
    branches: ['workshop/**']
    paths:
      - 'path/to/your/project/**'
      - 'scripts/**'
      - '.github/workflows/**'
  workflow_dispatch:
    inputs:
      quality:
        description: Enable optional quality gates
        type: boolean
        default: false
      sbom:
        description: Generate an optional pre-release SPDX SBOM
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: ${{ inputs.quality == true }}
      sbom: ${{ inputs.sbom == true }}
```

<a id="step-11-firmware-build"></a>

## 5. Final reusable firmware build

Save as `.github/workflows/firmware-build.yml`. Both the CI and release callers use this file from **your repository**, not from the workshop repository. Required builds/tests run first; quality gates and SBOM are independent opt-ins before packaging. Supporting scripts are provided [below]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-supporting-files).

<div class="warning">

> **Adapt every CMake/Arm build step to your targeted project.**
>
> Replace the compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner, source/build/artifact paths, analysis tools and thresholds. Native tests use a host compiler. Arm is illustrative, not the required customer target.

</div>

<!-- source: examples/workflows/04-full-build.yml -->
```yaml
# REQUIRED: replace path/to/your/project with your repository-relative source path.
# Adapt presets, include/source directories, output paths and tools to that project.
name: Reusable firmware build
on:
  workflow_call:
    inputs:
      quality:
        type: boolean
        default: false
      sbom:
        type: boolean
        default: false

permissions:
  contents: read

jobs:
  firmware:
    runs-on: ubuntu-24.04
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - name: Install reference host tools
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build gcc-13 python3-venv
      - name: Install verified reference target compiler
        run: |
          python3 scripts/install_arm.py
          echo "$GITHUB_WORKSPACE/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin" >> "$GITHUB_PATH"
      - name: Native configure, build and test
        env:
          CC: gcc-13
        # Adapt this CMake setup to your project; host tests require a host compiler.
        run: |
          cmake --preset host -S path/to/your/project
          cmake --build build/host
          ctest --test-dir build/host --output-on-failure --output-junit test-results.xml
      - name: Target firmware
        # Adapt the Arm/CMake toolchain, SDK, CPU/ABI, startup, linker map and paths to your target project.
        run: |
          cmake --preset arm -S path/to/your/project
          cmake --build build/arm
      - name: Optional quality gates
        if: inputs.quality
        env:
          CC: gcc-13
        # Adapt host coverage and target size tools to the project's actual toolchains.
        run: |
          sudo apt-get install -y cppcheck gcovr
          cmake --preset host-quality -S path/to/your/project
          cmake --build build/quality
          ctest --test-dir build/quality --output-on-failure --output-junit test-results.xml
          cppcheck --enable=warning,style,performance,portability --error-exitcode=1 --inline-suppr --std=c11 -I path/to/your/project/include path/to/your/project/src
          gcovr --root . --filter path/to/your/project/src/ --object-directory build/quality --gcov-executable gcov-13 --xml-pretty --output build/quality/coverage.xml --fail-under-line 80
          python3 scripts/check_size.py build/arm/monitor.elf --flash 16384 --ram 4096
      - name: Optional SBOM validator dependency
        if: inputs.sbom
        run: |
          python3 -m venv .venv
          .venv/bin/python -m pip install -r scripts/requirements-sbom.txt
      - name: Package exact built firmware, optionally generating SBOM
        env:
          SBOM: ${{ inputs.sbom }}
        run: |
          if [ "$SBOM" = "true" ]; then
            .venv/bin/python scripts/package_firmware.py --sbom
          else
            python3 scripts/package_firmware.py
          fi
      - name: Retain diagnostic reports, including on failure
        if: always()
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: diagnostics-${{ github.sha }}
          path: |
            build/host/test-results.xml
            build/host/Testing/Temporary/LastTest.log
            build/quality/test-results.xml
            build/quality/coverage.xml
          if-no-files-found: warn
          retention-days: 7
      - name: Upload firmware only after all selected checks pass
        uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4
        with:
          name: firmware-${{ github.sha }}
          path: dist/firmware/
          if-no-files-found: error
          retention-days: 7
```

<a id="step-11-release"></a>

## 6. Versioned release

Save as `.github/workflows/release.yml`. It calls the reusable workflow above and uses the package helper below. Review existing customer tag/deployment triggers first. The example creates prereleases only and will not overwrite an existing release. Manual option selection must target an existing matching tag; select the exercise route before creating a tag to avoid racing its automatic release.

<!-- source: .github/workflows/release.yml -->
```yaml
name: Firmware release
on:
  push:
    tags: ['workshop-v*']
  workflow_dispatch:
    inputs:
      quality:
        description: Enable optional quality gates
        type: boolean
        default: false
      sbom:
        description: Generate optional SBOM before publishing
        type: boolean
        default: false

permissions:
  contents: read

concurrency:
  group: firmware-release-${{ github.ref }}
  cancel-in-progress: false

jobs:
  tag:
    runs-on: ubuntu-24.04
    timeout-minutes: 5
    steps:
      - name: Require an existing workshop version tag
        env:
          REF_TYPE: ${{ github.ref_type }}
          REF_NAME: ${{ github.ref_name }}
        run: |
          python3 - <<'PY'
          import os, re
          if os.environ["REF_TYPE"] != "tag" or not re.fullmatch(r"workshop-v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", os.environ["REF_NAME"]):
              raise SystemExit("Select an existing workshop-vMAJOR.MINOR.PATCH tag, not a branch.")
          PY
  validate:
    needs: tag
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: ${{ inputs.quality == true }}
      sbom: ${{ inputs.sbom == true }}
  publish:
    needs: validate
    runs-on: ubuntu-24.04
    timeout-minutes: 10
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262 # v4
      - uses: actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093 # v4
        with:
          name: firmware-${{ github.sha }}
          path: release-assets
      - name: Verify package identity and checksums without rebuilding
        run: |
          python3 scripts/package_firmware.py --verify release-assets
          python3 - <<'PY'
          import json, os, subprocess
          from pathlib import Path
          manifest = json.loads(Path("release-\assets/manifest.json").read_text())
          head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
          if manifest["dirty"] or manifest["commit"] != head:
              raise SystemExit("Release package is dirty or does not match the tagged commit.")
          PY
      - name: Publish immutable workshop prerelease
        env:
          GH_TOKEN: ${{ github.token }}
          GH_REPO: ${{ github.repository }}
          TAG: ${{ github.ref_name }}
        run: |
          gh release create "$TAG" release-\assets/* --verify-tag --prerelease --title "$TAG" --notes "Workshop firmware delivery only. Not hardware-validated or deployed. Checksums and source/toolchain identity are included."
```

<a id="step-11-supporting-files"></a>

## Supporting files used by the workflows

Copy these scripts into the matching `scripts` paths in your own repository, or replace their calls with equivalent approved project tooling. Python 3.12+ is the reference runtime. No workshop repository access is needed to obtain this code.

**Adapt paths and inventory:** the package helper's `SOURCE`, `INVENTORY`, firmware filenames, target description and test-report path describe the reference configuration, not your project. Update them before use. Keep generated `build`, `dist`, `.tools` and `.venv` directories ignored by Git so a clean release manifest remains meaningful.

<a id="step-11-install-arm"></a>

### scripts/install\_arm.py

<div class="warning">

> **Adapt the target toolchain.**
>
> This installer is for the reference Arm compiler only. Replace it with approved compiler/SDK provisioning for your targeted project; also adapt CPU/ABI, startup, linker, presets, runner and output paths in the build steps.

</div>

<!-- source: scripts/install_arm.py -->
```python
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
```

<a id="step-11-check-size"></a>

### scripts/check\_size.py

<div class="warning">

> **Adapt the target size tool and metrics.**
>
> This Arm GNU example must be changed to fit your targeted project's toolchain, output files, memory layout and agreed size budgets. Host and target utilities are not interchangeable.

</div>

<!-- source: scripts/check_size.py -->
```python
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
```

<a id="step-11-sbom-requirements"></a>

### scripts/requirements-sbom.txt

Required only when the optional SBOM module is selected.

<!-- source: scripts/requirements-sbom.txt -->
```
# Optional official SPDX JSON-schema validation.
jsonschema==4.23.0
```

<a id="step-11-validate-sbom"></a>

### scripts/validate\_sbom.py

<!-- source: scripts/validate_sbom.py -->
```python
"""Validate SPDX 2.3 JSON with a pinned official schema and fixture semantics."""

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

SCHEMA_URL = (
    "https://raw.githubusercontent.com/spdx/spdx-spec/"
    "aadf3b0b8dbbabdb4d880b0fc714255fea436ff7/schemas/spdx-schema.json"
)
SCHEMA_SHA256 = "239208b7ac287b3cf5d9a9af23f9d69863971102a5e1587a27a398b43490b89b"


def check_identity(document, commit, elf_sha):
    package = document["packages"][0]
    if package["versionInfo"] != commit:
        raise ValueError("SBOM source commit does not match manifest")
    expected = {"algorithm": "SHA256", "checksumValue": elf_sha}
    if expected not in package["checksums"]:
        raise ValueError("SBOM firmware hash does not match manifest")
    if not document["files"]:
        raise ValueError("SBOM contains no source inventory")
    identifiers = {document["SPDXID"]}
    identifiers.update(item["SPDXID"] for item in document["packages"])
    identifiers.update(item["SPDXID"] for item in document["files"])
    if len(identifiers) != 1 + len(document["packages"]) + len(document["files"]):
        raise ValueError("SBOM SPDX identifiers must be unique")
    for relation in document["relationships"]:
        if relation["spdxElementId"] not in identifiers or relation["relatedSpdxElement"] not in identifiers:
            raise ValueError("SBOM relationship references a missing element")


def validate(path):
    import jsonschema

    document = json.loads(path.read_text(encoding="utf-8"))
    with urllib.request.urlopen(SCHEMA_URL, timeout=60) as response:
        schema_bytes = response.read()
    if hashlib.sha256(schema_bytes).hexdigest() != SCHEMA_SHA256:
        raise ValueError("Official SPDX schema checksum mismatch")
    jsonschema.Draft7Validator(json.loads(schema_bytes)).validate(document)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sbom", type=Path)
    args = parser.parse_args()
    validate(args.sbom)
    print("SPDX 2.3 JSON schema validation passed")


if __name__ == "__main__":
    main()
```

<a id="step-11-package-firmware"></a>

### scripts/package\_firmware.py

<div class="warning">

> **Adapt the package to your target project.**
>
> Change target compiler/version reporting, artifact paths/formats and inventory to your actual CMake/SDK/toolchain outputs. This helper packages existing firmware; it does not compile, rebuild, or validate hardware.

</div>

<!-- source: scripts/package_firmware.py -->
```python
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


def make_sbom(commit, elf_sha, created, source=None):
    source = SOURCE if source is None else source
    files = []
    for number, name in enumerate(INVENTORY, 1):
        files.append({
            "SPDXID": f"SPDXRef-File-{number}",
            "fileName": f"./{name}",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256(source / name)},
                {"algorithm": "SHA1", "checksumValue": hashlib.sha1((source / name).read_bytes()).hexdigest()},
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
                    "".join(sorted(hashlib.sha1((source / name).read_bytes()).hexdigest()
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
    parser.add_argument("--source", type=Path, default=SOURCE,
                        help="Reference source directory for the optional SBOM inventory")
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
            source = (ROOT / args.source).resolve()
            sbom_path.write_text(json.dumps(make_sbom(commit, firmware["monitor.elf"], created, source), indent=2) + "\n",
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
```

[← Learning journey]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-0-journey) | [Versioned-release lab →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-12-main"></a>

Solutions / Completed checkpoints

# Your lab solutions, brought together.

Use each solution after attempting its lab. At the end, the [final solution index]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-final) brings the complete pipeline and supporting files together. Every linked code example is included in this static workshop; workshop repository access is not required.

<div class="warning">

> **Set your own project path.**
>
> `path/to/your/project` is a placeholder for your existing project directory, relative to the repository root. Replace it in commands, workflow path filters and helper configuration before use; do not create a directory with that literal name. For a project at the repository root, use `.` in commands and `**` in source path filters. Also adapt include/source subdirectories, presets and output paths to your project.

</div>

<div class="warning">

> **Adapt solutions to your targeted project.**
>
> CMake and Arm GNU are references. Use your actual compiler/version, SDK, target CPU/ABI flags, startup/linker configuration, presets, runner and source/build/output paths. Keep your existing application and customer-required checks. Native tests use a host compiler, not the device compiler.

</div>

[Lab 1]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-01)[Lab 2]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-02)[Lab 3]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-03)[Lab 4]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-04)[Lab 5 (optional)]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-05)[Lab 6 (optional)]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-06)[Lab 7]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-lab-07)[Final solution]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-final)

<a id="step-12-lab-01"></a>

## Lab 1 solution: repeatable build

The completed checkpoint is a short set of verified command notes in OneNote or another customer-approved location. Record the working directory, environment/dependency setup, compiler/SDK versions, configure/build/test commands, host or target configuration, and output/report paths. No new script, JSON file or build configuration is required. Keep the existing project and build system; use these notes to create workflow steps in lab 2.

<div class="important">

> **Expected result**
>
> The recorded commands work from a clean build directory, at least one real test executes and passes, and the outputs and test report are available.

</div>

<a id="step-12-lab-02"></a>

## Lab 2 solution: first CI workflow

[Open the complete first-build YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-first-build)

Save the adapted example under an approved `.github/workflows` filename in your existing repository. Its final state checks out the expected commit, provisions the approved host tools, and runs the same build command as lab 1 with read-only permissions. Use approved push/PR triggers if the manual workflow is not yet available on the default branch.

The [complete CI caller]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci) shows the later reusable-workflow version. Preserve existing customer checks and adapt branch/path filters to your project.

<div class="important">

> **Expected result**
>
> The run builds the intended commit on the approved runner and exposes a meaningful PR check. Setup failure is not a firmware regression.

</div>

[Return to lab 2]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=3&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-lab-03"></a>

## Lab 3 solution: restored tests and retained evidence

[Open the complete build-and-test YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-tests)

The final test code must contain its **original correct expectation**. The deliberate wrong expectation must not remain. Do not change production logic, disable the test, weaken its assertion, or ignore its exit status.

1. The baseline test executes and passes.
2. The test-only intermediate change executes and fails for the intended expected/actual mismatch; diagnostics remain available.
3. Restoring the original expectation makes the same enabled test execute and pass again.

For an illustrative correct value of `50000`, the restored assertion expects `50000`, not the temporary `50001`. Use the original value from your own test, not this example value blindly.

<div class="important">

> **Expected result**
>
> You can show both CI runs and a final diff with no intentional failure. The completed pipeline prevents failed required tests from reaching firmware publication.

</div>

[Return to lab 3]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=4&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-lab-04"></a>

## Lab 4 solution: target firmware build

[Open the lab 4 caller and firmware-build checkpoint]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-target-build-checkpoint)

This stage runs required host tests, compiles the target and retains diagnostics and target outputs. It has no quality or SBOM inputs or steps; later labs extend it before the final packaging/release workflow.

Use the target-build step with your approved compiler and configuration. The [reference installer]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-install-arm), [CMake toolchain file]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-target-toolchain), [build targets]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-cmake-project), and [presets]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-cmake-presets) are all included in this workshop.

<div class="warning">

> **Adapt the Arm/CMake toolchain to your targeted project.**
>
> Replace compiler/version, architecture/ABI, SDK, startup/runtime, linker script/memory map, presets, paths and inspection tools as needed. Arm is illustrative. The target output directory must be separate from native tests.

</div>

```bash
cmake --preset arm -S path/to/your/project
cmake --build build/arm
```

<div class="important">

> **Expected result**
>
> The real target build produces the selected firmware outputs. Reference names are `monitor.elf`, `monitor.bin` and `monitor.map`. Compilation/linking is not hardware validation or proof of bootability.

</div>

[Return to lab 4]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=5&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-lab-05"></a>

## Lab 5 solution: optional quality gates

[Open the complete workflow with quality gates]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build)

Enable the caller's `quality` input only if this module is selected. Its warning/analysis/coverage/size steps must fail visibly when a selected check fails. The [complete size-check helper]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-check-size) is included.

```
jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: true
      sbom: false
```

Adapt this job into the [full caller]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci); it is not a standalone workflow. To select both optional modules, set both inputs to `true`. If quality is skipped, leave its input `false` and keep required builds/tests intact.

<div class="important">

> **Expected result when selected**
>
> Agreed checks run, diagnostics are reviewable, and gate failures prevent publication. Size equality passes; a one-byte overrun fails. Existing customer-required checks remain required.

</div>

[Return to optional lab 5]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=6&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-lab-06"></a>

## Lab 6 solution: optional pre-release SBOM

[Open the complete workflow with SBOM generation]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build)

Enable `sbom` independently of quality gates. The complete [package/SBOM helper]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-package-firmware), [validator]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-validate-sbom) and [requirements file]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-sbom-requirements) are included. Replace the reference inventory with approved tooling and scope for your actual dependencies.

```
jobs:
  validate:
    uses: ./.github/workflows/firmware-build.yml
    with:
      quality: false
      sbom: true
```

Adapt this job into the [full caller]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci). When skipped, the workflow must not depend on a missing SBOM artifact. When selected, generation/validation failures must prevent publication.

<div class="important">

> **Expected result when selected**
>
> A schema-valid inventory is associated with the source commit and firmware hash, generated before publication, and included in release \assets/checksums. Its scope and limitations are explicit.

</div>

[Return to optional lab 6]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-lab-07"></a>

## Lab 7 solution: completed versioned-release pipeline

[Open the complete release YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-release)

Add the release workflow to the CI/build components you created in the earlier labs; do not recreate or recopy those workflows. Confirm that the existing reusable build accepts the supplied optional-module inputs and uploads the checksummed release package for the same source commit and run. The minimal lab 4 checkpoint needs packaging/upload integration before its raw target outputs can be consumed by this release. The release then validates its tag, runs required checks and selected optional modules, and publishes the exact validated package without rebuilding.

The publisher downloads `firmware-<source SHA>` from the same run, verifies its checksums and clean source identity, and creates an approved workshop prerelease. It must not publish after failed required tests or overwrite an existing release. Select the safe tag namespace and optional-module settings before creating the tag; the full example explains the tag-push and manual-dispatch routes.

<div class="important">

> **Expected final assets**
>
> Target firmware files, linker map where applicable, `manifest.json` and `SHA256SUMS`; add `sbom.spdx.json` only when selected. The package is traceable but not deployed or hardware-validated.

</div>

[View the complete final solution index]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-final) · [Return to lab 7]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=8&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-final"></a>

## Final solution: all files in one place

This is the cumulative solution after the required labs. Every link opens complete code inside this static workshop, not the workshop repository. Keep your existing application, tests, startup and memory layout; use the reference configuration only to compare structure and adapt it to your project.

| Destination in your project | Complete solution | Required? |
| --- | --- | --- |
| `.github/workflows/ci.yml` | [CI caller YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-ci) | Core |
| `.github/workflows/firmware-build.yml` | [Reusable build/test/package YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-firmware-build) | Core, with optional modules off by default |
| `.github/workflows/release.yml` | [Versioned-release YAML]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-release) | Core, subject to customer publication policy |
| `scripts/install_arm.py` or approved equivalent | [Reference target compiler setup]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-install-arm) | Adapt to the targeted project |
| `scripts/package_firmware.py` or equivalent | [Package and checksum verification]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-package-firmware) | Core; adapt paths, target identity and inventory |
| `scripts/check_size.py` or equivalent | [Size-budget helper]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-check-size) | Optional quality module |
| `scripts/validate_sbom.py` and requirements | [SBOM validator]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-validate-sbom) and [requirements]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-11-sbom-requirements) | Optional SBOM module |
| Existing build-system files | [CMakeLists.txt]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-cmake-project), [presets]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-cmake-presets), [target toolchain]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-target-toolchain) | Reference structure; keep/adapt your existing configuration |

Keep generated `build`, `dist`, `.tools` and `.venv` directories ignored by Git. If SBOM generation is selected, include its validator and requirements alongside the package helper, or replace these consistently with your approved project tooling. If SBOM is skipped, its tools and artifacts are not required.

**Final review:** original test expectations restored; required tests execute and pass; selected optional modules succeed; package checksums/source identity match; customer release policy is respected. A published release is continuous delivery, not proof of device deployment.

[Open all complete workflow and script code]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

<a id="step-12-build-configuration"></a>

## Completed reference build configuration

The following files show the final native/target split used in the examples. Their application paths describe the reference structure; map them to your existing project's sources and target configuration. They are not a replacement for your board support or application code.

<a id="step-12-cmake-project"></a>

### CMakeLists.txt

<div class="warning">

> **Adapt this CMake configuration to your targeted project.**
>
> Change compiler/SDK, architecture/ABI flags, source and output names, startup files, linker script and memory map. Use the actual host compiler for tests; Cortex-M3 flags are reference-only. Do not copy the target settings unchanged unless they match your hardware.

</div>

<!-- source: samples/reference-firmware/CMakeLists.txt -->
```cmake
cmake_minimum_required(VERSION 3.25)
project(workshop_monitor VERSION 1.0.0 LANGUAGES C)

option(BUILD_FIRMWARE "Build the reference Arm image instead of host tests" OFF)
option(QUALITY_GATES "Enable extra warnings and native coverage" OFF)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_library(monitor STATIC src/monitor.c)
target_include_directories(monitor PUBLIC include)

if(QUALITY_GATES)
  if(NOT CMAKE_C_COMPILER_ID STREQUAL "GNU")
    message(FATAL_ERROR "The reference quality preset requires native GCC/gcov; adapt it for your compiler.")
  endif()
  target_compile_options(monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  if(NOT BUILD_FIRMWARE)
    target_compile_options(monitor PUBLIC --coverage -O0 -g)
    target_link_options(monitor PUBLIC --coverage)
  endif()
endif()

if(BUILD_FIRMWARE)
  enable_language(ASM)
  add_executable(firmware platform/startup.S platform/main.c)
  target_link_libraries(firmware PRIVATE monitor)
  target_compile_options(monitor PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_compile_options(firmware PRIVATE -mcpu=cortex-m3 -mthumb -ffreestanding -fno-builtin -ffunction-sections -fdata-sections -Os)
  target_link_options(firmware PRIVATE
    -mcpu=cortex-m3 -mthumb -nostdlib
    "-T${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld"
    "-Wl,-Map=${CMAKE_BINARY_DIR}/monitor.map"
    -Wl,--gc-sections -Wl,--build-id=none)
  set_target_properties(firmware PROPERTIES OUTPUT_NAME monitor SUFFIX .elf
    LINK_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/platform/memory.ld")
  add_custom_command(TARGET firmware POST_BUILD
    COMMAND "${CMAKE_OBJCOPY}" -O binary "$<TARGET_FILE:firmware>" "${CMAKE_BINARY_DIR}/monitor.bin"
    COMMAND "${CMAKE_SIZE}" "$<TARGET_FILE:firmware>"
    BYPRODUCTS "${CMAKE_BINARY_DIR}/monitor.bin"
    VERBATIM)
else()
  enable_testing()
  add_executable(test_monitor tests/test_monitor.c)
  target_link_libraries(test_monitor PRIVATE monitor)
  if(QUALITY_GATES)
    target_compile_options(test_monitor PRIVATE -Wall -Wextra -Wpedantic -Werror)
  endif()
  add_test(NAME monitor_logic COMMAND test_monitor)
endif()
```

<a id="step-12-cmake-presets"></a>

### CMakePresets.json

<div class="warning">

> **Adapt presets and toolchain paths to your project.**
>
> The relative output directories below assume the reference source layout. Change them, along with compiler/SDK and target flags, startup/linker settings and preset selection, for your targeted project. Keep host and target builds separate.

</div>

<!-- source: samples/reference-firmware/CMakePresets.json -->
```json
{
  "version": 6,
  "configurePresets": [
    {
      "name": "host",
      "displayName": "Native tests - adapt host compiler to your environment",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/../../build/host",
      "cacheVariables": { "CMAKE_BUILD_TYPE": "Debug" }
    },
    {
      "name": "host-quality",
      "inherits": "host",
      "displayName": "Optional native GCC quality gates",
      "binaryDir": "${sourceDir}/../../build/quality",
      "cacheVariables": { "QUALITY_GATES": "ON" }
    },
    {
      "name": "arm",
      "displayName": "Sample Cortex-M3 only - adapt toolchain to your target project",
      "generator": "Ninja",
      "binaryDir": "${sourceDir}/../../build/arm",
      "toolchainFile": "${sourceDir}/cmake/arm-gcc.cmake",
      "cacheVariables": { "CMAKE_BUILD_TYPE": "MinSizeRel", "BUILD_FIRMWARE": "ON" }
    }
  ]
}
```

<a id="step-12-target-toolchain"></a>

### cmake/arm-gcc.cmake

<div class="warning">

> **Replace this Arm toolchain with the one required by your targeted project.**
>
> Compiler selection is only one part of the target: adapt SDK/sysroot, CPU/ABI/FPU flags, startup/runtime, linker map, presets and artifact tools too. For a non-Arm project, use the actual target compiler rather than renaming these executables blindly.

</div>

<!-- source: samples/reference-firmware/cmake/arm-gcc.cmake -->
```cmake
# Reference only: adapt compiler/SDK, CPU/ABI, startup and linker map to your target.
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
find_program(CMAKE_C_COMPILER arm-none-eabi-gcc REQUIRED)
find_program(CMAKE_ASM_COMPILER arm-none-eabi-gcc REQUIRED)
find_program(CMAKE_OBJCOPY arm-none-eabi-objcopy REQUIRED)
find_program(CMAKE_SIZE arm-none-eabi-size REQUIRED)
```

[← Learning journey]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-0-journey) | [Final solution index]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=12&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$#step-12-final) | [From release to device →]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=9&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-13-main"></a>

Optional / Beyond the core

# Extend the evidence, not the claims.

The core is complete without these topics. Add them only when their prerequisites and customer objectives are clear.

## Independent pre-release modules

[Quality gates]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=6&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) and [SBOM generation]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=7&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) have their own guided labs. Either can run without the other; both precede release when selected.

## Matrices and caches

Test supported compiler/configuration combinations. Key caches by compiler version, target, configuration and dependency identity. Never treat a stale cache as validation.

## Emulator execution

Choose an actually supported machine model and define a pass/fail protocol, timeout and log capture. Cross-compilation alone is not emulation.

## HIL

Choose a real board and isolated trusted runner arrangement. Define device identity, locking, flash/reset, bounded assertions, and recovery before writing a workflow.

## Attestations and signing

Distinguish artifact hashes, producer identity/provenance, and device-verified image signatures. Plan key custody and bootloader trust rather than embedding secrets in YAML.

## Other embedded ecosystems

Map the same event/build/test/artifact/release structure to vendor SDKs, Zephyr/west, PlatformIO, or embedded Linux. Keep using the customer's actual toolchain.

<div class="warning">

> **Target adaptation still applies.**
>
> Any CMake compilation or Arm-build demonstration added for these topics must explicitly tell customers to change the compiler/SDK, target/ABI flags, startup/linker files, presets and paths to fit their targeted project.

</div>

These are discussion ideas, not promises of ready-to-run device workflows. The supplied active examples cover only the tested reference firmware CI/CD path.

[← Deployment discussion]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=9&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Workshop home]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)

---

<a id="step-14-main"></a>

Facilitator only / Delivery guide

# Teach the decisions behind the YAML.

Guide participants through the pipeline using their existing project, approved development environment, and target toolchain.

## Before delivery

1. Complete the [customer preflight]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=1&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) and adaptation map with the project owner. Resolve build/test/license/runner access before the session.
2. Agree a workshop branch, safe tag namespace, and required test-only intentional failure. Review all existing deployment triggers. Keep customer code and reports within their environment.
3. Confirm whether hosted release publication is allowed. If not, explain the packaging-only limitation rather than claiming release completion.
4. Select optional quality/SBOM modules independently; neither is needed for the minimum core activity budget.
5. Verify that the agreed build and test commands work with the customer's actual toolchain and runner configuration.

<div class="warning">

> **Repeat the target-toolchain reminder at every compilation demonstration.**
>
> CMake/Arm are references. Customers must adjust compiler/version, SDK, target CPU/ABI, startup, linker map, presets, runner and paths to their targeted project. Use a host compiler for native tests and a fresh output directory when changing toolchains.

</div>

## Core facilitation budget: 150 minutes

These are allocated teaching activities, excluding preflight and optional modules, not software implementation estimates. Do not replace hands-on practice with a long lecture or count optional material toward the minimum.

| Core activity | Allocated minutes | Facilitator evidence/prompt |
| --- | --- | --- |
| Orientation and project mapping | 10 | Ask where CI ends and device deployment begins. Confirm preflight boundaries. |
| Lab 1: repeatable build | 20 | Pairs explain a clean build and identify hidden workstation dependencies. |
| Lab 2: first CI | 25 | Participants trigger a run and locate source/runner/compiler evidence. |
| Lab 3: required test-only red to green | 30 | Observe both the intended assertion failure and its restored passing run. |
| Lab 4: target firmware | 20 | Compare host/target configuration and inspect actual firmware outputs. |
| Lab 7: versioned delivery | 30 | Review dependencies, source identity, package checksums, and approved release evidence. |
| Deployment discussion and evidence review | 15 | Participants explain what has not been validated on hardware. |

## Answer key: required failure

Only a deterministic test expectation changes. The test executes and fails with the intended expected/actual mismatch. Reports survive the failing run. Restore the exact original expectation, rerun successfully, and inspect the final diff. Compilation errors, test skips, forced shell failures, and firmware-code changes are not completion. Confirm failed required tests would block delivery through workflow dependencies and normal failure propagation.

## Optional modules before release

Quality gates add agreed warnings/analysis/coverage/size checks. The independent SBOM lab inventories components before publication. Show all four combinations: neither, quality only, SBOM only, and both. Selected modules must fail visibly and block publication when their checks fail. Disabled modules must not create missing-artifact dependencies. Never disable pre-existing customer checks.

## Recovery checkpoints

Use the [complete embedded workflow examples and supporting scripts]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=11&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) to compare structure with the customer's implementation. Participants do not need access to the workshop repository. Adapt commands and paths rather than overwriting existing automation.

If customer prerequisites fail during delivery, pause the relevant checkpoint and record the blocker. Do not claim the customer's pipeline works until the relevant checks have run successfully. Keep completed work, source, reports, and recovery notes inside approved customer systems.

## Exit questions

1. Which exact commit produced this package, and how can you verify the downloaded bytes?
2. What differs between your host test compiler and target toolchain?
3. Why does the restored test prove more than skipping it?
4. Which optional checks did you enable, and what do their results not prove?
5. What further evidence would you require before flashing a production device?

## MOAW handoff

Share the reviewed MOAW workshop link only after its Markdown is available on the intended public GitHub branch and the hosted rendering has been checked. MOAW reads `moaw/workshop.md` directly from this repository; no separate website deployment or repository copy is needed. The original HTML edition is unchanged and remains a separate delivery option.

Keep `published: false` during review. This excludes the workshop from catalogue publication; it is not access control and does not make a public repository or direct workshop link private. Catalogue registration is a separate, optional action. Follow the maintenance and publication instructions in `moaw/README.md` in the source repository. Never place customer code, reports or credentials in this public workshop.

## Reference documentation

- [GitHub reusable workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)
- [SPDX 2.3 specification](https://spdx.github.io/spdx-spec/v2.3/)
- [CMake toolchains](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)

[Workshop home]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=0&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$) | [Customer preflight]($$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$?step=1&vars=route:$$route:workshop/gh%3Achristophegigax-microsoft/gh-actions-embedded-workshop/main/moaw/$$)
