class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        a = [[x,i] for i,x in enumerate(nums)]
        a.sort()
        print(a)
        g1 = []
        g2 = []
        p = [a[0][1]]
        q = [a[0][0]]
        n = len(nums)
        for i in range(1,n):
            if abs(a[i][0]-q[-1])<=limit:
                p.append(a[i][1])
                q.append(a[i][0])
            else:
                g1.append(p)
                g2.append(q)
                p = [a[i][1]]
                q = [a[i][0]]
        g1.append(p)
        g2.append(q)
        # print(g1,g2)
        while g1:
            x,y = g1.pop(0),g2.pop(0)
            for i in sorted(x):
                nums[i] = y.pop(0)
        
        return nums
            

