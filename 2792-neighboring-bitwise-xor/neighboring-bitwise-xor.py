class Solution:
    def doesValidArrayExist(self, arr: List[int]) -> bool:
        n = len(arr)
        first = None
        curr = None
        if n==1:
            if arr[0]==1:
                return False
            else:
                return True
        for i in range(n):
            if i==0:
                if arr[i]==0:
                    first,curr = 0,0
                else:
                    first,cuur = 0,1
            elif i==n-1:
                if arr[i]==0:
                    if curr!=first:
                            return False
                else:
                    if curr==first:
                        return False
            else:
                if arr[i]==0:
                    curr = curr
                else:
                    curr = 1 if curr==0 else 0
        return True