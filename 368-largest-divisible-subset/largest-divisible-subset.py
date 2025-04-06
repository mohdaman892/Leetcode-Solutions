class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        ans = 1
        hm = [0 for i in range(n)]
        l = 0
        for i in range(n):
            hm[i] = i
            for j in range(i):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        hm[i] = j
            if dp[i]>ans:
                ans = dp[i]
                l = i
        ans = [nums[l]]
        while hm[l]!=l:
            ans.insert(0,nums[hm[l]])
            l = hm[l]
        return ans