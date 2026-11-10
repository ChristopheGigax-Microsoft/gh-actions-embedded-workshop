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
