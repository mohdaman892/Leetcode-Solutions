class Solution:
    def minCost(self, nums: List[int]) -> int:
        
        def f(i,j):
            if i>=n:
                if j!=-1:
                    return nums[j]
                else:
                    return sys.maxsize
            if i+1==n:
                if j!=-1:
                    return max(max(nums[i:]),nums[j])
                else:
                    return max(nums[i:])
            if i in dp:
                if j in dp[i]:
                    return dp[i][j]
            ans = sys.maxsize
            if j!=-1:
                # print(nums)
                ans = min(ans,max(nums[j],nums[i])+f(i+2,i+1),max(nums[j],nums[i+1])+f(i+2,i),max(nums[i],nums[i+1])+f(i+2,j))
            else:
                ans = min(ans,max(nums[i],nums[i+1])+f(i+3,i+2),max(nums[i],nums[i+2])+f(i+3,i+1),max(nums[i+1],nums[i+2])+f(i+3,i))
            if i not in dp:
                dp[i] = {}
            dp[i][j] = ans
            return ans


        n = len(nums)
        if n<=2:
            return max(nums)
        dp = {}
        return f(0,-1)