class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        @lru_cache(None)
        def f(i,j,h):
            if h==0:
                return False
            if i==n-1 and j==m-1:
                return h>=1
            

            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            ans = False
            for x in range(len(dx)):
                nx = i+dx[x]
                ny = j+dy[x]
                if nx>=0 and nx<n and ny>=0 and ny<m and not vis[nx][ny]:
                    vis[nx][ny] = 1
                    if grid[nx][ny] == 1:
                        ans |= f(nx,ny,h-1)
                    else:
                        ans |= f(nx,ny,h)
                    vis[nx][ny] = 0
            return ans




        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        vis[0][0] = 1
        if grid[0][0] == 1:
            health-=1
        return f(0,0,health)