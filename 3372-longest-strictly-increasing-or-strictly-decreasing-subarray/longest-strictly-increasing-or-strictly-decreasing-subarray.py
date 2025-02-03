class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        i = 0
        for j in range(1,len(nums)):
            if nums[j]>nums[j-1]:
                ans = max(ans, j-i+1)
            else:
                i = j
        
        ans2 = 1
        i = 0
        for j in range(1,len(nums)):
            if nums[j]<nums[j-1]:
                ans = max(ans, j-i+1)
            else:
                i = j
        
        
        return max(ans,ans2)