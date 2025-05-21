class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fr = False
        fc = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0:
                        fr = True
                    if j==0:
                        fc = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
                    
        if fr:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if fc:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        return matrix