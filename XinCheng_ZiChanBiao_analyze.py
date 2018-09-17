# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 23:11:04 2018

@author: Administrator
"""

from numpy import *
import operator


file_FenZhong_ZiChan_sheet                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_资产负债表.txt' #   only 
    ##################################################################can analyze txt ;
## 注意：  利润表中 净利润 数据有问题，季度数据及半年数据均为0，需要修改；
file_FenZhong_ZiChan_sheet_py                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_资产负债表_py.txt' 
##################################################################
fr = open(file_FenZhong_ZiChan_sheet)
##################################################################
arrayOfLines_zc = fr.readlines()
numOfLines = len(arrayOfLines_zc)  # 得到共计多少行信息；

dateLine = arrayOfLines_zc[0]
dateLineTrip = dateLine.strip()
dateFormLine = dateLineTrip.split('\t')
## 仅获取自 20131231 及其以后的数据，之前的不要；
dateEnd = '20131231'  
##################################################################
for i in  range(len(dateFormLine)):   
    if dateFormLine[i] == dateEnd :
        NColumn = i
        break
    
## get data from balance datasheet.
labelName_zc = []
returnMat_zc = []
returnMat_zc = zeros((numOfLines,NColumn))    # 创建返回的矩阵形态，这里仍为数组Array格式；
index = 0
for line in arrayOfLines_zc:
    lineTrip = line.strip()
    listFormLine = lineTrip.split('\t')
    if  (len(listFormLine) == 1):
        returnMat_zc[index,:] = zeros(NColumn)
    elif (listFormLine[1] != '元'):
        returnMat_zc[index,:] = listFormLine[1:NColumn+1] # list 一般到 N-1；
    else:
        returnMat_zc[index,:] = zeros(NColumn)
    index = index + 1
    labelName_zc.append( listFormLine[0] )

returnMat_zc[47,:] = returnMat_zc[59,:] - returnMat_zc[43,:] - returnMat_zc[44,:] -\
            returnMat_zc[45,:] - returnMat_zc[46,:] - returnMat_zc[48,:] - returnMat_zc[53,:] -\
            returnMat_zc[49,:] - returnMat_zc[50,:] - returnMat_zc[51,:] - returnMat_zc[52,:] -\
            returnMat_zc[54,:] - returnMat_zc[55,:] - returnMat_zc[56,:] - returnMat_zc[57,:] -\
            returnMat_zc[58,:] 

############
labelNameAdd_zc = []
writeData_zc = []

###  group1
labelNameAdd_zc.append( '' )
labelNameAdd_zc.append( '所有者权益翻倍' )
labelNameAdd_zc.append( '总资产翻倍' )
labelNameAdd_zc.append( '' )

dateOfYearMonDay = returnMat_zc[0,:]  # set the data..
suoYouZheQuanYiFanBei = returnMat_zc[83,:]/returnMat_zc[83,-1]
zongZiChanFanBei =  returnMat_zc[84,:]/returnMat_zc[84,-1]
tianchong = zeros(len( returnMat_zc[84,:]) )

writeData_zc.append( dateOfYearMonDay.tolist() )
writeData_zc.append( suoYouZheQuanYiFanBei.tolist() )
writeData_zc.append( zongZiChanFanBei.tolist() )
writeData_zc.append( tianchong.tolist() )

###  group2
labelNameAdd_zc.append( '' )
labelNameAdd_zc.append( '现金类资产' )
labelNameAdd_zc.append( '应收账款' )
labelNameAdd_zc.append( '投资账款' )
labelNameAdd_zc.append( '经营资产' )
labelNameAdd_zc.append( '' )

dateOfYearMonDay = returnMat_zc[0,:]  # set the data..
              #  =B4+B5+B6+B7 + B19+B39+B40
XianJin = returnMat_zc[3,:]+returnMat_zc[4,:]+\
                    returnMat_zc[5,:]+returnMat_zc[6,:]+\
                    returnMat_zc[18,:]+returnMat_zc[38,:]+returnMat_zc[39,:]
          #=B8+B9+B10+B11+B12 +B25
YingShouKuan =  returnMat_zc[7,:]+returnMat_zc[8,:]+\
                    returnMat_zc[9,:]+returnMat_zc[10,:]+\
                    returnMat_zc[11,:]+returnMat_zc[24,:]
                    #=B13+B15 +B23+B24+ B26+B27
TouZiKuan    = returnMat_zc[12,:]+returnMat_zc[14,:]+\
                    returnMat_zc[22,:]+returnMat_zc[23,:]+\
                    returnMat_zc[25,:]+returnMat_zc[26,:]
          # =B14 +B16+B17+B18 +B28+B29+B30+B31+B32+B33+B34+B35+B36+B37+B38+  +B22
JingYingZiChan = returnMat_zc[13,:]+returnMat_zc[15,:]+\
                    returnMat_zc[16,:]+returnMat_zc[17,:]+\
                    returnMat_zc[27,:]+returnMat_zc[28,:]+returnMat_zc[29,:]+returnMat_zc[30,:]+\
                    returnMat_zc[31,:]+returnMat_zc[32,:]+returnMat_zc[33,:]+returnMat_zc[34,:]+\
                    returnMat_zc[35,:]+returnMat_zc[36,:]+returnMat_zc[37,:]+returnMat_zc[21,:]

writeData_zc.append( dateOfYearMonDay.tolist() )
writeData_zc.append( XianJin.tolist() )
writeData_zc.append( YingShouKuan.tolist() )
writeData_zc.append( TouZiKuan.tolist() )
writeData_zc.append( JingYingZiChan.tolist() )
writeData_zc.append( tianchong.tolist() )

# group3
labelNameAdd_zc.append( '' )
labelNameAdd_zc.append( '有息负债' )
labelNameAdd_zc.append( '经营负债' )
labelNameAdd_zc.append( '' )

dateOfYearMonDay = returnMat_zc[0,:]  # set the data..
        # =B44+B62
YouXiFuZhai =  returnMat_zc[43,:]+returnMat_zc[61,:]
      ##  =SUM(B47:B54)+SUM(B65:B69)
JingYingFuZhai = returnMat_zc[46,:]+returnMat_zc[47,:]+returnMat_zc[48,:]+returnMat_zc[49,:]+\
                    returnMat_zc[50,:]+returnMat_zc[51,:]+returnMat_zc[52,:]+returnMat_zc[53,:]+\
                    returnMat_zc[64,:]+returnMat_zc[65,:]+returnMat_zc[66,:]+returnMat_zc[67,:]+\
                    returnMat_zc[68,:]

writeData_zc.append( dateOfYearMonDay.tolist() )
writeData_zc.append( YouXiFuZhai.tolist() )
writeData_zc.append( JingYingFuZhai.tolist() )
writeData_zc.append( tianchong.tolist() )


# group4 
labelNameAdd_zc.append( '' )
labelNameAdd_zc.append( '现金+应收款 占比' )
labelNameAdd_zc.append( '现金占比' )
labelNameAdd_zc.append( '应收款占比' )
labelNameAdd_zc.append( '投资款占比' )
labelNameAdd_zc.append( '经营资产占比' )
labelNameAdd_zc.append( '' )

Xianjin_YingShou_Sum_Pct = (XianJin + YingShouKuan)/returnMat_zc[84,:]
XianJinPct = XianJin/returnMat_zc[84,:]
YingShouKuanPct = YingShouKuan/returnMat_zc[84,:]
TouZiKuanPct = TouZiKuan/returnMat_zc[84,:]
JingYingZiChanPct = JingYingZiChan/returnMat_zc[84,:]

writeData_zc.append( dateOfYearMonDay.tolist() )
writeData_zc.append( Xianjin_YingShou_Sum_Pct.tolist() )
writeData_zc.append( XianJinPct.tolist() )
writeData_zc.append( YingShouKuanPct.tolist() )
writeData_zc.append( TouZiKuanPct.tolist() )
writeData_zc.append( JingYingZiChanPct.tolist() )
writeData_zc.append( tianchong.tolist() )

## group5
labelNameAdd_zc.append( '' )
labelNameAdd_zc.append( '有息负债占比' )
labelNameAdd_zc.append( '经营负债占比' )
labelNameAdd_zc.append( '' )


YouXiFuZhaiPct =YouXiFuZhai/returnMat_zc[84,:]
JingYingFuZhaiPct = JingYingFuZhai/returnMat_zc[84,:]

writeData_zc.append( dateOfYearMonDay.tolist() )
writeData_zc.append( YouXiFuZhaiPct.tolist() )
writeData_zc.append( JingYingFuZhaiPct.tolist() )
writeData_zc.append( tianchong.tolist() )

   
### 写数据到txt文件中：
fr_w = open(file_FenZhong_ZiChan_sheet_py,'w')  ## 写操作；
##################################################################

returnMatToList_zc = []
for k in list(range(len(returnMat_zc))):
    returnMatToList_zc.append(list(returnMat_zc[k]))
    
writeStrRetData = []
for i in list(range(len(returnMat_zc))):
    writeStrRetData.append('\t'.join(map(str, returnMatToList_zc[i] )))
    fr_w.write(labelName_zc[i])
    fr_w.write('\t')
    fr_w.write(writeStrRetData[i])
    fr_w.write('\n')


writeStr_zc = []

# 与正常data流出来空白。
fr_w.write('\n')
fr_w.write('\n')

for i in list(range(len(writeData_zc))):
    writeStr_zc.append('\t'.join(map(str, writeData_zc[i] )))
    fr_w.write(labelNameAdd_zc[i])
    fr_w.write('\t')
    fr_w.write(writeStr_zc[i])
    fr_w.write('\n')
fr_w.close()



