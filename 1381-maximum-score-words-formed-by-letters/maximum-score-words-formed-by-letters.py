class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def f(i,s,c):
            if i==n:
                return s
            
            flag = True
            d = deepcopy(c)
            sc = 0
            for j in words[i]:
                if j not in d:
                    flag = False
                    break
                if d[j] == 0:
                    flag = False
                    break
                sc += score[ord(j)-ord('a')]
                d[j]-=1
            if flag:
                return max(f(i+1,s+sc,d),f(i+1,s,c))
            else:
                return f(i+1,s,c)


        c = Counter(letters)
        n = len(words)
        return f(0,0,c)