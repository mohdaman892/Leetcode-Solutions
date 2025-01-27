class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
        child = {}
        # print(adj)
        for i in range(n):
            children = set()
            q = deque([i])
            vis = set()
            vis.add(i)
            while q:
                r = q.popleft()
                for node in adj[r]:
                    if node not in vis:
                        children.add(node)
                        q.append(node)
                        vis.add(node)
            child[i] = children
        ans = []
        # print(child)
        for q in queries:
            ans.append(q[1] in child[q[0]])
        return ans
            
