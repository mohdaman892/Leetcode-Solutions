class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums:
            x = heappop(nums)
            if x>=k:
                break
            if nums:
                y = heappop(nums)
                heappush(nums,2*x+y)
            ans+=1
        return ans
            