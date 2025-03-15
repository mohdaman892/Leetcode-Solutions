class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for i in range(26)] for j in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        a,b = ord(cell[0])-ord('A'), int(cell[1:])-1
        self.sheet[b][a] = value

    def resetCell(self, cell: str) -> None:
        a,b = ord(cell[0])-ord('A'), int(cell[1:])-1
        self.sheet[b][a] = 0

    def getValue(self, formula: str) -> int:
        cell,r = formula.lstrip("=").split("+")
        ans = 0
        if cell.isdigit():
            ans += int(cell)
        else:
            a,b = ord(cell[0])-ord('A'), int(cell[1:])-1
            ans += self.sheet[b][a]
        if r.isdigit():
            ans += int(r)
        else:
            a,b = ord(r[0])-ord('A'), int(r[1:])-1
            ans += self.sheet[b][a]
        return ans    


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)