# 🐍 Día 4 - Randomización y Listas

## 🌀 Randomización
En la vida cotidiana existen muchos eventos aleatorios.  
Sin embargo, una máquina es un objeto **determinístico**, es decir, realiza acciones de forma **repetible y predecible**.

En Python existe el módulo `random`, el cual permite **simular comportamientos aleatorios** dentro de un programa.  
Este módulo está documentado oficialmente en la biblioteca estándar de Python y ofrece diferentes funciones para generar números aleatorios, seleccionar elementos de listas, mezclar datos, entre otros.

👉 Documentación oficial: [random — Generar números pseudoaleatorios](https://docs.python.org/3/library/random.html)

## 📦 Módulos en Python
Un **módulo** en Python es un archivo o conjunto de archivos `.py` que contienen **funciones, clases y variables** relacionadas entre sí.  
Su propósito es **organizar el código** y **reutilizarlo** fácilmente en diferentes partes de un programa más grande.

Por ejemplo:

```python
import random

numero = random.randint(1, 10)
print(numero)
```

En este caso, `random` es el módulo y `randint()` es una de sus funciones.

## 🧱 Estructuras de datos
Las **estructuras de datos** son las diferentes formas de **almacenar y organizar información** dentro de un programa.  
En Python existen varios tipos, como:

- **Listas (`list`)**
- **Tuplas (`tuple`)**
- **Diccionarios (`dict`)**
- **Conjuntos (`set`)**

Cada una tiene características y usos distintos según el tipo de datos que se desee manejar.

### 🍎 Listas
Las **listas** son una forma de agrupar múltiples elementos dentro de una misma variable.  
Se definen utilizando corchetes `[]` y los elementos se separan por comas:

```python
frutas = ['Pera', 'Manzana', 'Fresa']
```

Podemos usarlas para guardar piezas de datos relacionados.  
Es importante entender que las listas **mantienen el orden** en el que se agregan o eliminan los elementos.

### 🔢 Índices en listas
En programación, los índices comienzan en **cero (Zero-based indexing)**.  
Esto significa que el primer elemento de la lista tiene índice `0`, el segundo `1`, y así sucesivamente.

```python
print(frutas[0])  # Pera
print(frutas[2])  # Fresa
```

> Esta forma de indexar viene de la historia de los lenguajes de programación, donde las posiciones se relacionan directamente con el desplazamiento de memoria (el primer elemento está a 0 pasos del inicio).

### 🧰 Métodos útiles que deberías conocer

| Método | Descripción | Ejemplo |
|--------|--------------|---------|
| `append()` | Agrega un elemento al final de la lista | `frutas.append('Mango')` |
| `remove()` | Elimina un elemento por su valor | `frutas.remove('Pera')` |
| `pop()` | Elimina y devuelve un elemento según su índice | `frutas.pop(1)` |
| `insert()` | Inserta un elemento en una posición específica | `frutas.insert(0, 'Banano')` |
| `sort()` | Ordena los elementos de forma ascendente | `frutas.sort()` |
| `reverse()` | Invierte el orden de los elementos | `frutas.reverse()` |
| `len()` | Devuelve la cantidad de elementos en la lista | `len(frutas)` |

### ⚠️ Errores comunes al usar listas

- **`IndexError`**: ocurre cuando intentas acceder a un índice que no existe.  
  ```python
  frutas = ['Pera', 'Manzana']
  print(frutas[3])  # ❌ IndexError: list index out of range
  ```

- **`ValueError`**: ocurre al intentar eliminar un elemento que no está en la lista.  
  ```python
  frutas.remove('Fresa')  # ❌ ValueError: list.remove(x): x not in list
  ```

## 📚 Recursos con más información
- 🧮 [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister): Algoritmo utilizado por Python para generar números pseudoaleatorios.  
- 🎓 [Generación de números pseudoaleatorios – Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
