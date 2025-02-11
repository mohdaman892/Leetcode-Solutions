class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        a = []
        n = len(s)
        for i in range(n):
            # print(a)
            if s[i] == part[-1]:
                a.append(s[i])
                j = len(part)-1
                b = []
                while a and j>=0:
                    if a[-1] == part[j]:
                        b.insert(0,a.pop())
                    else:
                        break
                    j-=1
                if len(b) != len(part):
                    a.extend(b)
            else:
                a.append(s[i])
        
        return "".join(x for x in a)