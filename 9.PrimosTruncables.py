# -*- coding: utf-8-spanish -*-
'''
Nombre: Abdias Edrei Alvarado
Cuenta: 0318-1997-00125
Fecha:  Viernes 10/Noviembre/2017
Script: Primos Truncables
'''
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

    if numero < 2 or numero % 2 == 0:
        return False

    for x in range(3, int(numero ** 0.5) + 1, 2):
        if numero % x == 0:
            return False

    return True


def EsPrimoTruncableIzquierda(numeroLista):
    '''
    Evalúa si un número ingresado por el usuario en formato
    de lista, es un primo truncable por la izquierda.

    Un número primo truncable por la izquierda, es aquel numero primo que
    al eliminar uno a uno sus dígitos más a la izquierda continúa siendo
    un número primo.

    Ejemplo:
    23 es primo
    3 sigue siendo primo

    Parámetros:
    numeroLista => el número en formato de lista a evaluar.
    '''
    controladorCiclo = len(numeroLista)
    contador = 0
    indiceIzquierdo = 0
    for x in range(controladorCiclo):
        if len(numeroLista) > 1:
            if EsPrimo(ConvertirAEntero(numeroLista)):
                contador += 1
                numeroLista.pop(indiceIzquierdo)
        else:
            if EsPrimo(ConvertirAEntero(numeroLista)):
                contador += 1

    if contador == controladorCiclo:
        return True
    else:
        return False


def EsPrimoTruncableDerecha(numeroLista):
    '''
    Evalúa si un número ingresado por el usuario en formato
    de lista, es un primo truncable por la derecha.

    Un número primo truncable por la derecha, es aquel numero primo que
    al eliminar uno a uno sus dígitos más a la derecha continúa siendo
    un número primo.

    Ejemplo:
    23 es primo
    2 sigue siendo primo

    Parámetros:
    numeroLista => el número en formato de lista a evaluar.
    '''
    controladorCiclo = len(numeroLista)
    contador = 0
    for x in range(controladorCiclo):
        indiceDerecha = len(numeroLista) - 1
        if len(numeroLista) > 1:
            if EsPrimo(ConvertirAEntero(numeroLista)):
                contador += 1
                numeroLista.pop(indiceDerecha)
        else:
            if EsPrimo(ConvertirAEntero(numeroLista)):
                contador += 1

    if contador == controladorCiclo:
        return True
    else:
        return False


def PrimosTruncables(cantidad):
    '''
    Encuentra una cantidad de números primos truncables y los
    imprime en pantalla.

    Un número primo truncable, es aquel numero primo que es truncable por
    la derecha y por la izquierda.

    Ejemplo:
    Por derecha:
        23 es primo
        3 sigue siendo primo
    Por derecha:
        23 es primo
        2 sigue siendo primo

    Parámetros:
    numeroLista => el número en formato de lista a evaluar.
    '''
    inicio = time.clock()
    contador = 0
    numero = 13

    while contador < cantidad:
        numeroListaDer = list(str(numero))
        numeroListaIzq = list(str(numero))
        if EsPrimo(numero) and EsPrimoTruncableDerecha(numeroListaDer) and EsPrimoTruncableIzquierda(numeroListaIzq):
            contador += 1
            print(contador, "=>", numero)

        numero += 2

    print("Tiempo:", time.clock() - inicio, "segundos")


def ConvertirAEntero(lista):
    '''
    Convierte una lista de dígitos a un sólo dígito entero.

    Parámetros:
    lista => lista con los dígitos a convertir en numero entero.
    '''
    numeroString = ""
    for x in range(len(lista)):
        numeroString += str(lista[x])

    numero = int(numeroString)
    return numero


PrimosTruncables(11)
