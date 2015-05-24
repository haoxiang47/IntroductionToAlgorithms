# -*- coding: utf-8 -*-
__author__ = 'haoxiang'

def maxHeapify(A,i,length):
    largest = -1
    left = 2*i
    right = 2*i+1
    if length > left and A[left] > A[i]:
        largest = left
    else :
        largest = i
    if length > right and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(A,largest,length)
    return A

def heapMaximun(A):
    return A[0]

def heapExtractMax(A):
    if len(A) < 1:
        return
    max = A[0]
    A[0] = A[len(A)-1]
    lens = len(A)-1
    maxHeapify(A,0,lens)
    print max
def heapIncreaseKey(A,i,key):
    if key < A[i]:
        print 'new key is smaller'
    A[i] = key
    while i > 1 and A[i/2] <A[i]:
        A[i],A[i/2] = A[i/2],A[i]
        i = i/2
def maxHeapInsert(A,key):
    lens = len(A)+1
    A[len(A)] = -999999
    heapIncreaseKey(A,lens-1,key)


test = [44,2,5,78,3,2,4,6]
heapExtractMax(test)