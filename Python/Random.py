# -*- coding:utf-8 -*-

import random as rd

def run():
    print("Bienvenido al juego de los numeros aleatorios\n\n")

    print('Elige de que numero hata cual otro numero quieres que se genere el numero')

    base = int(input('Desde: '))
    final = int(input('Hasta: '))


    number_found = False
    random_number = rd.randint(base, (final + 1))

    while not number_found:
        number = int(input('Intenta el numero: '))

        if random_number == number:
            print("Felicitaciones lo lograste!!!!")
            number_found = True
        elif number > random_number:
            print('El numero que ingreaste es mas grande que el generado')
        elif number < random_number:
            print("El numero que ingresaste es mas pequeño que el generado")


if __name__ == "__main__":
    run()