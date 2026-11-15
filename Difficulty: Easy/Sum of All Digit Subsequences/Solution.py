class Solution:
    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        n = len(s)
        total = sum(int(ch) for ch in s)
        return (total * pow(2, n-1, MOD)) % MOD
