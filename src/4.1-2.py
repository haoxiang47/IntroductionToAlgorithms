__author__ = 'haoxiang'

#  -*- coding: utf-8 -*-

def findMaxSubarray(array,low,mid,high):

    lowSum = 0
    highSum = 0
    minLow = -9999
    minHigh = -9999
    maxMid = 0
    maxHigh = 0
    for i in range(mid,low,-1):
        lowSum += array[i]
        if lowSum>minLow:
            minLow = lowSum
            maxMid = i
    for j in range(mid,high):
        highSum += array[j]
        if highSum > minHigh:
            minHigh = highSum
            maxHigh = j
    print str(maxMid)+"---"+str(maxHigh)

Array = [12,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print len(Array)
findMaxSubarray(Array,0,len(Array)/2,len(Array)-1)