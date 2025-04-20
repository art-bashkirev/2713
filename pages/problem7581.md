---
layout: full
---

# Разбор № 7581

Демо-2025

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров.

<span v-mark="{ at: 1, color: 'red', type: 'underline' }">Центроид – это одна из звёзд</span>
 на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна. Расстояние между двумя точками $A(x1, y1)$ и $B(x2, y2)$ вычисляется по формуле: $d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

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
layout: figuresplit
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
```python  {*}{maxHeight:'100px'}
# -*- coding: utf-8 -*-
```

```python 
# Расстояние
```

```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
```
````

<!--
В самом начале условия нам дали метрику расстояния [click]. Напишем функцию вычисления расстояния. [click]

На вход подаем две точки, вычисляем, возвращаем значение. [click] Читаем дальше - входные данные.
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Даны два входных файла (A и Б). В каждой строке записана информация о расположении на карте одной звезды: сначала координата $x$, затем координата $y$.

::right::

````md magic-move
```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
```
```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]
```
````

<!--
Считаем файл, получим список точек.
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Нахождение кластеров

::right::

````md magic-move
```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]
```

```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]
```

```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
```
````

<!--
Данные позволяют сгруппировать отношение звезды к кластеру вручную, поэтому создадим два кластера [click] и пробежимся по точкам. [click] Посмотрим на данные (Как будем группировать).
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

<PlotlyFigure csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/refs/heads/main/data-csv/7581_A.csv" xColumn="0" yColumn="1" />
<style>
.plotly-figure {
  margin: 0;
  align-contents: top;
  width: 350px;
  height: auto;
}
</style>

::right::

````md magic-move
```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
```

```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
```

```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```
````

<!--
Видно, что простой прямой здесь хватит. Напишем линейную функцию. Точки есть `(-2;4)`  и `(0;3)`. Получается прямая `y = -0.5x + 3`  Если точка ниже, то к одному кластеру, [click] если выше - к другому [click]

Начнем работать над логикой.

-->
---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Центроид – это одна из звёзд на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна.

::right::

````md magic-move
```python 
# Расстояние
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```

```python
clusters = [[...], [...]]

```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]
```
````

<!--
Код немного не влезает... [click] Создадим функцию `centroid`, она получает список точек кластера, и возвращает одну из точек, сумма расстояний от которой до других звезд минимальна. (Как в условии) [click] Будем хранить координаты такой точки, m - мин. найденная сумма расстояний. [click] Начнем считать [click] Берем i-тую точку и сравниваем с j-той. [click] Затем смотрим на полученную сумму. [click] Если меньше текущей минимальной, мы нашли 'лучший' центроид. Вернем эту точку[click]

Далее в программе
-->

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
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
```
````

<!--
Вычислим центроиды. [click] Получим две точки.
-->

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
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
xs = [x for x, y in centroids]
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```
````


<!--
Вытащим из `centroids` абсциссы [click] и ординаты. [click] Найдем ср. арифм. и перемножим [click]
-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

Ответ для файла A

::right::

```python {*}{maxHeight:'400px'}
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```md
10738.21226546789 30730.076059078103
```



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
def d(A: list[float, float], B: list[float, float]) -> float:
  return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5


points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```

```python 
# Расстояние
d = lambda A, B: ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] < point[0] * (-0.5) + 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[1] + point[0] * (0.5) < 3:
    clusters[0].append(point)
  else:
    clusters[1].append(point)
```

```python 
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] * (0.5) + p[1] < 3)],
  [p for p in points if (p[0] * (0.5) + p[1] > 3)]
]
```

```python
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  x_c, y_c, m = None, None, 10 ** 9
  for i in range(len(cluster)):
    s = 0 # Сумма расстояний от i-той точки до всех остальных в кластере
    for j in range(len(cluster)):
      s += d(cluster[i], cluster[j])
    if s < m:
      m = s
      x_c, y_c = cluster[i][0], cluster[i][1]
  return [x_c, y_c]

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)

```


```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  c, m = None, 10 ** 9
  for p in cluster:
    s = sum(d(p, other) for other in cluster)
    if s < m:
      m = s
      c = p
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  distances = [
      (p, sum(d(p, other) for other in cluster))
      for p in cluster
  ]
  c, m = distances[0], 10 ** 9
  for p, s in distances:
    if s < m:
      c, m = p, s
          
  return c


centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
clusters = [[...], [...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  c = min(cluster, 
              key=lambda p: sum(d(p, other) for other in cluster))
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
clusters = [[...], [...]]

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
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] * (0.5) + p[1] < 3)],
  [p for p in points if (p[0] * (0.5) + p[1] > 3)]
]

def centroid(cluster):
  c = min(cluster, key=lambda p: sum(d(p, o) for o in cluster))
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```
````

<!--
Начнем упрощать этот код. Сначала.

Я бы преобразовал вычисление расстояния в Lambda-функцию [click], но даже это плохая идея.
В модуле Math это уже сделали. [click]

Еще у нас есть линейная функция для отнесения точек к кластерам.

Т.к. у всех здесь плохо с математикой, я упрощу линейную функцию за вас. `y = -x + 4 => x + y = 4` [click]

Так лучше, потому что координаты вместе, а они - из Дано. К счастью, прямая проведена так, что она ни с чем не пересекается.

`clusters` Здесь мы проходимся по точкам и смотрим отношение точки к прямой. В таком нагромождении ничего плохого нет, но предлагаю просто два раза пройтись и использовать  [click] генератор. Точно так же сверну код. [click]

Смертельный номер. Мы здесь `s in centroid` считаем сумму, которую можно свернуть в генератор. А вместо безумия с индексами используем объекты точек. [click]

Переместим вычисления вверх и просто пройдемся по дистанциям. Видно, как мы считаем сумму дистанций, поэтому вытащим это в генератор. [click]

Остался последний цикл, где мы просто ищем точку с мин. суммой расстояний. Сворачивается это в `min` [click]

Букв много, поэтому можно поменьше.
Аннотации типов на экзамене писать крайне не рекомендуется. [click]

Ну и весь код [click]

Перейдем к файлу B.

-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025

::left::

<PlotlyFigure csvUrl="https://raw.githubusercontent.com/art-bashkirev/2713-pub/refs/heads/main/data-csv/7581_B.csv" xColumn="0" yColumn="1" />

<style>
.plotly-figure {
  margin: 0;
  align-contents: top;
  width: 350px;
  height: auto;
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
  [p for p in points if (p[0] * (0.5) + p[1] < 3)],
  [p for p in points if (p[0] * (0.5) + p[1] > 3)]
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
          for line in open("7581_B.txt")]

clusters = [
  [p for p in points if ],
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
````

<!--
Для файла B осталось только определить линейные функции. Три кластера у нас здесь [click]

`(0;6)` прекрасная точка для начала. 

Для прямой к ней пойдет `(6;0)` и `(6;8)`

Прямые `y = -x + 6` и `y = x/3 + 6` соответственно. Один кластер выше первой, второй между, третий - ниже второй.
[click]

Вписываем условие, получаем ответ [click]

-->

---
layout: codesplit
---

# Разбор № 7581

Демо-2025


::left::

Ответ для файла B.

::right::

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

```md
37522.944615707165 51277.95880214987
```

<!-- 
Далее идет аналогичная задача из ЕГКР. Решите сами)
-->