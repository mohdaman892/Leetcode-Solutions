class Solution:
    def numTilings(self, n: int) -> int:

        def f(i,gap):
            # print(dp)
            if i>n:
                return 0
            
            if i==n:
                if not gap:
                    return 1
                else:
                    return 0
            
            if dp[i][gap]!=-1:
                return dp[i][gap]

            ans = 0
            if not gap:
                ans +=  f(i+1,False) + f(i+2,False) + 2*f(i+2,True)
            else:
                ans +=  f(i+1,False) + f(i+1,True)
            dp[i][gap] = ans
            return ans

        mod = 10**9+7
        dp = [[-1,-1] for i in range(n)]
        print(dp)
        return f(0,False)%mod