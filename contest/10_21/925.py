#coding:utf-8
#########################################################################
# File Name: 925.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月21日 星期日 09时32分58秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def isLongPressedName(self, name, typed):
        if len(name) > len(typed):return False
        i = j = 0
        pre = name[0]
        while i < len(name) and j < len(typed):
            cnt_n = 0
            cnt_t = 0
            while i < len(name) and name[i] == pre:
                cnt_n += 1
                i += 1
            while j < len(typed) and typed[j] == pre:
                cnt_t += 1
                j += 1
            if cnt_n > cnt_t:
                return False
            if i > len(name):
                break
            pre = name[i]
        if i < len(name):
            return False
        while j < len(typed):
            if typed[j] != name[-1]:
                return False
            j += 1
        return True

if __name__ == '__main__':
    so = Solution()
    name = 'leelee'
    typed = 'lleeelle'
    print so.isLongPressedName(name, typed)
