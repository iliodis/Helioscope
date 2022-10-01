# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:40:23 2022

@author: You
"""

import pyspedas
import datetime
import cdflib
import pandas as pd
import numpy as np
import glob
from pathlib import Path
import functions as func

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
#     pyspedas.psp.fields(trange       = trange,
#                         datatype     = 'mag_RTN_1min',
#                         downloadonly = True,
#                         notplot      = True)
# =============================================================================
    

""" Function for reading the cdf and converting it to csv """
# =============================================================================
# def cdf_to_csv(where_cdf, where_csv):
#     
#     x = cdflib.cdf_to_xarray(where_cdf)
#     vals  = x['psp_fld_l2_mag_RTN_1min'].values.T
#     flags = x['psp_fld_l2_quality_flags'].values
#     
#     
#     df = pd.DataFrame({})
#     df['B_r']   = vals[0]
#     df['B_t']   = vals[1]
#     df['B_n']   = vals[2]
#     try:
#         df['flags'] = flags
#     except Exception as exc:
#         bool1       = np.full((len(vals[0])), True)
#         bool2       = np.full((-len(vals[0])+len(flags)), False)
#         boollist    = np.append(bool1,bool2)
#         df['flags'] = flags[boollist]
#         print(exc)
#         print(str(where_csv)[53:-4])
#         
#     df.to_csv(where_csv)
#     
#     return
# =============================================================================


""" Converting cdfs to csvs """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\fields\l2\mag_rtn_1min")
# path20     = path0.joinpath("2020")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# 
# for row in range(len(paths_from)):
#     
#     title_i = t_starts[row].strftime("%y")+"-"+t_starts[row].strftime("%m")+"-"+t_starts[row].strftime("%d")
#     
#     title_f = t_ends[row].strftime("%y")+"-"+t_ends[row].strftime("%m")+"-"+t_ends[row].strftime("%d")
#     title   = "fields"+title_i+"_"+title_f+".csv"
#     path_to = path0.joinpath("csvs").joinpath(title)
#     cdf_to_csv(paths_from[row], path_to)
# =============================================================================



""" Extending the csvs with data analysis """

""" Colors """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\fields\l2\mag_rtn_1min")
# path20     = path0.joinpath("csvs")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# for pth in paths_from:
#     df      = pd.read_csv(pth)
#     col_ar  = func.color_bar(pth)
#     df["r"] = col_ar.T[0]
#     df["b"] = col_ar.T[1]
#     df["g"] = col_ar.T[2]
#     df["a"] = col_ar.T[3]
#     
#     df.to_csv(pth)
# =============================================================================

""" Drop the non needed columns of the csvs """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\fields\l2\mag_rtn_1min")
# path20     = path0.joinpath("csvs")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# for pth in paths_from:
#     df      = pd.read_csv(pth)
#     to_drop = df.keys()[0:2]
#     df.drop(to_drop, axis=1, inplace = True)
#     df.to_csv(pth, index = False)
# =============================================================================
    

""" PVI """
# =============================================================================
# path0      = Path(r"C:\Users\You\Desktop\NASA\psp_data\fields\l2\mag_rtn_1min")
# path20     = path0.joinpath("csvs")
# paths_from = glob.glob(str(path20.joinpath("*")))
# 
# #In minutes
# tau = 5
# 
# for pth in paths_from:
#     
#     df      = pd.read_csv(pth)
#     
#     Bup = []
#     for i in range(len(df)-tau):
# 
#         Bi  = np.array([df['B_r'][i], df['B_t'][i], df['B_n'][i]])
#         Bf  = np.array([df['B_r'][i+tau], df['B_t'][i+tau], df['B_n'][i+tau]])
#         dB  = Bf - Bi
#         Bup.append(np.linalg.norm(dB))
#         
#     Bup = np.array(Bup)
#     
#     PVI = Bup/np.sqrt(np.average(Bup**2))
#         
#     PVI = list(PVI)
#     for k in range(len(df) - len(PVI)):
#         PVI.append(np.nan)
#     
#     df["PVI"] = PVI
#     
#     df.to_csv(pth, index = False)
# =============================================================================
    



