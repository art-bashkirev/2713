---
layout: full
---

# Решение № 7944

ЕГКР-2024

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров. Центр кластера – это одна из звёзд на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна. Расстояние между двумя точками $A(x_1, y_1)$ и $B(x_2, y_2)$ вычисляется по формуле: 
$$
d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

Даны два входных файла (A и Б). В файле A хранятся данные о звёздах двух кластеров. В каждой строке записана информация о расположении на карте одной звезды: сначала координата $x$, затем координата $y$ (в условных единицах). Известно, что количество звёзд не превышает $1000$. В файле Б хранятся данные о звёздах трёх кластеров. Известно, что количество звёзд не превышает $10 000$. Структура хранения информации о звездах в файле Б аналогична файлу А. Возможные данные одного из файлов иллюстрированы графиком.

Для каждого файла определите координаты центра каждого кластера, затем вычислите два числа: $P_x$ – среднее арифметическое абсцисс центров кластеров, и $P_y$ – среднее арифметическое ординат центров кластеров. В ответе запишите четыре числа: в первой строке сначала **абсолютное значение целой части произведения** $P_x \cdot 10 000$, затем **абсолютное значение целой части произведения** $P_y \cdot 10 000$ для файла А, во второй строке – аналогичные данные для файла Б.

---
layout: figuresplit
---

# Решение № 7944

ЕГКР-2024

::left::

Файл А

<PlotlyFigure csvUrl="/7944_A.csv" xColumn="0" yColumn="1" />

::right::

Файл B

<PlotlyFigure csvUrl="/7944_B.csv" xColumn="0" yColumn="1" />

---
layout: codesplit
---

# Решение № 7944

ЕГКР-2024

::left::

В предыдущей серии...

<PlotlyFigure csvUrl="/7944_A.csv" xColumn="0" yColumn="1" />

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
          for line in open("7581_B.txt")]

clusters = [
  [p for p in points if p[0] + p[1] < 6],
  [p for p in points if p[0] + p[1] > 6 and p[1] - p[0] * (1/3) < 6],
  [p for p in points if p[1] - p[0] * (1/3) > 6]
]

def centroid(cluster):
  c = min(cluster, key=lambda p: sum(d(p, o) for o in cluster))
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7944_A.txt")]

clusters = [
  [p for p in points if ],
  [p for p in points if ]
]

def centroid(cluster):
  c = min(cluster, key=lambda p: sum(d(p, o) for o in cluster))
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7944_A.txt")]

clusters = [
  [p for p in points if p[1] + p[0] * (1.5) > 0],
  [p for p in points if p[1] + p[1] * (1.5) < 0]
]

def centroid(cluster):
  return min(cluster, key=lambda p: sum(d(p, o) for o in cluster))


centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7944_A.txt")]

clusters = [
  [p for p in points if p[1] + p[0] * (1.5) > 0],
  [p for p in points if p[1] + p[1] * (1.5) < 0]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(abs((sum(xs) / len(xs)) * 10_000), 
      abs((sum(ys) / len(ys)) * 10_000))
```
````

---
layout: codesplit
---


# Решение № 7944

ЕГКР-2024

::left::

Ответ для файла A.

::right::

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7944_A.txt")]

clusters = [
  [p for p in points if p[1] + p[0] * (1.5) > 0],
  [p for p in points if p[1] + p[1] * (1.5) < 0]
]

centroid = lambda c: min(c, key=lambda p: sum(d(p, o) for o in c))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print(abs((sum(xs) / len(xs)) * 10_000), 
      abs((sum(ys) / len(ys)) * 10_000))
```

```md
43789.56525731115 62202.015534471495
```
