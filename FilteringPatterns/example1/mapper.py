#!/usr/bin/python


# We need to write them out to standard output, separated by a tab
import sys
import re
data=[]
end=0;
fileName=None
for line in sys.stdin:
    tmp= line.strip().replace('[','').replace("'",'',2).replace(']','').split()
    if len(tmp)==10:
       ip,identity,username,time,x,get,request,http,status,size = tmp
       requestStr=str(request)
       if  requestStr.find('http://www.the-associates.co.uk') != -1:
           end=len('http://www.the-associates.co.uk')
           fileName=requestStr[end:]
       else:
         fileName = requestStr[requestStr.index('/'):]

       print "{0}\t{1}".format(ip,fileName)





