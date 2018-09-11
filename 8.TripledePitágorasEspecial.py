# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 2. Triple de pitágoras especial.py
import time


def TriplePitagoras(valor):
    '''
    Encuentra todas las ternas pitagóricas especiales
    donde la suma de los valores de a, b y c son iguales
    a un valor establecido por el usuario.

    Parámetros:
    valor => el número a comparar con a + b + c.
    '''
    inicio = time.clock()

    for a in range(1, valor):
        for b in range(a, valor):
            for c in range(b, valor):
                if a ** 2 + b ** 2 == c ** 2:
                    if a + b + c == valor:
                        print("Terna encontada: [", a, ",", b, ",", c, "]")
                        print("Suma:", a, "+", b, "+", c, "=", a + b + c)
                        print("El producto abc es:", a * b * c)
                        break

    print('Tiempo:', time.clock() - inicio, "segundos.")


TriplePitagoras(1000)
