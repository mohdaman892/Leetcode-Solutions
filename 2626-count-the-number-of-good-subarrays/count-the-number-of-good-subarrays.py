class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = pairs = ans = 0
        N = len(nums)
        hm = defaultdict(int)
        for right in range(N):
            pairs += hm[nums[right]]
            hm[nums[right]] += 1
            while left<right and pairs>=k:
                ans += N-right
                hm[nums[left]]-=1
                pairs -= hm[nums[left]]
                left += 1
        return ans