# -*- coding:utf-8 -*-
__author__ = 'haoxiang'

def Merge(alist,p,q,r):
#p是第一个序列的子长度，r是整个序列的长度
    left = alist[p:q+1]
    right = alist[q+1:r+1]
    print left
    print right
    i = 0
    j = 0
    for a in range(p,r+1):
        if len(left)>0 and len(right)>0:
         if left[i] <= right[j]:
            alist[a] = left[i]
            i = i +1
         elif left[i] >= right[j]:
             alist[a] = right[j]
             j = j+1

    for b in range(i,len(left)):
         alist.append(left[b])

    for c in range(j,len(right)):
        alist.append(left[c])

def MergeSort(alist,p,r):
    if p <r:
        q =(p+r)/2
        MergeSort(alist,p,q)
        MergeSort(alist,q+1,r)
        Merge(alist,p,q,r)

    return alist

test = [1,2,67,3,5,7,4,3,56,7,7,4,2,2,4,5,]
MergeSort(test,0,len(test))
