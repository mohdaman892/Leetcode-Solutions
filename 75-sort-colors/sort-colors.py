class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=Counter(nums)
        j=0
        for i in range(c[0]):
            nums[j]=0
            j+=1
        for i in range(c[1]):
            nums[j]=1
            j+=1
        for i in range(c[2]):
            nums[j]=2
            j+=1
        