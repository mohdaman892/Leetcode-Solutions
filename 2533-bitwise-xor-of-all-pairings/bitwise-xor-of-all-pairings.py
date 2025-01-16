class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        hm = defaultdict(int)

        for i in nums1:
            hm[i]+=(len(nums2))
        
        for i in nums2:
            hm[i]+=(len(nums1))
        

        ans = 0
        for i in hm:
            if hm[i]%2!=0:
                ans^=i
            
        return ans
        