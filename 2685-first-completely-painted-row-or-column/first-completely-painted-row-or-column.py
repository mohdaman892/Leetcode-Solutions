class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hm1 = {}
        hm2 = {}
        hm3 = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hm3[mat[i][j]] = [i,j]
        for i in range(len(arr)):
            # print(hm1,hm2)
            k = hm3[arr[i]]
            if k[0] not in hm1:
                hm1[k[0]] = [-1]
            else:
                hm1[k[0]].append(-1)
            if len(hm1[k[0]])==len(mat[0]):
                return i
            if k[1] not in hm2:
                hm2[k[1]] = [-1]
            else:
                hm2[k[1]].append(-1)
            if len(hm2[k[1]])==len(mat):
                return i
        return i
            
