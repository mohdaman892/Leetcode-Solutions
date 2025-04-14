class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def f(x,y,z,vis):
            if grid[x][y] == 2:
                if z==zeros:
                    self.ans += 1
                return
            if grid[x][y] == -1:
                return
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            c = 1 if grid[x][y] == 0 else 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<m and not vis[nx][ny]:
                   vis[nx][ny] = 1
                   f(nx,ny,z+c,vis) 
                   vis[nx][ny] = 0
        
        
        zeros = 0
        n = len(grid)
        m = len(grid[0])
        a,b = -1,-1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zeros += 1
                elif grid[i][j] == 1:
                    a,b = i,j
                
        self.ans = 0
        vis = [[0 for i in range(m)] for i in range(n)]
        vis[a][b] = 1
        f(a,b,0,vis)
        return self.ans