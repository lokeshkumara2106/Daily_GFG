class Solution:
    def findRollOut(self, s, roll):
        # code here
        n=len(s)
        ans=[0]*n
        for i in range(len(roll)):
            ans[roll[i]-1]+=1
        for i in range(n-2,-1,-1):
            ans[i]+=ans[i+1]
        res=''
        for i,c in enumerate(s):
            res += chr((ord(c)-ord('a')+ans[i])%26 + ord('a'))
        return res
