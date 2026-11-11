'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = self.left = None
        
'''

class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        # code here
        def fun(node):
            if not node:
                return float('inf')
            ans=float('inf')
            ans=min(ans,abs(node.data-k))
            if node.data<k:
                ans=min(ans,fun(node.right))
            else:
                ans=min(ans,fun(node.left))
            return ans
        return fun(root)
