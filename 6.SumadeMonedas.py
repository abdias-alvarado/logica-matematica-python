# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 6. Suma de Monedas.py
import time


def CombinarMonedas(cantidadLibrasEsterlinas):
    '''
    Realiza todas las combinaciones posibles para
    una cantidad específica de libras esterlinas.

    Parámetros:
    cantidadLibrasEsterlinas => la suma total a generar combinando peniques.

    '''
    cantidadLibrasEsterlinas *= 100
    peniques = [1, 2, 5, 10, 20, 50, 100]
    total = 0

    for indice1 in range(cantidadLibrasEsterlinas):



