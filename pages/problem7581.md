---
layout: full
---

# Разбор № 7581

Демо-2025

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров.

<span v-mark="{ at: 1, color: 'red', type: 'underline' }">Центроид – это одна из звёзд</span>
 на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна. Расстояние между двумя точками $A(x1, y1)$ и $B(x2, y2)$ вычисляется по формуле:
$d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

<span v-mark="{ at: 2, color: 'red', type: 'underline' }">Даны два входных файла (A и Б).</span> В каждой строке записана информация о расположении на карте одной звезды: сначала координата $x$, затем координата $y$. В файле A хранятся данные о звёздах двух кластеров. Известно, что количество звёзд не превышает $1000$. В файле Б хранятся данные о звёздах трёх кластеров. Известно, что количество звёзд не превышает $10 000$. Структура хранения информации о звездах в файле Б аналогична файлу А.

Для каждого файла <span v-mark="{ at: 1, color: 'red', type: 'underline' }">определите координаты центра каждого кластера</span>, затем вычислите два числа: $P_x$ – среднее арифметическое абсцисс центров кластеров, и $P_y$ – среднее арифметическое ординат центров кластеров.
В ответе запишите четыре числа: в первой строке сначала целую часть произведения $P_x×10 000$, затем целую часть произведения $P_y×10 000$ для файла А, во второй строке – аналогичные данные для файла Б.

<!-- 

Начнем читать условие.

Что можно сразу выделить - это определение "Центроид". Центроидом считается одна из данных звезд и найти надо координаты уже существующие. Поэтому придётся ходить по данным.

[click]

Ещё важно - дается 2 файла. Один поменьше, другой побольше. В принципе, пока что можно и перебором все решать.
-->

---
layout: two-cols-header
---

# Разбор № 7581

Демо-2025

::left::

Файл А

<PlotlyFigure csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/refs/heads/main/data-csv/7581_A.csv" xColumn="0" yColumn="1" />

::right::

Файл B

<PlotlyFigure csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/refs/heads/main/data-csv/7581_B.csv" xColumn="0" yColumn="1" />


<!-- 
Посмотрим на данные. Здесь все очень просто и отношение звезды к кластеру можно сделать вручную - линейными функциями.

Программируем и читаем условие.
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

<v-click>
Центроид – это одна из звёзд на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна.

Расстояние между двумя точками $A$ и $B$ вычисляется по формуле:

$d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$
</v-click>

::right::

````md magic-move
```python
# -*- coding: utf-8 -*-
```

```python
# Расстояние
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
```

<!-- ```python
# Расстояние
def d(A, B):
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
```

```python
# Расстояние
d = lambda A, B: ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
``` -->
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Даны два входных файла (A и Б).

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
```
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025 / $\text{\tiny{derived from plugarinf}}$

::left::

Группировка на кластеры и перебор

::right::
````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025 / $\text{\tiny{derived from plugarinf}}$

::left::

<PlotlyFigure csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/refs/heads/main/data-csv/7581_A.csv" xColumn="0" yColumn="1" />
<style>
.plotly-figure {
  margin: 0;
  align-contents: top;
  width: 400px;
  height: auto;
}
</style>

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025 / $\text{\tiny{derived from plugarinf}}$

::left::

Группировка на кластеры и перебор

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):

```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Вычислите два числа: $P_x$ – среднее арифметическое абсцисс центров кластеров, и $P_y$ – среднее арифметическое ординат центров кластеров.

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Найденные центроиды

::right::

```python {monaco-run}
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
print(centroids)
```

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

В ответе запишите четыре числа: в первой строке сначала целую часть произведения $P_x×10 000$, затем целую часть произведения $P_y×10 000$ для файла А, во второй строке – аналогичные данные для файла Б.

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs = [x for x, y in centroids]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
```

```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```
````

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Ответ для файла A

::right::

```python {monaco-run}
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

<!--
Ответ мы получили, но среди вас крайне много любителей поменьше думать и поменьше писать, поэтому...
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Для любителей поменьше писать

::right::

````md magic-move
```python
# Расстояние
def d(A: tuple[float, float], B: tuple[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
d = lambda A, B: ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-1) + 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] + point[0] < 4:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] + p[1] < 4)],
  [p for p in points if (p[0] + p[1] > 4)]
]

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    i_point = cluster[i]
    for j in range(len(cluster)):
      B = cluster[j]
      s += d(i_point, B)
    if s < m:
      m = s
      x_c, y_c = i_point[0], i_point[1]
  return x_c, y_c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] + p[1] < 4)],
  [p for p in points if (p[0] + p[1] > 4)]
]

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  min_point, min_sum = None, 10 ** 9
  for point in cluster:
    total_distance = sum(d(point, other) for other in cluster)
    if total_distance < min_sum:
      min_sum = total_distance
      min_point = point
  return min_point

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] + p[1] < 4)],
  [p for p in points if (p[0] + p[1] > 4)]
]

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
    distances = [
        (point, sum(d(point, other) for other in cluster))
        for point in cluster
    ]
    min_point, min_dist = distances[0], 10 ** 9
    for point, dist in distances:
        if dist < min_dist:
            min_point, min_dist = point, dist
            
    return min_point


centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] + p[1] < 4)],
  [p for p in points if (p[0] + p[1] > 4)]
]

def centroid(cluster: list[list[float, float]]) -> tuple[float, float]:
  min_point = min(cluster, 
              key=lambda point: sum(d(point, other) for other in cluster))
  return min_point

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] + p[1] < 4)],
  [p for p in points if (p[0] + p[1] > 4)]
]

def centroid(cluster):
  min_point = min(cluster, key=lambda p: sum(d(p, o) for o in cluster))
  return min_point

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / 2) * 10_000, (sum(ys) / 2) * 10_000)
```
````

<!--
Начнем упрощать этот код. Сначала.

Я бы преобразовал вычисление расстояния в Lambda-функцию [click], но даже это плохая идея.
В модуле Math это уже сделали.  [click]

Еще у нас есть линейная функция для отнесения точек к кластерам.

Т.к. у всех здесь плохо с математикой, я упрощу линейную функцию за вас. `y = -x + 4 => x + y = 4`

[click] 

Так лучше, потому что координаты вместе, а они - из Дано.

К счастью, прямая проведена так, что она ни с чем не пересекается.

`clusters` Здесь мы проходимся по точкам и смотрим на ту прямую. Предлагаю просто два раза пройтись и использовать  [click] генератор.

Смертельный номер. Избавляемся от индексирования, используем генератор сразу в sum, используем объект точки вместо координат `x_c, y_c` [click]

Переместим вычисления вверх и просто пройдемся по дистанциям,
`min_point` берем первую попавшуюся
[click]

Теперь еще более ясно, что мы ищем точку с мин. суммой дистанций и видно как считается сумма. Видно, как свернуть это в `min` [click]

Букв много, поэтому можно поменьше. Аннотации типов на экзамене писать крайне не рекомендуется. 

Ну и переменные [click]

-->