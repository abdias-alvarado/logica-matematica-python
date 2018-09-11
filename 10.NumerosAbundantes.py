# -*- coding: utf-8-spanish -*-
'''
Nombre: Abdias Edrei Alvarado
Cuenta: 0318-1997-00125
Fecha:  Viernes 10/Noviembre/2017
Script: NumerosAbundantes
'''
import time


def EsAbundante(numero):
    '''
    Verifica si un número ingresado es o no abundante.

    Un número abundante es aquel cuya suma de divisores sin
    incluir al mismo es mayor que el mismo número.
    Sino es abundante entonces es "deficiente".

    Parámetros:
    numero => el número a evaluar si es o no abundante.
    '''

    suma = 0
    for x in range(1, numero):
        if numero % x == 0:
            suma += x

    if suma < numero:
        return False
    else:
        return True


def GenerarNumerosAbundantes(rango):
    '''
    Genera números y los agrega a un lista si éstos son
    abundantes.

    Parámetros:
    rango => número hasta el cual se generarán abundantes.
    '''
    abundantes = []
    for x in range(12, rango):
        if EsAbundante(x):
            abundantes.append(x)

    return abundantes


def BuscarNumeros():
    '''
    Genera numeros para evaluar si se pueden expresar como
    la suma de dos abundantes.

    '''
    suma = 0
    print("Generando abundantes...")
    abundantes = GenerarNumerosAbundantes(28123)
    print("Listo.")
    for numero in range(1, 28123):
        esPosible = False
        contador = 0
        if numero < 24:
            print(numero)
            suma += numero
        else:
            for x in range(len(abundantes)):
                if abundantes[x] > numero:
                    break
                elif numero % abundantes[x] == 0:
                    contador += 1

            if contador == 0:
                for y in range(len(abundantes)):
                    if abundantes[y] < numero:
                        for z in range(len(abundantes)):
                            if abundantes[z] < numero:
                                if abundantes[y] + abundantes[z] == numero:
                                    esPosible = True
                            else:
                                break
                    else:
                        break

            if not esPosible:
                print(numero)
                suma += numero
            else:
                esPosible = False

    return suma


print(BuscarNumeros())
# 20161
