class Solution:
    def maxValue(self, n: int) -> int:
        """code here"""
        b=list(bin(n)[2:])
        count=0
        for i,c in enumerate(b):
            if c=='1':
                count+=1
            else:
                count=0
            if count==3:
                b[i]='0'
                count=0
        return int(''.join(b),2)
