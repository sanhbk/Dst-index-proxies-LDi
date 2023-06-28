#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:18:46 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
import os

#Qdays.py
def Qdays(Y,M):
    """
    Function to open and organize the dates of the 10 quietes dates of each month
    
    Input:
    Y - year (int)
    M - month (int)

    Files:
    -'QDAYS_1955_2015.csv' dates of 10 quiest dates for month (WDC)
    
    With the input the code select the data between one year before the input date and the date
    
    Output:
    qdf - Quiet days Dataframe
    """
    
    path = '/Users/santiagopinzon/Mac/articles/Dst_proxies/DATA/QDAYS/'
    name = 'QDAYS_1955_2019.csv'
    fullpath = os.path.join(path,name)
    
    qf = pd.read_csv(fullpath,names = ['data'],skiprows=[0])
    qf['YYYY'] = qf.data.str[:4].astype(int)
    qf['MM'] = qf.data.str[5:7].astype(int)
    qf['q1q2q3q4q5'] = qf.data.str[8:18]
    qf['q6q7q8q9q0'] = qf.data.str[19:29]
    qf =qf.drop(columns=['data'])
    
    # create number date column (quiest 1st to quiest 10th day)
    qf['q1'] = qf.q1q2q3q4q5.str[:2]
    qf['q2'] = qf.q1q2q3q4q5.str[2:4]
    qf['q3'] = qf.q1q2q3q4q5.str[4:6]
    qf['q4'] = qf.q1q2q3q4q5.str[6:8]
    qf['q5'] = qf.q1q2q3q4q5.str[8:10]
    qf['q6'] = qf.q6q7q8q9q0.str[:2]
    qf['q7'] = qf.q6q7q8q9q0.str[2:4]
    qf['q8'] = qf.q6q7q8q9q0.str[4:6]
    qf['q9'] = qf.q6q7q8q9q0.str[6:8]
    qf['q0'] = qf.q6q7q8q9q0.str[8:]
    qf =qf.drop(columns=['q1q2q3q4q5','q6q7q8q9q0'])
    
    # select date as index 
    qf.index = pd.MultiIndex.from_arrays(qf[['YYYY', 'MM']].values.T, names=['YEAR', 'MONTH'])
    
    # slect data using the input day
    qdf = qf[(Y-1, M+1):(Y,M)] # datafrma of dates of the 10 quiest days
    
    return qdf

# ObsQdays.py

def ObsQdays(qdf,obsdf):
    """
    Function to take the 5 quietest days of each month between the input
    range. Depending on the data structure and observatory.
    
    Input:
    qdf - Quiet days DataFrame
    obsdf - observatory Data Frame
    
    
    Output:
    fqdays - array of the dates of the five quiest days of the month 
    yqdays - array of the first day of each month (date of the yqmean)
    yqmean - array of the mean of the 5 quietest days of each month
    """
    

    #### Select the quiest days from obsdf of each month using qf dates 

    # creating empty lists
    yqmean = [] # output: mean of the 5 quiest days
    yqdays = [] # output: first day of each month
    fqdays = [] # output: dates quiest days 

    # for loop to use the dates for each month in both dataframes
    for y,m in qdf.index:
        #empty list 
        qmean = [] #mean of the 5 quiest days
        qdays = [] #dates of the 5 quiest days

        #separate the date of the 10th quiest days 
        q1 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q1[y,m])) # date of the nth day
        q2 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q2[y,m]))
        q3 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q3[y,m]))
        q4 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q4[y,m]))
        q5 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q5[y,m]))
        q6 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q6[y,m]))
        q7 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q7[y,m]))
        q8 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q8[y,m]))
        q9 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q9[y,m]))
        q0 = date(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),int(qdf.q0[y,m]))

        # use the dates to search the dates in obsdf
        h1 = obsdf.HORIZONTAL[str(q1)].values# H components for the nth quiest day 
        h2 = obsdf.HORIZONTAL[str(q2)].values
        h3 = obsdf.HORIZONTAL[str(q3)].values
        h4 = obsdf.HORIZONTAL[str(q4)].values
        h5 = obsdf.HORIZONTAL[str(q5)].values
        h6 = obsdf.HORIZONTAL[str(q6)].values
        h7 = obsdf.HORIZONTAL[str(q7)].values
        h8 = obsdf.HORIZONTAL[str(q8)].values
        h9 = obsdf.HORIZONTAL[str(q9)].values
        h0 = obsdf.HORIZONTAL[str(q0)].values

        # arrays for dates (d) and horizontal components for the 10th quiest days (h)
        d = np.array([q1,q2,q3,q4,q5,q6,q7,q8,q9,q0])
        h = np.array([h1,h2,h3,h4,h5,h6,h7,h8,h9,h0])
        #print(type(obsdf.index))
        # for loop to organize and select the 5 quiest days
        # Append data if missing data, discard the day and jump to the next one

        for i in range(len(h)):

            if np.isnan(h[i]).any()==True:
                continue
            else:
                a = qmean.append(h[i].mean())
                ab = qdays.append(d[i])


        # array selecting the 5 quiest and its dates
        qmean = np.array(qmean[0:5])
        qdays = np.array(qdays[0:5])

        # calculating the mean of the 5 quiest days and append
        a = yqmean.append(qmean.mean())
        # appending first day of each month (date for the yqmean)
        b = yqdays.append(datetime(int(qdf.YYYY[y,m]),int(qdf.MM[y,m]),1,0,0,0))
        # quiest days dates
        c = fqdays.append(qdays)
    

    # converting to array
    yqmean = np.array(yqmean) #output
    yqdays = np.array(yqdays) #output 
    
    fqdays = np.array(fqdays) #output
    #print(len(fqdays))


    return yqmean,yqdays,fqdays, h,d