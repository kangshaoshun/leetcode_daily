#coding:utf-8
#########################################################################
# File Name: 714.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月22日 星期一 17时03分41秒
#########################################################################
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
最佳买股票的时间，每次交易需要费用，求最大利润
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        思路：
            这是一个动态规划的题目，状态有两种：手里有股票，　手里没股票
            转移有四种，　有　->  有　／　无
                        　无　->　无　／　有
            dp[i][0]:代表手里没有股票                        
            dp[i][1]:代表手里有股票
        """
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i] - fee)
            dp[i][1] = max(dp[i - 1][1], prices[i - 1][0] - prices[i])
        return dp[-1][0]
