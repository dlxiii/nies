# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:05:15 2018
@author: Yulong Wang
"""

import os
import pickle
import numpy as np
import pandas as pd

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
    path_year = "MK" + str(year)
    df_year = pd.DataFrame({"レコードID":[],"測定年度":[],"絶対番号":[],"都道府県コード":[],"水域コード":[],"地点コード":[], "地点統一番号":[]})
    if year >= 1984:
        for item in itemlist:
            df_year = df_year.merge(item_data(path_year, item), \
                                    on = ["レコードID","測定年度","絶対番号","都道府県コード","水域コード","地点コード", "地点統一番号"], \
                                    how = "outer")
    else:
        for item in itemlist[:len(itemlist) - 1]:
            df_year = df_year.merge(item_data(path_year, item), \
                                    on = ["レコードID","測定年度","絶対番号","都道府県コード","水域コード","地点コード", "地点統一番号"], \
                                    how = "outer")
    print("Total line number of the file in " + str(year) + " is " + str(len(df_year)) + ".")
    savepath = "outputs/"
    filename = "MK" + str(year) + "0000"
    df_year.to_csv(savepath + filename + ".csv", sep=',', encoding = "utf-8")
    pickle.dump(df_year, open(savepath + filename + ".tkb", mode = "wb"), protocol = True)
    return df_year
    
def item_data(path_year, item):
    path_item = path_year + "{:0>2d}".format(item)
    df_item = pd.concat([city_data(path_item, city) for city in citylist], ignore_index = True)
    print("Total line number of above files is " + str(len(df_item)) + ".")
    return df_item

        
def city_data(path_item, city):
    path_city = path_item + str(city) + "_0.txt"
    na_values = ["99", "999", "9999", "99999", "E"]
    if os.path.exists(path_city):
        print("Start importing " + path_city + "...")
        df_city = pd.read_csv(path_city, sep=',', skipinitialspace = True, header = 0, \
                     na_values = na_values, encoding = "utf-8", low_memory = False)
        df_city = pd_chiten_toitsu_code(df_city, "都道府県コード","水域コード","地点コード", "地点統一番号")
        return df_city
    else:
        print("Missing file of " + path_city + ", skip...")
   
if __name__  == '__main__':
    filelist = os.listdir()
    filename = [i for i in filelist if ("MK" in i and ".txt" in i)]
    yearlist = sorted(set([int(i[2:6]) for i in filename]), reverse = True)
    itemlist = sorted(set([int(i[6:8]) for i in filename]), reverse = False)
    citylist = sorted(set([int(i[8:10]) for i in filename]), reverse = False)
#    pathlist = ["MK" + str(year) + "{:0>2d}".format(item) + str(city) + "_0.txt" \
#                for year in yearlist for item in itemlist for city in citylist]
    for year in yearlist:
        year_data(year)
    