class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def f(i,s):
            if i==n//2:
                if n%2!=0:
                    for x in range(10):
                        ps = s + str(x) + s[-1:0:-1] + s[0]
                        if int(ps)%k==0:
                            a.append(int(ps))
                else:
                    ps = s + s[-1:0:-1] + s[0]
                    if int(ps)%k==0:
                        a.append(int(ps))
                return

            lo = 1 if i == 0 else 0
            for j in range(lo,10):
                f(i+1,s+str(j))

        if n==1:
            ans = 0
            for i in range(1,10):
                if i%k==0:
                    ans += 1
            return ans

        a = []
        f(0,"")
        # print(a)
        # print(len(a))
        hs = set()
        ans = 0
        for i in a:
            # print(hs,ans)
            s = str(i)
            l = "".join(x for x in sorted(list(s)))
            if l in hs:
                continue
            else:
                hs.add(l)
            c = Counter(s)
            # print(c)
            duplicate_fac_1 = 1
            for j in c.values():
                if j>=2:
                    duplicate_fac_1 *= factorial(j)
            duplicate_fac_2 = 1
            for j in c:
                if j!="0" and c[j]>=2:
                    duplicate_fac_2 *= factorial(c[j])
            ans += (factorial(len(s))//duplicate_fac_1)
            if "0" in c:
                if c["0"]>=2:
                    duplicate_fac_2 *= factorial(c["0"]-1) 
                ans -= (factorial(len(s)-1)//duplicate_fac_2)

        return ans


                