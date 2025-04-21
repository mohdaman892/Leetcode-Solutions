class Solution:
    def numberOfArrays(self, diff: List[int], l: int, r: int) -> int:
        x = 0
        a,b = 0,0
        for i in diff:
            x += i
            a = min(a,x)
            b = max(b,x)
        print(a,b)
        a = l-a
        b = r-b
        if a>b:
            return 0
        
        return b-a+1
