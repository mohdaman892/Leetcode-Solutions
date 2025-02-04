class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        s = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                s += nums[i]
            else:
                ans = max(ans, s)
                s = nums[i]
        ans = max(ans,s)
        return  ans