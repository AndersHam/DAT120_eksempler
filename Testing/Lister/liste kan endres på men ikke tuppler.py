#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:41:49 2021

@author: -anders-
"""

def endrer_liste(liste):
    liste.append(10)
    liste.append(12)
    print(liste)
    
    
if __name__ == "__main__":
    liste1 = [2, 4, 6, 8]
    print(liste1)
    endrer_liste(liste1)
    print(liste1)