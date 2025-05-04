class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:

        def f(st,c,k):
            if k==1:
                grid[st[0]][st[1]] = c
                return
                
            p,q = st[0],st[1]
            l = k//2
            f([p+0,q+0],c,l)
            f([p+l,q+0],c-l*l,l)
            f([p+l,q+l],c-2*l*l,l)
            f([p+0,q+l],c-3*l*l,l)




        grid = [[0 for i in range(2**n)] for j in range(2**n)]

        k = 2**n
        c = 2**(2*n)-1

        print(c,k)
        
        f([0,0],c,k)

        return grid

        
            

        