# Simple reference C project

This separate, dependency-free C environmental monitor supplies reference ideas
for the workshop. Customers use their existing project instead. It converts a 12-bit sensor sample
to millidegrees, calculates a moving average, and raises a threshold alarm.

**Adapt to your target project:** every CMake/Arm command here is a reference.
Customers must change the toolchain for their architecture, board, compiler/SDK,
CPU/ABI flags, startup/linker configuration, presets, runner, and output paths.
Do not apply this sample memory map to an arbitrary device.

## Tooling

Run commands from the **repository root**. Reference CI uses Ubuntu 24.04, GCC 13,
CMake, Ninja, Python 3.12+, and the SHA-256-verified xPack Arm GNU 15.2.1-1.1 toolchain.
`scripts/install_arm.py` supports Linux x64 and Windows x64, downloads from xPack,
and verifies a checked-in digest before extraction. It prints the compiler's
`bin` directory; add it to your PATH. Installation lives in `.tools`, not a system
directory. A working CMake >= 3.25, Ninja, and native C compiler are prerequisites.

The commands below and active workflows already select this reference project.
Customer-facing site snippets instead use `path/to/your/project`; replace it
with the customer's repository-relative directory. For a root-level customer
project, use `.` in commands and `**` in workflow source path filters. Also adapt
include/source subdirectories and output paths; do not create a directory with
the literal placeholder name.

On the reference Ubuntu environment:

```sh
sudo apt-get update
sudo apt-get install -y cmake ninja-build gcc-13 python3
export CC=gcc-13
python3 scripts/install_arm.py
export PATH="$PWD/.tools/xpack-arm-none-eabi-gcc-15.2.1-1.1/bin:$PATH"
```

In PowerShell, run `python scripts\install_arm.py` and prepend
`(Join-Path $PWD '.tools\xpack-arm-none-eabi-gcc-15.2.1-1.1\bin')` to `$env:PATH`.
Use an installed native C compiler appropriate for your environment.

## Native tests

**Target adaptation:** select your host compiler for these CMake presets, not the
device compiler. Use a fresh build directory when changing compilers/toolchains.

The portable repository-root commands used by CI are:

```sh
cmake --preset host -S samples/reference-firmware
cmake --build build/host
ctest --test-dir build/host --no-tests=error --output-on-failure --output-junit test-results.xml
```

## Required red-to-green exercise

First obtain a passing native run. In `samples/reference-firmware/tests/test_monitor.c`,
temporarily change only `EXPECTED_MIDPOINT_MC` from `50000` to `50001`. Build and
run the same tests: the midpoint assertion must fail with expected/actual values.
Restore `50000`, build, and confirm the test executes and passes. In a personal
GitHub rehearsal, commit each test-only state on an approved workshop branch to
observe both CI runs. Do not skip tests or change application behavior.

The repository is supplied in the passing state. This documentation does not
authorize the agent to create commits or push changes.

## Arm firmware

**Target adaptation:** change this Arm CMake toolchain for the customer's actual
target: compiler/SDK, architecture/ABI, startup, linker script, and artifact paths.
This fixture models a Cortex-M3 memory map with 128 KiB flash at `0x08000000` and
20 KiB RAM at `0x20000000`. It is not a certified board support package.

```sh
cmake --preset arm -S samples/reference-firmware
cmake --build build/arm
arm-none-eabi-size build/arm/monitor.elf
```

Outputs: `monitor.elf`, `monitor.bin`, and `monitor.map`. The minimal vector table,
data/BSS startup, and linker script produce genuine target code. No libc, vendor
SDK, RTOS, or external runtime library is linked. Compilation/linking do **not**
establish bootability, peripheral behavior, timing, or hardware safety.

## Optional quality gates

Install customer-approved analysis tools; the reference uses `cppcheck` and
`gcovr` from Ubuntu 24.04. Existing customer gates must not be weakened. Match
`gcov` to the native GCC version (the reference CI uses `gcov-13`).

**Target adaptation:** the coverage CMake preset uses host GCC/gcov; target
firmware size uses the selected device toolchain's size utility.

```sh
cmake --preset host-quality -S samples/reference-firmware
cmake --build build/quality
ctest --test-dir build/quality --no-tests=error --output-on-failure --output-junit test-results.xml
cppcheck --enable=warning,style,performance,portability --error-exitcode=1 --inline-suppr --std=c11 -I samples/reference-firmware/include samples/reference-firmware/src
gcovr --root . --filter samples/reference-firmware/src/ --object-directory build/quality --gcov-executable gcov-13 --xml-pretty --output build/quality/coverage.xml --fail-under-line 80
python3 scripts/check_size.py build/arm/monitor.elf --flash 16384 --ram 4096
```

Flash = `.text + .data`; RAM = `.data + .bss` reported by GNU size. These teaching
limits are not physical capacity or a stack/heap safety proof. The memory report
does not account for every possible linker section; adapt metrics to real firmware.

For an author-only negative check, run
`cppcheck --error-exitcode=1 tests/fixtures/analysis_failure.c` and require exit
code 1 with a null-pointer diagnostic. Never compile or execute that analyzer
fixture or add it to customer firmware. For size, run the size script with a
flash budget one byte below the measured value and require failure; equality
must pass. These are isolated reference checks, not customer production edits.

## Optional SBOM and firmware package

Use the **same already-built firmware**. An SBOM is optional and separate from
quality gates. This sample's generator inventories the explicitly listed linked
source files and firmware hashes; it is not a generic customer dependency scanner.
It declares licenses `NOASSERTION`, not invented licenses. For customer projects,
substitute an approved dependency-aware generator with a documented inventory scope.

```sh
python3 -m pip install -r scripts/requirements-sbom.txt
python3 scripts/package_firmware.py --source samples/reference-firmware --sbom
python3 scripts/validate_sbom.py dist/firmware/sbom.spdx.json
```

Without SBOM tooling, use
`python3 scripts/package_firmware.py --source samples/reference-firmware`. Both paths write
ELF/BIN/map, build manifest, and `SHA256SUMS` to `dist/firmware`. The optional SBOM
is generated before publication, validated, associated with the source commit
and ELF hash, and checksummed with the other files. The generator does not claim
vulnerability assessment, signing, or full transitive inventory for other projects.

## Hosted rehearsal

Enable Actions in your own repository copy. Run **Firmware CI** manually with
both options off, each option individually on, then both on. The reusable
workflow fails visibly if a selected module fails. Its output artifact is named
for the exact source SHA. After verifying the safe tag namespace and existing
triggers, a `workshop-v1.0.0` tag exercises the release workflow. Alternatively,
dispatch **Firmware release** against an existing matching tag with options.
No live release, commit, tag, or push is performed automatically by local setup.
