class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        pre = []
        s = 0
        for i in arr:
            s += i
            pre.append(s)
        
        ans = 0
        e = 0
        o = 0

        for x in pre:
            if x%2 != 0:
                ans += e+1
                o+=1
            else:
                ans += o
                e+=1
        return ans%(10**9+7)