class Solution:
    def socialNetwork(self, arr):
        n = len(arr) + 1
        ans = []

        # User numbers are 1 to n
        for i in range(2, n + 1):

            current = i
            distance = 0

            # Keep following the friend
            while current != 1:
                # arr[current - 2] is the friend of current
                current = arr[current - 2]
                distance += 1

                ans.append([i, current, distance])

        # For each i, destinations must be in increasing order.
        # The above traversal gives destinations in reverse order,
        # so sort the result accordingly.
        ans.sort(key=lambda x: (x[0], x[1]))

        return ans
