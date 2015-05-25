# -*- coding:utf-8 -*-
__author__ = 'haoxiang'


'''
算法导论版本的快速排序
'''
def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        #改变 >= <=可以变化排序的升降
        if A[j] >= x:
            i +=1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]

    if i==r:
        return (p+r)/2
    else:
        return i+1


def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)
    print A

'''
容易理解的快速排序
'''

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


'''
测试
'''
test = [9,2,5,3,8,8,5,3,6,8,4,19,3]
#注意参数，第二个一定要从0开始
quickSort(test,0,len(test)-1)
# quick_sort(test,0,len(test)-1)
# print(test)