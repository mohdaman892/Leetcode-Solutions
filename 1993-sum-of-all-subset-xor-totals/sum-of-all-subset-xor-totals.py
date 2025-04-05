class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def f(i,n,a,s):
            if i==n:
                self.xs+=s
                s=0
                return
            s=s^a[i]
            f(i+1,n,a,s)
            s=s^a[i]
            f(i+1,n,a,s)
        
        self.xs=0
        s=0
        f(0,len(nums),nums,s)
        return self.xs
        