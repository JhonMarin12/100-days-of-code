# Ver en consolo los elemetnos de una lista
frutas = ['Pera', 'Manzana', 'Fresa']

for fruta in frutas:
    print(fruta)
    print(fruta + " pie")

# Otro ejemplo de uso de loops
student_scores = [78, 65, 89, 92, 56, 74, 88, 45, 99, 67, 81, 59, 94, 72, 38, 83, 100, 47, 69, 91]

suma_puntajes = sum(student_scores)
print(suma_puntajes)

# Como lo puedo hacer con loops
acumulado = 0
for score in student_scores:
    acumulado += score
print(acumulado)

# Maximo puntaje
maximo_puntaje = max(student_scores)
print(maximo_puntaje)

# Haciendolo de forma manual
maximo = float('-inf')
for score in student_scores:
    if maximo < score:
        maximo = score
print(maximo)


# Superando a gauss sumando todos los numeros del 1 a 100
total = 0
for i in range(1,101):
    total += i
print(total)