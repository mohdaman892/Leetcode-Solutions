class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = 0
        while i<=n-3:
            if nums[i] == 0:
                flag = False
                for j in range(i,min(i+3,n)):
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
                    if nums[j] == 0 and not flag:
                        flag = True
                        i = j
                ans += 1
            else:
                i+=1
        # print(nums,i)
        # if nums[i] == 0:
        #     for j in range(i,min(i+3,n)):
        #         if nums[j] == 0:
        #             nums[j] = 1
        #         else:
        #             nums[j] = 0
        #     ans += 1
        # print(nums)
        if sum(nums) == len(nums):
            return ans
        else:
            return -1