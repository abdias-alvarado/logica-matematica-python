# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 1. Digitos Factoriales.py
import time


def EsPrimo(numero):
    '''
    Retorna True si el número dado es primo. Caso
    contrario retorna False.

    Parámetros:
    numero --> El numero a calcular si es primo.

    '''
    if numero == 2 or numero == 3:
        return True

    if numero % 2 == 0 or numero < 2:
        return False

    for x in range(3, int(numero ** 0.5) + 1, 2):
        if numero % x == 0:
            return False

    return True


def NumerosPrimos(rangoMaximo):
    '''
    Retorna los números primos desde 2 hasta el valor dado.

    Los números primos son aquellos que sólamente son
    divisibles entre el mismo número y el número uno. División entera.

    Parámetros:
    final ---> El valor hasta el cuál se calculas los números primos.
    inicio --> El valor desde el cuál se comienza el cálculo. (Opcional)

    '''
    inicio = time.clock()
    suma = 0
    for x in range(2, rangoMaximo + 1):
        if EsPrimo(x):
            suma += x

    print("Tiempo:", time.clock() - inicio, "segundos")
    print("La suma de los número primos menores a", rangoMaximo, "es:", suma)


rango = int(input('Ingrese un rango máximo de búsqueda: '))
NumerosPrimos(rango)
