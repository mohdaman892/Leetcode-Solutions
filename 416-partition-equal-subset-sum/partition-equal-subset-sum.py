class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def f(i,k,a):
            if k==0:
                return True
            if i==0:
                return a[0]==k 
            if dp[i][k]!=-1:
                return dp[i][k]
            l = f(i-1,k,a)
            r = False 
            if k>=a[i]:
                r = f(i-1,k-a[i],a)
            dp[i][k] = l or r
            return dp[i][k]
    
        s = sum(nums)
        n = len(nums)
        k = s//2
        if s%2!=0:
            return False
        # dp = [[False for i in range(k+1)] for j in range(n)]
        prev = [False for i in range(k+1)]
        prev[0] = True
        # for i in range(n):
        #     dp[i][0] = True
        if nums[0]==k:
            prev[nums[0]] = True
        for i in range(1,n):
            curr = [False for i in range(k+1)]
            curr[0] = True
            for j in range(1,k+1):
                l = prev[j]
                r = False
                if j>=nums[i]:
                    r = prev[j-nums[i]]
                curr[j] = l or r
            prev = curr
        return prev[k]
            