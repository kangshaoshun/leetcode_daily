#coding:utf-8
#########################################################################
# File Name: 922.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 09时35分08秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def sort_array(nums):
    res = []
    i, j = 0, 0
    while i < len(nums) and j < len(nums):
        while i < len(nums) and (nums[i] & 1) == 1:
            i += 1
        if i < len(nums):
            res.append(nums[i])
        i += 1
        while j < len(nums) and nums[j] & 1 == 0:
            j += 1
        if j < len(nums):
            res.append(nums[j])
        j += 1
    return res

print sort_array([4, 2, 5, 7])
print sort_array([4, 2, 5, 7, 3, 6])
print sort_array([4, 3])
