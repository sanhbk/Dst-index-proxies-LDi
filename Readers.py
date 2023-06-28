#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:12:14 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

"""
Functions modified by functions made by Natalia Gomez-Perez (BGS) ngp@nerc.ac.uk
The functions are readers for data from WDC database and INTERMAGNET database
"""

# Libraries
import pandas as pd
import numpy as np
import os
from datetime import datetime
#from dateutil.rrule import rrule, MONTHLY

from dateutil import rrule


# Clean data 
def clean_data(Bh):
   
    return [i for i, element in enumerate(np.diff(Bh)) if (abs(element)<250 and abs(element)>0)]

#WDC data reader
def ReadYear_OBS(ye,obs):
    datei = datetime(ye,1,1)
    datef = datetime(ye+1,1,1)  
    
    
    datea = []
    for i in rrule.rrule(rrule.HOURLY, dtstart=datei, until=datef):
        a = datea.append(i)
    datea = datea[:-1]
    
    
     
    wdc_hourpath = '/Users/santiagopinzon/Mac/articles/Dst_proxies/DATA/WDC/'
        
    filepath = os.path.join(os.path.dirname(wdc_hourpath),'wdc_'+obs.upper())
        
    filename = obs.lower()+str(ye)+'.wdc'
        
    full = os.path.join(filepath,filename)
    
    
    
    if os.path.exists(full):
        #number of chars on data from WDC:
        nc=4
        with open(full,'r') as csv_file:
            
            df1 = pd.read_csv(csv_file,names=['data'])
            if ye>=2000:
                df1['YYYY'] = df1.data.str[3:5].astype(int)+2000
            else:
                df1['YYYY'] = df1.data.str[3:5].astype(int)+1900
                
            df1['MM'] = df1.data.str[5:7].astype(int)
            df1['DD'] = df1.data.str[8:10].astype(int)
            df1['Component'] = df1.data.str[7].astype(str)
            df1['Val'] = df1.data.str[16:21].astype(str)
            df1['Vdata'] = df1.data.str[16:].astype(str)
            df1['list'] = None
            
          
            df1['length'] = df1['Vdata'].apply(len)
            #print(df.length[0])
            X = []
            Y = []
            H = []
            #F = []
            #if df1.Component[0]=='X':
                
            for j in range(len(df1.Vdata)):
                line = df1.Vdata[j]
                #df.list[j] = [line[i:i+nc] for i in range(0, len(line), nc)]
                l = np.array([int(line[i:i+nc]) for i in range(0, len(line), nc)])
                element = df1.Component[j]
                tabB = l[0]
                x = l[1:-1]
                
                
                #dfx = pd.DataFrame()
                #dfx2 = pd.DataFrame()
        
                magnitude = x+(tabB*100)
                
                
                if element=='H':
                    H.extend(magnitude)
                elif element=='X':
                    X.extend(magnitude)
                elif element=='Y':
                    Y.extend(magnitude)
                else: continue
                    
            #print(H)
            H1 = np.array(H)
            X1 = np.array(X)
            Y1 = np.array(Y)
            H2 = np.sqrt((X1**2)+(Y1**2))
                    
                
                #df1.insert(0,'t',[datetime(df.)])
                
            if len(H1)!=0:
                df = pd.DataFrame({'t':datea,'H':H1})
            else:
                df = pd.DataFrame({'t':datea,'H':H2})
            
            
            df.index = df.t
            df2 = df.copy()
            df2['Hc'] = df2['H'].values
            df2 = df2.drop(columns=['H'])
            cleanh = clean_data(np.asarray(df2['Hc']))
            df2 = df2.iloc[cleanh]
            
            dfc = pd.concat((df, df2), axis=1)
            
            dfc = dfc.drop(columns=['H','t'])
            
            
    return dfc




#Intermagnet Data Reader
def read_Intermagnet(day, obs):
    """
    Function to read Intermagnet data.
    Input:
        day: date
        obs: Observatory's IAGA code
    Output:
        df: Observatory's Dataframe
    """
    import datetime as dt
    
    IAGApath = ('/Users/santiagopinzon/Mac/articles/Dst_proxies/DATA/IAGA/')
    filepath = (os.path.join(os.path.dirname(IAGApath),day.strftime("%Y"),'IAGA_'+obs.upper()))
    filename=obs.lower()+day.strftime("%Y%m%ddmin.min")
    full=os.path.join(filepath,filename)
    
    """
    Review observatory format
    """
    ofile = open(full)
    rfile = ofile.read()
    sfile = rfile.split('\n')
    hn = sfile.index(' # value of horizontal intensity.                                    |')
    hn = hn+1
    #if obs.upper()=='HER':
     #   if day>dt.datetime(2013,12,31):
      #      hn=24
       # else:
       #     hn=25
   # else:
    #    if day>dt.datetime(2014,12,31):
     #       hn = 24
      #  else:
       #     hn=25
    
    my_parser = lambda x,y : dt.datetime.strptime(x+' '+y,"%Y-%m-%d %H:%M:%S.%f")
    
    df = pd.read_csv(full, sep='\s+',skiprows=hn,
                    #header=hn,
                    parse_dates={'DateTime':[0,1]},
                    date_parser=my_parser, index_col=0)
    df=df.where(df<99999.00)
    
    if obs.upper()+'X' in df.columns:
        df[obs.upper()+'H']=df.apply(lambda row: -(np.sqrt(row[obs.upper()+'X']**2 + row[obs.upper()+'Y']**2)), axis=1)
    
    df = df.drop(columns='|')
    return df
