class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        total = sum(grid[0])
        pre = 0
        ans = sys.maxsize
        for i in range(n):
            pre += grid[1][i]
            total -= grid[0][i]
            ans = min(ans,max(pre-grid[1][i],total))
        return ans

