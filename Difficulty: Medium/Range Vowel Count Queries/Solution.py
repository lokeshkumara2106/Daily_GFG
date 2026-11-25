class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        prefix=[0]*len(s)
        for i,c in enumerate(s):
            prefix[i] = (prefix[i-1] if i > 0 else 0)
            if c in 'aeiou':
                prefix[i] += 1
        return [prefix[y] - (prefix[x-1] if x > 0 else 0) for x, y in queries]
