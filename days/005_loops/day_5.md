# 🐍 Día 5 - Ciclos (Loops)

Los **ciclos** (o bucles) son estructuras que permiten **repetir un bloque de código** múltiples veces.  
En Python existen dos tipos principales:

- **Ciclo `for`**
- **Ciclo `while`**

La diferencia entre ambos radica en **qué controla la repetición**:

| Tipo de ciclo | Se repite mientras... | Depende de |
|----------------|------------------------|-------------|
| `for` | haya elementos en una secuencia (lista, string, rango, etc.) | un objeto iterable |
| `while` | una condición lógica sea verdadera | una condición booleana |

---

## 🔁 Ciclo `for`

El ciclo `for` se usa para **recorrer elementos** dentro de un objeto iterable (lista, string, rango, etc.).  

Ejemplo:
```python
frutas = ["Manzana", "Pera", "Fresa"]

for fruta in frutas:
    print(fruta)
```

➡️ Este código imprime cada elemento de la lista uno por uno.

También puedes usar `for` con la función `range()` para ejecutar un número específico de repeticiones sin depender de una lista.

```python
for numero in range(5):
    print(numero)
```

Salida:
```
0
1
2
3
4
```

> 🧠 Nota: `range(5)` genera los números del 0 al 4. El límite superior **no se incluye**.

---

## 🔄 Ciclo `while`

El ciclo `while` ejecuta un bloque de código **mientras una condición sea verdadera**.

```python
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```

Este ciclo imprimirá los números del 0 al 4, incrementando `contador` en cada vuelta.

⚠️ **Cuidado:** si la condición nunca se vuelve falsa, el ciclo se repetirá infinitamente.

---

## 🧱 Indentación

La **indentación** en Python es fundamental.  
Consiste en los espacios que indican **a qué bloque de código pertenece cada instrucción**.

Por ejemplo:
```python
for numero in range(3):
    print(numero)
    print("Dentro del ciclo")
print("Fuera del ciclo")
```

La indentación (por defecto 4 espacios) le dice a Python **qué líneas pertenecen al ciclo** y cuáles no.

> Si la indentación no es correcta, Python lanzará un `IndentationError`.

---

## 🔢 Inicializar valores correctamente

En ejercicios con ciclos (como buscar máximos, mínimos o acumuladores) es común **inicializar variables**.

A veces vemos esto:
```python
maximo = 0
```

Sin embargo, **no siempre es lo ideal**, ya que no sabemos si los valores de la lista serán positivos o negativos.

Opciones más seguras:

- Inicializar con el **primer elemento**:
  ```python
  maximo = lista[0]
  ```

- Usar **menos infinito**, lo que garantiza que cualquier valor sea mayor:
  ```python
  maximo = float('-inf')
  ```

Esto evita errores lógicos y hace el código más robusto.

---

## 🧮 La función `range()`

La función `range()` genera una **secuencia de números enteros** que puede ser usada dentro de un ciclo `for`.

### Sintaxis:
```python
range(inicio, fin, paso)
```

- `inicio` → valor inicial (por defecto 0)
- `fin` → valor hasta el cual llega (sin incluirlo)
- `paso` → incremento entre valores (por defecto 1)

Ejemplos:

```python
for numero in range(1, 6):
    print(numero)  # 1 2 3 4 5

for numero in range(0, 10, 2):
    print(numero)  # 0 2 4 6 8
```

Puedes combinarlo con otras estructuras:
```python
suma = 0
for numero in range(1, 11):
    suma += numero
print(f"La suma total es: {suma}")
```

---

## 🧠 Conceptos clave del día

- Los **ciclos `for`** se usan para recorrer elementos.
- Los **ciclos `while`** dependen de una **condición lógica**.
- La **indentación** define el flujo del programa.
- **No siempre inicialices con 0**, usa valores más seguros según el contexto.
- `range()` es una herramienta poderosa para iteraciones controladas.

---

## 📚 Recursos recomendados

- 🔗 [Documentación oficial sobre bucles en Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- 🎓 [Curso de Python Loops – W3Schools](https://www.w3schools.com/python/python_for_loops.asp)
- 💡 [Visualización interactiva de loops en PythonTutor](https://pythontutor.com/)
