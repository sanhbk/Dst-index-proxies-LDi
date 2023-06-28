#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:05:43 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

import pandas as pd
from dipolar import Dlat
import numpy as np
import os
from datetime import timedelta




def FDst (obs, Y,M):
     

    
    df = pd.DataFrame()
    
    path = '/Users/santiagopinzon/Mac/articles/Dst_proxies/Disturbance/'
    folder = str(Y)+'-'+str(M)
    
    dpath = os.path.join(path,folder)
    
    #df.index = df.t
    #df.drop(columns=['t'])
    l = []
    
    if type(obs)==str:
        
        name = obs.upper()+'_'+ str(Y)+'_'+str(M)+'.csv'
        abs_path = os.path.join(dpath,name)
        DisDf = pd.read_csv(abs_path, index_col=0)
        DisDf.index = pd.to_datetime(DisDf.index)
        phi = Dlat(Y, obs)
        FDst = DisDf/np.cos(phi)
        #FDst = Dst_index(DisDf.Dst, phi)
    else:
        for i in obs:
            
            if i == 'fuq':
                obsname = i.upper()+'_'+ str(Y)+'_'+str(M)+'.csv'
                obs_path = os.path.join(dpath,obsname)
                ObsDis = pd.read_csv(obs_path,index_col=0)
                ObsDis.index = pd.to_datetime(ObsDis.index)-timedelta(minutes=59)
                df[i] = ObsDis.Dst
                
                obsphi = Dlat(Y,i)
            
            else:
                obsname = i.upper()+'_' +str(Y)+'_'+str(M)+'.csv'
                obs_path = os.path.join(dpath,obsname)
                ObsDis = pd.read_csv(obs_path,index_col=0)
                ObsDis.index = pd.to_datetime(ObsDis.index)
                df[i] = ObsDis.Dst
                
                obsphi = Dlat(Y,i)
            
            l.append(np.cos(obsphi))
            
            
        #elif 'fuq' in obs ==True:
            #fuqname = 'FUQ_'+ str(Y)+'_'+str(M)+'.csv'
            #FuqDis = pd.read_csv(fuqname,index_col=0)
            
            
        #FDst = pd.concat([HonDis,HerDis,SjgDis,AscDis],axis=1)
        la = np.array(l)
        lmean = np.mean(la)
        #df2 = pd.DataFrame(columns='Dst')
        df2 = df.mean(axis = 1, skipna = False)
        FDst = df2/lmean
        
    return FDst


