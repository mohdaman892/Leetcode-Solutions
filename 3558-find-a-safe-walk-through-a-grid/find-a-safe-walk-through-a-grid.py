class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        vis[0][0] = 1
        dist = [[sys.maxsize for i in range(m)] for j in range(n)]
        if grid[0][0] == 1:
            dist[0][0] = 1
        else:
            dist[0][0] = 0
        pq = [[0,0,dist[0][0]]]
        heapify(pq)
        while pq:
            r = heappop(pq)
            x,y = r[0],r[1]
            dx = [0,1,0,-1]
            dy = [1,0,-1,0]
            for i in range(len(dx)):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx>=0 and ny>=0 and nx<n and ny<m:
                    d = 0
                    if grid[nx][ny]==1:
                        d = 1
                    if r[2]+d<dist[nx][ny]:
                        dist[nx][ny] = r[2]+d
                        heappush(pq,[nx,ny,r[2]+d])
        return health-dist[n-1][m-1]>=1