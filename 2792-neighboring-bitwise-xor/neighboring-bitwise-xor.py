class Solution:
    def doesValidArrayExist(self, arr: List[int]) -> bool:
        n = len(arr)
        a = []
        if n==1:
            if arr[0]==1:
                return False
            else:
                return True
        for i in range(n):
            if i==0:
                if arr[i]==0:
                    a.append(0)
                    a.append(0)
                else:
                    a.append(0)
                    a.append(1)
            elif i==n-1:
                if arr[i]==0:
                    if a[-1]!=a[0]:
                            return False
                else:
                    if a[-1]==a[0]:
                        return False
            else:
                if arr[i]==0:
                    a.append(a[-1])
                else:
                    k = 1 if a[-1]==0 else 0
                    a.append(k)
        return True