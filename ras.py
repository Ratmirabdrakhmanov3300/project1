class Queen:

    def __init__(self):
        self.brd = []
        for i in range(8):
            line = []
            for j in range(8):
                line.append(0)
            self.brd.append(line)
        self.solve(0)
#        self.print_brd()

    def print_brd(self):
        for line in self.brd:
            print(line)
        print()

    def solve(self, col):
        if col >=8:
            self.print_brd()
            return True
        else:
            for row in range(8):
                if self.check(row, col):
                    self.brd[col][row] = 1
                    if self.solve(col+1):
                        return True
                    self.brd[col][row] = 0
        return False

    def check(self, row, col):
        for i in range(col): # проверка строки
            if self.brd[i][row]==1:
                return False
        for i in range(col):
            j = (row - col) + i
            if j>=0 and j<8 and self.brd[i][j]==1:
                return False
            k = (row + col) - i
            if k>=0 and k<8 and self.brd[i][k]==1:
                return False
        return True
