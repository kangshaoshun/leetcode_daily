#coding:utf-8
#########################################################################
# File Name: graph.py
# Author: kangshaoshun
# mail: kangshaoshun@gmail.com
# Created Time: 2018年10月14日 星期日 11时18分39秒
#########################################################################
import sys
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def build_graph(self, matrix):
        graph = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j and matrix[i][j]:
                    graph[i].add(j)
        return graph
    
    def travel_graph(self, graph):
        def dfs(graph, start):
            res = [start]
            has_visited = set([start])
            stack = [start]
            while stack:
                node = stack.pop()
                for val in graph[node]:
                    if val not in has_visited:
                        stack.append(val)
                        res.append(val)
                        has_visited.add(val)
            return res
        return dfs(graph, 1)

            
    def get_ans(self, matrix):
        node_graph = self.build_graph(matrix)
        print node_graph
        return self.travel_graph(node_graph)


if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 0, 1], 
            [0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1]]
    print so.get_ans(matrix)

