class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        d={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=[]
            if len(d[arr[i]])>=1:
                if i-d[arr[i]][-1]<=k:
                    return True
            d[arr[i]].append(i)
        return False
