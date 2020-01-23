# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:20:42 2018
@author: Yulong Wang
"""
import numpy as np
from datetime import datetime
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.gridspec as gridspec

temp_atm = [8.3, 10.6, 6.2, 20.2, 22.6, 25.0, 29.0, 29.1, 27.4, 21.1, 19.3, 12.6]
date     = ["2004-01-06", "2004-02-03", "2004-03-02", "2004-04-20",\
           "2004-05-11", "2004-06-07", "2004-07-07", "2004-08-03",\
           "2004-09-14", "2004-10-12", "2004-11-10", "2004-12-07"]
date = [datetime.strptime(i, "%Y-%m-%d") for i in date]

date_up = ["2004-01-06 11:16:00", "2004-02-03 12:02:00", "2004-03-02 11:06:00", "2004-04-20 11:08:00",\
           "2004-05-11 11:44:00", "2004-06-07 12:17:00", "2004-07-07 11:30:00", "2004-08-03 12:15:00",\
           "2004-09-14 12:10:00", "2004-10-12 11:17:00", "2004-11-10 12:29:00", "2004-12-07 11:21:00"]
date_up = [datetime.strptime(i, "%Y-%m-%d  %H:%M:%S") for i in date_up]
temp_sea_up = [12.1, 9.5, 10.5, 16.8, 19.1, 22.7, 27.0, 29.1, 25.6, 21.9, 19.4, 15.9]
to_nitro_up = [0.86, 0.83, 1.20, 0.92, 0.97, 1.00, 1.30, 0.71, 0.74, 0.93, 0.80, 1.00]
to_phosp_up = [0.05, 0.04, 0.05, 0.05, 0.08, 0.08, 0.13, 0.09, 0.09, 0.09, 0.05, 0.08]
no2_no3_up  = [0.51, 0.39, 0.49, 0.28, 0.25, 0.16, 0.02, 0.02, 0.02, 0.50, 0.48, 0.60]
no2_up      = [np.nan, np.nan, np.nan, 0.032, 0.024, 0.027, 0.005, 0.002, 0.007, 0.028, 0.036, 0.036]

ph_up       = [8.1, 8.3, 8.2, 8.6, 8.4, 8.6, 8.6, 8.9, 8.6, 7.9, 8.1, 7.9]
do_up       = [9.5, 12.0, 9.5, 12.0, 10.0, 9.9, 10.0, 13.0, 10.0, 5.7, 7.8, 8.4]
cod_up      = [2.0, 2.5, 2.8, 4.8, 4.2, 5.3, 6.8, 7.5, 6.2, 2.1, 2.0, 2.2]


date_dn = ["2004-01-06 11:21:00", "2004-02-03 12:07:00", "2004-03-02 11:11:00", "2004-04-20 11:13:00",\
           "2004-05-11 11:49:00", "2004-06-07 12:22:00", "2004-07-07 11:35:00", "2004-08-03 12:20:00",\
           "2004-09-14 12:15:00", "2004-10-12 11:22:00", "2004-11-10 12:34:00", "2004-12-07 11:26:00"]
date_dn = [datetime.strptime(i, "%Y-%m-%d  %H:%M:%S") for i in date_dn]
temp_sea_dn = [12.1, 9.8, 10.4, 16.2, 17.3, 19.2, 26.2, 26.5, 25.4, 22.2, 20.3, 16.1]
to_nitro_dn = [0.88, 0.93, 1.00, 1.00, 0.75, 0.69, 0.88, 0.70, 0.74, 0.78, 0.62, 0.82]
to_phosp_dn = [0.049, 0.051, 0.044, 0.054, 0.058, 0.097, 0.09, 0.084, 0.082, 0.077, 0.061, 0.067]
no2_no3_dn  = [0.500, 0.370, 0.480, 0.400, 0.180, 0.096, 0.026, 0.015, 0.100, 0.420, 0.380, 0.480]
no2_dn      = [np.nan, np.nan, np.nan, 0.037, 0.019, 0.026, 0.006, 0.002, 0.021, 0.011, 0.021, 0.032]
ph_dn       = [8.1, 8.2, 8.2, 8.5, 8.3, 7.9, 8.5, 8.6, 8.4, 7.9, 7.9, 7.9]
do_dn       = [8.4, 8.7, 8.9, 9.9, 7.9, 1.8, 6.0, 1.9, 7.3, 4.2, 2.6, 7.4]
cod_dn      = [1.8, 2.5, 2.5, 4.6, 3.5, 1.8, 5.0, 5.3, 4.3, 2.1, 1.7, 1.9]

fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, :])
ax.plot(date, temp_atm)
ax.plot(date, temp_sea_up)
ax.plot(date, temp_sea_dn)
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
ax.set_ylabel('Air temp [deg]')
ax.set_xlabel('2004')

fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, :])
ax.plot(date, to_nitro_up)
ax.plot(date, to_phosp_up)
ax.plot(date, no2_no3_up)
ax.plot(date, no2_up)
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
ax.set_ylabel('Air temp [deg]')
ax.set_xlabel('2004')

fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, :])
ax.plot(date, to_nitro_dn)
ax.plot(date, to_phosp_dn)
ax.plot(date, no2_no3_dn)
ax.plot(date, no2_dn)
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(ticker.NullFormatter())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
ax.set_ylabel('Air temp [deg]')
ax.set_xlabel('2004')


