class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        r = [0 for i in range(n)]
        c = [0 for i in range(m)]

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r[i]+=1
                    c[j]+=1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if r[i]>1 or c[j]>1:
                        ans+=1
        return ans

