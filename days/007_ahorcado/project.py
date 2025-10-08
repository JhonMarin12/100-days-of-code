import random
from resources import stages, list_palabras, letras, mensaje_inicial

disponibles = letras
palabra_secreta = random.choice(list_palabras)
vidas = 6


def mensaje_vidas(vidas):
    '''Muestra en pantalla la actualizacion de las vidas restantes'''
    print('*'*15, f'{vidas}/6 Vidas Restante', '*'*15)


def validar_letra(letra_adividada, palabra_secreta):
    if letra_adividada in palabra_secreta:
        return True
    else:
        return False


def estado_ahorcado(vidas, stages):
    estado = -vidas
    return stages[estado]


print(mensaje_inicial)
while vidas > 0:
    letra_usuario = input("Adivina una letra: ")
    letra_en_palabra = validar_letra(letra_usuario, palabra_secreta)
    if letra_en_palabra:
        print('Ya tienes una')
    else:
        vidas -= 1
        print(f"La letra {letra_usuario}, no está en la palabra, has perdido una vida")
    estado_jugador = estado_ahorcado(vidas, stages)
    print(estado_jugador)
    mensaje_vidas(vidas)
print("Juego Finalizado")
