class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        h=[]
        c=0
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                c+=1
            else:
                h.append(i)
        for i in range(c):
            l.append(pivot)
        for j in h:
            l.append(j)
        return l
        