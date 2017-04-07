#!/usr/bin/env python
# -*- coding: utf-8 -*-

def colatz( c ):
    step = 0
    odd = 0
    even = 0
    while c > 1:
        if (c % 2 == 0):
            c = c / 2
            even += 1
        else:
            c = (3 * c) + 1
            odd += 1
        step += 1
    return "Kroku je " + str(step) + "\n" + "Pocet sudych cisel = " + str(even) + "\n" + "Pocet sudych lichych = " + str(odd)




def colatzList( c ):

    n = []
    n.append(c)

    while c > 1:
        if (c % 2 == 0):
            c = c / 2
            n.append(c)
        else:
            c = (3 * c) + 1
            n.append(c)
    return n

# Bez listu = výstup je string
print colatz(27)

# S listem = výstup je množina čísel
print colatzList(27)
