# -*- coding:utf-8 -*-
__author__ = 'haoxiang'

def InsertRecurison(list,q):

    if q>0 :
        InsertRecurison(list,q-1)
        Insert(list,q)

def Insert(A,q):

    key = A[q+1]
    j=q
    while j>0 and A[j]>key:
        A[j+1]=A[j]
        j= j-1
    A[j+1]=key


