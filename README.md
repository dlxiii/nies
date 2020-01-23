# Data from National Institute for Environmental Studies

Data from: https://www.nies.go.jp/igreen/index.html

Downloader: Yulong

## (Update: 20181016)

Public water data station in Chiba, Tokyo and Kanagawa are listed in the map respectlly.

* https://www.nies.go.jp/igreen/water/map/map12_w.jpg

* https://www.nies.go.jp/igreen/water/map/map13_w.jpg

* https://www.nies.go.jp/igreen/water/map/map14_w.jpg

They are also downloaded, with name of map12_w.jpg map13_w.jpg and map14_w.jpg

Currently, the lon. and lat. are not known, it is better to find their location.

There are 3 manual avaliable.
*   MD means "公共用水域水質年間値データ(Kōkyōyōsuiiki suishitsu nenkan-chi dēta)(Annual water quality data for public water bodies)" https://www.nies.go.jp/igreen/manual/MD_manu.pdf

*   MK means "公共用水域水質検体値データ(Kōkyōyōsuiiki suishitsu kentai-chi dēta)(Public water body water quality sample value data)" https://www.nies.go.jp/igreen/manual/MK_manu.pdf

*   MM means "公共用水域水質測定点データ(Kōkyōyōsuiiki suishitsu sokutei-ten dēta)(Public water body water quality measurement point data)" https://www.nies.go.jp/igreen/manual/MM_manu.pdf

So more data will be downloaded in those three folders.

## (Update: 20181019)

Data in each folder is downloaded and then orgnized. (in "MD/outputs","MD/outputs"and"MM/jp/outputs").

## (Update: 20200123)

* MD/MD.py: read MD********_0.txt, convert to csv and tkb files in MD/optputs

* MK/MK.py: read MK********_0.txt, convert to csv and tkb files in MK/optputs

* MM/jp/MK.py: read MM********_0.txt, convert to csv and tkb files in MK/jp/optputs

* scr/merge_mm_mk_md.py: read above tkb files, merge them in outputs/mk and outputs/md

* scr/tkb.py: merge files in outputs/mk for tokyo bay area in outputs/tkb

* scr/tkb_plot.py: plot station map and station water variables