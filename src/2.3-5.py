# -*- coding:utf-8 -*-
__author__ = 'haoxiang'

'''
默认序列从小到大排序好了
'''
def doubleSearch(A,n):

    i = 1
    j = len(A)
    while i<j :
        m = (i+j)/2;
        if A[m]==n:
            print(m)
            return m
        elif A[m]>n:
            j = m-1
        else:
            i = m+1
    return 0
test = [1,2,3,4,5,6,7,8,9]
doubleSearch(test,6)