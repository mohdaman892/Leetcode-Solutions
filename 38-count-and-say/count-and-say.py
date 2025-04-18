class Solution:
    def countAndSay(self, n: int) -> str:
        def count(x):
            c = 1
            s = ""
            k = x[0]
            if len(x)==1:
                s+=str(c)+k
                return s
            for i in range(1,len(x)):
                if x[i]==k:
                    c+=1
                else:
                    s+=str(c)+k
                    c = 1
                    k = x[i]
            s+=str(c)+k
            return s
        
        def f(a,s):
            if a==n:
                return s
            s = count(s)
            return f(a+1,s)
        
        return f(1,"1")
            
