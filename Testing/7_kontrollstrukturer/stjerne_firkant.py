# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:41:13 2021

@author: 2900888
"""

hoyde = int(input("Høyde: "))
# bredde = int(input("Bredde: "))

for j in range(hoyde):
    for i in range(j+1):
        print("*", end="")
    print()
