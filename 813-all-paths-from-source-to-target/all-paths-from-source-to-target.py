class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def f(root):
            if root == n-1:
                self.ans.append(list(a))
                return

            for node in graph[root]:
                if not vis[node]:
                    vis[node] = 1
                    a.append(node)
                    f(node)
                    vis[node] = 0
                    a.pop()


        self.ans = []
        a = [0]
        n = len(graph)
        vis = [0 for i in range(n)]
        vis[0] = 1
        f(0)
        return self.ans