class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def f(i,c,a,n):
            if len(a) == c:
                s.add("".join(x for x in list(a)))
                return
            if i == n:
                return
            a.append(tiles[i])
            f(i+1,c,a,n)
            a.pop()
            f(i+1,c,a,n)


        n = len(tiles)
        ans = 0
        for c in range(1,n+1):
            s = set()
            f(0,c,[],n)
            s2 = set()
            for st in s:
                for st2 in set(permutations(st)):
                    s2.add(st2)
            ans += len(s2)

        
        return ans