#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:40:38 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

#Fourier.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def fourier(obsdf,fqdays,n):
    """
    Function to do the first fourier transform denoising data using the nth harmonic (coeficient) and a
    low pass band filter. Take the nth coeficient of each month and do a Second Fourier transform 
    apply a low pass band filter again. 
    After the Second inverse Fourier tranform we obtain the Sq variation for each month
    Input:
    obsdf - observatory dataframe. contains date with hour and H component
    fqdays - array of the dates of the five quiest days of the month 
    n - harmonic value (used n=3)
    
    Output:
    Sq_month - array of the Sq variation of each month
    optional - graph of the 1st and 2nd fourier transforms and the inverse of each one
    graph of the Sq_month
    """
    # create and empty array size (n,12) (nth coeficients, 12 months)
    coef = np.empty((n,12) ,dtype=complex)
    # create and empty array for the first frequency (0)
    A = np.empty(12)
    
    ### for loop to select the 5 quiest dates for each month and low pass filter
    
    for i in range(12):
        idf= fqdays[i] # 5 quiest dates for each month
        
        # selecting dates in obsdf (observed H)
        df1 = obsdf.HORIZONTAL[str(idf[0])]
        df2 = obsdf.HORIZONTAL[str(idf[1])]
        df3 = obsdf.HORIZONTAL[str(idf[2])]
        df4 = obsdf.HORIZONTAL[str(idf[3])]
        df5 = obsdf.HORIZONTAL[str(idf[4])]
        
        # create a new dataframe using the quiest days 
        ndf = pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True),df3.reset_index(drop=True),df4.reset_index(drop=True),df5.reset_index(drop=True)],axis=1)
        # calculate a mean of the 5 quiest days per hour
        ndf['MEAN'] = ndf.mean(axis=1)

        ### Fourier transform
        
        f = ndf.MEAN # data 
        npts = len(f)
        nf = round((npts/2.)+1)
        # Fourier trnasform using rfft
        f_signal = (np.fft.rfft(f)) # fourier signal spectrum
        f_signal1 = ((f_signal[1:])) # signal without the 1st spectrum (0)
        
        freq = (np.fft.rfftfreq(npts)) #frequencies of the data
        freq1 = freq[1:] # frequencies without the 1st frequency (0)
        
        ### Low pass filter
        
        cut_f_signal = f_signal.copy()
        cut_f_signal[freq>freq[n+1]] = 0 #eliminate the frequencies > nth frequency (coeficient)
        
        ### Inverse Fourier
        filtered_signal = np.fft.irfft(((cut_f_signal)))
        
        ### Apending the coefficients
        
        A[i]=abs(cut_f_signal[0])
        for j in range(n):
            coef[j,i]=(cut_f_signal[j+1]) ## output


        ### Optional output the graph to evaluate the first fourier transform
        
        #fig = plt.figure(figsize=(15,10))
        #ax1 = fig.add_subplot(2,2,1)
        #ax1.plot((f), label="data")
        #ax1.plot(abs(filtered_signal), color='k', label="clean")
        #ax1.legend()
        #ax1 = fig.add_subplot(2,2,2)
        #ax1.plot(freq1,abs(f_signal1),"k")
    
    
    ### Second Fourier transform
    
    #create an array for the filtered coeficients
    invcoef = np.empty((n,12) ,dtype=complex)
    
    #loop for the Second Fourier transfor for the nth coeficient at each month
    for i in range(n):
        ft2 = np.fft.fft(coef[i]) #fourier transform
    
        ft2freq = np.fft.fftfreq(len(coef[i]))
        ft2freq = abs(ft2freq)
    
        cut = ft2.copy()
        cut[ft2freq>ft2freq[1]] = 0 #low pass band filter
    
        inv = np.fft.ifft(cut) ## First inverse Fourier transform
        invcoef[i]=(inv)
        
        ### Optional output the graph to evaluate the second fourier transform
        
        #plt.plot(abs(coef[i]))
        #plt.plot(abs(inv))
        #plt.show()
        
    Sq_month = [] #list for the Sq monthly variation

    m = np.zeros((12,13), dtype=complex)
    #for loop appending the coeficients and prepare a matrix m to do the second inverse
    for i in range(12):
        for j in range(3):
            m[i,j+1]=invcoef[j,i]   
    
    ## Second inverse Fourier transform (graph of the final result)
    for i in range(12):
        d = fqdays[i][0]
        f_inv = np.fft.irfft(m[i])
        a =Sq_month.append(f_inv)
        plt.plot(f_inv, label=str(d.month) +'/'+ str(d.year))#graph of Sq variation of each month
        plt.ylabel('nT')
        plt.xlabel('time (H)')
        plt.legend(bbox_to_anchor=(1.3,0.5),loc='center right')
        plt.suptitle("Fourier "+str(fqdays[0][0].month)+"/"+str(fqdays[0][0].year)+" - "+str(fqdays[11][0].month)+"/"+str(fqdays[11][0].year),size=20)
    Sq_month = np.array(Sq_month)
    
    return Sq_month
