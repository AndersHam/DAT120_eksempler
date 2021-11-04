# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:28:54 2021

@author: 2900888
"""

teksten = ""
tekstlinje = input("Skriv inn første linje: ")
while tekstlinje != "":
    teksten += tekstlinje + "\n"
    tekstlinje = input("Skriv inn neste linje: ")
print("Den endelige teksten ble:")
print(teksten)
