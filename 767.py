#coding:utf-8
#########################################################################
# File Name: 767.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 20时10分41秒
#########################################################################
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

"""
重排字符串
"""

class Solution(object):
    def rearrange(self, S):
        a = sorted(sorted(S), key=S.count)
        print a

    def get_ans(self, s):
        counter = Counter(s)
        res = '#'
        while counter:
            stop = True
            for val, time in counter.most_common():
                if val != res[-1]:
                    res += val
                    counter[val] -= 1
                    if counter[val] == 0:
                        counter.pop(val)
                    stop = False
                    break
            if stop:
                break
        return res[1:] if len(res) == len(s) + 1 else ''


if __name__ == '__main__':
    so = Solution()
    #print so.get_ans('aaabba')
    so.rearrange('aaabba')
