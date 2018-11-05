#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Solution(object):
    def nth_digit(self, n):
        if n <= 0:return
        if n > 0 and n <= 9:return n % 10
        base, num, tSum = 1, 9, 9
        #找出n所在的区间，数字长度是几位数
        while n > tSum:
            if tSum == n:return 9
            base += 1
            num *= 10
            tSum += base * num
        #得到在本区间的位置
        tSum -= base * num
        n -= tSum
        #计算在哪个数上
        c1 = n / base
        c2 = n % base
        #提取该数字，num/9是该区间第一个数字，以0结尾，比如100, c1是该区间第几个数，c2是这个数的位置偏移
        if c2 == 0:
            return (num / 9 + c1 - 1) % 10
        else:
            return int(str(num / 9 + c1)[c2 - 1])

if __name__ == '__main__':
    s = Solution()
    print s.nth_digit(int(sys.argv[1]))
