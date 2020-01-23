# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 20:55:22 2018
@author: Yulong Wang
"""

import os
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

def merge_datetime(data_mk, year, monthday, hourminutes, ymdhm):
    df = data_mk[["採取_年", "採取_月日", "採取_時分"]].fillna("0000")
    df = ["{:0>4d}{:0>4d}{:0>4d}".format(i1,i2,i3) \
         for i1,i2,i3 in zip(df[year].astype(int).values, \
                             df[monthday].astype(int).values, \
                             df[hourminutes].astype(int).values)]
    data_mk[ymdhm] = [datetime.strptime(s, "%Y%m%d%H%M") for s in df]
    return data_mk

def find_tkb(filename):
    data_mk = pickle.load(open(path_dir[0] + filename, mode = "rb"))
    data_mk = data_mk[data_mk["地点統一番号"].notnull()]
    data_mk = data_mk[(data_mk["都道府県コード"] >= 12) & (data_mk["都道府県コード"] <= 14)]
    data_mk = data_mk[(data_mk["水域コード"] >= 601) & (data_mk["水域コード"] <= 611)]
    data_mk = merge_datetime(data_mk, "採取_年", "採取_月日", "採取_時分", "採取_年月日時分")
    print("Reading " + filename + " , line number is " + str(len(data_mk)) + ".")
    return data_mk

if __name__  == '__main__':
    path_dir = ["../outputs/mk/"]
    filelist = [sorted((n for n in os.listdir(p) if ".tkb" in n), reverse=True) for p in path_dir]
    df_mk = pd.concat([find_tkb(filelist[0][i]) for i in range(len(filelist[0]))], ignore_index = True, sort = True)
    df_mk = df_mk[["地点統一番号","地点名称_漢字","地点名称_カタカナ","地点名称_ローマ字",\
                   "緯度_Ｎ","経度_Ｅ","緯度_Ｎ_dms","経度_Ｅ_dms",\
                   "天候コード","流況コード","臭気コード","色相コード",\
                   "気温(℃)","水温(℃)","流量(m3/s)","全水深(m)","透明度(m)",\
                   "採取_年","採取_月日","採取_時分","採取_年月日時分","採取水深(m)",\
                   "カドミウム(mg/l)",\
                   "全シアン(mg/l)",\
                   "鉛(mg/l)",\
                   "六価クロム(mg/l)",\
                   "砒素(mg/l)",\
                   "総水銀(mg/l)",\
                   "アルキル水銀(mg/l)",\
                   "PCB(mg/l)",\
                   "有機リン(mg/l)",\
                   "ジクロロメタン(mg/l)",\
                   "四塩化炭素(mg/l)",\
                   "1，2-ジクロロエタン(mg/l)",\
                   "1，1-ジクロロエチレン(mg/l)",\
                   "シス-1，2-ジクロロエチレン(mg/l)",\
                   "1，1，1-トリクロロエタン(mg/l)",\
                   "1，1，2-トリクロロエタン(mg/l)",\
                   "トリクロロエチレン(mg/l)",\
                   "テトラクロロエチレン(mg/l)",\
                   "1，3-ジクロロプロペン(mg/l)",\
                   "チウラム(mg/l)",\
                   "シマンジン(mg/l)",\
                   "チオベンカルプ(mg/l)",\
                   "ベンゼン(mg/l)",\
                   "セレン(mg/l)",\
                   "亜硝酸性窒素(mg/l)",\
                   "硝酸性窒素及び亜硝酸性窒素(mg/l)",\
                   "ふっ素(mg/l)",\
                   "ほう素(mg/l)",
                   "pH",\
                   "DO(mg/l)",\
                   "BOD(mg/l)",\
                   "COD(mg/l)",\
                   "SS(mg/l)",
                   "大腸菌群数(MPN/100ml)",\
                   "n-ヘキサン抽出物質(mg/l)",\
                   "全窒素(mg/l)",\
                   "全燐(mg/l)"]]
    savepath = "../outputs/tkb/"
    filename_mk = "MK_tokyobay"
    print("File: " + filename_mk + " contains " + str(len(df_mk)) + " lines.")
    df_mk.to_csv(savepath + filename_mk + ".csv", sep=',', encoding = "utf-8")
    pickle.dump(df_mk, open(savepath + filename_mk + ".tkb", mode = "wb"), protocol = True)
    