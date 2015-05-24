# -*- coding:utf-8 -*-
__author__ = 'haoxiang'

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i +=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    print A

test = [1,2,5,3,8,8,5,3,6,8,4,19,384]
quickSort(test,1,len(test)-1)