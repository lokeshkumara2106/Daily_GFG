class Solution:
    def getCount (self, s, k):
        freq = {}

        for i in range(len(s)):
            # Count only the start of each group
            if i == 0 or s[i] != s[i - 1]:
                freq[s[i]] = freq.get(s[i], 0) + 1

        return sum(1 for count in freq.values() if count == k)
