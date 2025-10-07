import random
import my_module

# random.seed(123)

# a = random.randint(1,10)
# b = random.randint(1,10)

# print(a, b)

#LLamanda de una variable a partir de un modulo propio
print(my_module.my_favourite_number)

# real_valued_distribution
random_number_0_to_1 = random.random() # Obtenemos un numero entre 0 y 1, sin incluir el 1.
print(random_number_0_to_1)

# ramdon_float_generation
random_float = random.uniform(1,10)
print(random_float)

coin_flip = random.randint(0,1)

if coin_flip == 0:
    print("Heads")
else:
    print("Tails")


############## Jugando con listas ###################

states_of_america = ["Delaware", "Pnnsylvania", "New Jersey", "Georgia"]

# Acceder a datos mediante el indice
print(states_of_america[0])

# Contar de forma inversa
print(states_of_america[-1])

# Las listas son elementos mutables
states_of_america[1] = 'Venezuela'
print(states_of_america)

# Podemos añadir elementos con metodos integrados en las listas
states_of_america.append("Polombia")
print(states_of_america)