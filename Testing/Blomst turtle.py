#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:00:31 2021

@author: Anders Hamarsland
"""

import turtle

STORRELSE = 100
VINKEL = 10

turtle.setup(1500,1500,0,0)
turtle.speed(0)
vinkel_saa_langt = 0
while vinkel_saa_langt < 360:
    turtle.circle(STORRELSE)
    turtle.right(VINKEL)
    vinkel_saa_langt += VINKEL
turtle.done()
