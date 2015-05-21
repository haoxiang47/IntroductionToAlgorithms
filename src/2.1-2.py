__author__ = 'haoxiang'


def InsertSort(list):

    lens = len(list)
    for i in range(1,lens):
        key = list[i]
        j = i-1
        while j>=0 and list[j]<key:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = key
    print(list)
test = [1,2,4,7,9,3,2,6,9]
InsertSort(test)