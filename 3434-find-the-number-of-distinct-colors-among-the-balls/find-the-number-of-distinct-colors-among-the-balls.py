class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hm1 = {}
        hm2 = {}
        ans = []
        for query in queries:
            x,y = query[0],query[1]
            prev = None
            if x in hm1:
                prev = hm1[x]
            if prev:
                hm2[prev]-=1
                if hm2[prev]==0:
                    hm2.pop(prev)
            hm1[x] = y
            if y not in hm2:
                hm2[y] = 0
            hm2[y] += 1
            # print(hm1,hm2)
            ans.append(len(hm2))
        
        return ans
            
