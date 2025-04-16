class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        i = 0
        n = len(nums)
        hm = {}
        c = 0
        ans = 0
        for j in range(n):
            if nums[j] not in hm:
                hm[nums[j]] = 0
            c += hm[nums[j]]
            hm[nums[j]] += 1
            while i<j and c>=k:
                ans += n-j
                hm[nums[i]]-=1
                c -= hm[nums[i]]
                i += 1
        
        return ans