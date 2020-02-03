# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:34:03 2020

@author: hz
for 2019-nCov data analysis

"""
import os
import matplotlib.pyplot as plt
from matplotlib.pylab import date2num
import numpy as np
import pandas


def get_municipalities_count(cin_name,date):
    #print('-----processing-----city{}-----date{}-----'.format(cin_name,date))
    
    city_name = cin_name
    confirmed_count = 0
    suspected_count = 0
    cured_count = 0 
    dead_count = 0
    total_count = 0
    try:
        files = os.listdir(os.path.abspath('data'))
        for j_file in files:
            if date in j_file:
                #print(j_file)
                df = pandas.read_json('./data/{}'.format(j_file),encoding='utf-8')
                #print(df.iloc[:,6])
                bf = np.array(df).tolist()
                

        for city in bf:
            #print(city)
            if date > '20200131' :
                if cin_name == city[1]:
                    print(city)
                    confirmed_count = city[2]
                    suspected_count = city[4]
                    cured_count = city[3]
                    dead_count = city[5]
                    city_name = city[1]
                    
                    total_count = confirmed_count + suspected_count + cured_count + dead_count
            else :  
                if cin_name == city[1]:
                    #print(city)
                    confirmed_count = city[2]
                    suspected_count = city[4]
                    cured_count = city[5]
                    dead_count = city[3]
                    city_name = city[1]
                    
                    total_count = confirmed_count + suspected_count + cured_count + dead_count
            
                #print('city:{},confirmed:{},total:{}'.format(city_name,confirmed_count,total_count))
    finally:
        return (confirmed_count,total_count)
    
def get_city_count(cin_name,date):
    #print('-----processing-----city{}-----date{}-----'.format(cin_name,date))
    
    city_name = cin_name
    confirmed_count = 0
    suspected_count = 0
    cured_count = 0 
    dead_count = 0
    total_count = 0
    try:
        files = os.listdir(os.path.abspath('data'))
        for j_file in files:
            if date in j_file:
                #print(j_file)
                df = pandas.read_json('./data/{}'.format(j_file),encoding='utf-8')
                #print(df.iloc[32,7])
                #print(df.values)
        for province in range(0,34):
            if date > '20200131':
                for city in df.iloc[province,8]:
                    if cin_name == city['cityName']:
                        #print(city)
                        confirmed_count = city['confirmedCount'] 
                        suspected_count = city['suspectedCount'] 
                        cured_count = city['curedCount']
                        dead_count = city['deadCount']
                        city_name = city['cityName']
                        
                        total_count = confirmed_count + suspected_count + cured_count + dead_count
            else :        
                for city in df.iloc[province,7]:
                    if cin_name == city['cityName']:
                        #print(city)
                        confirmed_count = city['confirmedCount'] 
                        suspected_count = city['suspectedCount'] 
                        cured_count = city['curedCount']
                        dead_count = city['deadCount']
                        city_name = city['cityName']
                        
                        total_count = confirmed_count + suspected_count + cured_count + dead_count
            
                    #print('city:{},confirmed:{},total:{}'.format(city_name,confirmed_count,total_count))
    finally:
        return (confirmed_count,total_count)
    
def plot_confirmed(li1, city):
    counts = []
    for count in li1:
        counts.append(count[0])
    
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.8, 0.8, 0.8])
    ax1.plot(date_list, counts,'-o')
    ax1.grid()
    plt.title('{},总确诊数'.format(city))
    
    
def plot_delta(li1, city):
    counts = []
    counts.append(0)
    while len(li1) > 1:
        temp = li1.pop(0)
        counts.append(li1[0][0] - temp[0])
    
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.8, 0.8, 0.8])
    ax1.plot(date_list, counts,'-o')
    ax1.grid()
    plt.title('{},每日增加'.format(city))
    #ax1.axhline(y=200, ls='--', c='r') #threshold
    return ax1
    
    
def main():
    city_list = ['武汉','温州','深圳','广州','黄冈','孝感']
    municipalities = ['北京','上海','重庆','香港','澳门','台湾']
    #city_list = ['荆州']
    #municipalities = ['上海']
    
    global date_list
    #date_list = ['20200130']
    date_list = ['20200126','20200127','20200128','20200129',
                 '20200130','20200131','20200201','20200202']
    #print(get_city_count_temp(city_list[4],date_list[1]))
    confirm = {}
    
    confirm_2 = []
    for city in city_list:
        confirm.setdefault(city)
        for date in date_list:
            confirm_2.append(get_city_count(city,date))
        confirm[city] = confirm_2
        confirm_2 = []
    
    for city in municipalities:
        confirm.setdefault(city)
        for date in date_list:
            confirm_2.append(get_municipalities_count(city,date))
        confirm[city] = confirm_2
        confirm_2 = []
    
    print(confirm)
    
    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.1, 0.8, 1.8])
    #ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8],ylim=(0,300))
    ax1.grid()
    ax1.axhline(y=200, ls='--', c='r') #threshold
    #plt.yscale('log', nonposy='clip')
    for cin in city_list + municipalities:
        #plot_confirmed(confirm[cin],cin)
        li1 = confirm[cin]
        city = cin
        counts = []
        counts.append(0)
        while len(li1) > 1:
            temp = li1.pop(0)
            counts.append(li1[0][0] - temp[0])
            
        ax1.plot(date_list, counts,'-o',label=city)
        
    ax1.legend(loc='center left', frameon=True, shadow=True);
    

if __name__ == '__main__':
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    main()

"""
城市 每日增长量，每日总量
"""