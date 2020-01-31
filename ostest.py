# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:32:40 2020

@author: Administrator

OS module test
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin')
ax.plot(x, np.cos(x), '--', label='cos')
ax.legend(loc='upper left', frameon=False);
