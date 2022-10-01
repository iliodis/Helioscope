# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 17:22:54 2022

@author: You
"""

import pyspedas
import datetime
import cdflib
import pandas as pd
import numpy as np
import glob
from pathlib import Path


""" Creating the starting and ending dates """
# =============================================================================
# start = datetime.datetime(2020,1,19)
# end   = datetime.datetime(2020,2,10)
# 
# dt    = datetime.timedelta(hours = 24)
# 
# t_starts = []
# t_ends   = []
# 
# 
# N = int((end-start)/dt)
# for i in range(N):
#     t_starts.append(start+i*dt)
#     t_ends.append(start+dt+i*dt)
# =============================================================================


""" Downloading the data as cdf """
# =============================================================================
# for j in range(N):
#     trange = [str(t_starts[j]), str(t_ends[j])]
#     
#     pyspedas.psp.spc(trange       = trange,
#                      datatype     = 'l3i',
#                      level        = 'l3',
#                      varnames     = ["np_moment","wp_moment","vp_moment_RTN"],
#                      downloadonly = True,
#                      notplot      = True)
# =============================================================================
    

""" Function for reading the cdf and converting it to csv """
# =============================================================================
# def cdf_to_csv(where_cdf, where_csv):
#     
#     x = cdflib.cdf_to_xarray(where_cdf)
#     
#     np_m = x.np_moment.values
#     wp_m = x.wp_moment.values
#     vp_m = x.vp_moment_RTN.values
#     
#     vp_r = vp_m.T[0]
#     vp_t = vp_m.T[1]
#     vp_n = vp_m.T[2]
#     
#     lista = []
#     length = len(np_m)
#     modulo = int(length/1440)
#     for count in range(length):
#         if (count % modulo == 0) and (len(lista) < 1440):
#             lista.append(count)
#             
#     np_m = np_m[lista]
#     wp_m = wp_m[lista]
#     vp_r = vp_r[lista]
#     vp_t = vp_t[lista]
#     vp_n = vp_n[lista]
#     
#     df = pd.DataFrame({})
#     df['vp_r'] = vp_r
#     df['vp_t'] = vp_t
#     df['vp_n'] = vp_n
#     df['np']   = np_m
#     df['wp']   = wp_m
#     
#     
#     df.to_csv(where_csv)
#     
#     return
# =============================================================================


""" Converting cdfs to csvs """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\sweap\spc\l3\l3i")
# path20     = path0.joinpath("2020")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# 
# for row in range(len(paths_from)):
#     
#     title_i = t_starts[row].strftime("%y")+"-"+t_starts[row].strftime("%m")+"-"+t_starts[row].strftime("%d")
#     
#     title_f = t_ends[row].strftime("%y")+"-"+t_ends[row].strftime("%m")+"-"+t_ends[row].strftime("%d")
#     title   = "spc"+title_i+"_"+title_f+".csv"
#     path_to = Path(r"C:\Users\You\Desktop\NASA\psp_data\sweap").joinpath("csvs").joinpath(title)
#     cdf_to_csv(paths_from[row], path_to)
# =============================================================================


""" Drop the non needed columns of the csvs """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\sweap")
# path20     = path0.joinpath("csvs")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# for pth in paths_from:
#      df      = pd.read_csv(pth)
#      to_drop = df.keys()[0]
#      df.drop(to_drop, axis=1, inplace = True)
#      df.to_csv(pth, index = False)
# =============================================================================
    