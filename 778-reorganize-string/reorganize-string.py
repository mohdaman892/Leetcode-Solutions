class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        n = len(s)
        max_v = max(c.values())
        max_c = None
        for i in c:
            if c[i]==max_v:
                max_c = i
                break
        if len(s)-c[max_c]<c[max_c]-1:
            return ""
        
        l = [max_c]*c[max_c]
        c.pop(max_c)
        # print(c)
        xx = []
        for i in c:
            xx.extend(list(i*c[i]))
        # print(l,xx)
        while xx:
            # print(l,xx)
            x = len(l)
            for j in range(1,2*x,2):
                if not xx:
                    return "".join(i for i in l)
                l.insert(j,xx.pop())

        return "".join(i for i in l)