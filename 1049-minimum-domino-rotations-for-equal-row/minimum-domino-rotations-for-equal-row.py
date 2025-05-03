class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:




        n = len(tops)
        k = tops[0]
        flag1 = True
        flag3 = True
        a,c = 0,1
        for i in range(1,n):
            if tops[i]!=k:
                if bottoms[i]==k:
                    a += 1
                else:
                    flag1 = False
            if bottoms[i]!=k:
                if tops[i]==k:
                    c += 1
                else:
                    flag3 = False

        k = bottoms[0]
        flag2,flag4 = True,True
        b,d = 0,1
        for i in range(1,n):
            if bottoms[i]!=k:
                if tops[i]==k:
                    b+=1
                else:
                    flag2 = False
            if tops[i]!=k:
                if bottoms[i]==k:
                    d+=1
                else:
                    flag4 = False

        x = [flag1,flag2,flag3,flag4]
        y = [a,b,c,d]


        ans = sys.maxsize
        for i in range(len(x)):
            if x[i]:
                ans = min(ans, y[i])
        
        if ans == sys.maxsize:
            return -1
        
        return ans