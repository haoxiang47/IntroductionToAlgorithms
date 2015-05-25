# -*- coding: utf-8 -*-
__author__ = 'haoxiang'

def countSort(A,B,k):
    C=[]
    for i in range(0,k):
        C.append(0)
    for j in range(0,len(A)):
        C[A[j]] = C[A[j]] + 1
    for k in range(1,k):
        C[i] = C[i] + C[i-1]
    for l in range(len(A),0,-1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    print(B)

test = [1,3,2,5,7]
B = []
countSort(test,B,100)