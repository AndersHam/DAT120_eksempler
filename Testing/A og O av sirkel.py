# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
radius = input("Skriv inn radiusen til sirkelen: ")
Radius_tall = float(radius)
omkrets = 2*math.pi*Radius_tall
areal = math.pi*Radius_tall*Radius_tall
print(f"Dette er omkretsen av sirkelen:  {omkrets:8.2f}")
print("Dette er arealet av sirkelen: ", end="")
print(round(areal, 3))      
