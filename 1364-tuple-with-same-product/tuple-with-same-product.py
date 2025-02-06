class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hm = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                p = nums[i]*nums[j]
                if p not in hm:
                    hm[p] = 0
                hm[p]+=1
        print(hm)
        ans = 0
        for i in hm:
            if hm[i]>=2:
                comb = factorial(hm[i])//(factorial(hm[i]-2)*2)
                ans += 8*comb
        return ans

        # 12 34 56
        # 3

        # 1234
        # 2143
        # 1243
        # 2134
        