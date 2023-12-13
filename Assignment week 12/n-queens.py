class Queens:
    def __init__(self):
        self.n = 4
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        
    def possible(self,row,col):
        if 1 in self.board[row][0:]:return False 
        i,j = row,col
        while i and j:
            if self.board[i][j] == 1:return False
            i-=1
            j-=1
        i,j = row,col
        while i <self.n and j > -1:
            if self.board[i][j] == 1:return False
            i+=1
            j-=1
        return True
    
    def solution(self,col):
        if col >=self.n:return True
        for i in range(self.n):
            if self.possible(i,col):
                self.board[i][col] = 1
                if self.solution(col+1):
                    return True
                self.board[i][col] = 0
        return False
    
    def get_answer(self):
        if not self.solution(0):
            return -1
        return self.board


obj = Queens()
final = obj.get_answer()

for i in range(len(final)):
    print(final[i])

        