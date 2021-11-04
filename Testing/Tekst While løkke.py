#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 19:03:59 2021

@author: -anders-
"""


teksten = ""
tekstlinje = input("Skriv inn første linje: ")
while tekstlinje != "":
    teksten += tekstlinje + "\n"
    tekstlinje = input("Skriv inn neste linje: ")
print("Den endelige teksten ble: ")
print(teksten)