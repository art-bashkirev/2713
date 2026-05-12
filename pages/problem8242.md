---
layout: full
---

# Решение № 8242

Моя задача с ЕГЭ-2025

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров.

<span v-mark="{ at: 1, color: 'red', type: 'underline' }">Центр кластера, или центроид, – это одна из звёзд</span>
на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна.

<span v-mark="{ at: 2, color: 'red', type: 'underline' }">Даны два входных файла (файл A и файл Б).</span> В файле A хранятся данные о звёздах двух кластеров. В файле Б хранятся данные о звёздах трёх кластеров.

<span v-mark="{ at: 3, color: 'red', type: 'underline' }">В файле Б имеются координаты ровно трёх «лишних» точек</span>, являющихся аномалиями, их учитывать не нужно.

Для файла А определите координаты центра каждого кластера, затем найдите два числа: $P_x$ - сумму абсцисс центров кластеров, и $P_y$ – сумму ординат центров кластеров.

Для файла Б определите координаты центра каждого кластера, затем найдите два числа: $Q_1$ – минимальное расстояние между центрами различных кластеров, и $Q_2$ – максимальное расстояние между центрами различных кластеров.

В ответе запишите четыре числа: в первой строке – сначала целую часть абсолютного значения произведения $P_x \cdot 10000$, затем целую часть абсолютного значения произведения $P_y \cdot 10000$; во второй строке – сначала целую часть абсолютного значения произведения $Q_1 \cdot 10000$, затем целую часть абсолютного значения произведения $Q_2 \cdot 10000$.

---
layout: figuresplit
---

# Решение № 8242

Моя задача с ЕГЭ-2025

::left::

Файл А

<PlotlyFigure csvUrl="/8078_A.csv" xColumn="0" yColumn="1" />

::right::

Файл Б

<PlotlyFigure csvUrl="/8078_B.csv" xColumn="0" yColumn="1" />

---
layout: codesplit
---

# Решение № 8242

Моя задача с ЕГЭ-2025

::left::

В предыдущей серии... и адаптация под следующую задачу.

<PlotlyFigure csvUrl="/8078_A.csv" xColumn="0" yColumn="1" />

<style>
.plotly-figure {
  margin: 0;
  align-contents: top;
  width: 350px;
  height: 400px;
}
</style>

::right::

````md magic-move
```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
          for line in open("7944_A.txt")]

clusters = [
  [p for p in points if p[1] + p[0] * 1.5 > 0],
  [p for p in points if p[1] + p[0] * 1.5 < 0]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(abs((sum(xs) / len(xs)) * 10_000),
      abs((sum(ys) / len(ys)) * 10_000))
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8078_A.txt")]

clusters = [
  [p for p in points if p[1] < 5],
  [p for p in points if p[1] > 5]
]

def centroid(cluster):
  return min(cluster, key=lambda p: sum(d(p, o) for o in cluster))

centroids = [centroid(clstr) for clstr in clusters]
px = sum(x for x, y in centroids)
py = sum(y for x, y in centroids)
print(abs(int(px * 10_000)), abs(int(py * 10_000)))
```

```python
# Расстояние
from itertools import combinations
from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8078_B.txt")]

extra = [
  [20.16999236, 16.84154051],
  [9.715587819, 18.74129471],
  [24.18647922, -18.98201366],
]
points = [p for p in points if p not in extra]

clusters = [
  [p for p in points if p[0] < 0],
  [p for p in points if p[0] > 0 and p[1] > 10],
  [p for p in points if p[0] > 0 and p[1] < 10],
]

def centroid(cluster):
  return min(cluster, key=lambda p: sum(d(p, o) for o in cluster))

centroids = [centroid(clstr) for clstr in clusters]
q1 = min(d(a, b) for a, b in combinations(centroids, 2))
q2 = max(d(a, b) for a, b in combinations(centroids, 2))
print(abs(int(q1 * 10_000)), abs(int(q2 * 10_000)))
```
````

---
layout: codesplit
---

# Решение № 8242

Моя задача с ЕГЭ-2025

::left::

Ответ.

::right::

```python
# Расстояние
from itertools import combinations
from math import dist as d

# Файл A
points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8078_A.txt")]

clusters = [
  [p for p in points if p[1] < 5],
  [p for p in points if p[1] > 5]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
px = sum(x for x, y in centroids)
py = sum(y for x, y in centroids)
print(abs(int(px * 10_000)), abs(int(py * 10_000)))

# Файл B
points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8078_B.txt")]

extra = [
  [20.16999236, 16.84154051],
  [9.715587819, 18.74129471],
  [24.18647922, -18.98201366],
]
points = [p for p in points if p not in extra]

clusters = [
  [p for p in points if p[0] < 0],
  [p for p in points if p[0] > 0 and p[1] > 10],
  [p for p in points if p[0] > 0 and p[1] < 10],
]

centroids = [centroid(clstr) for clstr in clusters]
q1 = min(d(a, b) for a, b in combinations(centroids, 2))
q2 = max(d(a, b) for a, b in combinations(centroids, 2))
print(abs(int(q1 * 10_000)), abs(int(q2 * 10_000)))
```

```md
335980 146086
316610 376330
```
