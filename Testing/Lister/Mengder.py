#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:20:41 2021

@author: -anders-
"""

mengde = set()
mengde.add("Henrik")
mengde.add("Petter")
mengde.add("PEtter")
mengde.add("Anders")

for element in mengde:
    print(element)
    
mengde.remove("PEtter")

for element in mengde:
    print(element)


mengde2 = set()
mengde2.add("Henrik")
mengde2.add("Per")
mengde2.add("Fishnet")
mengde2.add("Petter")
mengde2.add("Pål")
for element in mengde2:
    print(element)

# Mengden av alle som er med i minst en av de to mengdene
m3 = mengde.union(mengde2)
print("\n Unioun: ")
for element in m3:
    print(element)
    
# Mengden av de som er med i begge mengdene
m3 = mengde.intersection(mengde2)
print("\n Snitt: ")
for element in m3:
    print(element)
    
#mengde i m1 or ikke i m2   
m3 = mengde.difference(mengde2)
print("\n m1 minus m2: ")
for element in m3:
    print(element)