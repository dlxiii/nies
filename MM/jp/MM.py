# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:12:15 2018
@author: Yulong Wang
"""

import os
import pickle
import numpy as np
import pandas as pd

def pd_integrate_ddd_mm_ss(df, ddd, mm, ss, col_name):
  '''
  Integrate cols of "ddd", "mm" and "ss" into a col of "ddd:mm:ss"
    In : df = DataFrame; ddd, mm, ss = col names; col_name = added col name
    Out: DataFrame with adding	the "ddd:mm:ss" col
  将纬度经度统一为度（3位）：分（2位）：秒（2位）后，创建新一列
  '''
  dfc = ["{0:3d}:{1:02d}:{2:02d}".format(i1,i2,i3) \
         for i1,i2,i3 in zip(df[ddd].astype(int).values, df[mm].astype(int).values, df[ss].astype(int).values)]
  df[col_name] = dfc
  return df

def pd_decimalize_ddd_mm_ss(df, ddd, mm, ss, col_name):
  '''
  Integrate cols of "ddd", "mm" and "ss" into a col of "ddd:mm:ss"
    In : df = DataFrame; ddd, mm, ss = col names; col_name = added col name
    Out: DataFrame with adding	the "ddd:mm:ss" col
    将纬度经度统一为小数化格式后，创建新一列
  '''
  temp = df[ddd].astype(float).values + df[mm].astype(float).values/60 + df[ss].astype(float).values/3600
  dfcc = ["{:.8f}".format(i) for i in temp]
  df[col_name] = dfcc
  return df

def pd_chiten_toitsu_code(df, ken_code, suiiki_code, chiten_code, col_name):
  '''
  Integrate cols of "ken_code", "suiiki_code" and "chiten_code" into
  a col of "chitentoitsu_code"
    In : df=DataFrame, ken_code, suiiki_code, chiten_code = col names,
         col_name = added col name
    Out: DateFrame with adding the "kencode""suiiki_code""chiten_code" col
  将县代码，水域代码和地点代码统一到一行代码中后，创建新一列
  '''
  dfc = [np.nan if pd.isnull(i1) or pd.isnull(i2) or pd.isnull(i3) else \
         "{0:02d}{1:03d}{2:02d}".format(int(i1),int(i2),int(i3)) \
         for i1,i2,i3 in zip(df[ken_code].values, df[suiiki_code].values, \
         df[chiten_code].values)]
  df[col_name] = dfc
  return df

def year_data(year):
    print("Begin to analysis data of", year, "...")
    filepath = "MM" + str(year) + "0000.txt"
    names = ["西暦年度","ＲＬＳ識別コード","水系コード","絶対番号",\
             "地点新設等コード","県コード_地点統一番号","水域コード_地点統一番号","地点コード_地点統一番号",\
             "ＣＯＤ等基準点識別コード","水域名称_漢字","水域名称_カタカナ","水域名称_ローマ字",\
             "地点名称_漢字","地点名称_カタカナ","地点名称_ローマ字","類型","達成期間","指定区分",\
             "類型指定年_ＣＯＤ等","類型指定月_ＣＯＤ等","類型指定日_ＣＯＤ等",\
             "特例１","特例２","特例３","特例４","特例５",\
             "ＣＯＤの測定方法","県際水域コード","県際地点コード",\
             "測定中止年","測定中止月","測定中止日","測定再開年","測定再開月","測定再開日",\
             "ＮＰ測定コード","ＮＰ基準点識別コード","ＮＰ水域コード",\
             "ＮＰ水域名称_漢字","ＮＰ水域名称_カタカナ","ＮＰ水域名称_ローマ字",\
             "ＮＰ地点名称_漢字","ＮＰ地点名称_カタカナ","ＮＰ地点名称_ローマ字",\
             "ＮＰ類型","ＮＰ達成期間","ＮＰ指定区分",\
             "ＮＰ類型指定年","ＮＰ類型指定月","ＮＰ類型指定日",\
             "Ｎ指定の有無","Ｐ指定の有無","Ｎ暫定基準値","Ｐ暫定基準値","ＮＰ基準の特例","Ｎ測定方法","Ｐ測定方法",\
             "ＮＰ県際水域コード","ＮＰ県際地点コード","ＮＰ測定中止年","ＮＰ測定中止月","ＮＰ測定中止日",\
             "ＮＰ測定再開年","ＮＰ測定再開月","ＮＰ測定再開日","水道の取水地点",\
             "緯度_Ｎ(度)","緯度_Ｎ(分)","緯度_Ｎ(秒)","経度_Ｅ(度)","経度_Ｅ(分)","経度_Ｅ(秒)",\
             "水質年鑑コード","推定絶対番号","推定水系コード","備考"]
    usecols = [i for i in range(76)]
    df = pd.read_csv(filepath, sep = ',', skipinitialspace = True, header = None, skiprows = 1,\
                     names = names, usecols = usecols, encoding = "utf-8", low_memory = False)
    df = df[df["緯度_Ｎ(度)"].notnull()]
    df = pd_decimalize_ddd_mm_ss(df, "緯度_Ｎ(度)", "緯度_Ｎ(分)", "緯度_Ｎ(秒)", "緯度_Ｎ")
    df = pd_decimalize_ddd_mm_ss(df, "経度_Ｅ(度)", "経度_Ｅ(分)", "経度_Ｅ(秒)", "経度_Ｅ")
    df = pd_integrate_ddd_mm_ss(df, "緯度_Ｎ(度)", "緯度_Ｎ(分)", "緯度_Ｎ(秒)", "緯度_Ｎ_dms")
    df = pd_integrate_ddd_mm_ss(df, "経度_Ｅ(度)", "経度_Ｅ(分)", "経度_Ｅ(秒)", "経度_Ｅ_dms")
    df = pd_chiten_toitsu_code(df, "県コード_地点統一番号","水域コード_地点統一番号","地点コード_地点統一番号", "地点統一番号")
    df.drop(["緯度_Ｎ(度)", "緯度_Ｎ(分)", "緯度_Ｎ(秒)","経度_Ｅ(度)", "経度_Ｅ(分)", "経度_Ｅ(秒)"], axis = 1, inplace = True)
    savepath = "outputs/"
    filename = "MM" + str(year) + "0000"
    df.to_csv(savepath + filename + ".csv", sep=',', encoding = "utf-8")
    pickle.dump(df, open(savepath + filename + ".tkb", mode = "wb"), protocol = True)

if __name__  == '__main__':
    filelist = os.listdir()
    filelist = [i for i in filelist if ("MM" in i and ".txt" in i)]
    yearlist = sorted([int(i[2:6]) for i in filelist], reverse = True)
    for year in yearlist:
        year_data(year)




