#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:29:29 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

def correlation(y,m):
    
        
    from Final_Dst import FDst
    
    
    
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    from datetime import timedelta
    
    fuq = FDst('fuq',y,m)
    fuq.index = pd.to_datetime(fuq.index)
    fuq.index = fuq.index - timedelta(minutes=59)
    
    asc = FDst('asc',y,m)
    asc.index = pd.to_datetime(asc.index)
    
    #hua = FDst('hua',y,m)
    #hua.index = pd.to_datetime(hua.index)
    
    obs = ['hon','her','kak','sjg']
    wdc = FDst(obs,y,m)
    wdc.index = pd.to_datetime(wdc.index)
    
    eobs =['her','kak']
    ewdc = FDst(eobs,y,m)
    
    wobs =['hon','sjg']
    wwdc = FDst(wobs,y,m)
    
    
    ##################################################
    ##################################################
    #data = [fuq['Dst'],wdc,ewdc,wwdc,asc['Dst']]
    headers = ["FUQ", "ASC",'WDC','EWDC','WWDC']
    
    df_comp = pd.concat([fuq['Dst'],asc['Dst'],wdc,ewdc,wwdc],axis=1,keys=headers)
    df_comp = df_comp.dropna()
    
    corr_fuq_wdc = round(df_comp['FUQ'].corr(df_comp['WDC'],method='pearson'),3)
    corr_asc_wdc = round(df_comp['ASC'].corr(df_comp['WDC'],method='pearson'),3)
    corr_fuq_asc = round(df_comp['FUQ'].corr(df_comp['ASC'],method='pearson'),3)
    corr_fuq_wwdc = round(df_comp['FUQ'].corr(df_comp['WWDC'],method='pearson'),3)
    corr_fuq_ewdc = round(df_comp['FUQ'].corr(df_comp['EWDC'],method='pearson'),3)
    corr_wdc_ewdc = round(df_comp['WDC'].corr(df_comp['EWDC'],method='pearson'),3)
    corr_wdc_wwdc = round(df_comp['WDC'].corr(df_comp['WWDC'],method='pearson'),3)
    corr_asc_ewdc = round(df_comp['ASC'].corr(df_comp['EWDC'],method='pearson'),3)
    corr_asc_wwdc = round(df_comp['ASC'].corr(df_comp['WWDC'],method='pearson'),3)
    
    
    r = {'F_D':str(corr_fuq_wdc),'A_D':str(corr_asc_wdc),'F_A':str(corr_fuq_asc),
         'F_W':str(corr_fuq_wwdc),'F_E':str(corr_fuq_ewdc),'A_W':str(corr_asc_wwdc),
         'A_E':str(corr_asc_ewdc),'D_E':str(corr_wdc_ewdc),'D_W':str(corr_wdc_wwdc)}
    
    return r
    
    
    
    
    
    ##################################################
    ##################################################
    
    
    ##fig, axs = plt.subplots(6,1,sharex ='all',sharey='all',figsize=(12,12))
    
    #plot 1:
    
    ##axs[0].plot(df_comp['FUQ'],df_comp['WDC'],'.',color='tab:blue', label=('Dst FUQ vs WDC '+ 'r = '+str(corr_fuq_wdc)))
    #axs[0].plot(wdc,#'--',
                #label='Dst WDC',color='tab:red')
    #axs[0].set_ylim(miny,maxy)
    ##axs[0].tick_params(labelsize=12)
    #axs[0].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[0].set_ylabel('Dst (nT)',fontsize=20)
    ##axs[0].legend(loc=2,fontsize=16)
    ##axs[0].set_title('A. Dst FUQ vs WDC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[0].grid()
    
    #plot 2:
    
    ##axs[1].plot(df_comp['FUQ'],df_comp['WWDC'],'.',color='tab:blue', label=('Dst FUQ vs wwdc '+'r = '+str(corr_fuq_wwdc)))
    ##axs[1].plot(df_comp['FUQ'],df_comp['EWDC'],'.',color='tab:red', label=('Dst FUQ vs ewdc '+'r = '+str(corr_fuq_ewdc)))
    #axs[1].plot(ewdc,#'--',
                #color='r', label='Dst E-WDC')
    #axs[1].plot(wwdc,# ':',
                #color='g', label='Dst W-WDC')
    #axs[1].plot(wwdc1,# ':',
                #color='k', label='Dst 2W-WDC')
    #axs[1].set_ylim(miny,maxy)
    ##axs[1].set_ylabel('Dst (nT)',fontsize=20)
    ##axs[1].tick_params(labelsize=12)
    #axs[1].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[1].legend(loc=2,fontsize=16)
    ##axs[1].set_title('B. Dst FUQ vs East and West WDC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[1].grid()
        
    
    #plot 3:
    ##axs[2].plot(df_comp['FUQ'],df_comp['ASC'],'.',color='tab:blue',label=('Dst FUQ vs ASC '+'r = '+str(corr_fuq_asc)))
    #axs[2].plot(asc,#':',
                #color='saddlebrown',label='Dst ASC')
    ##axs[2].set_ylabel('Dst (nT)',fontsize=20)
    #axs[2].set_ylim(miny,maxy)
    ##axs[2].tick_params(labelsize=12)
    #axs[2].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[2].legend(loc=2,fontsize=16)
    ##axs[2].set_title('C. Dst FUQ vs ASC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[2].grid()
    
    #plot 4:
    ##axs[3].plot(df_comp['ASC'],df_comp['WDC'],'.',color='tab:blue',label=('Dst ASC vs WDC '+'r = '+str(corr_asc_wdc)))
    #axs[2].plot(asc,#':',
                #color='saddlebrown',label='Dst ASC')
    ##axs[3].set_ylabel('Dst (nT)',fontsize=20)
    #axs[3].set_xlabel('Dst (nT)',fontsize=20)
    #axs[2].set_ylim(miny,maxy)
    ##axs[3].tick_params(labelsize=12)
    #axs[2].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[3].legend(loc=2,fontsize=16)
    
    ##axs[3].set_title('D. Dst ASC vs WDC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[3].grid()
    
    
    #plot 5:
    ##axs[4].plot(df_comp['WDC'],df_comp['EWDC'],'.',color='tab:blue',label=('Dst ASC vs WDC '+'r = '+str(corr_wdc_ewdc)))
    #axs[2].plot(asc,#':',
                #color='saddlebrown',label='Dst ASC')
    ##axs[4].set_ylabel('Dst (nT)',fontsize=20)
    #axs[3].set_xlabel('Dst (nT)',fontsize=20)
    #axs[2].set_ylim(miny,maxy)
    ##axs[4].tick_params(labelsize=12)
    #axs[2].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[4].legend(loc=2,fontsize=16)
    
    ##axs[4].set_title('D. Dst ASC vs WDC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[4].grid()
    
    #plot 6:
    ##axs[5].plot(df_comp['WDC'],df_comp['WWDC'],'.',color='tab:blue',label=('Dst ASC vs WDC '+'r = '+str(corr_wdc_wwdc)))
    #axs[2].plot(asc,#':',
                #color='saddlebrown',label='Dst ASC')
    ##axs[5].set_ylabel('Dst (nT)',fontsize=20)
    #axs[3].set_xlabel('Dst (nT)',fontsize=20)
    #axs[2].set_ylim(miny,maxy)
    ##axs[5].tick_params(labelsize=12)
    #axs[2].yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ##axs[5].legend(loc=2,fontsize=16)
    
    ##axs[5].set_title('D. Dst ASC vs WDC '+str(y)+'-'+str(m),fontsize=22)
    ##axs[5].grid()
    
    
    
    ##plt.xlabel("Dst (nT)", fontsize=20)
    ##fig.tight_layout()
    
    ##name = 'COR'+str(y)+str(m)+'.png'
    ##path = ('/Users/santiagopinzon/Mac/articles/Dst_proxies/Images/Correlation/')
    
    ##plt.savefig(os.path.join(path,name), dpi=250)
    ##plt.show()
    
    



