#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:05:38 2021

@author: -anders-
"""


def skriv_firkant(hoyde=5, bredde=10, tegn="*"):
    for j in range(hoyde):
        for i in range(bredde):
            print(tegn, end="")
        print()

bruker_hoyde = int(input("Høyde: "))
bruker_bredde = int(input("Bredde: "))


skriv_firkant(3, 3)
print("\n ny firkant \n")
skriv_firkant(bruker_hoyde, bruker_bredde, "#")
print("ferdig")