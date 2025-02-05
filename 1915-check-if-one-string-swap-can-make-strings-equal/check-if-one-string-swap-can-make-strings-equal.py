class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1)!=Counter(s2):
            return False
        l1 = list(s1)
        l2 = list(s2)
        n = len(l1)
        for i in range(n):
            for j in range(i+1,n):
                l1[i],l1[j] = l1[j],l1[i]
                if l1 == l2:
                    return True
                l1[i],l1[j] = l1[j],l1[i]
        return False