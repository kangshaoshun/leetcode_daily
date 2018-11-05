#coding:utf-8
#########################################################################
# File Name: 924.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 10时51分15秒
#########################################################################
import sys
from collections import defaultdict

reload(sys)
sys.setdefaultencoding('utf-8')


class Solution(object):
    def build_graph(self, matrix):
        graph = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    graph[i].add(j)
        return graph
    
    def dfs(self, graph, node):
        if node not in graph:return 0
        res = [node]
        has_visited = set([node])
        stack = [node]
        while stack:
            node = stack.pop()
            for val in graph[node]:
                if val not in has_visited:
                    stack.append(val)
                    has_visited.add(val)
                    res.append(val)
        return res


    def get_ans(self, matrix, initial):
        node_graph = self.build_graph(matrix)
        print node_graph
        res = initial[0]
        max_cnt = 1
        for node in initial:
            tmp = self.dfs(node_graph, node)
            print tmp
            if len(tmp) > max_cnt:
                max_cnt = len(tmp)
                res = node
            if len(tmp) == max_cnt:
                res = min(res, node)
        return res

if __name__ == '__main__':
    so = Solution()
    
    #matrix = [[1,1,0],[1,1,0],[0,0,1]]
    #print so.build_graph(matrix)
    #initial = [0, 1]
    #print so.get_ans(matrix, initial)
    matrix = [[1,0,0],[0,1,0],[0,0,1]]
    initial = [0,2]
    assert so.get_ans(matrix, initial) == 0
    
    matrix = [[1,1,1],[1,1,1],[1,1,1]]
    initial = [1,2]
    assert so.get_ans(matrix, initial) == 1
    
    matrix = [[1,0,0,0,1,0,0,0],[0,1,1,0,0,1,0,0],[0,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,0],[1,0,1,1,1,0,0,1],[0,1,0,0,0,1,0,0],[0,0,0,0,0,0,1,1],[0,0,0,0,1,0,1,1]]
    initial = [7,2]
    print so.get_ans(matrix, initial)
