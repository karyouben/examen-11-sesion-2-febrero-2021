# -*- coding: utf-8 -*-
'''
Created on 27 ene 2022

@author: willi
'''
from collections import namedtuple, Counter
import csv
from parsers import *
import statistics

Venta= namedtuple('Venta', 'identidad,fecha,cliente,producto,cantidad,precio,beneficio')

def lee_fichero(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        res = []
        for identidad,fecha,cliente,producto,cantidad,precio,beneficio in lector:
            tupla = Venta(identidad,parsea_fecha(fecha),cliente,producto,int(cantidad),float(precio),float(beneficio))
            res.append(tupla)
    return res

def clientes_productos1_productos2(registros, producto1,producto2):
    return {t.cliente for t in registros if t.producto== producto1 and t.producto == producto2}

def diccionario_porcentaje_cantidad_producto(registros):
    dicc_sum = agrupa_por_producto(registros)
    total_cantidad = sum(t.cantidad for t in registros)
    dicc = {}
    for t in dicc:
        dicc[t] = (dicc_sum[t]/total_cantidad[t])*100
    return dicc
        
def agrupa_por_producto(registros):
    dicc = {}
    for t in registros:
        clave = t.producto
        if clave in dicc:
            dicc[clave]+= t.cantidad
        else:
            dicc[clave]= t.cantidad
    return dicc

def producto_mas_vendido(registros,nombres,n=3):
    lista_aux = [t for t in registros if t.cliente in nombres]
    lista_aux.sorted(key = lambda x:x.cantidad,reverse = True)
    contador =Counter(t.producto for t in lista_aux[:n])
    return contador.most_common(1)[0]
    
    