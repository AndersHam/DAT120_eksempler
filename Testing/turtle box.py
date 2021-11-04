#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:22:18 2021

@author: -anders-
"""

STORRELSE = 50
import turtle

turtle.setup(1000,1000,0,0)
for i in range(4):
    turtle.forward(STORRELSE)
    turtle.right(90)
turtle.done()