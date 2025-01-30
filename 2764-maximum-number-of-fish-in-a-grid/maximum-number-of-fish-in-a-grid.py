class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(a,x,y,m,n):
            vis = [[False for j in range(m)] for i in range(n)]
            root = [x,y]
            q = deque([root])
            c = a[x][y]
            vis[x][y] = True
            while len(q)!=0:
                r = q.popleft()
                dx = [0,1,0,-1]
                dy = [1,0,-1,0]
                for i in range(len(dx)):
                    nx = r[0]+dx[i]
                    ny = r[1]+dy[i]
                    if nx>=0 and nx<n and ny>=0 and ny<m:
                        if not vis[nx][ny] and a[nx][ny]!=0:
                            vis[nx][ny] = True
                            c+=a[nx][ny]
                            q.append([nx,ny])
            print(c)
            return c
        
        
        m = len(grid[0])
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    ans = max(ans, bfs(grid,i,j,m,n))
        return ans