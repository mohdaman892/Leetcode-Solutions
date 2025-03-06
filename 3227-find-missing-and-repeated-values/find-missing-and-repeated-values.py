class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = set([i for i in range(1,n**2+1)])
        ans = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in s:
                    ans.append(grid[i][j])
                else:
                    s.discard(grid[i][j])
        ans.append(list(s)[0])
        return ans