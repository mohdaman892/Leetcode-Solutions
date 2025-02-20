class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def f(n,s):
            if n==0:
                if s not in b:
                    return s
                else:
                    return ""
            k = s+"0"
            x = f(n-1,s+"0")
            if x!="":
                return x
            k = s[:-1] + "1"
            y = f(n-1,s+"1")
            return y
        
        
        s = ""
        b = set(nums)
        return f(len(nums),s)