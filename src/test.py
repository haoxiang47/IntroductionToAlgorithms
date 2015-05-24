# -*- coding :utf-8 -*-
__author__ = 'haoxiang'
# def max_heap(A, i, heapsize):
#     largest = -1
#     while True:
#         left = 2*i+1
#         right = 2*i + 2
#         if left<heapsize and A[i]<A[left]:
#             largest=left
#         else:
#             largest=i
#         if right<heapsize and A[largest]<A[right]:
#             largest=right
#         if largest  is not i:
#             A[largest],A[i] = A[i],A[largest]
#             i=largest
#         else:
#             break
# def build_max_heap(A):
#     n = len(A)
#     for i in range(int(n/2)-1,-1,-1):
#         max_heap(A, i, n)
# def heap_sort(A):
#     build_max_heap(A)
#     n = len(A)
#     for i in range(n-1,-1,-1):
#         A[0],A[i]=A[i],A[0]
#         max_heap(A,0, i)
# A=[1,3,8,6,1,4,6,4,0]
# heap_sort(A)
# print A

class QueueElement:
    """
    Private class only for class QHeap. Suppling as a device to cobmine
    key and object together.
    """
    def __init__(self, obj, prio):
        self.key = prio
        self.obj = obj


class QHeap: # max heap
    """
    Private class
    Implement the basic data structure for Priority Queue.
    """
    def __init__(self, compare):
        self.HeapAry = [0]
        # method given by subclass. for config whether be a maxqueue or a minqueue.
        self.com = compare
    def EnQueue(self, obj, priority):
        self.HeapAry.append(QueueElement(obj, priority))
        i = self.QueueLen()
        while (i > 1) and self.com(self.HeapAry[i/2].key, self.HeapAry[i].key):
            self.HeapAry[i/2] ,self.HeapAry[i] = self.HeapAry[i] ,self.HeapAry[i/2]
        i = i/2

def __MakeHeapify(self, i):
    if i > self.QueueLen()/2:
        return
    max_idx = i
    # find out the maximun(or minmun, judged by self.com method) one in
    # parent,left and right node. Identify it be max_idx
    if self.com(self.HeapAry[max_idx].key, self.HeapAry[i*2].key):
        max_idx = i*2
    if i*2+1 <= self.QueueLen() and self.com(self.HeapAry[max_idx].key, self.HeapAry[i*2 + 1].key):
        max_idx = i*2 + 1
        # if the max_idx is not parent, exchange parent and max_idx element.
    if max_idx != i:
        self.HeapAry[max_idx] ,self.HeapAry[i] = self.HeapAry[i] ,self.HeapAry[max_idx]
    self.__MakeHeapify(i*2)

def DeQueue(self):
    head = self.HeapAry[1]
    last = self.HeapAry.pop()
    if (self.QueueLen() >= 1):
        self.HeapAry[1] = last
        self.__MakeHeapify(1)
    return head.obj

def QueueLen(self):
    return len(self.HeapAry) - 1
def Empty(self):
    return self.QueueLen() == 0

class MaxPrioQueue(QHeap):
    """
    Maximun priority queue.
    """
    def __init__(self):
        # max queue use x < y to judge the change node configration.
        self.com = lambda x, y: x < y
        self.HeapAry = []

class MinPrioQueue(QHeap):
    """
    Minmun priority queue.
    """
    def __init__(self):
        # max queue use x > y to judge the change node configration.
        self.com = lambda x, y: x > y
        self.HeapAry = []

    #-----------------------------------------------------------------
# for test only.

if __name__ == '__main__':
    h = MaxPrioQueue()
    chars = ['L', 'i', 'Y', 'i', 'W', 'e', 'n']
    keys  = [ 8 ,  4 ,  6 ,  3 ,  10,  9 ,  5 ]
    for i in range(0, len(chars)):
        h.EnQueue(chars[i], keys[i])
    result = []
    while not h.Empty():
        result.append(h.DeQueue())
    print "length of result is %d:" % len(result)
    print "".join(result)

    h = MinPrioQueue()
    for i in range(0, len(chars)):
        h.EnQueue(chars[i], keys[i])
    result = []
    while not h.Empty():
        result.append(h.DeQueue())
    print "length of result is %d:" % len(result)
    print "".join(result)