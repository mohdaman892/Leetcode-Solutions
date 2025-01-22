class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        ans = [[0 for i in range(m)] for i in range(n)]
        vis = [[0 for i in range(m)] for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i,j,0])
                    vis[i][j] = 1
        while q:
            r = q.popleft()
            x,y,d = r[0],r[1],r[2]
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<m and not vis[nx][ny] and grid[nx][ny]==0:
                    ans[nx][ny] = d+1
                    vis[nx][ny] = 1
                    q.append([nx,ny,ans[nx][ny]])
        
        return ans


