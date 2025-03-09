class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        a = []
        b = []
        n = len(nums1)
        for i in range(n):
            a.append([nums1[i],i,nums2[i]])
        a.sort()
        print(a)
        ans = [0 for i in range(n)]
        from sortedcontainers import SortedList
        x = SortedList()
        s = 0
        for i in range(n):
            if a[i][0]==a[i-1][0]:
                ans[a[i][1]] = ans[a[i-1][1]]
                x.add(a[i][2])
                s += a[i][2]
                if len(x)>k:
                    s -= x[0]
                    x.discard(x[0])
                continue
            if len(x)<k:
                ans[a[i][1]] = s
                s += a[i][2]
                x.add(a[i][2])
            else:
                ans[a[i][1]] = s
                x.add(a[i][2])
                s -= x[0]
                s += a[i][2]
                x.discard(x[0])
        
        return ans



