# -*- coding: utf-8 -*-
__author__ = 'haoxiang'

def selectionSort(list):
    lens = len(list)
    #只要对n-1和元素运行
    for i in range(0,lens-2):
        small = list[i]
        for j in range(i,lens-1):
            if list[j] < small:
                small = list[j]
            localtion = small
        list[i] = localtion
    print list

test = [1,3,2,5,6,4,3,6,8]
selectionSort(test)