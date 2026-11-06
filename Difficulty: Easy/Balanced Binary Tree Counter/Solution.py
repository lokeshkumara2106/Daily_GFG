class Solution:
    def countBT(self, h: int) -> int:
        MOD = 10**9 + 7

        if h <= 1:
            return 1

        a, b = 1, 1

        for i in range(2, h + 1):
            c = (b * b + 2 * b * a) % MOD
            a, b = b, c

        return b
