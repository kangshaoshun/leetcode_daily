#coding:utf-8
#########################################################################
# File Name: 923.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 09时54分37秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_ans(nums, target):
    cnt_dict = {}
    digits = []
    for val in nums:
        if val not in cnt_dict:
            cnt_dict[val] = 1
            digits.append(val)
        else:
            cnt_dict[val] += 1
    res = 0
    for i in range(len(digits) - 2):
        for j in range(i + 1, len(digits) - 1):
            for k in range(j + 1, len(digits)):
                if digits[i] + digits[j] + digits[k] == target:
                    res += (cnt_dict[digits[i]] * cnt_dict[digits[j]] * cnt_dict[digits[k]])
    for i in range(len(digits) - 1):
        if cnt_dict[digits[i]] < 2:
            continue
        for j in range(i + 1, len(digits)):
            if 2 * digits[i] + digits[j] == target:
                res += (cnt_dict[digits[i]] * (cnt_dict[digits[i]] - 1) / 2) * cnt_dict[digits[j]]
    for i in range(len(digits) - 1):
        for j in range(i + 1, len(digits)):
            if cnt_dict[digits[j]] < 2:
                continue
            if digits[i] + digits[j] * 2 == target:
                res += cnt_dict[digits[i]] * (cnt_dict[digits[j]] * (cnt_dict[digits[j]] - 1) / 2)
    for i in range(len(digits)):
        if cnt_dict[digits[i]] < 3:
            continue
        if 3 * digits[i] == target:
            tmp = 1
            for t in range(cnt_dict[digits[i]], cnt_dict[digits[i]] - 3, -1):
                tmp *= t
            res += tmp / 6
    print res
    return res


#assert get_ans([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8) == 20
#assert get_ans([1, 1, 2, 2, 2, 2], 5) == 12
#assert get_ans([1, 2, 3], 6) == 1
#assert get_ans([1, 1, 2, 2, 3, 3], 6) == 8
assert get_ans([1, 1, 1, 1, 1], 3) == 10
assert get_ans([0, 0, 0], 0) == 1
