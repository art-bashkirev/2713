from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
                                        for line in open("public/8715_B.txt")]

clusters = [
    [p for p in points if p[1] > 23],
    [p for p in points if 15 < p[1] < 23],
    [p for p in points if p[1] < 15],
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))  # noqa: E731

centroids = [centroid(c) for c in clusters]
q1, q2 = None, None
mpcluster = max(clusters, key=len)
mpcentroid = centroid(mpcluster)

print(len(list(filter(lambda p: d(mpcentroid, p) < 1.2, mpcluster))))