# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:03:49 2022

@author: You
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import functions as func
from pathlib import Path

""" The norm of a vector """
def norma(x, y, z):
    return np.sqrt(x**2+y**2+z**2)


""" Creating colorbars as png for the total magnetic field """
def color_bar(where_csv):
    # Reading the data
    df = pd.read_csv(where_csv)


    df['B'] = func.norma(df['B_r'], df['B_t'], df['B_n'])
    
    vmin = df.B.min()
    vmax = df.B.max()
    
    
    y = list(df.B)
    
    
    
    
    
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)
    
    norm    =  mpl.colors.Normalize(vmin=vmin, vmax= vmax)
    cmap    =  mpl.cm.ScalarMappable(norm = norm, cmap='coolwarm')
    
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap = mpl.cm.coolwarm),
                 cax=ax, orientation='horizontal', label='B [nT]')
    
    pathi = Path(r"C:\Users\You\Desktop\NASA\psp_data\fields\l2\mag_rtn_1min\figures")
    pathf = pathi.joinpath((str(where_csv)[-27:-4]))
    plt.savefig(pathf, dpi=150)
    
    
    color_list = []
    for i in range(len(df)):
        color_list.append(cmap.to_rgba(y[i]))
        
    
    return np.array(color_list)

