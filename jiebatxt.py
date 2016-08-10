#coding:utf-8
import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
list = []
with open('h://bigdata/data/gy58A.txt','r') as f:    #打开结巴分好的词文本A
    lines = f.readlines()
    for x in lines:
        list.append(x)    #添加到列表
        f.close()    #关闭文本A

jobs = nltk.FreqDist(list)    #去重 + 词频统计
for job in jobs:
    print u'writting', job, jobs[job]
    with open('h://bigdata/data/gy58B.txt','a+') as w:
        w.write(job+ str(jobs[job]) + '\n')    #写入文本B
        #w.write('\n')
        w.close()    #关闭文本B