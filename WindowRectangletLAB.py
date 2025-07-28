# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt

def window(x, N1, N2):
    wx = np.zeros(x.size)
    for i in range(0, x.size):
        if i >= N1 and i <= N2:
            # Add code
            wx[i] = x[i]
        else:
            # Add code
            wx[i] = 0
    return wx

# Create signal, x
# Add code 
#Original signal
#x = np.array([1,1,1,1,1,1,1,1, 1, 1])
x = np.array([-2,1.5,0,1.5,0.5,1,-1,-1, 0.25, 0.3])
# Create array of sample numbers, n
# Add code 
n = np.arange(0, x.size)
# Calculate windowed signal, wx
# Add code
#Windowed signal
wx = window(x, 2, 6) 

def format_stem():
    plt.setp(stemline, color='k', linewidth=2.0)
    plt.setp(baseline, color='k', linewidth=2.0)
    plt.setp(markerline, color='k', markersize=10)
    ax.set_xlabel('n', fontsize=24, labelpad=12)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.tick_params(axis='both', which='both', labelsize=18, length=0)
    markerline.set_clip_on(False)

fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(211)
# Stem plot x
# Add code 
markerline, stemline, baseline = ax.stem(n, x, markerfmt='o')
plt.ylabel('x[n]', fontsize=24, labelpad=15)
plt.title("Original Signal", fontsize=24, pad=15)
format_stem()
ax = fig.add_subplot(212)
# Stem plot wx
# Add code 
markerline, stemline, baseline = ax.stem(n, wx, markerfmt='o')
plt.ylabel('wx[n]', fontsize=24, labelpad=15)
plt.title("Windowed Signal", fontsize=24, pad=15)
format_stem()
plt.subplots_adjust(hspace=0.5)

plt.show()
