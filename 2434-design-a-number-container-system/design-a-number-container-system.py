class NumberContainers:

    def __init__(self):
        self.ind_to_num = {}
        self.num_to_inds = {}
        

    def change(self, index: int, number: int) -> None:
        from sortedcontainers import SortedSet
        prev = None
        if index in self.ind_to_num:
            prev = self.ind_to_num[index]
        self.ind_to_num[index] = number
        if prev:
            self.num_to_inds[prev].discard(index)
            if not self.num_to_inds[prev]:
                self.num_to_inds.pop(prev)
        if number not in self.num_to_inds:
            self.num_to_inds[number] = SortedSet()
        self.num_to_inds[number].add(index)
        

    def find(self, number: int) -> int:
        if number not in self.num_to_inds:
            return -1
        for i in self.num_to_inds[number]:
            return i
        # return list(self.num_to_inds[number])[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)