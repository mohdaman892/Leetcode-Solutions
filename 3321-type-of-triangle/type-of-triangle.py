class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        c = 0
        if nums[0] + nums[1] > nums[2]:
            c+=1
        if nums[1] + nums[2] > nums[0]:
            c+=1
        if nums[0] + nums[2] > nums[1]:
            c+=1
        if c<3:
            return "none"
        s = set(nums)
        if len(s)==1:
            return "equilateral"
        elif len(s)==2:
            return "isosceles"
        else:
            return "scalene"