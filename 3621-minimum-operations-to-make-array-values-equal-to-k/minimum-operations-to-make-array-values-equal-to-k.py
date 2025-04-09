class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        ans = 0
        s = set()
        for i in nums:
            if i not in s:
                if i<k:
                    return -1
                else:
                    if i>k:
                        ans+=1
                s.add(i)
        return ans