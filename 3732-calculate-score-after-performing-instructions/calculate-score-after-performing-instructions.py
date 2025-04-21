class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        x = 0
        i = 0
        s = 0
        n = len(values)
        vis = set()
        while i>=0 and i<n and i not in vis:
            k = instructions[i]
            vis.add(i)
            if k=="add":
                s += values[i]
                i += 1
            else:
                i += values[i]        
        
        return s