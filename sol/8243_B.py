from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
          for line in open("public/8243_B.txt")]

clusters = [
  [p for p in points if p[1] > 20],
  [p for p in points if 15 < p[1] < 20],
  [p for p in points if p[1] < 15]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(sum(xs)*10000, sum(ys)*10000)
