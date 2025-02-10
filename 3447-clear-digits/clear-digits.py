class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                for j in range(i,-1,-1):
                    if s[j].isalpha():
                        s[j] = "-1"
                        s[i] = "-1"
                        break
        ans = ""
        for i in s:
            if i!="-1":
                ans += i
        return ans