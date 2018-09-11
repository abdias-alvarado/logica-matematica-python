# -*- coding: utf-8-spanish -*-
'''
Nombre: Abdias Edrei Alvarado
Cuenta: 0318-1997-00125
Fecha:  Viernes 10/Noviembre/2017
Script: Palíndromos de Doble Base
'''
import time


def EsPalindromo(frase):
    '''
    Evalúa si una frase ingresada es o no palíndromo.

    Un palíndromo es una frase o numero que se escribe
    igual al derecho y al revés.

    Ejemplo:
    o s o = o s o
    1 0 0 1 = 1 0 0 1

    Parámetros:
    frase => frase o número a evaluar.
    '''
    list(frase)
    listaReversa = []
    contador = 0
    for x in range(len(frase) - 1, -1, -1):
        listaReversa.append(frase[x])

    for x in range(len(frase)):
        if frase[x] == listaReversa[x]:
            contador += 1
    if contador == len(frase):
        return True
    else:
        return False


def PalindromosDobleBase(rango):
    '''
    Encuentra todos los palíndromos de doble base hasta un rango
    dado por el usuario.

    Un palíndromo de doble base es un número que es palíndromo
    en el sistema decimal como su equivalente en el sistema binario.

    Ejemplo:
    585 = 1001001001
    Ambos son palíndromos.

    Parámetros:
    rango => rango final hasta el cual buscar.
    '''
    inicio = time.clock()
    suma = 0
    for x in range(10, rango):
        if EsPalindromo(str(x)) and EsPalindromo(ConvertirABinario(x)):
            print(x, "=>", ConvertirABinario(x))
            suma += x

    print("La suma total de Palindromos de Doble base hasta",
          rango, "es:", suma)
    print("Tiempo:", time.clock() - inicio, "segundos")


def ConvertirABinario(numero):
    '''
    Convierte un número del sistema decimal al sistema binario.

    Parámetros:
    numero => numero a convertir.
    '''
    numeroEnBinario = []
    residuo = 0

    while numero > 0:
        residuo = numero % 2
        numeroEnBinario.append(residuo)
        numero = int(numero / 2)

    numeroEnBinario.reverse()

    while numeroEnBinario[0] != 1:
        if numeroEnBinario[0] == 0:
            numeroEnBinario.pop(0)
        else:
            return numeroEnBinario

    return numeroEnBinario


PalindromosDobleBase(1000000)
