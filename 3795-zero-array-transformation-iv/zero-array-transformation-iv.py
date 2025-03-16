class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        @lru_cache(None)
        def f(i,s,ind):
            if s == 0:
                return i-1
            if s < 0:
                return sys.maxsize
            if i == len(queries):
                return i-1 if s == 0 else sys.maxsize
            ans = sys.maxsize
            if queries[i][0]<=ind<=queries[i][1]:
                ans = min(ans,f(i+1,s-queries[i][2],ind))
            ans = min(ans,f(i+1,s,ind))
            return ans
        
        res = -sys.maxsize
        for i in range(len(nums)):
            target = nums[i]
            x = f(0,target,i)
            if x == sys.maxsize:
                return -1
            res = max(res,x)
    
        return res+1