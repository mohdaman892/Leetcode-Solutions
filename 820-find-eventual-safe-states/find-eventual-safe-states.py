class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            self.vis[node] = 1
            self.pvis[node] = 1
            for i in graph[node]:
                if self.vis[i]==0:
                    x = dfs(i)
                    if x:
                        return True
                else:
                    if self.pvis[i]==1:
                        return True
            self.pvis[node] = 0
            self.check[node] = 1
            return False
            
        V = len(graph)
        self.vis = [0 for i in range(V)]
        self.pvis = [0 for i in range(V)]
        self.check = [0 for i in range(V)]
        ans = []
        for i in range(len(self.vis)):
            if self.vis[i] == 0:
                dfs(i)
        for i in range(len(self.check)):
            if self.check[i]==1:
                ans.append(i)
        return ans