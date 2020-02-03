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


files = os.listdir(os.path.abspath('data'))
for j_file in files:
    if '20200201' in j_file:
        #print(j_file)
        df = pandas.read_json('./data/{}'.format(j_file),encoding='utf-8')
        #print(df.iloc[:,6])
        bf = np.array(df).tolist()
        print(df.iloc[1,-2] == '上海')
