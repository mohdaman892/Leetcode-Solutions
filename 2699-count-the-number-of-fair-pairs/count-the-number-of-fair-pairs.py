class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bs(l,r,k):
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>=k:
                    r = mid-1
                else:
                    l = mid+1
            return l
        
        
        
        ans = 0  
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            p =  bs(i+1,n-1,lower-nums[i])
            q =  bs(i+1,n-1,upper-nums[i]+1)
            ans += q-p
        return ans