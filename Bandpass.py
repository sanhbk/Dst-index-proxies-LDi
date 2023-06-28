#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:35:24 2022

@author: Santiago Pinzon-Cortes
@contact: sanpinzoncor@unal.edu.co
"""

from Final_Dst import FDst

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import os
from datetime import timedelta


y = 2004
m= 7

fuq = FDst('fuq',y,m)
fuq.index = pd.to_datetime(fuq.index)-timedelta(minutes=59)

obs = ['hon','her','kak','sjg']
wdc = FDst(obs,y,m)
wdc.index = pd.to_datetime(wdc.index)

hua = FDst('hua',y,m)
hua.index = pd.to_datetime(hua.index)

fig, axs = plt.subplots(figsize=(20,5))

axs.plot((fuq.Dst),'k', label='fuq',zorder=10)
axs.plot(wdc, label='wdc',zorder=5)
axs.plot(hua.Dst, label='hua',zorder=0)

axs.legend()

plt.show()


from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

import numpy as np
from scipy.signal import freqz
# Sample rate and desired cutoff frequencies (in Hz).
fs = 744.0/2
lowcut = 11.0
highcut = 25.0

# Plot the frequency response for a few different orders.
plt.figure(1)
plt.clf()
for order in [1, 2, 3]:
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    w, h = freqz(b, a, worN=2000)
    plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
         '--', label='sqrt(0.5)')
#plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(True)
plt.legend(loc='best')
plt.show()

lowcut = 10
highcut = 14
fs = len(hua.Dst)/2



signal = butter_bandpass_filter(hua.Dst, lowcut, highcut, fs, order=1)
fuq_signal = butter_bandpass_filter(fuq.Dst, lowcut, highcut, fs, order=1)

plt.plot(hua.index,signal,label='filter')
plt.plot(hua.Dst, label='hua')
plt.legend()
plt.show()

plt.plot(fuq.index,fuq_signal,label='filter fuq')
plt.plot(fuq.Dst, label='fuq')
plt.legend()
plt.show()




fuq = FDst('fuq',y,m)
fuq.index = pd.to_datetime(fuq.index)-timedelta(minutes=59)

df = pd.read_csv('/Users/santiagopinzon/Mac/articles/Dst_proxies/DATA/F107/noaa_radio_flux.csv',low_memory=False)
df.rename(columns = {'f107_adjusted (solar flux unit (SFU))':'f107_adjusted', 'f107_observed (solar flux unit (SFU))':'f107_observed'}, inplace = True)

df['dates'] = pd.to_datetime(df['time (yyyyMMdd)'], format='%Y%m%d')

df.index = df.dates

init = str(y)+'-'+str(m)+'-'+'01'
fint = str(y)+'-'+str(m+1)+'-'+'01'


df_cut = df[init:fint]

fig, ax1 = plt.subplots(figsize=(15,8))

ax2 = ax1.twinx()
lns1 = ax1.plot(df_cut.index, df_cut.f107_adjusted, 'g-',label='f107')
lns2 = ax2.plot(hua.index, signal, 'b-',label='FUQ')

ax1.set_xlabel('X data')
ax1.set_ylabel('f107 adjusted (solar flux unit (SFU))')
ax2.set_ylabel('Dst (nT)')

lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=0)


plt.show()


plt.show()



