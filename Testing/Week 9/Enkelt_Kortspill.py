#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:55:07 2021

@author: -anders-
"""

# Korttypene som konstanter
KLOVER = 1
RUTER = 2
SPAR = 3
HJERTER = 4

import random

class Kort:
    def __init__(self, korttype, verdi):
        self.korttype = korttype
        self.verdi = verdi
        
    def __str__(self):
        korttypene = ["ingen", "Kløver", "Ruter", "Spar", "Hjerter"]
        if self.verdi == 1:
            return korttypene[self.korttype] + " Ess"
        elif self.verdi <= 10:
            return f"{korttypene[self.korttype]} {self.verdi}"
        elif self.verdi == 11:
            return korttypene[self.korttype] + " Knekt"
        elif self.verdi == 12:
            return korttypene[self.korttype] + " Dame"
        elif self.verdi == 13:
            return korttypene[self.korttype] + " Konge"
        else:
            return "ugyldig kort!"

        
        
        
class Kortstokk:
    def __init__(self):
        self.kortene = list()
        
    def lag_kortene(self):
        for t in range(1,5):
            for v in range(1,14):
                self.kortene.append(Kort(t, v))
                
    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet
    
    def stokk(self):
        random.shuffle(self.kortene)
        
    def __str__(self):
        resultat = f"Kortstokk med {len(self.kortene)} kort\n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat
        
class Spillere:
    def __init__(self, navn, kort):
        self.navn = navn
        self.kort = kort

        
if __name__ == "__main__":
    antall_spillere = int(input("Antall spillere: "))
    spillerene = []
    stokken = Kortstokk()
    stokken.lag_kortene()
    stokken.stokk()
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i}:")
        kortene = stokken.trekk()
        print(f"Spilleren {navn} for kortet {kortene}")
        spilleren = Spillere(navn, kortene)
        spillerene.append(spilleren)
    vinnere = list()
    vinnere.append(spillerene[0])
    for spiller in spillerene:
        if spiller == spillerene[0]:
            continue
        if spiller.kort.verdi > vinnere[0].kort.verdi:
            vinnere.clear()
            vinnere.append(spiller)
        elif spiller.kort.verdi == vinnere[0].kort.verdi:
            vinnere.append(spiller)

        
    print("Vinnere: ")        
    for spiller in vinnere:
        print(f"{spiller.navn} har {spiller.kort}")
        
        
        
        
        
        
        
        
        
        
        