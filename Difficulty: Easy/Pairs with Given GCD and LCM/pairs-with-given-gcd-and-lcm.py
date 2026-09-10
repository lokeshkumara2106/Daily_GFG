class Solution:

    def pairCount(self, x, y):
        """code here"""
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        product=x*y
        pairs=0
        for a in range(x,y+1):
            if product%a==0:
                b=product//a
                if gcd(a,b)==x:
                    pairs+=1
        return pairs