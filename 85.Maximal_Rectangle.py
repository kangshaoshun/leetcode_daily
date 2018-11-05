#coding:utf-8
#########################################################################
# File Name: 85.Maximal_Rectangle.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月10日 星期三 21时48分55秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def get_ans(self, matrix):
        """
        时间复杂度:O(n ^ 2)
        空间复杂度:O(N)
        """
        if not matrix or not matrix[0]:
            return 0
        nums = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for i in range(len(row)):
                nums[i] = nums[i] + 1 if row[i] == 1 else 0
            #这一部分是84题的题解
            nums.append(-1)
            stack = []
            for j in range(len(nums)):
                cur = nums[j]
                while stack and cur < nums[stack[-1]]:
                    height = nums[stack.pop()]
                    width = j if not stack else j - 1 - stack[-1]
                    ans = max(ans, height * width)
                stack.append(j)
            nums.pop()
        return ans
            

if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print so.get_ans(matrix)
