# Presentation + Notes (Draft)
> Consolidated for quick review before presenting.
> Generated from `slides.md` and included page files.

## Deck entry: `slides.md`

---
author: Artem Bashkirev
title: Задание 27 ЕГЭ
keywords: 27, ЕГЭ Информатика
aspectRatio: 4/3
fonts:
  sans: IBM Plex Sans
  serif: IBM Plex Serif
  mono: Monaspace Krypton
  # mono: IBM Plex Mono
mdc: true
layout: full
remoteAssets: true
---

<!-- THIS IS THE COVER -->

<style>
.huge-number {
  font: 35rem "Monaspace Neon", sans-serif;
  font-weight: 600;
  margin: 0;
  margin-top: 3rem;
  line-height: 1;
  background: linear-gradient(45deg, #ff0861, #ff2a63, #f43f47, #ff6a00, #ffd300);
  background-size: 300% 300%; /* Adjusted background size for better visibility */
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: gradient 15s ease infinite, pulse 5s ease infinite;
  position: relative; /* Changed to relative */
  text-shadow: 0 0 40px rgba(255, 8, 97, 0.7);
  filter: drop-shadow(0 0 20px rgba(255, 72, 0, 0.5));
  display: flex; /* Added for centering */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 100%; /* Full height of the container */
  z-index: 1; /* Ensure number is above particles */
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.void-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(ellipse at center, #000000 0%, #0a0a0a 100%);
  z-index: -1; /* Ensure background is behind other elements */
}

.glow-particles {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0; /* Ensure particles are behind the number */
}

.glow-particles div {
  position: absolute;
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: particle-anim 20s linear infinite;
}

@keyframes particle-anim {
  0% { transform: scale(0) translateY(0); opacity: 0; }
  50% { transform: scale(1.5) translateY(-100px); opacity: 0.5; }
  100% { transform: scale(0) translateY(-200px); opacity: 0; }
}
</style>

<div class="void-background">
  <div class="glow-particles">
  <!-- <div class="w-96 h-96 bg-gradient-to-r from-cyan-500/30 to-blue-600/30 top-1/4 left-1/4 blur-3xl"></div>
  <div class="w-64 h-64 bg-gradient-to-r from-red-500/40 to-purple-600/40 top-1/3 right-1/4 blur-2xl"></div> -->
  <div class="w-80 h-80 bg-gradient-to-r from-green-500/30 to-yellow-600/30 top-1/2 left-1/4 blur-2xl"></div>
  <div class="w-72 h-72 bg-gradient-to-r from-blue-500/40 to-pink-600/40 top-1/4 right-1/4 blur-3xl"></div>
  <div class="w-56 h-56 bg-gradient-to-r from-purple-500/30 to-orange-600/30 top-3/4 left-1/2 blur-2xl"></div>
  <div class="w-48 h-48 bg-gradient-to-r from-pink-500/40 to-cyan-600 /40 top-1/2 right-1/3 blur-3xl"></div>
  <div class="w-40 h-40 bg-gradient-to-r from-yellow-500/30 to-red-600/30 top-1/3 left-1/3 blur-2xl"></div>
  <div class="w-60 h-60 bg-gradient-to-r from-teal-500/40 to-indigo-600/40 top-1/4 left-3/4 blur-3xl"></div>
  <div class="w-72 h-72 bg-gradient-to-r from-orange-500/30 to-red-600/30 top-0 left-0 blur-3xl"></div>
</div>
  <h1 class="huge-number">27</h1>
</div>

<!--
THIS IS THE COVER
-->

---
src: ./pages/overview.md
---
---
src: ./pages/lambda-warmup.md
---
---
# Демо-2025
src: ./pages/problem7581.md 
---
---
# ЕГКР-2024
src: ./pages/problem7944.md 
---
---
# Моя задача с ЕГЭ-2025
src: ./pages/problem8242.md
---
---
# ЕГКР-2025
src: ./pages/problem8715.md
---
---
# Досрочный ЕГЭ-2026
src: ./pages/problem9025.md
---


## Included source: `pages/overview.md`

---
layout: statement
---

# 27

## Анализ данных

### **Задача** - Разделение объектов на группы (кластеры) по метрикам анализа


## Included source: `pages/lambda-warmup.md`

---
layout: codesplit
---

# `Lambda`-разгон

::left::

`Lambda` - анонимная функция


- Одно выражение, значение возвращается сразу
- Обычно используется как аргумент в высокоуровневых функциях

::right::

````md magic-move
```python
# -*- coding: utf-8 -*-
```

```python
def manhattan_dist(point: list[float, float]) -> float:
  return abs(point[0]) + abs(point[1])

manhattan_dist(3, -4) # -> 7
```

```python
manhattan_dist = lambda p: abs(p[0]) + abs(p[1])

manhattan_dist(3, -4) # -> 7
```

```python
(lambda p: abs(p[0]) + abs(p[1]))((3, -4))  # -> 7
```
````

<!--
Лямбда функция - это выражение без имени, значение которого сразу возвращается. При этом, мы получаем её объект обратно и можем его вызвать. Для наглядности напишем метрику манхэттенского расстояния до начала координат. 
[click]
Такое нехитрое выражение очень прость свернуть в `lambda` функцию.
[click]
Т.к. возвращается вызываемый объект, то можно осуществить и такое безумие. Пока несложно.
-->

---
layout: codesplit
---

# `Lambda`-разгон / `map`

::left::

- `map(f, *iterable)`
- Применяет `f` к *каждому* элементу `iterable`
- Возвращает `iterable`

::right::

````md magic-move
```python
manhattan_dist = lambda p: abs(p[0]) + abs(p[1])
```

```python
manhattan_dist = lambda p: abs(p[0]) + abs(p[1])

points = [(1, 2), (3, 4), ..., (8, 9)]
```

```python
manhattan_dist = lambda p: abs(p[0]) + abs(p[1])

points = [(1, 2), (3, 4), ..., (8, 9)]

dist = map(manhattan_dist, points)
# [3, 7, ..., 17]
```

```python
points = [(1, 2), (3, 4), ..., (8, 9)]

dist = map(lambda p: abs(p[0]) + abs(p[1]), points)
# [3, 7, ..., 17]
```

```python
x_coords = [0, 1, 2, 3]
y_coords = [5, 4, 3, 2]

points = map(lambda x, y: (x, y), x_coords, y_coords)
# [(0, 5), (1, 4), (2, 3), (3, 2)]
```

```python
points1 = [(0, 0), (1, 1), (2, 2)]
points2 = [(3, 4), (5, 1), (0, 7), (9, 9)]

dist_sq = map(lambda p1, p2: (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2,
                   points1, points2)
```
````

<!--
Далее функция map. map берет по элементу из каждого объекта и передает в lambda.

Предположим, что у нас есть список точек, от которых надо посчитать манх. расстояние.

[click]
Пока все просто.
[click]

В этом прелесть lambda-функции - можно сразу воткнуть её в map
[click]

Еще есть вариант - собрать несколько объектов. Тут мы передаем два списка и соединяем их в объекты - точки.

[click]
Тем же способом можно найти в данном случае квадрат евклидова расстояния между точками. Здесь map выдаст три значения, т.к. кончились точки, к которым можно это применить.

[click]
Пока что хватит. Перейдем к задачам.
-->


## Included source: `pages/problem7581.md`

---
layout: full
---

# Разбор № 7581

Демо-2025

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике. Каждая звезда обязательно принадлежит только одному из кластеров.

<span v-mark="{ at: 1, color: 'red', type: 'underline' }">Центроид – это одна из звёзд</span>
 на графике, сумма расстояний от которой до всех остальных звёзд кластера минимальна. Расстояние между двумя точками $A(x_1, y_1)$ и $B(x_2, y_2)$ вычисляется по формуле: 
$$
d(A, B) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
$$

<span v-mark="{ at: 2, color: 'red', type: 'underline' }">Даны два входных файла (A и Б).</span> В каждой строке записана информация о расположении на карте одной звезды: сначала координата $x$, затем координата $y$. В файле A хранятся данные о звёздах двух кластеров. Известно, что количество звёзд не превышает $1000$. В файле Б хранятся данные о звёздах трёх кластеров. Известно, что количество звёзд не превышает $10 000$. Структура хранения информации о звездах в файле Б аналогична файлу А.

Для каждого файла <span v-mark="{ at: 1, color: 'red', type: 'underline' }">определите координаты центра каждого кластера</span>, затем вычислите два числа: $P_x$ – среднее арифметическое абсцисс центров кластеров, и $P_y$ – среднее арифметическое ординат центров кластеров.
В ответе запишите четыре числа: в первой строке сначала целую часть произведения $P_x \cdot 10 000$, затем целую часть произведения $P_y \cdot 10 000$ для файла А, во второй строке – аналогичные данные для файла Б.

<!-- 

Начнем читать условие. Первое правило ЕГЭ - ответить на вопрос "Что спрашивают"! [click]

Что можно сразу выделить - это определение "Центроид". Центроидом считается одна из данных звезд и найти надо координаты уже существующие. Поэтому придётся ходить по данным.

[click]

Ещё важно - дается 2 файла. Один поменьше, другой побольше. Вроде как на этот год сущую переборную халяву оставили.

Предлагаю посмотреть на файлы.
-->

---
layout: figuresplit
---

# Разбор № 7581

Демо-2025

::left::

Файл А

<PlotlyFigure csvUrl="/7581_A.csv" xColumn="0" yColumn="1" />

::right::

Файл B

<PlotlyFigure csvUrl="/7581_B.csv" xColumn="0" yColumn="1" />


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

$$
d(A, B) = \sqrt{(x_A - x_B)^2 + (y_A - y_B)^2}
$$


$$
d\left(\begin{bmatrix}
x_A \\ y_A
\end{bmatrix}, 
\begin{bmatrix}
x_B \\ y_B
\end{bmatrix}
\right) = \sqrt{(x_A - x_B)^2 + (y_A - y_B)^2}
$$
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

Даны два входных файла (A и Б). В каждой строке записана информация о расположении на карте одной звезды:

сначала координата $x$, затем координата $y$.

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

<PlotlyFigure csvUrl="/7581_A.csv" xColumn="0" yColumn="1" />

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
Код немного не влезает... [click] Создадим функцию `centroid`, она получает список точек кластера, и возвращает одну из точек, сумма расстояний от которой до других звезд минимальна. (Как в условии) [click] Будем хранить координаты такой точки, m - мин. найденная сумма расстояний. [click] Начнем ходить по точкам. [click] Берем i-тую точку и считаем расстояние от нее до j-той. [click] Затем смотрим на полученную сумму. [click] Если меньше текущей минимальной, мы нашли 'лучший' центроид. Вернем эту точку[click]

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

В ответе запишите четыре числа: в первой строке сначала целую часть произведения $P_x \cdot 10 000$, затем целую часть произведения $P_y \cdot 10 000$ для файла А, во второй строке – аналогичные данные для файла Б.

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
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [[], []]

for point in points:
  if point[0] * (0.5) + point[1] < 3:
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

```python
# Расстояние
from math import dist as d

points = [list(map(float, line.replace(",", ".").split())) 
          for line in open("7581_A.txt")]

clusters = [
  [p for p in points if (p[0] * (0.5) + p[1] < 3)],
  [p for p in points if (p[0] * (0.5) + p[1] > 3)]
]

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
clusters = [[...],[...]]

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
clusters = [[...],[...]]

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
clusters = [[...],[...]]

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
clusters = [[...],[...]]

def centroid(cluster: list[list[float, float]]) -> list[float, float]:
  c = min(cluster, 
              key=lambda p: sum(d(p, other) for other in cluster))
  return c

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```

```python 
clusters = [[...],[...]]

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
  return min(cluster, key=lambda p: sum(d(p, o) for o in cluster))

centroids = [centroid(clstr) for clstr in clusters]
xs, ys = [x for x, y in centroids], [y for x, y in centroids]
print((sum(xs) / len(xs)) * 10_000, (sum(ys) / len(ys)) * 10_000)
```
````

<!--
Начнем упрощать этот код. Сначала.

Я бы преобразовал вычисление расстояния в Lambda-функцию [click], но даже это плохая идея.
В модуле Math это уже сделали. Функция `dist`, элиасим как d чтобы ничего не менять в коде. [click]

Еще у нас есть линейная функция для отнесения точек к кластерам.

Т.к. у всех здесь плохо с математикой, я упрощу линейную функцию за вас. `y = -x + 4 => x + y = 4` [click]

К счастью, прямая проведена так, что она ни с чем не пересекается.

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

<PlotlyFigure csvUrl="/7581_B.csv" xColumn="0" yColumn="1" />

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
  return min(cluster, key=lambda p: sum(d(p, o) for o in cluster))

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


## Included source: `pages/problem7944.md`

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
  [p for p in points if p[1] + p[0] * (1.5) < 0]
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
  [p for p in points if p[1] + p[0] * (1.5) < 0]
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
  [p for p in points if p[1] + p[0] * (1.5) < 0]
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


## Included source: `pages/problem8242.md`

---
layout: full
---

# Решение № 8243

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

# Решение № 8243

Моя задача с ЕГЭ-2025

::left::

Файл А

<PlotlyFigure csvUrl="/8242_A.csv" xColumn="0" yColumn="1" />

::right::

Файл Б

<PlotlyFigure csvUrl="/8242_B.csv" xColumn="0" yColumn="1" />

---
layout: codesplit
---

# Решение № 8243

Моя задача с ЕГЭ-2025

::left::

В предыдущей серии... и адаптация под следующую задачу.

<PlotlyFigure csvUrl="/8242_A.csv" xColumn="0" yColumn="1" />

<style>
.plotly-figure {
  margin: 0;
  align-content: top;
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
from math import dist as d

points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8242_A.txt")]

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
````

---
layout: codesplit
---

# Решение № 8243

Моя задача с ЕГЭ-2025

::left::

Ответ.

::right::

````md magic-move
```python
# Расстояние
from itertools import combinations
from math import dist as d

# Файл A
points = [list(map(float, line.replace(",", ".").split()))
          for line in open("8242_A.txt")]

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
          for line in open("8242_B.txt")]

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
110156 196632
224871 273226
```
````


## Included source: `pages/problem8715.md`

---
layout: codesplit
---

# Решение № 8715

ЕГКР-2025

::left::

::right::


## Included source: `pages/problem9025.md`

---
layout: codesplit
---

# Решение № 9025

Досрочный ЕГЭ-2026

::left::

::right::
