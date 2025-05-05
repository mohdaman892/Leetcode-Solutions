class Solution:
    def numTilings(self, n: int) -> int:

        @lru_cache(None)
        def f(i,gap):
            if i>n:
                return 0
            
            if i==n:
                if not gap:
                    return 1
                else:
                    return 0

            if not gap:
                return f(i+1,False) + f(i+2,False) + 2*f(i+2,True)
            else:
                return f(i+1,False) + f(i+1,True)

        grid = [[0 for i in range(n)] for i in range(2)]
        mod = 10**9+7
        return f(0,False)%mod