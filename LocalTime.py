#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:15:32 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""



def Local_Time(y, m, inid,find,y2, m2, inid2,find2):
    from Final_Dst import FDst
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    from datetime import timedelta
    
    
    ## First date
    eobs =['her','tam']
    ewdc = FDst(eobs,y,m)
    ewdc = ewdc.to_frame()
    ewdc.rename(columns={0:'Dst'}, inplace=True )
    ewdc['UT'] = ewdc.index
    ewdc['LocalTime'] = ewdc.index + timedelta(hours=1.5)
    
    
    wobs =['hon','ipm']
    wwdc = FDst(wobs,y,m)
    wwdc = wwdc.to_frame()
    wwdc.rename(columns={0:'Dst'}, inplace=True )
    wwdc['UT'] = wwdc.index
    wwdc['LocalTime'] = wwdc.index - timedelta(hours=8.5)
    
    obs = ['hon','her','kak','sjg']
    wdc = FDst(obs,y,m)
    wdc.index = pd.to_datetime(wdc.index)
    wdc = wdc.to_frame()
    wdc.rename(columns={0:'Dst'}, inplace=True )
    
     
    
    neobs =['kak','lrm']
    newdc = FDst(neobs,y,m)
    newdc = newdc.to_frame()
    newdc.rename(columns={0:'Dst'}, inplace=True )
    newdc['UT'] = newdc.index
    newdc['LocalTime'] = newdc.index + timedelta(hours=8.5)
    
    
    nwobs =['fuq','sjg']
    nwwdc = FDst(nwobs,y,m)
    nwwdc = nwwdc.to_frame()
    nwwdc.rename(columns={0:'Dst'}, inplace=True )
    nwwdc['UT'] = nwwdc.index
    nwwdc['LocalTime'] = nwwdc.index - timedelta(hours=4.5)
    
    
    
    ewdclt = ewdc.copy()
    ewdclt['datehour'] = ewdclt['LocalTime'].dt.hour
    
    wwdclt = wwdc.copy()
    wwdclt['datehour'] = wwdclt['LocalTime'].dt.hour
    
    newdclt = newdc.copy()
    newdclt['datehour'] = newdclt['LocalTime'].dt.hour
    
    nwwdclt = nwwdc.copy()
    nwwdclt['datehour'] = nwwdclt['LocalTime'].dt.hour
    
        
    
    init =str(y)+'-'+str(m)+'-'+str(inid)
    fint =str(y)+'-'+str(m)+'-'+str(find)
    
    
    
    ewdclt = ewdclt[init:fint]
    wwdclt = wwdclt[init:fint]
    newdclt = newdclt[init:fint]
    nwwdclt = nwwdclt[init:fint]
    wdc = wdc[init:fint]
    
    
    ## Second date
    eobs2 =['her','tam']
    ewdc2 = FDst(eobs2,y2,m2)
    ewdc2 = ewdc2.to_frame()
    ewdc2.rename(columns={0:'Dst'}, inplace=True )
    ewdc2['UT'] = ewdc2.index
    ewdc2['LocalTime'] = ewdc2.index + timedelta(hours=1.5)
    
    
    wobs2 =['hon','ipm']
    wwdc2 = FDst(wobs2,y2,m2)
    wwdc2 = wwdc2.to_frame()
    wwdc2.rename(columns={0:'Dst'}, inplace=True )
    wwdc2['UT'] = wwdc2.index
    wwdc2['LocalTime'] = wwdc2.index - timedelta(hours=8.5)
    
    obs2 = ['hon','her','kak','sjg']
    wdc2 = FDst(obs2,y2,m2)
    wdc2.index = pd.to_datetime(wdc2.index)
    wdc2 = wdc2.to_frame()
    wdc2.rename(columns={0:'Dst'}, inplace=True )
    
     
    
    neobs2 =['kak','lrm']
    newdc2 = FDst(neobs2,y2,m2)
    newdc2 = newdc2.to_frame()
    newdc2.rename(columns={0:'Dst'}, inplace=True )
    newdc2['UT'] = newdc2.index
    newdc2['LocalTime'] = newdc2.index + timedelta(hours=8.5)
    
    
    nwobs2 =['fuq','sjg']
    nwwdc2 = FDst(nwobs2,y2,m2)
    nwwdc2 = nwwdc2.to_frame()
    nwwdc2.rename(columns={0:'Dst'}, inplace=True )
    nwwdc2['UT'] = nwwdc2.index
    nwwdc2['LocalTime'] = nwwdc2.index - timedelta(hours=4.5)
    
    
    
    ewdclt2 = ewdc2.copy()
    ewdclt2['datehour'] = ewdclt2['LocalTime'].dt.hour
    
    wwdclt2 = wwdc2.copy()
    wwdclt2['datehour'] = wwdclt2['LocalTime'].dt.hour
    
    newdclt2 = newdc2.copy()
    newdclt2['datehour'] = newdclt2['LocalTime'].dt.hour
    
    nwwdclt2 = nwwdc2.copy()
    nwwdclt2['datehour'] = nwwdclt2['LocalTime'].dt.hour
    
    
    init2 =str(y2)+'-'+str(m2)+'-'+str(inid2)
    fint2 =str(y2)+'-'+str(m2)+'-'+str(find2)
    
       
    ewdclt2 = ewdclt2[init2:fint2]
    wwdclt2 = wwdclt2[init2:fint2]
    newdclt2 = newdclt2[init2:fint2]
    nwwdclt2 = nwwdclt2[init2:fint2]
    wdc2 = wdc2[init2:fint2]
    
    from matplotlib.lines import Line2D
    #from matplotlib.patches import Patch
    
    
    
    

    
    
    fig, axs = plt.subplots(4,1,figsize=(47,45),dpi=300)
    #fig.autofmt_xdate(rotation=45)
    
    ## First Date
    axs[0].plot(wdc.Dst,'k',label='Dst index',linewidth=5)
    axs[0].plot(ewdclt.Dst,'--',color='blue',label='$Dst_{+15}$',alpha=0,linewidth=4)
    axs[0].plot(wwdclt.Dst,color='blue',label='$Dst_{-85}$',alpha=0,linewidth=4)
    for i in range(len(ewdclt)):
        if 6<=(ewdclt.datehour[i])<=17:
            axs[0].plot(ewdclt.Dst[i:i+2],'--',color='red',linewidth=6)
            if (ewdclt.datehour[i])==6:
                axs[0].plot(ewdclt.Dst[i:i+1],'o',color='red',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
        else:
            axs[0].plot(ewdclt.Dst[i:i+2],'--',color='blue',linewidth=6)
            if (ewdclt.datehour[i])==18:
                axs[0].plot(ewdclt.Dst[i:i+1],'o',color='blue',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
    
            
    for i in range(len(wwdclt)):
        if 6<=(wwdclt.datehour[i])<=17:
            axs[0].plot(wwdclt.Dst[i:i+2],color='red',linewidth=6)
            if (wwdclt.datehour[i])==6:
                axs[0].plot(wwdclt.Dst[i:i+1],'o',color='red',markersize=22)
        else:
            axs[0].plot(wwdclt.Dst[i:i+2],color='blue',linewidth=6)
            if (wwdclt.datehour[i])==18:
                axs[0].plot(wwdclt.Dst[i:i+1],'o',color='blue',markersize=22)
    
    axs[0].tick_params(labelsize=50)
    leg = axs[0].legend(loc=3,fontsize=40)
    for lh in leg.legend_handles: 
        lh.set_alpha(1)
    axs[0].set_ylabel('Dst (nT)',fontsize=50)
    #axs[0].set_title('A. HER-TAM vs HON-IPM '+str(y)+'-'+str(m)+'-'+str(inid)+' to '+
                     #str(y)+'-'+str(m)+'-'+str(find),fontsize=45)
    axs[0].text(0.01, 0.98,'A', transform=axs[0].transAxes, fontsize=65,weight='bold',
        verticalalignment='top')
    axs[0].grid()
    axs[0].tick_params('x', labelbottom=False)
            
    
    
    axs[1].sharex(axs[0])
    axs[1].plot(wdc.Dst,'k',label='Dst index',linewidth = 5)
    axs[1].plot(newdclt.Dst,'--',color='blue',label='$Dst_{+85}$',alpha=0,linewidth=4)
    axs[1].plot(nwwdclt.Dst,color='blue',label='$Dst_{-45}$',alpha=0,linewidth=4)
    for i in range(len(ewdclt)):
        if 6<=(newdclt.datehour[i])<=17:
            axs[1].plot(newdclt.Dst[i:i+2],'--',color='red',linewidth=6)
            if (newdclt.datehour[i])==6:
                axs[1].plot(newdclt.Dst[i:i+1],'o',color='red',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
            
        else:
            axs[1].plot(newdclt.Dst[i:i+2],'--',color='blue',linewidth=6)
            if (newdclt.datehour[i])==18:
                axs[1].plot(newdclt.Dst[i:i+1],'o',color='blue',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
    for i in range(len(nwwdclt)):
        if 6<=(nwwdclt.datehour[i])<=17:
            axs[1].plot(nwwdclt.Dst[i:i+2],color='red',linewidth=6)
            if (nwwdclt.datehour[i])==6:
                axs[1].plot(nwwdclt.Dst[i:i+1],'o',color='red',markersize=22) 
        else:
            axs[1].plot(nwwdclt.Dst[i:i+2],color='blue',linewidth=6)
            if (nwwdclt.datehour[i])==18:
                axs[1].plot(nwwdclt.Dst[i:i+1],'o',color='blue',markersize=22)

    axs[1].tick_params(labelsize=50)
    leg1 = axs[1].legend(loc=3,fontsize=40)
    for lh in leg1.legend_handles: 
        lh.set_alpha(1)
    axs[1].set_ylabel('Dst (nT)',fontsize=50)
    axs[1].text(0.01, 0.98,'B', transform=axs[1].transAxes, fontsize=65,weight='bold',
        verticalalignment='top')
    axs[1].grid()
    axs[1].tick_params('x', labelbottom=True)

    
    
    ##Second Date##
    ###############
    axs[2].plot(wdc2.Dst,'k',label='Dst index',linewidth=5)
    axs[2].plot(ewdclt2.Dst,'--',color='blue',label='$Dst_{+15}$',alpha=0,linewidth=4)
    axs[2].plot(wwdclt2.Dst,color='blue',label='$Dst_{-85}$',alpha=0,linewidth=4)
    for i in range(len(ewdclt2)):
        if 6<=(ewdclt2.datehour[i])<=17:
            axs[2].plot(ewdclt2.Dst[i:i+2],'--',color='red',linewidth=6)
            if (ewdclt2.datehour[i])==6:
                axs[2].plot(ewdclt2.Dst[i:i+1],'o',color='red',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
        else:
            axs[2].plot(ewdclt2.Dst[i:i+2],'--',color='blue',linewidth=6)
            if (ewdclt2.datehour[i])==18:
                axs[2].plot(ewdclt2.Dst[i:i+1],'o',color='blue',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
    
            
    for i in range(len(wwdclt2)):
        if 6<=(wwdclt2.datehour[i])<=17:
            axs[2].plot(wwdclt2.Dst[i:i+2],color='red',linewidth=6)
            if (wwdclt2.datehour[i])==6:
                axs[2].plot(wwdclt2.Dst[i:i+1],'o',color='red',markersize=22)
        else:
            axs[2].plot(wwdclt2.Dst[i:i+2],color='blue',linewidth=6)
            if (wwdclt2.datehour[i])==18:
                axs[2].plot(wwdclt2.Dst[i:i+1],'o',color='blue',markersize=22)
    
    axs[2].tick_params(labelsize=50)
    leg2 = axs[2].legend(loc=3,fontsize=40)
    for lh in leg2.legend_handles: 
        lh.set_alpha(1)
    axs[2].set_ylabel('Dst (nT)',fontsize=50)
    axs[2].text(0.01, 0.98,'C', transform=axs[2].transAxes, fontsize=65,weight='bold',
        verticalalignment='top')
    axs[2].grid()
    axs[2].tick_params('x', labelbottom=False)
            
    
    
    
    axs[3].plot(wdc2.Dst,'k',label='Dst index',linewidth = 5)
    axs[3].plot(newdclt2.Dst,'--',color='blue',label='$Dst_{+85}$',alpha=0,linewidth=4)
    axs[3].plot(nwwdclt2.Dst,color='blue',label='$Dst_{-45}$',alpha=0,linewidth=4)
    for i in range(len(ewdclt2)):
        if 6<=(newdclt2.datehour[i])<=17:
            axs[3].plot(newdclt2.Dst[i:i+2],'--',color='red',linewidth=6)
            if (newdclt2.datehour[i])==6:
                axs[3].plot(newdclt2.Dst[i:i+1],'o',color='red',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
            
        else:
            axs[3].plot(newdclt2.Dst[i:i+2],'--',color='blue',linewidth=6)
            if (newdclt2.datehour[i])==18:
                axs[3].plot(newdclt2.Dst[i:i+1],'o',color='blue',markerfacecolor = 'none',markersize=22,markeredgewidth=4)
    for i in range(len(nwwdclt2)):
        if 6<=(nwwdclt2.datehour[i])<=17:
            axs[3].plot(nwwdclt2.Dst[i:i+2],color='red',linewidth=6)
            if (nwwdclt2.datehour[i])==6:
                axs[3].plot(nwwdclt2.Dst[i:i+1],'o',color='red',markersize=22) 
        else:
            axs[3].plot(nwwdclt2.Dst[i:i+2],color='blue',linewidth=6)
            if (nwwdclt2.datehour[i])==18:
                axs[3].plot(nwwdclt2.Dst[i:i+1],'o',color='blue',markersize=22)

    axs[3].tick_params(labelsize=50)
    leg3 = axs[3].legend(loc=3,fontsize=40)
    for lh in leg3.legend_handles: 
        lh.set_alpha(1)
    axs[3].set_ylabel('Dst (nT)',fontsize=50)
    axs[3].text(0.01, 0.98,'D', transform=axs[3].transAxes, fontsize=65,weight='bold',
        verticalalignment='top')

    axs[3].grid()
    axs[3].sharex(axs[2])

    
    plt.xlabel("UT Time (days)", fontsize=60)
    
    ###Legend
    
    legend_elements = [Line2D([0], [0], marker = 's',color='w',markerfacecolor='red',markersize=35,
                            label = 'Local time from 06:00 to 18:00'),
                       Line2D([0], [0], marker = 's',color='w',markerfacecolor='blue',markersize=35,
                                               label = 'Local time from 18:00 to 06:00')]
    
    legend_elementsA = [Line2D([0], [0], marker = 'o',color='w',markeredgecolor='red',markerfacecolor = 'none',markersize=22,
                            markeredgewidth=4,label = '$Dst_{+15}$ 06:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='blue',markerfacecolor = 'none',markersize=22,
                              markeredgewidth=4,label = '$Dst_{+15}$ 18:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='red',markerfacecolor = 'red',markersize=22,
                              markeredgewidth=4,label = '$Dst_{-85}$ 06:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='blue',markerfacecolor = 'blue',markersize=22,
                              markeredgewidth=4,label = '$Dst_{-85}$ 18:00')]
    
    legend_elementsB = [Line2D([0], [0], marker = 'o',color='w',markeredgecolor='red',markerfacecolor = 'none',markersize=22,
                            markeredgewidth=4,label = '$Dst_{+85}$ 06:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='blue',markerfacecolor = 'none',markersize=22,
                              markeredgewidth=4,label = '$Dst_{+85}$ 18:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='red',markerfacecolor = 'red',markersize=22,
                              markeredgewidth=4,label = '$Dst_{-45}$ 06:00'),
                       Line2D([0], [0], marker = 'o',color='w',markeredgecolor='blue',markerfacecolor = 'blue',markersize=22,
                              markeredgewidth=4,label = '$Dst_{-45}$ 18:00')]
    
    
    fig.legend(handles = legend_elements,loc='lower left',
           bbox_transform=axs[3].transAxes, bbox_to_anchor=[0, -0.6], fontsize = 60)
    
    
    fig.legend(handles = legend_elementsA,loc='lower left',
           bbox_transform=axs[0].transAxes,bbox_to_anchor=[0.11, 0], fontsize = 43)
    fig.legend(handles = legend_elementsB, loc='lower left',
           bbox_transform=axs[1].transAxes,bbox_to_anchor=[0.11, 0], fontsize = 43)
    fig.legend(handles = legend_elementsA,loc='lower left',
           bbox_transform=axs[2].transAxes,bbox_to_anchor=[0.11, 0], fontsize = 43)
    fig.legend(handles = legend_elementsB, loc='lower left',
           bbox_transform=axs[3].transAxes,bbox_to_anchor=[0.11, 0], fontsize = 43)

    
    
    fig.tight_layout()
    
    
    name = 'LocalT'+str(y)+str(m)+'_'+str(y2)+str(m2)+'.pdf'
    Name = 'LocalT'+str(y)+str(m)+'_'+str(y2)+str(m2)+'.svg'
    
    path = ('/Users/santiagopinzon/Mac/articles/Dst_proxies/Images/LocalTimeDst/')
    
    plt.savefig(os.path.join(path,name), bbox_inches='tight' ,dpi=300)
    plt.savefig(os.path.join(path,Name), bbox_inches='tight' ,dpi=300)
    
    plt.show()


