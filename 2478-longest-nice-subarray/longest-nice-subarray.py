class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            bits = bin(nums[i])[2:]
            bits = (32-len(bits))*"0"+bits
            nums[i] = bits
        hm = {}
        for i in range(len(nums[0])):
            if nums[0][i] == "1":
                hm[i] = 1
            else:
                hm[i] = 0
        

        i = 0
        ans = 1
        for j in range(1,n):
            for k in range(len(nums[j])):
                if nums[j][k]=="1":
                    if hm[k]==1:
                        while i<j:
                            flag = False
                            for x in range(len(nums[i])):
                                if nums[i][x] == "1":
                                    if x == k:
                                        flag = True
                                    hm[x] = 0
                            if flag:
                                i+=1
                                break
                            i+=1
            ans = max(ans,j-i+1)
            for k in range(len(nums[j])):
                if nums[j][k] == "1":
                    hm[k] = 1
            
        ans = max(ans,n-i)
        return ans