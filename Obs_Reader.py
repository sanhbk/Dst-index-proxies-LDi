#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 08:59:03 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

#OBS_reader.py

import pandas as pd
from datetime import timedelta
from datetime import datetime
from dateutil.relativedelta import *
from Readers import ReadYear_OBS,read_Intermagnet

def Reader(Y,M,D,obs,database='FUQ'):
    """
    Function to open and organize the data from different obsevatories. Thw function
    reads 3 types of data format. 
    Input:
    Y - year (int)
    M - month (int)
    D - day (int)
    obs - Observatory IAGA code. Default FUQ
    database - data structure (WDC, INT, FUQ). Default FUQ
    Files: 
    -'Componentes_1955_2014.csv' data from IGAC (magnetic field components) (edit: new data available)
    - Data downladed by BGS WDC and INTERMAGNET
    With the input the code select the data between one year before the input date and the date
    

    Output:
    Y - input year (int)
    M - input month (int)
    D - day (int)
    inpdate - input date
    initdate - one year before input date
    obsdf - observatory Data Frame
    """
    #### selecting the input (inpdate) day and the one year before date (initdate)

    inpdate = datetime(Y,M,D,0,0,0)+timedelta(days=1)#output
    initdate = datetime(Y-1,M,1,0,0,0)+relativedelta(months=+1)#output
        
    ####### FUQ OBSERVATORY
    if database=='FUQ':

        #### open the IGAC file and organize the data 
        df = pd.read_csv('/Users/santiagopinzon/Mac/articles/Dst_proxies/Componentes_1955_2015.csv',low_memory=False)

        # create a t column with date in datetime 
        df.insert(0,'t',[datetime(df.AÑO[i],df.MES[i],df.DIA[i],(df.HORA[i]-1),59,0) for i in range(len(df))])
        # drop unnecesary columns 
        df = df.drop(columns = ['AÑO','MES','DIA','HORA','DECLINACION','VERTICAL','NORTE', 'ESTE', 'INTENSIDAD_TOTAL', 'INCLINACION'])
        df.index = df.t # use date as index

        # select the data using the input date
        obsdf = df[str(initdate):str(inpdate)] # output (observatory dataframe)
    
    
    ####### WDC DATA
    
    elif database=='WDC':
        dfi = ReadYear_OBS(Y-1, obs)
        
        dff = ReadYear_OBS(Y,obs)
        
        df = dfi.append(dff)
        
        df['t']=df.index
        df['HORIZONTAL'] = df['Hc'].values
        df = df.reset_index(drop=True)
        
        obsdf = df[['t','HORIZONTAL']].copy()
        obsdf.index=obsdf.t
        
        
        obsdf = obsdf[str(initdate):str(inpdate)]
        
        
        
    ####### INTERMAGNET DATA
    elif database=='INT':
        
        data=[]
        dlist=pd.date_range(initdate,(inpdate-+timedelta(days=1)),freq='d')
        for d in dlist:
            data.append(read_Intermagnet(d,obs))
        df=pd.concat(data)
        df['HORIZONTAL'] = abs(df[obs.upper()+'H'])
        df['t'] = df.index
        df = df.reset_index(drop=True)
        obsdf = df[['t', 'HORIZONTAL']].copy()
        obsdf.index = obsdf.t
        obsdf = obsdf.resample('60min').mean()
        
        
        
    return Y,M,D,inpdate,initdate,obsdf