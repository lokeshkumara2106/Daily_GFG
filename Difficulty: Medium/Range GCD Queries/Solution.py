from math import gcd
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr=arr
        self.tree = [0] * (4 * self.n)

        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        # Leaf node
        if start == end:
            self.tree[node] = self.arr[start]
            return

        mid = (start + end) // 2

        self.build(2 * node + 1, start, mid)
        self.build(2 * node + 2, mid + 1, end)

        # Store maximum of left and right child
        self.tree[node] = gcd(
            self.tree[2 * node + 1],
            self.tree[2 * node + 2]
        )

    def query(self, node, start, end, l, r):

        # Completely outside range
        if end < l or r < start:
            return 0

        # Completely inside range
        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2

        left = self.query(
            2 * node + 1,
            start,
            mid,
            l,
            r
        )

        right = self.query(
            2 * node + 2,
            mid + 1,
            end,
            l,
            r
        )

        return gcd(left, right)
    
    def update(self, node, start, end, index, value):
            # Found the index
            if start == end:
                self.arr[index] = value
                self.tree[node] = value
                return

            mid = (start + end) // 2

            if index <= mid:
                self.update(
                    2 * node + 1,
                    start,
                    mid,
                    index,
                    value
                )
            else:
                self.update(
                    2 * node + 2,
                    mid + 1,
                    end,
                    index,
                    value
                )

            # Recalculate current node
            self.tree[node] = gcd(
                self.tree[2 * node + 1],
                self.tree[2 * node + 2]
            )

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        st=SegmentTree(arr)
        res=[]
        n=len(arr)
        for t,x,y in queries:
            if t==0:
                res.append(st.query(0,0,n-1,x,y))
            else:
                st.update(0,0,n-1,x,y)
        return res
