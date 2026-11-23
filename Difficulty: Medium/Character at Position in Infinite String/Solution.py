class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        lengths = [len(s)]
        i = 1
        while lengths[-1] < pos:
            lengths.append(2 * lengths[-1] + i)
            i += 1
        for step in range(i - 1, 0, -1):
            L = lengths[step - 1]
            if pos <= L:
                continue
            elif pos <= L + step:
                return '$'
            else:
                pos = 2 * L + step - pos + 1
        return s[pos - 1]
