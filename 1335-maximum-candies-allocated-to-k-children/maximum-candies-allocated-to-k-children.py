class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def check(x):
            s = 0
            if x == 0:
                return True
            for i in candies:
                s += i//x
            return s>=k

        candies.sort()
        l = 0
        r = candies[-1]
        ans = -sys.maxsize

        while l<r:
            mid = (l+r)//2
            if check(mid):
                ans = max(ans,mid)
                l = mid+1
            else:
                r = mid
        
        if check(l):
            ans = max(ans,l)
        
        return ans
        