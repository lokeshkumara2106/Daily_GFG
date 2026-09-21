from collections import deque
"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        q1=deque([root1])
        q2=deque([root2])
        while q1 and q2:
            l1=len(q1)
            l2=len(q2)
            if l1!=l2:
                return False
            d1={}
            d2={}
            for _ in range(l1):
                node1=q1.popleft()
                node2=q2.popleft()
                d1[node1.data]=d1.get(node1.data,0)+1
                d2[node2.data]=d2.get(node2.data,0)+1
                if node1.left:
                    q1.append(node1.left)
                if node1.right:
                    q1.append(node1.right)
                if node2.left:
                    q2.append(node2.left)
                if node2.right:
                    q2.append(node2.right)
            if d1!=d2:
                return False
        return not q1 and not q2