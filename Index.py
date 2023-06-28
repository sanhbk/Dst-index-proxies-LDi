#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:16:31 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

# import libraries
import pandas as pd
import numpy as np
from datetime import datetime



def Disturbance(Sq_month,DeltaH,inpdate,initdate):
    """
    Function to calculate the disturbance. Take the the DeltaH and substract the Sq variation of each month
    
    Input:
    Sq_month - array of the Sq variation of each month
    DeltaH - H observed - base line 
    inpdate - input date
    initdate - one year before input date
    
    Output:
    Disturbance - array of the disturbance (DeltaH - Sq_month)
    """
    dates = pd.date_range(str(initdate), str(inpdate), freq='MS')+pd.offsets.Day(14)
    dff=[]

    #for loop to create a dataframe for the Sq_month related to the month (date as index)
    for i in range(12):
        df = pd.DataFrame()
        df['Sq'] = Sq_month[i]
        x = []
        for j in range(1,25):
            idx = datetime(dates.year[i],dates.month[i],j,0,0,0)
            a = x.append(idx)
        df.index = x
        dff.append(df)


    dff = pd.concat(dff, axis=0)
    Sqdf = dff.Sq #dataframe with Sq variation each month
    
    
    
    DATES = []
    disturbance = [] #empty array for the disturbance calculation
    
    #for loop substractin DeltaH - Sq variation of respective month
    for i in DeltaH.index:
        #istr = i.strftime('%Y-%m-%d')
        MonthSq = Sqdf[(str(i.year)+'-'+str(i.month)+'-'+str((i.hour+1)))] #selecting date of the Sq variation
        Res = DeltaH[i]-MonthSq ##distrubance 
        aDst = disturbance.append(Res)
        aDATES = DATES.append(i)
        
    ###create a data frame with the disturbance
    disturbance = pd.DataFrame(disturbance, index =DATES,columns =['Dst'])#output
    
    return disturbance



def Dst_index(disturbance, phi):
    """
    Function to calculate the Dst index. Formula Dst = disturbance/cos(angle). Angle is the dipolar latitude
    Input:
    Disturbance - array of the disturbance (DeltaH - Sq_month)
    phi - dipolar latitude
    
    Out:
    Dst - Final Dst index
    """
    angle = phi*np.pi/180 
    Dst = disturbance/np.cos(angle)
    
    return Dst