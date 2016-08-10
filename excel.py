#coding:utf-8
import jieba
import nltk
from xlwt import *
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
list = []
with open('h://bigdata/data/gy58A.txt','r') as f:    #打开文本B
    lines = f.readlines()
    for x in lines:
        list.append(x)
        f.close()
jobs = nltk.FreqDist(list)
w =Workbook(encoding='utf-8')
ws = w.add_sheet(u'贵阳58招聘词频统计')
i = 1
default = easyxf('font: name Arial;') # define style out the loop will work
for x in jobs:
    i = i + 1
    print jobs[x]
    ws.write(i,0, x,default)
    ws.write(i,1,jobs[x],default)
    ws.row(i).set_style(default)
    print x
    w.save('h://bigdata/data/58.xls')
