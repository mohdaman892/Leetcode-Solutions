class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        hm = {}
        for num in nums:
            x = str(num)
            s = 0
            for j in x:
                s += int(j)
            if s not in hm:
                hm[s] = SortedList()
            hm[s].add(num)
        ans = -1
        for i in hm:
            if len(hm[i])>=2:
                ans = max(ans,hm[i][-1]+hm[i][-2])
        return ans