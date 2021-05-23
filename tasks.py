import math
import numpy as np
import numpy.random as rand

def triangle(nums):
    if(len(nums)<3):
        return 0
    last = 2
    middle = 1
    first = 0
    num_last = len(nums)-1
    num_middle = num_last-1
    num_first = num_middle-1
    sum=0
    while first<=num_first:
        if nums[last]+nums[first]+nums[middle] > sum:
            if (nums[last]<nums[first]+nums[middle]) and (nums[first]<nums[last]+nums[middle]) and (nums[middle]<nums[last]+nums[first]):
                sum = nums[last]+nums[first]+nums[middle]
        if last<num_last:
            last+=1
        else:
            if middle<num_middle:
                middle+=1
                last=middle+1
            else:
                first+=1
    return sum

def maxnum(nums):
    strums = []
    for i in nums:
        strums.append(str(i))
    result = []
    startlen = len(strums)
    while len(result)<startlen:
        max='0'
        for i in strums:
            if len(i)<len(max):
                if int(max)<int(i)*10**(len(max)-len(i)):
                    max=i
            elif len(i)>len(max):
                if int(i)>int(max)*10**(len(i)-len(max)):
                    max=i
            else:
                if int(i)>int(max):
                    max=i
        result.append(max)
        strums.remove(max)
    resstr=''
    for i in result:
        resstr=resstr+i
    return resstr 

def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(nums) - 1):
            for j in range(len(nums[0]) - 1):
                if nums[i][j] > nums[i + 1][j + 1]:
                    # Меняем элементы
                    nums[i][j], nums[i + 1][j + 1] = nums[i + 1][j + 1], nums[i][j]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True
                    
n = rand.randint(1, 100)
m = rand.randint(1, 100)
min_lim = 1
max_lim = 100
matrix = rand.randint(min_lim, max_lim, (n, m))                    
print(triangle([2,3,2])
print(maxnum([2,3,2,1,5])
