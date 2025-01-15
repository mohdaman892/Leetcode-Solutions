class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        num1,num2 = bin(num1)[2:],bin(num2)[2:]

        n = max(len(num1),len(num2))

        num1,num2 = "0"*(n-len(num1))+num1,"0"*(n-len(num2))+num2   # Balancing bits

        k = num2.count("1") # Counting 1's

        ans = []

        for i in range(len(num1)):  # Left-right if we have 1's and set-bits remaining we set it
            if num1[i]=="1":
                if k>0:
                    ans.append("1")
                    k-=1
                else:
                    ans.append("0")
            else:
                ans.append("0")

        for i in range(len(ans)-1,-1,-1):  # Right-left if we have remaining set bit we set the smallest unset bits 
            if ans[i]=="0" and k>0:
                ans[i] = "1"
                k-=1

        ans = "".join(x for x in ans)

        return int(ans,2)
        