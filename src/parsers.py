# -*- coding: utf-8 -*-
'''
Created on 27 ene 2022

@author: willi
'''
def parsea_fecha(cadena):
    return datetime.strptime(cadena, '%d/%m/%Y').date()

def parsea_booleano(cadena):
    res= True
    cadena = cadena.upper()
    if cadena =='VERDADERO':
        res = True
    elif cadena == 'FALSO':
        res = False
    return res