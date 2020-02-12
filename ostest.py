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
from scipy.optimize import curve_fit
from scipy.optimize import fsolve

from scipy import integrate



plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

date_list = ['20200126','20200127','20200128','20200129',
                 '20200130','20200131','20200201','20200202',
                 '20200203','20200204','20200205','20200206',
                 '20200207','20200208','20200209','20200210']
date_list2 = [i for i in range(17)]
date_list3 = [i for i in range(50)]
city_name = '武汉'

city_list1 = {'武汉': [(618, 703), (698, 803), (1590, 1722), (1905, 2056), (2261, 2444), (2639, 2901), (3215, 3513), (4109, 4508), (5142, 5635), (6384, 7003), (8351, 9087), (10117, 10986), (11618, 12638), (13603, 14846), (14982, 16468), (16902, 18629), (18454, 20444)]}


city_list2 = {}
city_list2[city_name] = city_list1[city_name].copy()
total_counts = []
delta_counts = []

while( len(city_list1[city_name]) > 0):
    temp = city_list1[city_name].pop(0)
    total_counts.append(temp[0])
    
delta_counts.append(0)
while( len(city_list2[city_name]) > 1):
    temp = city_list2[city_name].pop(0)
    delta_counts.append(city_list2[city_name][0][0] - temp[0])
    # print(delta_counts)
    

def total_func(x,a1,a2,a3):
    return a3 * ( 1 - 1.0/(1.0 + np.exp((x-a1)/a2)) )
    # return ( 1 - 1.0/(1.0 + np.tanh((x-a1)/a2)) 

# def total_func(x,c1,a1,a2):
#     return c1 + integrate.quad(delta_func(x,a1,a2),0,17)

# def delta_func(x,a1,a2,a3):
#     return a1 / (np.sqrt(2*np.pi) * a2) * np.exp(-(x-a3)*(x-a3)/2/a2/a2)
def delta_func(x,a1,a2):
    return a1 * np.exp(-a2 * np.power(x,2)) * np.power(x,2)


fig = plt.figure()
# fig.title("荆州")
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8],xlim=(-1,date_list3[-1]))
ax1.grid()
ax1.plot(date_list2,total_counts,'b^',label='感染总数')
ax1.set_title(city_name,fontsize=16)

ax2 = ax1.twinx()
ax2.yaxis.label.set_color('red')
ax2.tick_params(axis='y', colors='red')
ax2.plot(date_list2,delta_counts,'r^',label='日增数目')

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1+handles2, labels1+labels2, loc='center right',
            frameon=True, shadow=True)

# popt, pcov = sp.optimize.curve_fit(total_func, date_list, total_counts,bounds=(0, [3., 0.5]))
# popt, pcov = curve_fit(total_func, date_list2, total_counts)
popt_delta, pcov_delta = curve_fit(delta_func, date_list2, delta_counts)

ax2.plot(date_list3, delta_func(date_list3, *popt_delta), 'r--',)



popt_total, pcov_total = curve_fit(total_func, date_list2, total_counts,bounds=([0,0,0],[20,100,50000] )  )
print(popt_total)
ax1.plot(date_list3, total_func(date_list3, *popt_total), 'b--',)

def delta_func_cal_days(x,a1=popt_delta[0],a2=popt_delta[1]):
    return a1 * np.exp(-a2 * np.power(x,2)) * np.power(x,2) - 1
r = fsolve(delta_func_cal_days, (50))
ax1.axvline(x=r, ls='--', c='y',label='end date') #end date


handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles2+handles1, labels2+labels1, loc='center right',
            frameon=True, shadow=True)
plt.xticks(date_list3[::2])





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
