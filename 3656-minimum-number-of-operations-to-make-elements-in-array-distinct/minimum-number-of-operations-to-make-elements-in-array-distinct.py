class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        x = -1
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] in s:
                x = i
                break
            s.add(nums[i])
        if x==-1:
            return 0
        if (x+1)%3==0:
            return (x+1)//3
        else:
            return (x+1)//3 + 1