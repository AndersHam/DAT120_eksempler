#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:23:27 2021

@author: -anders-
"""

liste = list()
for verdi in range(1,11):
    liste.append(verdi**2)
print(liste)

liste2 = [verdi**2 for verdi in range(1, 11)]
print(liste2)

liste3 = [verdi**2 for verdi in range(1, 20) if verdi%2 == 1]
print(liste3)

liste4 = list()
for verdi in range (1, 20):
    if verdi%2 == 1:
        liste4.append(verdi**2)
print(liste4)