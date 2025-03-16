class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        hm = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hm:
                hm[nums[i]] = SortedList()
            hm[nums[i]].add(i)
        
        ans = []
        print(hm)
        for q in queries:
            if len(hm[nums[q]]) == 1:
                ans.append(-1)
            else:
                a = hm[nums[q]]
                k = bisect_left(a,q)
                if k == len(a)-1:
                    ans.append(min(a[k]-a[k-1],a[0]+n-a[k]))
                elif k == 0:
                    ans.append(min(a[k+1]-a[0],a[0]+n-a[-1]))
                else:
                    ans.append(min(a[k]-a[k-1],a[k+1]-a[k]))
        
        return ans
