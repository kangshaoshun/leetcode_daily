#coding:utf-8
#########################################################################
# File Name: 794.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月15日 星期一 15时04分20秒
#########################################################################
import sys
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def valid_win(self, board, player):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        cnt_dict = defaultdict(int)
        for s in board:
            for c in s:
                if c == ' ':
                    cnt_dict[' '] += 1
                elif c == 'X':
                    cnt_dict['X'] += 1
                else:
                    cnt_dict['O'] += 1
        print cnt_dict
        if cnt_dict['O'] > cnt_dict['X'] or cnt_dict['X'] > cnt_dict['O'] + 1:
            return False
        if cnt_dict['O'] + cnt_dict['X'] == 0:return True
        if self.valid_win(board, 'O'):
            if self.valid_win(board, 'X'):
                return False
            return cnt_dict['O'] == cnt_dict['X']:
        if self.valid_win(board, 'X') and cnt_dict['X'] != cnt_dict['O'] + 1:
            return False
        return True

if __name__ == '__main__':
    so = Solution()
    #board = ["O  ", "   ", "   "]
    #board = ["XOX", " X ", "   "]
    #board = ["XXX", "   ", "OOO"]
    board = ["XOX", "O O", "XOX"]
    print so.validTicTacToe(board)

