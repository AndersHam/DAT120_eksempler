# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:41:13 2021

@author: 2900888
"""

hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))

if hoyde <= 0:
    print("Høyden må være positiv")
    hoyde = 1
    
if bredde <= 0:
    print("Bredden må være positiv")
    bredde = 1



for j in range(hoyde):
    for i in range(bredde):
        print("*", end="")
    print()
