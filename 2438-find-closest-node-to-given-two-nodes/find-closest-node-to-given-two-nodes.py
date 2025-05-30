class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def find_distance(src,adj):
            dist = [sys.maxsize for i in range(len(edges))]
            vis = [False for i in range(len(edges))]
            q = deque([[0,src]])
            dist[src] = 0
            while len(q)!=0:
                r = q.popleft()
                d = r[0]
                x = r[1]
                for i in adj[x]:
                    if i==-1:
                        break
                    if vis[i]:
                        break
                    else:
                        if d+1<dist[i]:
                            dist[i] = d+1
                            q.append([d+1,i])
            return dist
            
        adj = [[] for i in range(len(edges))]
        [adj[i].append(edges[i]) for i in range(len(edges))]
        a,b = find_distance(node1,adj),find_distance(node2,adj)
        x = 0
        m = sys.maxsize
        for i in range(len(a)):
            if max(a[i],b[i])<m:
                x = i
                m = max(a[i],b[i])
        if m==sys.maxsize:
            return -1
        return x