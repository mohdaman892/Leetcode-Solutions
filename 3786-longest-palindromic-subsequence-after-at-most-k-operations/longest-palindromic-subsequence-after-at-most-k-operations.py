class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        @lru_cache(None)
        def f(i,j,k):
            if i>j:
                return 0
            ans = -sys.maxsize
            if s[i]==s[j]:
                l = 2
                if i==j:
                    l = 1
                ans = max(ans, l + f(i+1,j-1,k))
            else:
                if k>0:
                    if ord(s[j])>ord(s[i]):
                        x = min(ord(s[i])-ord('a')+1+ord('z')-ord(s[j]), ord(s[j])-ord(s[i]))
                    else:
                        x = min(ord('z')-ord(s[i])+1+ord(s[j])-ord('a'), ord(s[i])-ord(s[j]))
                    if x<=k:
                        ans = max(ans, 2 + f(i+1,j-1,k-x))
                ans = max(ans, 0 + max(f(i+1,j,k),f(i,j-1,k)))

            return ans


        n = len(s)
        return f(0,n-1,k)