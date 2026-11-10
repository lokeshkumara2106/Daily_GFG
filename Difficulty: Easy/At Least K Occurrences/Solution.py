class Solution:
    def firstElementKTime(self, arr: list[int], k: int) -> int:
        # code here
        d={}
        for num in arr:
            d[num]=d.get(num,0)+1
            if d[num]==k:
                return num
        return -1
