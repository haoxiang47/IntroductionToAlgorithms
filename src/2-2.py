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