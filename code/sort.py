# -*- coding: utf-8 -*-
# @Time    : 19-6-22 下午7:49
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : sort.py
# @Software: PyCharm

def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return  nums

def selectSort(nums):
    for i in range(len(nums)-1):
        min = i
        for j in range(i,len(nums)):
            if nums[j] < nums[i]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]
    return  nums

def insertSort(nums):
    for i in range(1,len(nums)):
        j = i-1
        key = nums[i]
        while j >= 0:
            if nums[j] > key:
                nums[j+1] = nums[j]
                nums[j] = key
            j -= 1
    return nums



nums = [5,4,2,3,1]
print(bubbleSort(nums))
print(selectSort(nums))
print(insertSort(nums))

