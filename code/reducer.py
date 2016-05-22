#!/usr/bin/python

import sys


dict = {}
dict1={}
topHitCount=0;
fileWithMaxCount=None

# Loop around the data
# It will be in the format key\tval
# Where key is the IP name, val is the hitCount

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisIP,thisFileName = data_mapped

    ip=str(thisIP).strip();
    fileName=str(thisFileName).strip()

    if dict.get(fileName):
        highestVal=dict[fileName]
        dict[fileName]=highestVal+1
    else:
        dict[fileName]=1

    if dict[fileName]>topHitCount:
        topHitCount=dict[fileName]
        fileWithMaxCount=fileName

    if dict1.get(ip):
        tmp=dict1[ip]
        dict1[ip] = tmp + 1
    else:
        dict1[ip] = 1


print '**************************************'
if dict.get('/assets/js/the-associates.js'):
    print 'the-associates.js:' +  str(dict['/assets/js/the-associates.js'])
if dict1.get('10.99.99.186'):
    print '10.99.99.186:' +  str(dict1['10.99.99.186'])
print fileWithMaxCount + ':'+ str(topHitCount)





