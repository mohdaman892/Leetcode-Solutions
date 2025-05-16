class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        def hamm(a,b):
            x = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    x += 1
            return x

        n = len(words)
        dp = [1 for i in range(n+1)]
        back = [-1 for i in range(n)]
        ans = 1
        last_ind = 0
        for i in range(n):
            for p in range(i+1):
                if (groups[i]!=groups[p] and len(words[i]) == len(words[p]) and hamm(words[i],words[p])==1):
                    if 1 + dp[p] > dp[i]:
                        dp[i] = 1 + dp[p]
                        back[i] = p
            if dp[i] > ans:
                ans = dp[i]
                last_ind = i
        # print(dp,back,last_ind)
        ans = []
        while last_ind!=-1:
            ans.insert(0,words[last_ind])
            last_ind = back[last_ind]
        return ans