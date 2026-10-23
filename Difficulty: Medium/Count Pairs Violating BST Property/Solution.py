''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)

        def merge_sort(sub_arr):
            if len(sub_arr) <= 1:
                return sub_arr, 0

            mid = len(sub_arr) // 2
            left, left_inv = merge_sort(sub_arr[:mid])
            right, right_inv = merge_sort(sub_arr[mid:])

            merged = []
            i = j = 0
            inv_count = left_inv + right_inv

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i  # All remaining elements in left are greater
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        inorder(root)
        _, count = merge_sort(arr)
        return count
