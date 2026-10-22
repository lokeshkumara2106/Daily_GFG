class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        half = n // 2

        # Check whether a palindrome is possible
        for i in range(half):
            j = n - 1 - i
            if s[i] != '?' and s[j] != '?' and s[i] != s[j]:
                return -1

        # Build the left half, using mirrored fixed characters
        a = []
        for i in range(half):
            j = n - 1 - i
            if s[i] != '?':
                a.append(s[i])
            elif s[j] != '?':
                a.append(s[j])
            else:
                a.append('?')

        # For odd-length strings, include the center
        if n % 2:
            a.append(s[half])

        # DP: dp[c] is the minimum cost ending with character c.
        # '?' can be any lowercase letter.
        dp = [0] * 26
        first = a[0]

        if first != '?':
            dp = [0 if c == ord(first) - ord('a') else float('inf')
                  for c in range(26)]

        for ch in a[1:]:
            ndp = [float('inf')] * 26
            allowed = range(26) if ch == '?' else [ord(ch) - ord('a')]

            for c in allowed:
                ndp[c] = min(dp[p] + abs(c - p) for p in range(26))

            dp = ndp

        return 2 * min(dp)
