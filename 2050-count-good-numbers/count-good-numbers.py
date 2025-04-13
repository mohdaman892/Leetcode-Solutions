class Solution:
    def countGoodNumbers(self, n: int) -> int:

        ans = 1
        k = n//2
        mod = 10**9+7
        if k>0:
            ans *= pow(5,k,mod)
            ans *= pow(4,k,mod)
        if n%2!=0:
            ans *= 5
        return ans%mod