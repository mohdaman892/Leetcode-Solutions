class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        a = []
        c = 0
        d = Counter(nums)
        for i in nums:
            if i!=0:
                a.append(i)
        for i in range(d[0]):
            a.append(0)
        return a