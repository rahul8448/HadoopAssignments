#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
oldStoreName=None
highestSale=float("-inf")
currentHighestSale=0
totalNumberOfSales=0
totalSales=0
dict = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey,thisStore,thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print 'SalesTotal:',"\t",oldKey,"\t",salesTotal
        salesTotal = 0

    oldKey = thisKey
    oldStoreName=str(thisStore)
    salesTotal += float(thisSale)
    totalNumberOfSales+=1
    totalSales+=float(thisSale)
    currentHighestSale=float(thisSale)

    if dict.get(oldStoreName):
        highestVal=dict[oldStoreName]
        if highestVal<currentHighestSale:
            dict[oldStoreName]=currentHighestSale
    else:
        dict[oldStoreName]=currentHighestSale


if oldKey != None:
    print 'SalesTotal:', "\t", oldKey, "\t", salesTotal

#Prints the highest value for each store.
for i in dict:
    print i, dict[i]

print 'TotalSales:'+ str(totalSales)
print 'TotalNumberOfSales:' + str(totalNumberOfSales)



