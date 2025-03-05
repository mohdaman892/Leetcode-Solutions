class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        k = n-1
        return 2*k*(k+1) + 1
        
        