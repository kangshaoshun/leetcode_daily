#coding:utf-8
#########################################################################
# File Name: 921.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 09时44分21秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_ans(s):
    if not s:return 0
    stack = []
    cnt = 0
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                cnt += 1
    return cnt + len(stack)

assert get_ans('())') == 1
assert get_ans('') == 0
assert get_ans('(((') == 3
assert get_ans(()) == 0
assert get_ans('()))((') == 4
