#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:28:20 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

#Base_line.py


import numpy as np
from datetime import datetime
from dateutil.relativedelta import *


def quadratic_reg(Y,M,D,yqmean,yqdays,obsdf):
    """
    Function to calculate the base line of the H component.The baseline
    is calculated as a quadratic regretion using the mean of the 5 quietest
    days of each month.
    
    Input: 
    Y - year (int)
    M - month (int)
    D - day (int)
    yqmean - array of the mean of the 5 quietest days of each month
    yqdays - array of the first day of each month (date of the yqmean)
    obsdf - observatory Data Frame
    
    Output:
    Hbase - linear regression (numpy.poly1d)
    base - array of the points for the regression
    tts - (timestamp) Seconds between the selected date and one year before
    """
    
    #### calculating the quadratic regression
    
    # empty list for x values (time of the dates)
    yqdaysts = []
    
    #reference time (one year before input date)
    reference_time = datetime.timestamp(datetime(Y-1,M,1,0,0,0)+relativedelta(months=+1)) #Reference time in YYYY/MM/DD hh:mm:ss
    #reference_time = reference_time+relativedelta(months=+1)
    # for loop substracting yqdays - reference date (conver to a number for the regression)
    for i in yqdays:
        timestamp = datetime.timestamp(i)-reference_time
        a = yqdaysts.append(timestamp)
    yqdaysts = np.array(yqdaysts) # array for the diference values (seconds)
    
    # calculating the queadratic regression
    Hbase = np.poly1d(np.polyfit(yqdaysts,yqmean,2)) ###
    
    # total time between the last input data date and the year before date
    tts = datetime.timestamp(datetime(Y,M,D,23,59,59))-reference_time #Reference time in seconds
       

        
        
    ## using the regression for the whole year data
    
    b = [] # empty list for append the regression values
    # for loop to append the dates in second (for use the regression)
    for i in obsdf.index:
        ts = datetime.timestamp(i)-reference_time
        ab = b.append(ts)
    b = np.array(b) #array of the dates in seconds
    
    ## calculate the base line using the dates in seconds
    base = Hbase(b) 

    return Hbase,base,tts