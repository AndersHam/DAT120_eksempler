#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:49:28 2021

@author: -anders-
"""

#Ordeteller for tekstfil:
    #Les inn ei tekstfil
    #Finn alle ordene
    #Tell antall forekomster av hvert ord

textfila = input("Hva er navnet på textfila? ")


ordliste = dict()
with open(textfila, "r", encoding="UTF8") as fila:
    for linje in fila:
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:
                teller = ordliste[ordet]
                teller += 1
                ordliste[ordet] = teller
            else:
                ordliste[ordet] = 1
    for ordet in ordliste:
        print(f"Ordet {ordet} forekommer {ordliste[ordet]} antall ganger")
            