# -*- coding: utf-8-spanish -*-
'''
Nombre: Abdias Edrei Alvarado
Cuenta: 0318-1997-00125
Fecha:  Viernes 10/Noviembre/2017
Script: Productos Pandigitales
'''
import time


def EsPandigital(numeroLista, rangoInicio, rangoFinal):
    '''
    Evalúa si un número es o no Pandigital.

    Un número Pandigital es aquel cuyos dígitos son todos
    los número en un rango determinado.

    Ejemplo:
    15324 es un número Pandigital del 1 al 5.

    Parámetros:
    numeroLista => el número en formato de lista para ser
                   evaluado.
    rangoInicio => el rango desde el cual se evalua si cumple.

    rangoFinal => el numero hasta el cual se evalua si cumple el
                  pandigital.
    '''
    numeroLista.sort()
    listaRango = list(range(rangoInicio, rangoFinal + 1))

    contador = 0
    if len(listaRango) == len(numeroLista):
        for x in range(len(numeroLista)):
            if numeroLista[x] == str(listaRango[x]):
                contador += 1

        if contador == len(numeroLista):
            return True
        else:
            return False
    else:
        return False


def GenerarProductosPandigitales(rangoInicio, rangoFinal):
    '''
    Genera números desde un rango de inicio hasta un rango final
    y los multiplica para evaluar si el multiplicando, el multiplicador
    y el producto concatenados son un pandigital.

    Parámetros:
    rangoInicio => el número inicial a evaluar en EsPandigita()
    rangoFinal => el número final a evaluar en EsPandigital()
    '''
    inicio = time.clock()
    total = 0
    resultados = []
    for x in range(1, 101):
        for y in range(1, 9999):
            res = x * y
            numeroCompleto = []
            numeroCompleto = list(str(x) + str(y) + str(res))
            if EsPandigital(numeroCompleto, rangoInicio, rangoFinal):
                if res in resultados:
                    break
                else:
                    resultados.append(res)
                    print(x, "*", y, "=", x * y)
                    total += res

    print("Tiempo:", time.clock() - inicio, "segundos")
    print("La suma de los productos es:", total)


GenerarProductosPandigitales(1, 9)
