#!/usr/bin/env python3
from __future__ import annotations

import csv
import itertools
import math
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = REPO_ROOT / "public"


def read_points(file_name: str) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    with (PUBLIC_DIR / file_name).open(newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)  # header
        for row in reader:
            if not row:
                continue
            if len(row) >= 3:  # index,x,y
                x, y = float(row[1]), float(row[2])
            else:  # x,y
                x, y = float(row[0]), float(row[1])
            points.append((x, y))
    return points


def centroid(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    if not cluster:
        raise ValueError("empty cluster")
    return min(cluster, key=lambda p: sum(math.dist(p, o) for o in cluster))


def answer_avg_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [centroid(c) for c in clusters]
    px = sum(x for x, _ in centers) / len(centers)
    py = sum(y for _, y in centers) / len(centers)
    return abs(int(px * 10_000)), abs(int(py * 10_000))


def answer_sum_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [centroid(c) for c in clusters]
    px = sum(x for x, _ in centers)
    py = sum(y for _, y in centers)
    return abs(int(px * 10_000)), abs(int(py * 10_000))


def answer_q_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [centroid(c) for c in clusters]
    distances = [math.dist(a, b) for a, b in itertools.combinations(centers, 2)]
    return abs(int(min(distances) * 10_000)), abs(int(max(distances) * 10_000))


@dataclass
class CheckResult:
    name: str
    ok: bool
    details: str


def check_7581() -> list[CheckResult]:
    results: list[CheckResult] = []

    a_points = read_points("7581_A.csv")
    a_clusters = [
        [p for p in a_points if p[0] * 0.5 + p[1] < 3],
        [p for p in a_points if p[0] * 0.5 + p[1] > 3],
    ]
    a_ans = answer_avg_int(a_clusters)
    results.append(
        CheckResult(
            "7581/A",
            a_ans == (10738, 30730),
            f"computed={a_ans}, expected=(10738, 30730)",
        )
    )

    b_points = read_points("7581_B.csv")
    b_clusters = [
        [p for p in b_points if p[0] + p[1] < 6],
        [p for p in b_points if p[0] + p[1] > 6 and p[1] - p[0] * (1 / 3) < 6],
        [p for p in b_points if p[1] - p[0] * (1 / 3) > 6],
    ]
    b_ans = answer_avg_int(b_clusters)
    results.append(
        CheckResult(
            "7581/B",
            b_ans == (37522, 51277),
            f"computed={b_ans}, expected=(37522, 51277)",
        )
    )
    return results


def check_7944() -> list[CheckResult]:
    points = read_points("7944_A.csv")
    results: list[CheckResult] = []

    # As written on slides (contains typo p[1] + p[1] * 1.5 < 0)
    slide_clusters = [
        [p for p in points if p[1] + p[0] * 1.5 > 0],
        [p for p in points if p[1] + p[1] * 1.5 < 0],
    ]
    slide_covered = len(slide_clusters[0]) + len(slide_clusters[1])
    slide_unassigned = len(points) - slide_covered
    slide_ans = answer_avg_int(slide_clusters)
    results.append(
        CheckResult(
            "7944/A slide method",
            False,
            (
                "method is not valid on current files: "
                f"unassigned={slide_unassigned}, computed={slide_ans}, "
                "slide shows ~ (43789, 62202)"
            ),
        )
    )

    corrected_clusters = [
        [p for p in points if p[1] + p[0] * 1.5 > 0],
        [p for p in points if p[1] + p[0] * 1.5 < 0],
    ]
    corrected_ans = answer_avg_int(corrected_clusters)
    results.append(
        CheckResult(
            "7944/A corrected method",
            corrected_ans == (43789, 62202),
            f"computed={corrected_ans}, expected=(43789, 62202)",
        )
    )
    return results


def check_8242() -> list[CheckResult]:
    results: list[CheckResult] = []

    a_points = read_points("8242_A.csv")
    slide_a_clusters = [
        [p for p in a_points if p[1] < 5],
        [p for p in a_points if p[1] > 5],
    ]
    if not slide_a_clusters[0] or not slide_a_clusters[1]:
        results.append(
            CheckResult(
                "8242/A slide method",
                False,
                (
                    "method is not runnable on current files: "
                    f"cluster sizes={[len(c) for c in slide_a_clusters]}"
                ),
            )
        )
    else:
        results.append(
            CheckResult(
                "8242/A slide method",
                False,
                "unexpectedly runnable",
            )
        )

    # Corrected split for current data
    corrected_a_clusters = [
        [p for p in a_points if p[0] < 5],
        [p for p in a_points if p[0] > 5],
    ]
    corrected_a_ans = answer_sum_int(corrected_a_clusters)
    results.append(
        CheckResult(
            "8242/A corrected method",
            corrected_a_ans == (53501, 161870),
            f"computed={corrected_a_ans}, expected=(53501, 161870)",
        )
    )

    b_points = read_points("8242_B.csv")
    slide_b_clusters = [
        [p for p in b_points if p[0] < 0],
        [p for p in b_points if p[0] > 0 and p[1] > 10],
        [p for p in b_points if p[0] > 0 and p[1] < 10],
    ]
    slide_b_ans = answer_q_int(slide_b_clusters)
    results.append(
        CheckResult(
            "8242/B slide method",
            False,
            (
                "method ignores anomaly-removal requirement and does not form intended clusters: "
                f"cluster sizes={[len(c) for c in slide_b_clusters]}, computed={slide_b_ans}"
            ),
        )
    )

    # Remove 3 anomalies, then split three main clouds by x-coordinate.
    core = [p for p in b_points if 0 < p[0] < 30]
    corrected_b_clusters = [
        [p for p in core if p[0] < 10],
        [p for p in core if 10 < p[0] < 19],
        [p for p in core if p[0] > 19],
    ]
    corrected_b_ans = answer_q_int(corrected_b_clusters)
    results.append(
        CheckResult(
            "8242/B corrected method",
            corrected_b_ans == (58778, 151839),
            (
                f"computed={corrected_b_ans}, expected=(58778, 151839), "
                f"removed_anomalies={len(b_points) - len(core)}"
            ),
        )
    )

    return results


def print_results(results: list[CheckResult]) -> None:
    for res in results:
        status = "OK" if res.ok else "FAIL"
        print(f"[{status}] {res.name}: {res.details}")


def main() -> int:
    all_results: list[CheckResult] = []
    all_results.extend(check_7581())
    all_results.extend(check_7944())
    all_results.extend(check_8242())
    print_results(all_results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
