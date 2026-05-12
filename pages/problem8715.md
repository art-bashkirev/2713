---
layout: full
---

# Решение № 8715

ЕГКР-2025 · Накидали гробов

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров. Центр кластера – это одна из звёзд на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна. Расстояние между двумя точками $A(x_1, y_1)$ и $B(x_2, y_2)$ вычисляется по формуле:
$$
d\left(A, B\right) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

Даны два входных файла (файл A и файл Б). В файле A хранятся данные о звёздах двух кластеров. В каждой строке записана информация о расположении на карте одной звезды: сначала координата x, затем координата y (в условных единицах). Известно, что количество звёзд не превышает $1000$. В файле Б хранятся данные о звёздах трёх кластеров. Известно, что количество звёзд не превышает $10 000$. Структура хранения информации о звездах в файле Б аналогична файлу А.

Для файла А определите координаты центра каждого кластера, затем найдите два числа: $P_x$ – минимальное расстояние от точки с координатами $(1.0; 1.0)$ до центра кластера, и $P_y$ – максимальное расстояние от этой же точки до центра кластера. 

Для файла Б определите координаты центра каждого кластера, затем найдите два числа: $Q_1$ – в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более $1.2$ от центра кластера, и $Q_2$ – в кластере с наибольшим количеством точек число таких точек, которые находятся на расстоянии не более $0.75$ от центра кластера. Гарантируется, что во всех кластерах количество точек различно. 

В ответе запишите четыре числа: в первой строке сначала целую часть произведения $P_x\cdot 10 000$, затем целую часть произведения $P_y\cdot 10 000$ для файла А, во второй строке – сначала $Q_1$, затем $Q_2$.

---
layout: figuresplit
---

# Решение № 8715

ЕГКР-2025 · Накидали гробов

::left::

Файл А

<PlotlyFigure csvUrl="/8715_A.csv" xColumn="0" yColumn="1" />

::right::

Файл B

<PlotlyFigure csvUrl="/8715_B.csv" xColumn="0" yColumn="1" />

---
layout: codesplit
---

# Решение № 8715

ЕГКР-2025 · Накидали гробов

::left::

Они даже не старались

::right::
````md magic-move
```python
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("8243_B.txt")]

clusters = [
  [p for p in points if p[1] > 20],
  [p for p in points if 15 < p[1] < 20],
  [p for p in points if p[1] < 15]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(min(d(c, (0, 0)) for c in centroids) * 10000,
      max(d(c, (0, 0)) for c in centroids) * 10000)
```
```python
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("8715_A.txt")]

clusters = [
  [p for p in points if p[1] > 10],
  [p for p in points if p[1] < 10]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(min(d(c, (0, 0)) for c in centroids) * 10000,
      max(d(c, (0, 0)) for c in centroids) * 10000)
```
```python
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("8715_A.txt")]

clusters = [
  [p for p in points if p[1] > 10],
  [p for p in points if p[1] < 10]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(min(d(c, (1, 0)) for c in centroids) * 10000,
      max(d(c, (1, 0)) for c in centroids) * 10000)
```
````