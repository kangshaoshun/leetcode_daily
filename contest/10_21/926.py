#coding:utf-8
#########################################################################
# File Name: 926.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月21日 星期日 10时08分29秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def minFlipsMonoIncr(self, S):
        cnt_0 = 0
        cnt_1 = 0
        flag = False
        for val in S:
            if not flag and val == '1':
                flag = True
            if flag and val == '0':
                cnt_0 += 1
        flag = False
        for val in reversed(S):
            if not flag and val == '0':
                flag = True
            if flag and val == '1':
                cnt_1 += 1
        print cnt_0, cnt_1
        return min(cnt_0, cnt_1)

if __name__ == '__main__':
    so = Solution()
    print so.minFlipsMonoIncr('01')
