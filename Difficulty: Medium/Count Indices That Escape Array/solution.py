class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n
        # 0 = unvisited, 2 = good, 3 = bad

        for i in range(n):
            if state[i] != 0:
                continue

            path = []
            node = i
            pos = {}

            while 0 <= node < n and state[node] == 0 and node not in pos:
                if arr[node] == 0:
                    state[node] = 3
                    break

                pos[node] = len(path)
                path.append(node)
                node += arr[node]

            if node < 0 or node >= n:
                result = 2
            elif node in pos:
                result = 3
            else:
                result = state[node]

            for j in reversed(path):
                state[j] = result

        return state.count(2)
