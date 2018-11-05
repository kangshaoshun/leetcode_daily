#coding:utf-8
import sys
import copy
reload(sys)
sys.setdefaultencoding('utf-8')

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype : List[str]
        """
        #build dict
        path_dict = dict()
        for path in tickets:
            fr, to = path
            if fr not in path_dict:
                path_dict[fr] = [to]
            else:
                path_dict[fr].append(to)
        for key in path_dict:
            path_dict[key].sort(reverse=True)
        print path_dict
        #dfs
        current_path = ['JFK']
        routes = []        
        while current_path:
            while current_path[-1] in path_dict:
                tmp = current_path[-1]
                d = path_dict[tmp]
                current_path.append(d.pop())
                if not d:
                    path_dict.pop(tmp)
            routes.append(current_path.pop())
        return routes[::-1]
                 

if __name__ == '__main__':
    so = Solution()
    #tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print so.findItinerary(tickets)
