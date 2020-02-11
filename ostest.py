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
import scipy as sp

date_list = ['20200126','20200127','20200128','20200129',
                 '20200130','20200131','20200201','20200202',
                 '20200203','20200204','20200205','20200206',
                 '20200207','20200208','20200209','20200210']
date_list2 = [i for i in range(16)]

city_list1 = {'温州': [(18, 19), (32, 33), (60, 63), (114, 117), 
                    (172, 175), (227, 234), (241, 249), (265, 280), 
                    (291, 306), (340, 368), (364, 392), (396, 432), 
                    (421, 470), (438, 487), (448, 526), (464, 563)]}
city_list2 = {'温州': [(18, 19), (32, 33), (60, 63), (114, 117), 
                    (172, 175), (227, 234), (241, 249), (265, 280), 
                    (291, 306), (340, 368), (364, 392), (396, 432), 
                    (421, 470), (438, 487), (448, 526), (464, 563)]}
total_counts = []
delta_counts = []

while( len(city_list1['温州']) > 0):
    temp = city_list1['温州'].pop(0)
    total_counts.append(temp[0])
    
delta_counts.append(0)
while( len(city_list2['温州']) > 1):
    temp = city_list2['温州'].pop(0)
    delta_counts.append(city_list2['温州'][0][0] - temp[0])
    # print(delta_counts)
    

def total_func(x,a1,a2):
    # return ( 1 - 1.0/(1.0 + np.exp((x-a1)/a2)) )
    return ( 1 - 1.0/(1.0 + np.tanh((x-a1)/a2)) )
ax1 = plt.subplot()
ax1.plot(date_list,total_counts,'bo',label='感染总数')

ax2 = ax1.twinx()
ax2.plot(date_list,delta_counts,'ro',label='日增数目')

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1+handles2, labels1+labels2, loc='lower center')

# popt, pcov = sp.optimize.curve_fit(total_func, date_list, total_counts,bounds=(0, [3., 0.5]))
popt, pcov = sp.optimize.curve_fit(total_func, date_list2, total_counts)

print(type(popt))

ax1.plot(date_list, total_func(date_list2, *popt), 'b--',)




def delta_func(x,a1,a2,a3):
    pass

# x = np.linspace(0, 10, 1000)
# fig, ax = plt.subplots()

# ax.plot(x, np.sin(x), label='sin')
# ax.plot(x, np.cos(x), '--', label='cos')
# ax.legend(loc='upper left', frameon=False);


# files = os.listdir(os.path.abspath('data'))
# for j_file in files:
#     if '20200201' in j_file:
#         #print(j_file)
#         df = pandas.read_json('./data/{}'.format(j_file),encoding='utf-8')
#         #print(df.iloc[:,6])
#         bf = np.array(df).tolist()
#         print(df.iloc[1,-2] == '上海')
