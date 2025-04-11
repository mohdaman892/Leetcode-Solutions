class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low,high+1):
            x = list(map(int,str(i)))
            if len(x)%2==0:
                if sum(x[:len(x)//2])==sum(x[len(x)//2:]):
                    ans+=1
        return ans