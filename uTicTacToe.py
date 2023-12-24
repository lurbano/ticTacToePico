import random

class winInfo:
    def __init__(self, winner=None, winBy=None, winIndex=None):
        self.winner = winner    # "X" or "O"
        self.winBy = winBy      # "row" or "col" or "dia"
        self.winIndex = winIndex    # int 
    def __str__(self):
        return f' Winner: {self.winner} by {self.winBy} {self.winIndex}'

class uTicTacToe:
    def __init__(self):
        self.resetBoard()

    def resetBoard(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.nMove = 0
        self.l_win = False
        self.player = "X"

    def switchPlayer(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def printBoard(self):
        print("-")
        for i in range(len(self.board)-1, -1, -1):
            print(self.board[i])

    def makeMove(self, r, c):
        if not self.isEmpty(r, c):
            return False
        # if self.nMove % 2 == 0:
        #     player = "X"
        # else:
        #     player = "O"
        self.board[r][c] = self.player
        self.nMove += 1
        self.l_win = self.winCheck()
        self.switchPlayer()
        #print("makeMove:", self.l_win)
        return True

    def isEmpty(self, r, c):
        ''' check  if a cell is empty'''
        if self.board[r][c] == " ":
            return True
        else: 
            return False
        
    def randMove(self):
        l_check = True
        while l_check:
            r = random.randint(0,2)
            c = random.randint(0,2)
            if self.isEmpty(r,c):
                l_check = False
        self.makeMove(r,c)

    def inputMove(self):
        l_legal = False 
        while not l_legal:
            rc = input("Enter move: r, c:")
            r, c = rc.split(",")
            r, c = int(r), int(c)
            if c < 0 or c > 2 or r < 0 or r > 2:
                print("Move out of bounds [0, 1, 2]. Try again.")
            else:
                l_legal = self.makeMove(r, c)
                if not l_legal:
                    print(f"Space already taken ({r}, {c}). Try again.")

    def winCheck(self):
        xWin = ["X", "X", "X"]
        oWin = ["O", "O", "O"]
        self.winfo = winInfo()
        # by row and colum
        for i in range(3):
            if self.board[i] ==  xWin:
                print("X wins") 
                self.winfo = winInfo("X", "row", i)
                return True
            if self.board[i] == oWin:
                print("O wins") 
                self.winfo = winInfo("O", "row", i)
                return True
            if [self.board[0][i],self.board[1][i],self.board[2][i]] == xWin:
                print("X wins", [self.board[0][i],self.board[0][i],self.board[0][i]]) 
                self.winfo = winInfo("X", "col", i)
                return True
            if [self.board[0][i],self.board[1][i],self.board[2][i]] == oWin:
                print("O wins", [self.board[i][1],self.board[i][1],self.board[i][1]]) 
                self.winfo = winInfo("O", "col", i)
                return True
        # diagonals 
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == xWin:
            print("X wins") 
            self.winfo = winInfo("X", "dia", 1)
            return True
        if [self.board[0][0], self.board[1][1], self.board[2][2]] == oWin:
            print("X wins") 
            self.winfo = winInfo("O", "dia", 1)
            return True
        if [self.board[2][0], self.board[1][1], self.board[0][2]] == xWin:
            print("X wins") 
            self.winfo = winInfo("X", "dia", 2)
            return True
        if [self.board[2][0], self.board[1][1], self.board[0][2]] == oWin:
            print("X wins") 
            self.winfo = winInfo("O", "dia", 2)
            return True
        return False
    
    def printWinInfo(self):
        print(self.winfo)
    
    def playGame(self, computerStrategy = "random", firstMove = "player", l_print=True):
        self.resetBoard()
        if l_print:
            self.printBoard()
        while self.nMove < 9: # maximum number of plays
            print("   nMove:", self.nMove)
            if firstMove == "player":
                self.inputMove()
            else:
                self.randMove()
            if self.nMove >= 9:
                break
            if self.l_win:
                print("You Win")
                self.printWinInfo()
                break
            if l_print:
                self.printBoard()

            if firstMove == "player":
                self.randMove()
            else:
                self.inputMove()
            if self.nMove >= 9:
                break
            if self.l_win:
                print("Computer Wins")
                self.printWinInfo()
                break 
            if l_print:
                self.printBoard()
        if not game.l_win:
            print("Game Tied")
        if l_print:
                self.printBoard()

            

#game = uTicTacToe()
#game.playGame()

# game.printBoard()
# game.makeMove(1,1)
# game.printBoard()
# game.randMove()
# game.printBoard()

# game.inputMove()
# game.printBoard()

# game.randMove()
# game.printBoard()

# game.inputMove()
# game.printBoard()
# game.winCheck()
