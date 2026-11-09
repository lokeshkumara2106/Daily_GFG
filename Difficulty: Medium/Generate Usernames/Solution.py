class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        reserved = set(arr)
        assigned = set()
        res = []

        for c in arr:
            original = c
            step = 1

            if c in assigned:
                while original + str(step) in reserved or original + str(step) in assigned:
                    step += 1

                c = original + str(step)

            assigned.add(c)
            res.append(c)

        return res
