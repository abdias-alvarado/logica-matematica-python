# -*- coding: utf-8-spanish -*-
# Autor: Abdias Alvarado
# Fecha: 28/Oct/2017
# Script: 5. Contando Domingos.py
from datetime import datetime
from datetime import timedelta
import time


def DomingosInicioMes(fechaInicio, fechaFinal):
    '''
    Retorna la cantidad de veces que un mes
    comenzó con un domingo, en un rango
    específico de tiempo.

    Parámetros:
    fechaInicio => 
    '''
    inicio = time.clock()
    fechaFinal = datetime.strptime(fechaFinal, "%Y-%m-%d")
    fechaEvaluada = datetime.strptime(fechaInicio, "%Y-%m-%d")
    contador = 0
    print("Rango:", fechaEvaluada, "a", fechaFinal)

    while (fechaEvaluada <= fechaFinal):
        if fechaEvaluada.strftime("%A") == 'Sunday' and fechaEvaluada.strftime("%d") == '01':
            contador += 1

        fechaEvaluada = fechaEvaluada + timedelta(days=1)

    print("Tiempo:", time.clock() - inicio, "segundos")

    return contador


print("La cantidad de veces que un mes comienza con domingo es:",
      DomingosInicioMes('1901-1-1', '2000-12-31'), "veces")
