from math import gcd
class Solution:
    def sameMod(self, arr):
        g=0
        for i in range(1,len(arr)):
            g=gcd(g,abs(arr[i-1]-arr[i]))
        if g==0:
            return -1
        count=0
        for i in range(1,int(g**0.5)+1):
            if g%i==0:
                count+=1
                if g//i!=i:
                    count+=1
        return count