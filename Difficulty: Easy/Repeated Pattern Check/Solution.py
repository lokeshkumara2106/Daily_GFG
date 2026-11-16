class Solution:
    def findPattern(self, s):
        x=0
        y=0
        for i,c in enumerate(s):
            if i>0 and s[i]=='x' and s[i-1]=='y':
                if x!=y:
                    return False
                else:
                    x=y=0
            if c=='x':
                x+=1
            else:
                y+=1
        return x==y
