class Solution:
    def maxHeight(self, height: list[int], width: list[int], length: list[int]) -> int:
        n = len(height)

        # Generate all 3 rotations of every box.
        # Each tuple is (base_width, base_length, height)
        boxes = []

        for i in range(n):
            h, w, l = height[i], width[i], length[i]

            boxes.append((min(w, l), max(w, l), h))
            boxes.append((min(h, l), max(h, l), w))
            boxes.append((min(h, w), max(h, w), l))

        m = len(boxes)

        # dp[i] = maximum height when boxes[i] is at the bottom
        dp = [0] * m

        def solve(i):
            if dp[i]:
                return dp[i]

            base_w, base_l, h = boxes[i]
            dp[i] = h

            for j in range(m):
                next_w, next_l, next_h = boxes[j]

                # Strictly smaller base dimensions
                if next_w < base_w and next_l < base_l:
                    dp[i] = max(dp[i], h + solve(j))

            return dp[i]

        ans = 0

        for i in range(m):
            ans = max(ans, solve(i))

        return ans
