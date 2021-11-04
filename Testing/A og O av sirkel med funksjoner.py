#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:11:30 2021

@author: -anders-
"""

import math

def areal_sirkel(radius):
    areal = math.pi * radius * radius
    return areal


def omkrets_sirkel(radius):
    omkrets = 2 * math.pi * radius
    return omkrets


if __name__ == "__main__":
    radius_streng = input("Skriv inn radiusen til sirkelen: ")
    radius_bruker = float(radius_streng)
    areal = areal_sirkel(radius_bruker)
    print(f"Arealet ble: {areal:8.2f}")
    omkrets = omkrets_sirkel(radius_bruker)
    print(f"Omkretsen ble: {omkrets:8.2f}")