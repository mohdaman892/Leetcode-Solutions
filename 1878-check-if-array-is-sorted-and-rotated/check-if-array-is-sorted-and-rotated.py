class Solution:
    def check(self, nums: List[int]) -> bool:
        a = sorted(nums)
        a = a + a
        for i in range(len(a)):
            if a[i]==nums[0]:
                if a[i:i+len(nums)]==nums:
                    return True
        return False