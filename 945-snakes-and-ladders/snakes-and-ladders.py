class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def convert(_next):
            if (_next//n)%2 == 0:
                nx,ny = n - 1 - _next//n, _next%n-1
            else:
                nx,ny = n - 1 - _next//n, n - _next%n
            if _next%n == 0:
                nx += 1
                if (_next//n)%2==0:
                    ny+=1
                else:
                    ny -= 1
            return nx,ny
        
        n = len(board)
        vis = {1}
        k = n*n
        dist = [sys.maxsize for i in range(k+1)]
        dist[1] = 0
        q = deque([[1,0]])

        while q:
            r = q.popleft()
            # print(r)
            for i in range(r[0]+1,min(r[0]+6,k)+1):
                if i<=0 or i>=k+1:
                    continue
                x,y = convert(i)
                new_pos = board[x][y] if board[x][y]!=-1 else i
                if new_pos not in vis:
                    if r[1]+1<dist[new_pos]:
                        dist[new_pos] = r[1]+1
                        vis.add(new_pos)
                        q.append([new_pos, dist[new_pos]])
        
        if dist[k] == sys.maxsize:
            return -1
        return dist[k]

