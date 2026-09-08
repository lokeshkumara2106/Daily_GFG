class Solution:
    def findMax(self, n):
        s = str(n)
        nsum = sum(map(int, s))

        for i in range(len(s)):
            if s[i] != '0':
                candidate = int(s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i - 1))
                csum = sum(map(int, str(candidate)))

                if csum > nsum or (csum == nsum and candidate > n):
                    n = candidate
                    nsum = csum

        return n
