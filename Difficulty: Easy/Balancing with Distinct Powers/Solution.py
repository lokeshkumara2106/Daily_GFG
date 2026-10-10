class Solution:
    def balancePan(self, a, b):
        while b > 0:
            rem = b % a

            if rem == 0 or rem == 1:
                b //= a
            elif rem == a - 1:
                b = b // a + 1
            else:
                return False

        return True
