#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:58:17 2021

@author: -anders-
"""

#Dictionary, map, assasiativ tabell
#Assosierer nøkler med verdier
#Nøkkel: Det du leter etter
#verdi: verdien du finner
#Hvordan assosiativ tabell ser ut inni er dat200 pensum


dictionary = dict()
dictionary["Jan Johansen"] = 2345645
dictionary["Jan Fishnet"] = 2342345345346
dictionary["Jan Pettersen"] = 35235345
dictionary["Jan Petter"] = 2312412

for nokkel in dictionary:
    print(nokkel + ": ", end="")
    print(dictionary[nokkel])