#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
考虑：
    1. 正负数
    2. 将divmod的结果添加到result中，b添加到set中。判断重复出现的b的位置
    3. 找到开始出现重复的位置。括号括起来
"""

class Solution():
    def fraction_to_decimal(self, nume, deno):
        res = ''
        if (deno < 0 and nume > 0) or (deno > 0 and nume < 0):
            res = '-' + res
        nume, deno = abs(nume), abs(deno)
        a, b = divmod(nume, deno)
        print a, b
        res += str(a)
        if b == 0:
            return res
        else:
            res += '.'
        has_seen = dict()
        i = 0
        while b != 0 and b not in has_seen:
            has_seen[b] = i
            i += 1
            b *= 10
            tmp_a, tmp_b = divmod(b, deno)
            res += str(tmp_a)
            b = tmp_b
        if b == 0:
            return res
        else:
            ind = res.index('.')
            pos = has_seen[b]
            print res, pos, ind
            return res[:ind + 1 + pos] + '(' + res[ind + 1 +  pos:] + ')'

if __name__ == '__main__':
    s = Solution()
    print s.fraction_to_decimal(int(sys.argv[1]), int(sys.argv[2]))
