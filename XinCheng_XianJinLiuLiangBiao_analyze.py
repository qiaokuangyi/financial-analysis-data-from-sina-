# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:02:41 2018

@author: Administrator
"""

from numpy import *
import operator

"""
##################### 来自利润表的内容####
"""

file_FenZhong_LiRun_sheet                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_利润表.txt' #   only  can analyze txt ;
## 注意：  利润表中 净利润 数据有问题，季度数据及半年数据均为0，需要修改；
#######################################################################
fr = open(file_FenZhong_LiRun_sheet)
#######################################################################

arrayOfLines_lr = fr.readlines()
numOfLines = len(arrayOfLines_lr)  # 得到共计多少行信息；

dateLine = arrayOfLines_lr[0]
dateLineTrip = dateLine.strip()
dateFormLine = dateLineTrip.split('\t')
## 仅获取自 20131231 及其以后的数据，之前的不要；
dateEnd = '20131231'  
for i in  range(len(dateFormLine)):   
    if dateFormLine[i] == dateEnd :
        NColumn = i
        break
    
## get data from balance datasheet.
labelName_lr = []
returnMat_lr = []
returnMat_lr = zeros((numOfLines,NColumn))    # 创建返回的矩阵形态，这里仍为数组Array格式；
index = 0
for line in arrayOfLines_lr:
    lineTrip = line.strip()
    listFormLine = lineTrip.split('\t')
    if  (len(listFormLine) == 1):
        returnMat_lr[index,:] = zeros(NColumn)
    elif (listFormLine[1] != '元'):
        returnMat_lr[index,:] = listFormLine[1:NColumn+1] # list 一般到 N-1；
    else:
        returnMat_lr[index,:] = zeros(NColumn)
    index = index + 1
    labelName_lr.append( listFormLine[0] )
# 以上合计共计31行,也即 元素 0-30；
"""
##################### 来自利润表的内容到此结束####
"""

"""
#################### 以下为现金流量表的内容
"""


file_FenZhong_XianJin_sheet                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_现金流量表.txt' #   only  can analyze txt ;
#######################################################################
file_FenZhong_XianJin_sheet_py                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_现金流量表_py.txt' #
    #######################################################################
    
fr = open(file_FenZhong_XianJin_sheet)
arrayOfLines = fr.readlines()
numOfLines = len(arrayOfLines)  # 得到共计多少行信息；

dateLine = arrayOfLines[0]
dateLineTrip = dateLine.strip()
dateFormLine = dateLineTrip.split('\t')

## dateEnd = '20131231'    # use above 
#######################################################################
for i in  range(len(dateFormLine)):   
    if dateFormLine[i] == dateEnd :
        NColumn = i
        break
    

labelName_xj = []
returnMat_xj = []
returnMat_xj = zeros((numOfLines,NColumn))    # 创建返回的矩阵形态，这里仍为数组Array格式；
index = 0
for line in arrayOfLines:
    lineTrip = line.strip()
    listFormLine = lineTrip.split('\t')
    if  (len(listFormLine) == 1):
        returnMat_xj[index,:] = zeros(NColumn)
    elif (listFormLine[1] != '元'):
        returnMat_xj[index,:] = listFormLine[1:NColumn+1] # list 一般到 N-1；
    else:
        returnMat_xj[index,:] = zeros(NColumn)
    index = index + 1
    labelName_xj.append( listFormLine[0] )
    
returnMat_xj[44,:] = returnMat_lr[21,:]

labelNameAdd_xj = []
writeData_xj = []


# group 1
labelNameAdd_xj.append( '' )
labelNameAdd_xj.append( '自由现金流量（经营-购建）' )
labelNameAdd_xj.append( '经营活动现金流' )
labelNameAdd_xj.append( '净利润' )
labelNameAdd_xj.append( '购建固定资产付出资金' )
labelNameAdd_xj.append( '' )

dateOfYearMonDay = returnMat_xj[0,:]  # set the data..
ziYouXianJin = returnMat_xj[12,:] - returnMat_xj[20,:]
jingYingXianJin = returnMat_xj[12,:]
jingLiRun = returnMat_xj[44,:]
gouJianZhiChu = returnMat_xj[20,:]
tianChong = zeros(len(returnMat_xj[0,:]))  # tian chong all zeros.

writeData_xj.append( dateOfYearMonDay.tolist() )
writeData_xj.append( ziYouXianJin.tolist() )
writeData_xj.append( jingYingXianJin.tolist() )
writeData_xj.append( jingLiRun.tolist() )
writeData_xj.append( gouJianZhiChu.tolist() )
writeData_xj.append( tianChong.tolist() )

# group 2
## 营业成本、销售费用、管理费用占比；
labelNameAdd_xj.append( '' )
labelNameAdd_xj.append( '经营现金流量/净利润' )
labelNameAdd_xj.append( '自由现金流量/净利润' )
labelNameAdd_xj.append( '' )

dateOfYearMonDay = returnMat_xj[0,:]  # set the data..
jingYing_jingLiRun_Pct = returnMat_xj[12,:]/returnMat_xj[44,:]
ziYou_jingLiRun_Pct = ziYouXianJin/returnMat_xj[44,:]
tianChong = zeros(len(returnMat_xj[0,:]))  # tian chong all zeros.

writeData_xj.append( dateOfYearMonDay.tolist() )
writeData_xj.append( jingYing_jingLiRun_Pct.tolist() )
writeData_xj.append( ziYou_jingLiRun_Pct.tolist() )
writeData_xj.append( tianChong.tolist() )

    
### 写数据到txt文件中：
fr_w = open(file_FenZhong_XianJin_sheet_py,'w')  ## 写操作；

returnMatToList_xj = []
for k in list(range(len(returnMat_xj))):
    returnMatToList_xj.append(list(returnMat_xj[k]))
    
writeStrRetData = []
for i in list(range(len(returnMat_xj))):
    writeStrRetData.append('\t'.join(map(str, returnMatToList_xj[i] )))
    fr_w.write(labelName_xj[i])
    fr_w.write('\t')
    fr_w.write(writeStrRetData[i])
    fr_w.write('\n')


writeStr_xj = []

## # 与正常data流出来空白。
fr_w.write('\n')
fr_w.write('\n')

for i in (range(len(writeData_xj))):
    writeStr_xj.append('\t'.join(map(str, writeData_xj[i] )))
    fr_w.write(labelNameAdd_xj[i])
    fr_w.write('\t')
    fr_w.write(writeStr_xj[i])
    fr_w.write('\n')
fr_w.close()



