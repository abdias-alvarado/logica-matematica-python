# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 4. Secuencia Collatz Larga.py
import time


def Collatz(secuencia, n):
    '''
    Encuentra la secuencia de Collatz de manera recursiva
    para un numero dado.

    Parámetros:
    secuencia => una lista en la que se agregaran valores
                 generados por la función.

    n => el número a calcularle la secuencia.
    '''
    if len(secuencia) == 0:
        secuencia.append(int(n))
    if n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        secuencia.append(int(n))
    else:
        return secuencia

    return Collatz(secuencia, n)


def CollatzMasLarga(rango):
    '''
    Encuentra la sencuencia de Collatz más larga y la cantidad
    de órbitas que le corresponden.

    Parámetros:
    rango => número hasta el cual se buscará la secuencia collatz
             más larga.
    '''
    inicio = time.clock()
    longitudesSecuencia = []
    for indice in range(rango):
        lista = []
        longitudesSecuencia.append(len(Collatz(lista, indice)))

    lista = []
    print("Tiempo transcurrido:", time.clock() - inicio, "segundos")
    print("Longitud del mayor:",
          len(Collatz(lista, Mayor(longitudesSecuencia))),
          "orbitas")
    return Mayor(longitudesSecuencia)


def Mayor(lista):
    '''
    Recorre todos los elementos de una lista para encontrar
    el número mayor de la misma y devolver la posición en la
    que se encuentra.

    Parámetros:
    lista => la lista de la cual se quiere encontrar el mayor.
    '''
    mayor = lista[0]
    for x in range(len(lista) - 1):
        if mayor < lista[x]:
            mayor = lista[x]

    return lista.index(mayor)


lista = []
print("El mayor Collatz es:", CollatzMasLarga(1000000))
