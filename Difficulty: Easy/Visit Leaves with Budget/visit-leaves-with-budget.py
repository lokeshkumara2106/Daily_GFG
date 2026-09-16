''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        levels = []

        def fun(root, level):
            if not root:
                return

            # Leaf node
            if not root.left and not root.right:
                levels.append(level)
                return

            fun(root.left, level + 1)
            fun(root.right, level + 1)

        fun(root, 1)

        levels.sort()

        count = 0

        for val in levels:
            if k >= val:
                count += 1
                k -= val
            else:
                break

        return count