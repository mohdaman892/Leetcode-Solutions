class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        @lru_cache(None)
        def f(i,s):
            if i == len(a):
                # print(s)
                return s == n
            
            return f(i+1,s+a[i]) or f(i+1,s)
        
        
        a = [1]
        x = 1
        while 3**x<=n:
            a.append(3**x)
            x+=1
        # print(a)
        return f(0,0)