from bisect import bisect_right
class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        n=len(s)
        maxii=0
        res=''
        pos=[[] for _ in range(26)]
        for i,c in enumerate(s):
            pos[ord(c)-ord('a')].append(i)
        for word in d:
            possible=True
            prev=-1
            for c in word:
                arr=pos[ord(c)-ord('a')]
                idx=bisect_right(arr,prev)
                if idx==len(arr):
                    possible=False
                    break
                prev=arr[idx]
            if possible:
                if len(word)>maxii:
                    maxii=len(word)
                    res=word
                elif len(word)==maxii and word<res:
                    res=word
        return res