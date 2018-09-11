# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 1. Digitos Factoriales.py
import time


def EsFactorialCurioso(numero):
    '''
    Verifica si un número ingresado es un
    factorial curioso.

    Un factorial curioso es un número tal que
    la suma del factorial de sus dígitos es igual
    al mismo número.

    Ejemplo:
    145 = 1! + 4! + 5!

    Parámetros:
    numero => el número a verificar.
    '''
    # Convertimos el número en tipo lista para manejarlo
    # dígito a dígito.
    numeroFormatoLista = list(str(numero))

    sumaFactorialDigitos = 0
    for indice in range(0, len(numeroFormatoLista)):
        sumaFactorialDigitos += Factorial(int(numeroFormatoLista[indice]))

    if sumaFactorialDigitos == numero:
        return True
    else:
        return False


def Factorial(numero):
    '''
    Calcula el factorial de un número ingresado por
    el usuario.

    El factorial se define como:
    n(n - 1)!

    Parámetros:
    numero => el número al cual se le calculará el
              factorial.
    '''
    if numero < 2:
        return 1
    else:
        return numero * Factorial(numero - 1)


def SumaFactorialesCuriosos(rango):
    '''
    Retorna la suma de los factoriales curiosos
    hasta un rango determinado.

    Un factorial curioso es un número tal que
    la suma del factorial de sus dígitos es igual
    al mismo número.

    Ejemplo:
    145 = 1! + 4! + 5!

    Parámetros:
    rango => rango de búsqueda.
    '''
    suma = 0
    for numero in range(3, rango):
        if EsFactorialCurioso(numero):
            suma += numero

    return suma


def run():
    '''
    Función main del programa.
    '''
    print('===== Dígitos Factoriales Curiosos =====')
    rango = int(input('Ingrese el rango maximo de búsqueda:'))
    print("Rango de busqueda:", rango)
    inicio = time.clock()
    print("La suma de los digitos factoriales curiosos es:",
          SumaFactorialesCuriosos(rango))
    print("Tiempo de busqueda:", time.clock() - inicio, "segundos")


if __name__ == '__main__':
    run()
