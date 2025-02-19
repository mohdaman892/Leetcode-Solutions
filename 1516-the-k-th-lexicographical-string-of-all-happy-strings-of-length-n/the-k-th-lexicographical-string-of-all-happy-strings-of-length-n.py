class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def f(i):
            if i == n:
                st = "".join(j for j in list(a))
                self.b.append(st)
                return
            
            for x in ["a","b","c"]:
                if not a or x != a[-1]:
                    a.append(x)
                    f(i+1)
                    a.pop()

        a = []
        self.b = []
        f(0)
        self.b.sort()
        # print(self.b)
        if k>len(self.b):
            return ""
        return self.b[k-1]
        