#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:57:08 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

import pandas as pd
import numpy as np
import os

def Dlat(Y,obs):
    
    path = '/Users/santiagopinzon/Mac/articles/Dst_proxies/Dipolar/'
    name = obs.upper()+'_MagneticCoordinates.xlsx'
    
    obspath= os.path.join(path,name)
    
    
    df = pd.read_excel(obspath)
    df = df.drop(columns=['DLON','QLAT','QLON'])

    df['dif'] = Y - df['Epoch']

    pdf = df.loc[(df['dif'] >= 0) & (df['dif'] < 5)]

    tetha = pdf.iloc[0]['DLAT']
    
    tetha = tetha*np.pi/180
    
    return tetha