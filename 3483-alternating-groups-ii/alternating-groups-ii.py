class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors[:k-1]
        print(colors)
        i = 0
        j = 1
        n = len(colors)
        ans = 0
        while j<n:
            if colors[j]!=colors[j-1]:
                if j-i+1 == k:
                    ans += 1
                    i+=1
                else:
                    j+=1
            else:
                i = j
                j = i+1

        return ans