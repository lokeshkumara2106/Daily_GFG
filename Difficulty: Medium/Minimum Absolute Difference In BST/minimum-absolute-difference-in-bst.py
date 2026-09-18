'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        res=[]
        def fun(root):
            if not root:
                return
            res.append(root.data)
            fun(root.left)
            fun(root.right)
        fun(root)
        res.sort()
        mini=float('inf')
        for i in range(1,len(res)):
            mini=min(mini,res[i]-res[i-1])
        return mini