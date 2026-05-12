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


def medoid(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    if not cluster:
        raise ValueError("empty cluster")
    return min(cluster, key=lambda p: sum(math.dist(p, o) for o in cluster))


def answer_avg_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [medoid(c) for c in clusters]
    px = sum(x for x, _ in centers) / len(centers)
    py = sum(y for _, y in centers) / len(centers)
    return abs(int(px * 10_000)), abs(int(py * 10_000))


def answer_sum_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [medoid(c) for c in clusters]
    px = sum(x for x, _ in centers)
    py = sum(y for _, y in centers)
    return abs(int(px * 10_000)), abs(int(py * 10_000))


def answer_q_int(clusters: list[list[tuple[float, float]]]) -> tuple[int, int]:
    centers = [medoid(c) for c in clusters]
    distances = [math.dist(a, b) for a, b in itertools.combinations(centers, 2)]
    return abs(int(min(distances) * 10_000)), abs(int(max(distances) * 10_000))


@dataclass
class CheckResult:
    name: str
    ok: bool
    details: str


def mean_point(cluster: list[tuple[float, float]]) -> tuple[float, float]:
    return (
        sum(x for x, _ in cluster) / len(cluster),
        sum(y for _, y in cluster) / len(cluster),
    )


def kmeans_clusters(
    points: list[tuple[float, float]], k: int, steps: int = 50
) -> list[list[tuple[float, float]]]:
    if k <= 0 or k > len(points):
        raise ValueError("invalid k")
    first = min(points, key=lambda p: (p[0], p[1]))
    centers = [first]
    while len(centers) < k:
        centers.append(
            max(points, key=lambda p: min(math.dist(p, c) for c in centers))
        )
    clusters: list[list[tuple[float, float]]] = [[] for _ in range(k)]
    for _ in range(steps):
        clusters = [[] for _ in range(k)]
        for p in points:
            idx = min(range(k), key=lambda i: math.dist(p, centers[i]))
            clusters[idx].append(p)
        new_centers = [
            mean_point(cluster) if cluster else centers[i]
            for i, cluster in enumerate(clusters)
        ]
        if all(math.dist(a, b) < 1e-10 for a, b in zip(centers, new_centers)):
            break
        centers = new_centers
    return clusters


def remove_outliers_by_knn(
    points: list[tuple[float, float]], outlier_count: int, neighbors: int = 5
) -> list[tuple[float, float]]:
    scored: list[tuple[float, int]] = []
    for i, p in enumerate(points):
        dists = sorted(
            math.dist(p, q) for j, q in enumerate(points) if i != j
        )
        scored.append((sum(dists[:neighbors]), i))
    ranked = sorted(scored, key=lambda item: item[0], reverse=True)
    outlier_indices = {idx for _, idx in ranked[:outlier_count]}
    return [p for idx, p in enumerate(points) if idx not in outlier_indices]


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
    auto_b_ans = answer_avg_int(kmeans_clusters(b_points, 3))
    results.append(
        CheckResult(
            "7581/B automatic clustering",
            auto_b_ans == (37522, 51277),
            f"computed={auto_b_ans}, expected=(37522, 51277)",
        )
    )
    return results


def check_7944() -> list[CheckResult]:
    points = read_points("7944_A.csv")
    results: list[CheckResult] = []

    # As written on slides (contains typo p[1] + p[1] * 1.5 < 0)
    slide_clusters = [
        [p for p in points if p[1] + p[0] * 1.5 > 0],
        # Intentional: replicate exact slide code (y + y*1.5 < 0 -> y < 0), not the corrected boundary (y + x*1.5 < 0).
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
    auto_ans = answer_avg_int(kmeans_clusters(points, 2))
    results.append(
        CheckResult(
            "7944/A automatic clustering",
            auto_ans == (43789, 62202),
            f"computed={auto_ans}, expected=(43789, 62202)",
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
                "method became runnable unexpectedly; expected one empty cluster for y<5/y>5 on current data",
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
            corrected_a_ans == (107002, 323741),
            f"computed={corrected_a_ans}, expected=(107002, 323741)",
        )
    )
    auto_a_ans = answer_sum_int(kmeans_clusters(a_points, 2))
    results.append(
        CheckResult(
            "8242/A automatic clustering",
            auto_a_ans == (107002, 323741),
            f"computed={auto_a_ans}, expected=(107002, 323741)",
        )
    )

    b_points = read_points("8242_B.csv")
    slide_b_clusters = [
        [p for p in b_points if p[0] < 0],
        [p for p in b_points if p[0] > 0 and p[1] > 10],
        [p for p in b_points if p[0] > 0 and p[1] < 10],
    ]
    slide_b_sizes = [len(c) for c in slide_b_clusters]
    if min(slide_b_sizes) == 0:
        results.append(
            CheckResult(
                "8242/B slide method",
                False,
                (
                    "method ignores anomaly-removal requirement and does not form intended clusters: "
                    f"cluster sizes={slide_b_sizes}"
                ),
            )
        )
    else:
        slide_b_ans = answer_q_int(slide_b_clusters)
        results.append(
            CheckResult(
                "8242/B slide method",
                False,
                (
                    "method ignores anomaly-removal requirement and does not form intended clusters: "
                    f"cluster sizes={slide_b_sizes}, computed={slide_b_ans}"
                ),
            )
        )

    # Remove 3 anomalies, then split three main clouds by x-coordinate.
    # On current 8242_B data, x<0 and x>30 isolate exactly the 3 stated anomalies.
    core = [p for p in b_points if 0 < p[0] < 30]
    corrected_b_clusters = [
        # After anomaly removal, the three dense clouds are separated by clear x-gaps around ~10 and ~19.
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
    auto_core = remove_outliers_by_knn(b_points, outlier_count=3)
    auto_b_ans = answer_q_int(kmeans_clusters(auto_core, 3))
    results.append(
        CheckResult(
            "8242/B automatic clustering",
            auto_b_ans == (58778, 151839),
            (
                f"computed={auto_b_ans}, expected=(58778, 151839), "
                f"removed_anomalies={len(b_points) - len(auto_core)}"
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
