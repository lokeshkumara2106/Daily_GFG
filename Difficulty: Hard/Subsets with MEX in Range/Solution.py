class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 1)
        for x in arr:
            freq[x] += 1

        # Number of subsets formed using values greater than x
        suffix = [0] * (n + 2)
        for x in range(n, -1, -1):
            suffix[x] = suffix[x + 1] + freq[x]

        ans = 0
        ways = 1  # Ways to include every required value below current MEX

        for mex in range(r + 1):
            if mex > 0:
                ways = ways * (pow(2, freq[mex - 1], MOD) - 1) % MOD

            if mex >= l:
                if ways == 0:
                    break

                extra = pow(2, suffix[mex + 1], MOD)
                ans = (ans + ways * extra) % MOD

        return ans
