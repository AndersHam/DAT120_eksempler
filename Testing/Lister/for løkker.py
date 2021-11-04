#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:48:37 2021

@author: -anders-
"""

liste = [1, 3, 5, 7, 9]

for element in liste:
    element = element*2
    print(element)

print(liste)

element = input("skriv inn et tall for å sjekke om det er i lista: ")
element = int(element)
if element in liste:
    print("Tallet er i lista")
else:
    print("Tallet er ikke i lista")

for index, element in enumerate(liste):
    print(f"Element {element} ligger på indexen {index}")