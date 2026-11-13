''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        def inorder(root,arr):
            if not root:
                return
            inorder(root.left,arr)
            arr.append(root.data)
            inorder(root.right,arr)
        a=[]
        b=[]
        inorder(r1,a)
        inorder(r2,b)
        i=j=0
        res=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                res.append(a[i])
                i+=1
                j+=1
            elif a[i]>b[j]:
                j+=1
            else:
                i+=1
        return res
