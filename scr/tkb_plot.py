# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:01:51 2018
@author: Yulong Wang
"""

import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

def chk_sta_name(df, station_name):
    dft = df.iloc[:, 0:4]
    dfc = dft[dft["地点名称_漢字"] == station_name]
    dfcc = list(sorted(set(dfc["地点統一番号"]), reverse = False))
    if len(dfcc) != 1:
        print("There are " + str(len(dfcc)) + " codes of station '" + station_name + "'." )
        for n in dfcc:
            print("They are '" + str(n) + "'." )
            print("By default, the code will be set as '" + str(dfcc[0]) + "'." )
            df.loc[df["地点名称_漢字"] == station_name, "地点統一番号"] = dfcc[0]
#    else:
#        station_code = dfcc[0]
#        print("'" + station_name + "' station has been located, its code is " + station_code + ".")
    return df
        
def chk_sta_code(df, station_code):
    dft = df.iloc[:, 0:3]
    dfc = dft[dft["地点統一番号"] == station_code]
    dfc_1 = sorted(dfc["地点名称_漢字"].drop_duplicates(), reverse = False)
    dfc_2 = sorted(dfc["地点名称_カタカナ"].drop_duplicates(), reverse = True)
    for i in [dfc_1, dfc_2]:
        if len(i) != 1:
            print("There are " + str(len(i)) + " names of station '" + station_code + "'." )
            for n in i:
                print("They are '" + str(n) + "'." )
            print("By default, the name will be set as '" + i[0] + "'." )
            df.loc[df["地点統一番号"] == station_code, "地点名称_漢字"] = dfc_1[0]
            df.loc[df["地点統一番号"] == station_code, "地点名称_カタカナ"] = dfc_2[0]
        else:
            print("There is only 1 name of station " + station_code + ".")
    return df

def check(df):
    sta_code = [i for i in df["地点統一番号"]]
    sta_code = sorted(set(i for i in sta_code), reverse = False)
    df["地点名称_漢字"] = df["地点名称_漢字"].str.replace("　","")
    for code in sta_code:
        df = chk_sta_code(df, code)
    sta_name = [i for i in df["地点名称_漢字"]]
    sta_name = sorted(set(i for i in sta_name), reverse = False)
    for name in sta_name:
        chk_sta_name(df, name)
    sta_code = [i for i in df["地点統一番号"]]
    sta_code = sorted(set(i for i in sta_code), reverse = False)
    sta_name = [i for i in df["地点名称_漢字"]]
    sta_name = sorted(set(i for i in sta_name), reverse = False)
    if len(sta_code) == len(sta_name):
        print("After checking, there are " + str(len(sta_code)) + " stations in database.")
    return df

def filler_year(df, year):
    dfct = df[df["採取_年"] == year]
    return dfct

def lat_lon(df, name):
    dfll = df[df["地点名称_漢字"] == name]
    return dfll[["地点名称_漢字","緯度_Ｎ","経度_Ｅ"]].iloc[-1:]

def find_sta(df):
    sta_year = sorted(set(i for i in [j for j in df["採取_年"]]), reverse = False)
    sta_name = sorted(set(i for i in [j for j in df["地点名称_漢字"]]), reverse = False)
    for year in sta_year:
        dff = filler_year(df, year)
        sta = sorted(set(i for i in [j for j in dff["地点名称_漢字"]]), reverse = False)
        stations = [i for i in sta_name if i in sta]
        print("In the year of " + str(year) + ", there are " + str(len(sta)) + " stations.")   
    sta_info = pd.DataFrame({"地点名称_漢字":[],"緯度_Ｎ":[],"経度_Ｅ":[]})
    for name in stations:
        sta_info = sta_info.merge(lat_lon(df, name), on = ["地点名称_漢字","緯度_Ｎ","経度_Ｅ"], how = "outer")
    return sta_info    

    # service = 'ESRI_Imagery_World_2D'
    # service = 'ESRI_StreetMap_World_2D'
    # service = 'I3_Imagery_Prime_World'
    # service = 'NASA_CloudCover_World'
    # service = 'NatGeo_World_Map'
    # service = 'NGS_Topo_US_2D'
    # service = 'Ocean_Basemap'
    # service = 'USA_Topo_Maps'
    # service = 'World_Imagery'
    # service = 'World_Physical_Map'
    # service = 'World_Shaded_Relief'
    # service = 'World_Street_Map'
    # service = 'World_Terrain_Base'
    # service = 'World_Topo_Map'
  
def mak_layer(value, maxvalue, num_lay):
    cat = value / maxvalue
    for i in range(1, num_lay + 1):
        if cat > ((1 / num_lay) * (i - 1)) and cat <= ((1 / num_lay) * i):
            num_lay = i
    return num_lay
       
def mod_depth(dfpl, col_ori, col_mod, col_lay):
    dmax = dfpl["全水深(m)"].max()
    dfmd = [i for i in dfpl[col_ori]]
    for i in range(len(dfmd)):
        if dfmd[i] > dmax:
            dfmd[i] = dfmd[i] / 10
        else:
            dfmd[i] = dfmd[i]
    dfpl[col_mod] = [cm for cm in dfmd]
    dfpl[col_lay] = [mak_layer(cm, dmax, 5) for cm in dfmd]
    dfpl.drop([col_ori], axis = 1, inplace = True)
    return dfpl
    
def plot_sta(df, na, year_b, year_e):
    dfpl = df[df["採取_年"] >= year_b]
    dfpl = dfpl[dfpl["採取_年"] <= year_e]
    dfpl = dfpl[dfpl["地点名称_漢字"] == na]
    dfpl = mod_depth(dfpl, "採取水深(m)", "採取水深_mod(m)", "採取水深分层番号")
    dfpl = dfpl[pd.notnull(dfpl["全窒素(mg/l)"])]
    dfpl = dfpl[pd.notnull(dfpl["採取水深_mod(m)"])]
    dfpl = dfpl.sort_values("採取_年月日時分")
    ly_n = dfpl["採取水深分层番号"].max()
    for ly in range(1, ly_n + 1):
        dfp = dfpl[dfpl["採取水深分层番号"] == ly]
        plt.cla()
        plt.clf()
        nax = 6
        g_ratio = (1. + np.sqrt(5.)) / 2.
        fig_wid = 7.48
        figsize = (fig_wid, fig_wid / g_ratio * nax / 3)
        fig, ax = plt.subplots(nax, 1, sharex = 'col', sharey = 'all', squeeze = False, figsize = figsize)
        
        plt.subplot(nax, 1, 1)
        plt.plot(dfp["採取_年月日時分"],dfp["水温(℃)"])
        plt.plot(dfp["採取_年月日時分"],dfp["気温(℃)"], linestyle = '--')
        plt.title("Temp of water and atoms. (℃), No. of water layer: " + str(ly) + ".", fontsize = 10)
        plt.subplot(nax, 1, 2)
        plt.plot(dfp["採取_年月日時分"],dfp["pH"])
        plt.title("pH, No. of water layer: " + str(ly) + ".", fontsize = 10)
        plt.subplot(nax, 1, 3)
        plt.plot(dfp["採取_年月日時分"],dfp["DO(mg/l)"])
        plt.title("DO(mg/l), No. of water layer: " + str(ly) + ".", fontsize = 10)
        plt.subplot(nax, 1, 4)
        plt.plot(dfp["採取_年月日時分"],dfp["COD(mg/l)"])
        plt.title("COD(mg/l), No. of water layer: " + str(ly) + ".", fontsize = 10)
        plt.subplot(nax, 1, 5)
        plt.plot(dfp["採取_年月日時分"],dfp["全窒素(mg/l)"])
        plt.title("TN (mg/l), No. of water layer: " + str(ly) + ".", fontsize = 10)
        plt.subplot(nax, 1, 6)
        plt.plot(dfp["採取_年月日時分"],dfp["全燐(mg/l)"])
        plt.title("TP (mg/l), No. of water layer: " + str(ly) + ".", fontsize = 10)
        
        plt.tight_layout()
        fig.savefig(savepath + "plot_station/" +str(year_b) + " to " + str(year_e) + " '" + na + "' change in No. " + str(ly) + " layer of water.png", dpi = 1200)
        plt.close('all')
        

if __name__  == '__main__':
    filepath = "../outputs/tkb/MK_tokyobay.tkb"
    savepath = "../outputs/tkb/outputs/"
    df = pickle.load(open(filepath, mode = "rb"))
    df = check(df)
    sta_info = find_sta(df)
#    lats = [float(lats) for lats in sta_info['緯度_Ｎ'][:]]
#    lons = [float(lons) for lons in sta_info['経度_Ｅ'][:]]
#    service = 'World_Imagery'
#    map = Basemap(llcrnrlat = 34.80, urcrnrlat = 35.85, \
#                  llcrnrlon = 139.35, urcrnrlon = 140.35, \
#                  resolution = 'f', epsg = 3857)
#    x, y = map(lons,lats)
#    map.arcgisimage(service = service, xpixels = 1800, dpi = 2400, verbose= True)
#    map.scatter(x, y, 0.5, marker='o', color='y')
#    fig = plt.gcf()
#    plt.title("%s stations in Tokyo Bay." %(str(len(lats))), fontsize = 10)
#    plt.show()
#    fig.savefig(savepath + "/plot_stations_map/TokyoBay_Stations" + ".png", dpi = 2400)

#
#    year_b = 1981
#    year_e = 2009
#    name = sorted(set(i for i in [j for j in sta_info["地点名称_漢字"]]), reverse = False)
#    for na in name:
#        plot_sta(df, na, year_b, year_e)


#    year_b = 1999
#    year_e = 2009
#    name = ["船橋１", "船橋２", "東京湾１", "東京湾２", "東京湾３", "東京湾４"]
#    for na in name:
#        plot_sta(df, na, year_b, year_e)
        
    year_b = 1981
    year_e = 1990
    name = ["船橋１", "船橋２", "東京湾１", "東京湾２", "東京湾３", "東京湾４"]
    for na in name:
        plot_sta(df, na, year_b, year_e)
    












