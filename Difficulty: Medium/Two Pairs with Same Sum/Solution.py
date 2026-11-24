class Solution:
    def findPairs(self, arr):
        n = len(arr)
        d = {}
        best = None
        for i in range(n):
            arr_i = arr[i]
            for j in range(i + 1, n):
                s = arr_i + arr[j]
                pairs = d.get(s)
                if pairs is not None:
                    for a, b in pairs:
                        if a != i and a != j and b != i and b != j:
                            if a < i or (a == i and b < j):
                                cand = [a, b, i, j]
                            else:
                                cand = [i, j, a, b]
                            if best is None or cand < best:
                                best = cand
                    if len(pairs) < 2:
                        pairs.append((i, j))
                else:
                    d[s] = [(i, j)]
        return best if best is not None else [-1, -1, -1, -1]
