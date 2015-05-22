#-*- coding:utf-8 -*-
__author__ = 'haoxiang'

def bubble_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return sort_list
    for i in range(iter_len-1):
        for j in range(iter_len-i-1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list

def find(S,x):
    bubble_sort(S)
    lens = len(S)
    i = 1
    j = lens-1
    while i<j:
        if S[i]+S[j] < x:
            i+=1
        if S[i]+S[j] > x:
            j-=1
        if S[i]+S[j] == x:
            print(S[i],S[j])
            i+=1
            j-=1


test = [1,2,3,4,3,6,2,4,7,9,3,1,5,7,8,9]
find(test,10)


