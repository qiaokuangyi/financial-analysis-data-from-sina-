# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 22:42:32 2018

@author: Administrator
"""

from numpy import *
import operator

# there is the path need to be replaced, if you analyze other company.
# there are above ########
# dataend is used to make sure the data of the begin year.like 20151231..

file_FenZhong_LiRun_sheet                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_利润表.txt' #   only 
    ##################################################################
## 注意：  利润表中 净利润 数据有问题，季度数据及半年数据均为0，需要修改；
file_FenZhong_LiRun_sheet_py                =\
    r'E:\00_乔旷怡_CW学习\02-房地产行业\房地产--新城\新城控股(601155)_利润表_py.txt' 
##################################################################
fr = open(file_FenZhong_LiRun_sheet)
##################################################################
arrayOfLines_lr = fr.readlines()
numOfLines = len(arrayOfLines_lr)  # 得到共计多少行信息；

dateLine = arrayOfLines_lr[0]
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
### 以上为原始数据
    
labelNameAdd_lr = []
writeData_lr = []

## 首先分析营业收入，营业成本，营业利润，净利润的曲线；
# fist add name, second add data, third change them to string
labelNameAdd_lr.append( '' )# set the data..
labelNameAdd_lr.append( '营业收入' )
labelNameAdd_lr.append( '营业成本' )
labelNameAdd_lr.append( '营业利润' )
labelNameAdd_lr.append( '净利润' )
labelNameAdd_lr.append( '' ) # 填充全零...

dateOfYearMonDay = returnMat_lr[0,:]  # set the data..
yingYeShouRu = returnMat_lr[3,:]
yingYeChengBen = returnMat_lr[5,:]
yingYeLiRun = returnMat_lr[15,:]
jingLiRun = returnMat_lr[21,:]
tianChong = zeros(len(returnMat_lr[21,:]))  # tian chong all zeros.

writeData_lr.append( dateOfYearMonDay.tolist() )
writeData_lr.append( yingYeShouRu.tolist() )
writeData_lr.append( yingYeChengBen.tolist() )
writeData_lr.append( yingYeLiRun.tolist() )
writeData_lr.append( jingLiRun.tolist() )
writeData_lr.append( tianChong.tolist() )

## 营业成本、销售费用、管理费用占比；
labelNameAdd_lr.append( '' )# set the data..
labelNameAdd_lr.append( '营业成本比例' )
labelNameAdd_lr.append( '销售费用比例' )
labelNameAdd_lr.append( '管理费用比例' )
labelNameAdd_lr.append( '' ) # 填充全零...

dateOfYearMonDay = returnMat_lr[0,:]  # set the data..
yingYeChengBenPct = returnMat_lr[5,:]/returnMat_lr[2,:]
XiaoShouFeiYongPct = returnMat_lr[7,:]/returnMat_lr[2,:]
GuanLiFeiYongPct = returnMat_lr[8,:]/returnMat_lr[2,:]

writeData_lr.append( dateOfYearMonDay.tolist() )
writeData_lr.append( yingYeChengBenPct.tolist() )
writeData_lr.append( XiaoShouFeiYongPct.tolist() )
writeData_lr.append( GuanLiFeiYongPct.tolist() )
writeData_lr.append( tianChong.tolist() )

labelNameAdd_lr.append( '' )# set the data..
labelNameAdd_lr.append( '毛利润率' )
labelNameAdd_lr.append( '营业利润率' )
labelNameAdd_lr.append( '净利润率' )

dateOfYearMonDay = returnMat_lr[0,:]  # set the data..
maoLiRunPct = (returnMat_lr[3,:] - returnMat_lr[5,:])/returnMat_lr[3,:]
yingYeLiRunPct = returnMat_lr[15,:]/returnMat_lr[3,:]
jingLiRunPct = returnMat_lr[21,:]/returnMat_lr[3,:]


writeData_lr.append( dateOfYearMonDay.tolist() )
writeData_lr.append( maoLiRunPct.tolist() )
writeData_lr.append( yingYeLiRunPct.tolist() )
writeData_lr.append( jingLiRunPct.tolist() )
writeData_lr.append( tianChong.tolist() )

labelNameAdd_lr.append( '' )# set the data..
labelNameAdd_lr.append( '营业收入翻倍' )
labelNameAdd_lr.append( '净利润翻倍' )
labelNameAdd_lr.append( '' ) # 填充全零...

dateOfYearMonDay = returnMat_lr[0,:]  # set the data..
yingYeShouRuFanBei = returnMat_lr[2,:]/returnMat_lr[2,-1]
jingLiRunFanBei =  returnMat_lr[21,:]/returnMat_lr[21,-1]


writeData_lr.append( dateOfYearMonDay.tolist() )
writeData_lr.append( yingYeShouRuFanBei.tolist() )
writeData_lr.append( jingLiRunFanBei.tolist() )
writeData_lr.append( tianChong.tolist() )
   
### 写数据到txt文件中：
fr_w = open(file_FenZhong_LiRun_sheet_py,'w')  ## 写操作；
##################################################################

returnMatToList_lr = []
for k in list(range(len(returnMat_lr))):
    returnMatToList_lr.append(list(returnMat_lr[k]))
    
writeStrRetData = []
for i in list(range(len(returnMat_lr))):
    writeStrRetData.append('\t'.join(map(str, returnMatToList_lr[i] )))
    fr_w.write(labelName_lr[i])
    fr_w.write('\t')
    fr_w.write(writeStrRetData[i])
    fr_w.write('\n')
####以上为数据格式转换。。。

writeStr_lr = []

# 与正常data流出来空白。
fr_w.write('\n')
fr_w.write('\n')

for i in list(range(len(writeData_lr))):
    writeStr_lr.append('\t'.join(map(str, writeData_lr[i] )))
    fr_w.write(labelNameAdd_lr[i])
    fr_w.write('\t')
    fr_w.write(writeStr_lr[i])
    fr_w.write('\n')
fr_w.close()

### 以上为写数据到txt中。


