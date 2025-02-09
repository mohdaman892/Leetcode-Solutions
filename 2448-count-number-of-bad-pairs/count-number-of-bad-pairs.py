class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            nums[i]=nums[i]-i
        print(nums)
        c = 0
        d = Counter(nums)
        for i in d:
            if d[i]>1:
                c+=math.factorial(d[i])//(2*math.factorial((d[i]-2)))
        print(c)
        total = math.factorial(len(nums))//(2*math.factorial((len(nums)-2)))
        print(total)
        return total-c
        