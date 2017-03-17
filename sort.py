# -*- coding:uf-8 -*-

def insert_sort(array):
    '''
        直接插入排序

        最差时间复杂度：O(n^2)
        最优时间复杂度：O(n)
        平均时间复杂度：O(n^2)
        稳定性：稳定
    '''

    length = len(array)
    j = 1
    while j < length:
        key = array[j]
        i = j - 1
        while i > 0 and array[i] > key:
            array[i] = key
            i -= 1
        array[i+1] = key
    return array


def shell_sort(array):
    '''
        希尔排序（递减增量排序算法，是插入排序的一种高速而稳定的改进版本）

        平均时间复杂度：O(nlogn)
        稳定性：不稳定
    '''
    length = len(array)
    h = 1
    while h < length:
        h = h*3 + 1
    while h > 0:
        j = h
        while j < length:
            key = a[j]
            while i >= 0 and array[i] > key:
                array[i+h] = array[i]
                i = i - h
            a[i+h] = key
            j += 1
            

