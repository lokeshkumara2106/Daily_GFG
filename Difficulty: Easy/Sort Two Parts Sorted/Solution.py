class Solution:
    def mergeTwoParts(self, arr):
        n = len(arr)
        i = 0

        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1

        mid = i + 1
        res = []
        i, j = 0, mid

        while i < mid and j < n:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1

        res.extend(arr[i:mid])
        res.extend(arr[j:n])

        for i in range(n):
            arr[i]=res[i]
