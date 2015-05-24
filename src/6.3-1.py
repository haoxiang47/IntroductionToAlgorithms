# -*- coding:utf-8 -*-
__author__ = 'haoxiang'

def minHeapify(A,length,i):
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
    return (A)

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

def buildMinHeap(A):
    size = len(A)
    for i in range(size/2,1,-1):
        minHeapify(A,i)
    return A
def buildMaxHeap(A):
    n = len(A)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1):
        maxHeapify(A,start,n)
    return A

def heapSort(A):
    buildMaxHeap(A)
    lens = len(A)
    for i in range(lens-1,-1,-1):
        A[i],A[0] = A[0],A[i]
        maxHeapify(A,0,i)
    print A



def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    print ary

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break
test = [1,3,2,4,8,5,9,36]
# buildMinHeap(test)
# buildMaxHeap(test)
# heapSort(test)
heapSort(test)