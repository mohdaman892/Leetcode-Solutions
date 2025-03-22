class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node,arr):
            vis.add(node)
            if node in adj:
                for child in adj[node]:
                    if child not in vis:
                        arr.append(child)
                        dfs(child,arr)
        
        adj = defaultdict(list)
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        print(adj)
        vis = set()
        ans = 0
        for v in range(n):
            if v not in vis:
                comp_v = [v]
                dfs(v,comp_v)
                # print(comp_v)
                flag = True
                for i in comp_v:
                    if i in adj and len(adj[i])!=len(comp_v)-1:
                        flag = False
                        break
                if flag:
                    ans += 1
        
        return ans


