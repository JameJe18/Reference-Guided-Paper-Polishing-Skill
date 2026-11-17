#!/usr/bin/env python3
"""Validate declared manuscript-package invariants.

Usage:
    python check_manuscript_package.py package-check.json
    Get-Content package-check.json -Raw | python check_manuscript_package.py -

The manifest validates only explicit invariants. Citation-to-claim support and
statistical appropriateness still require scientific review.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    raise ValueError(message)


def load_manifest(path: str) -> tuple[dict[str, Any], Path]:
    if path == "-":
        return json.load(sys.stdin), Path.cwd()

    manifest_path = Path(path).resolve()
    with manifest_path.open("r", encoding="utf-8") as handle:
        return json.load(handle), manifest_path.parent


def resolve_files(manifest: dict[str, Any], base_dir: Path) -> list[Path]:
    raw_files = manifest.get("files")
    if not isinstance(raw_files, list) or not raw_files:
        fail("'files' must be a non-empty list")

    resolved: list[Path] = []
    for item in raw_files:
        if not isinstance(item, str) or not item.strip():
            fail("each entry in 'files' must be a non-empty path string")
        path = Path(item)
        resolved.append(path if path.is_absolute() else (base_dir / path).resolve())
    return resolved


def reference_section(text: str) -> str:
    matches = list(
        re.finditer(
            r"^\s*#{1,6}\s*(?:\d+\.?\s*)?(?:references|参考文献)\s*$",
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    )
    if not matches:
        return ""
    return text[matches[-1].end() :]


def reference_lines(text: str) -> list[str]:
    section = reference_section(text)
    return [
        line.strip()
        for line in section.splitlines()
        if re.match(r"^\s*\d+\.\s+\S", line)
    ]


def body_before_references(text: str) -> str:
    matches = list(
        re.finditer(
            r"^\s*#{1,6}\s*(?:\d+\.?\s*)?(?:references|参考文献)\s*$",
            text,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    )
    return text[: matches[-1].start()] if matches else text


def expand_range(part: str) -> list[int]:
    part = part.strip()
    if not part:
        return []
    match = re.fullmatch(r"(\d+)\s*[–-]\s*(\d+)", part)
    if match:
        start, end = map(int, match.groups())
        if start > end:
            fail(f"descending citation range: {part}")
        return list(range(start, end + 1))
    if part.isdigit():
        return [int(part)]
    return []


def cited_numbers(text: str) -> set[int]:
    body = body_before_references(text)
    numbers: set[int] = set()
    for match in re.finditer(r"\[([0-9,;\s–-]+)\]", body):
        for part in re.split(r"[,;]", match.group(1)):
            numbers.update(expand_range(part))
    return numbers


def check_text(
    path: Path,
    text: str,
    manifest: dict[str, Any],
    global_errors: list[str],
) -> None:
    if not text.strip():
        global_errors.append(f"{path}: file is empty")
        return

    if "```" in text and text.count("```") % 2:
        global_errors.append(f"{path}: unbalanced Markdown code fences")

    for phrase in manifest.get("required_phrases", []):
        if phrase not in text:
            global_errors.append(f"{path}: missing required phrase {phrase!r}")

    for phrase in manifest.get("forbidden_phrases", []):
        if phrase in text:
            global_errors.append(f"{path}: contains forbidden phrase {phrase!r}")

    concepts = manifest.get("required_concepts", [])
    folded = text.casefold()
    for concept in concepts:
        if str(concept).casefold() not in folded:
            global_errors.append(f"{path}: missing required concept {concept!r}")

    expected_refs = manifest.get("reference_count")
    refs = reference_lines(text)
    if expected_refs is not None and len(refs) != int(expected_refs):
        global_errors.append(
            f"{path}: expected {expected_refs} numbered references, found {len(refs)}"
        )

    if manifest.get("require_reference_doi"):
        for index, ref in enumerate(refs, start=1):
            lowered = ref.casefold()
            if "doi:10." not in lowered and "doi.org/10." not in lowered:
                global_errors.append(f"{path}: reference {index} has no DOI")

    citation_range = manifest.get("citation_range")
    if citation_range is not None:
        if not (
            isinstance(citation_range, list)
            and len(citation_range) == 2
            and all(isinstance(value, int) for value in citation_range)
        ):
            fail("'citation_range' must be [start, end]")
        start, end = citation_range
        expected = set(range(start, end + 1))
        found = cited_numbers(text)
        missing = sorted(expected - found)
        outside = sorted(found - expected)
        if missing:
            global_errors.append(f"{path}: uncited reference numbers {missing}")
        if outside:
            global_errors.append(f"{path}: citations outside range {outside}")


def check_sums(manifest: dict[str, Any]) -> tuple[list[str], list[str]]:
    passes: list[str] = []
    errors: list[str] = []
    sums = manifest.get("sums", [])
    if not isinstance(sums, list):
        fail("'sums' must be a list")
    for index, item in enumerate(sums, start=1):
        if not isinstance(item, dict):
            fail(f"sums[{index - 1}] must be an object")
        total = item.get("total")
        parts = item.get("parts")
        if not isinstance(total, (int, float)):
            fail(f"sums[{index - 1}].total must be numeric")
        if not isinstance(parts, list) or not parts:
            fail(f"sums[{index - 1}].parts must be a non-empty list")
        if not all(isinstance(value, (int, float)) for value in parts):
            fail(f"sums[{index - 1}].parts must contain numbers")
        observed = sum(parts)
        if abs(observed - total) > 1e-9:
            errors.append(
                f"sum rule {index}: total {total} != parts {parts} (sum {observed})"
            )
        else:
            passes.append(f"sum rule {index}: {total} = {' + '.join(map(str, parts))}")
    return passes, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(
            "Usage: python check_manuscript_package.py <manifest.json|->",
            file=sys.stderr,
        )
        return 2

    try:
        manifest, base_dir = load_manifest(argv[1])
        files = resolve_files(manifest, base_dir)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"MANIFEST ERROR: {exc}", file=sys.stderr)
        return 2

    errors: list[str] = []
    passes: list[str] = []

    texts: dict[Path, str] = {}
    for path in files:
        try:
            texts[path] = path.read_text(encoding="utf-8")
            passes.append(f"found: {path}")
        except OSError as exc:
            errors.append(f"{path}: cannot read file: {exc}")

    for path, text in texts.items():
        check_text(path, text, manifest, errors)
        if not any(error.startswith(f"{path}:") for error in errors):
            passes.append(f"content checks: {path}")

    if manifest.get("same_citation_coverage") and len(texts) > 1:
        coverage = {path: cited_numbers(text) for path, text in texts.items()}
        baseline_path = files[0]
        baseline = coverage.get(baseline_path)
        if baseline is not None:
            for path, found in coverage.items():
                if path != baseline_path and found != baseline:
                    errors.append(
                        f"{path}: citation coverage differs from {baseline_path.name}"
                    )

    sum_passes, sum_errors = check_sums(manifest)
    passes.extend(sum_passes)
    errors.extend(sum_errors)

    for message in passes:
        print(f"[PASS] {message}")
    for message in errors:
        print(f"[FAIL] {message}")

    if errors:
        print(f"\nRESULT: FAIL ({len(errors)} issue(s))")
        return 1
    print(f"\nRESULT: PASS ({len(passes)} check(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
