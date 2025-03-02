class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hm = {}
        for i in nums1:
            if i[0] not in hm:
                hm[i[0]] = i[1]
            else:
                hm[i[0]]+=i[1]
        for i in nums2:
            if i[0] not in hm:
                hm[i[0]] = i[1]
            else:
                hm[i[0]]+=i[1]
        ans = []
        for i in sorted(hm.keys()):
            ans.append([i,hm[i]])
        return ans