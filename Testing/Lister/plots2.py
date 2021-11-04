#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:39:19 2021

@author: -anders-
"""

import matplotlib.pyplot as plt
import random

karakterer = ["A", "B", "C", "D", "E", "F"]

antall = [5, 15, 40, 24, 18, 26]


plt.subplot(1, 3, 1)
plt.bar(karakterer, antall, color=("red", "green", "blue", "magenta", "red", "black"))
plt.title("Karakterfordeling, stolper")


plt.subplot(1, 3, 2)
plt.pie(antall, labels=karakterer)
plt.title("Karakterfordeling, kakediagram")


plt.subplot(1, 3, 3)
verdier = []
for i in range(20000):
    verdi = random.random() + random.random() + random.random()
    verdier.append(verdi)
plt.hist(verdier, 40)
plt.title("3 forskjellige tall")
plt.show()