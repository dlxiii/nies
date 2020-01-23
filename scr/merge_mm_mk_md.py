# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 11:32:39 2018
@author: Yulong Wang
"""

import os
import pickle

def merge_files_mk(year):
    data_samp = pickle.load(open(path_dir[0] + filelist[0][2009 - year], mode = "rb"))
    data_stat = pickle.load(open(path_dir[1] + filelist[1][2009 - year], mode = "rb"))
    df_year_mk = data_samp.merge(data_stat, on = ["地点統一番号"], how = "inner")
    savepath = "../outputs/mk/"
    filename_mk = "MK_MM" + str(year)
    print("File: " + filename_mk + " contains " + str(len(df_year_mk)) + " lines.")
    df_year_mk.to_csv(savepath + filename_mk + ".csv", sep=',', encoding = "utf-8")
    pickle.dump(df_year_mk, open(savepath + filename_mk + ".tkb", mode = "wb"), protocol = True)
    return df_year_mk

def merge_files_md(year):
    data_stat = pickle.load(open(path_dir[1] + filelist[1][2009 - year], mode = "rb"))
    data_annu = pickle.load(open(path_dir[2] + filelist[2][2009 - year], mode = "rb"))
    if year <= 1977:
        df_year_md = data_annu.merge(data_stat, on = ["西暦年度","絶対番号"], how = "inner")
    else:
        df_year_md = data_annu.merge(data_stat, on = ["西暦年度","県コード_地点統一番号","水域コード_地点統一番号","地点コード_地点統一番号","地点統一番号"], how = "inner")
    savepath = "../outputs/md/"
    filename_md = "MD_MM" + str(year)
    print("File: " + filename_md + " contains " + str(len(df_year_md)) + " lines.")
    df_year_md.to_csv(savepath + filename_md + ".csv", sep=',', encoding = "utf-8")
    pickle.dump(df_year_md, open(savepath + filename_md + ".tkb", mode = "wb"), protocol = True)
    return df_year_md

if __name__  == '__main__':
    path_dir = ["../MK/outputs/", "../MM/jp/outputs/","../MD/outputs/"]
    filelist = [sorted((n for n in os.listdir(p) if ".tkb" in n), reverse=True) for p in path_dir]
    for year in range(1981,2010):
        merge_files_mk(year)
    for year in range(1971,2010):
        merge_files_md(year)