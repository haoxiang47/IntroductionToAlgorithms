# -*- coding: utf-8 -*-
__author__ = 'haoxiang'


def minHeapify(A,i):
    smallest = i
    left = 2*i
    right = 2*i+1
    if left<= i and A[left]<A[smallest]:
        smallest = left
    if right<=i and A[right]<A[smallest]:
        smallest = right
    if smallest!=i:
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        minHeapify(A,smallest)
    print(A)
def maxHeapify(A,i):
    largest = i
    left = 2*i
    right = 2*i+1
    if i >= left and A[left] > A[largest]:
        largest = left
    if i >= right and A[right] > A[largest]:
        largest = right
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A,largest)
    print(A)
test = [1,3,6,3,5,7,9,4,2,5,3,6,4,]
maxHeapify(test,8)
# minHeapify(test,4)