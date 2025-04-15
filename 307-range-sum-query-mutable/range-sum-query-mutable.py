class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0]+nums
        self.tree = [0 for i in range(self.n+1)]
        for i,a in enumerate(nums):
            self.add(i+1,a)
        # print(self.tree)

    def update(self, i: int, val: int) -> None:
        self.add(i+1,val-self.nums[i+1])
        self.nums[i+1] = val
    
    def add(self,k,x):
        while k<=self.n:
            self.tree[k]+=x
            k += k&-k

    def sum_(self,k):
        s = 0
        while k>=1:
            s += self.tree[k]
            k -= k&-k
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_(right+1) - self.sum_(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)