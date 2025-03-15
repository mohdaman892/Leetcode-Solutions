class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def check(x):
            s = 0
            i = 0
            while i<n:
                if nums[i]<=x:
                    s+=1
                    i+=2
                else:
                    i+=1
            return s>=k

        
        
        n = len(nums)

        l = min(nums)
        r = max(nums)

        while l<r:
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        
        return l

