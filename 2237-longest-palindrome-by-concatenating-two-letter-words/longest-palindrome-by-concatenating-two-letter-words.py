class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        s=set()
        c=Counter(words)
        k=0
        flag=0
        for i in range(len(words)):
            if words[i] in s:
                continue
            
            elif words[i][0]==words[i][1] and c[words[i]]>1:
                if c[words[i]]%2!=0 and flag==0:
                    flag=1
                    k+=2*c[words[i]]
                    s.add(words[i])
                elif c[words[i]]%2!=0 and flag==1:
                    k+=2*c[words[i]]-2
                    s.add(words[i])
                elif c[words[i]]%2==0:
                    k+=2*c[words[i]]
                    s.add(words[i])
            elif words[i][0]==words[i][1] and c[words[i]]==1 and flag==0:
                k+=2
                flag=1
                s.add(words[i])
            elif words[i][1]+words[i][0] in c and words[i][0]!=words[i][1]:
                k+=4*min(c[words[i]],c[words[i][1]+words[i][0]])
                s.add(words[i])
                s.add(words[i][1]+words[i][0])
        print(s)
        return k
            
                
                
        