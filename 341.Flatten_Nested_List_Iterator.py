# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.ns = []
        self.flatten(nestedList)
        self.index = 0
        self.length = len(self.ns)
        
    def flatten(self, nestedList):
        if not nestedList:
            return
        #遇到int添加，list递归
        for item in nestedList:
            if item.isInteger():
                self.ns.append(item.getInteger())
            else:
                self.flatten(item.getList())
        
    def next(self):
        """
        :rtype: int
        """
        pre = self.index
        self.index += 1
        return self.ns[pre]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < self.length:
            return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())