# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:07:16 2023

@author: Felip
"""
import numpy as np

entradas = np.array([1,7,5])
pesos = np.array([0.8,0.1,0])

def soma (e, p):
    return e.dot(p)
        
s = soma(entradas,pesos)

def stapFunction(soma):
    if(soma >= 1):
        return 1
    return 0
r = stapFunction(s)         