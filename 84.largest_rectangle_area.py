#coding:utf-8
#########################################################################
# File Name: 84.largest_rectangle_area.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月10日 星期三 21时35分14秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def get_ans(self, nums):
        if not nums:return
        stack = []
        nums.append(-1)
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            while stack and cur < nums[stack[-1]]:
                height = nums[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)
            print stack
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [2,1,5,6,2,3]
    print so.get_ans(nums)
