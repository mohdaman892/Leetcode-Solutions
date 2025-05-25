class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        ans = 0
        print(c)
        double_flag = True
        processed = set()
        for word in c.keys():
            if word[0]==word[1]:
                if c[word]==1:
                    if double_flag:
                        ans += 2
                        double_flag = False
                else:
                    ans += 2*(2*(c[word]//2))
                    if double_flag and c[word]%2==1:
                        ans += 2
                        double_flag = False
            else:
                rev = word[1]+word[0]
                if rev in c and rev not in processed and word not in processed:
                    ans += 4*min(c[word],c[rev])
                    processed.add(word)
                    processed.add(rev)
        
        return ans
        
