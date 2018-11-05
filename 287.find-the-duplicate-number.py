#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (45.43%)
# Total Accepted:    128.2K
# Total Submissions: 280.1K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        思路：
            1.二分查找；抽屉原理。如果区间1-n/2 中的个数大于n/2，则重复元素在这个区间中，否则在后半段区间；
            2.快慢指针，环形入口
        """
        if len(nums) == 1:return -1
        left, right = 1, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            cnt = 0
            for val in nums:
                if val <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findDuplicate2(self, nums):
        """
        思路二：数组的环形入口
        如果没有重复元素，下标到值得映射就是一一对应的；
        如果有重复元素，下标到值的映射就可能出现多对一的情况，从而出现环
        如数组  2, 1, 3, 1 映射关系 0->2 {1, 3}->1 2->3
        其中1和3都会映射到1，就会出现环
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 2]
    print s.findDuplicate2(nums)
    

