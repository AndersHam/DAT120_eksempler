#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:41:36 2021

@author: -anders-
"""

import matplotlib.pyplot as plt
import numpy as np

x_koordinater = np.linspace(0,10,11)
y_koordinater = x_koordinater ** 2
y_koordinater2 = x_koordinater * 2

plt.plot(x_koordinater,y_koordinater, "o-", label="x i andre")
plt.plot(x_koordinater,y_koordinater2, "o-", label="2 ganger x")
# (o) = kuler i linja (-) = linje mellom kulene
plt.title("Enkler figurer")
plt.xlabel("Verdi")
plt.ylabel("Resultat")
plt.legend()
plt.grid(True)
# plt.savefig("x_i_andre_figur.pdf") (hvis du skal lagre det som pdf)
plt.show()