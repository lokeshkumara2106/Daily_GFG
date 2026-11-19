class Solution:
    def minFlips(self, s):
        n=len(s)
        p1='10'*n
        p2='01'*n
        s1=p1[:n]
        s2=p2[:n]
        count1=count2=0
        for i in range(len(s)):
            if s1[i]!=s[i]:
                count1+=1
            if s2[i]!=s[i]:
                count2+=1
        return min(count1,count2)
