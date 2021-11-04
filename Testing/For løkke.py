#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:34:04 2021

@author: -anders-
"""

tall = int(input("Skriv inn tallet du ønsker fakultet av: "))
while tall < 0:
    print("Fakultet for negative tall finnes ikke!")
    tall = int(input("Skriv inn tallet du ønsker fakultet av: "))

resultat = 1
for i in range(1, tall+1):
    print(i)
    resultat += i
print("Etter for- løkka er ferdig")
print(resultat)