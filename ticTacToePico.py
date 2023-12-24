# Goes with programming lessons on: https://soriki.com/pico/
# Lensyl Urbano

import board
import time
import digitalio
from ledPixelsPico import *
from uTicTacToe import *


class TicTacToeBoardPico(ledPixels):
    def __init__(self, ledPin=board.GP15,
                 rPins=[board.GP0, board.GP1,board.GP2],
                 cPins=[board.GP5, board.GP4, board.GP3]):
        '''
        rPins and cPins are in order of the grid on the board
        '''
        
        ledPixels.__init__(self, nPix=3*3, ledPin=ledPin)
        # self.ledPix = ledPixels(9, board.GP15)
        self.off()
        
        self.row = []
        self.col = []
        for i in range(3):
            self.row.append( digitalio.DigitalInOut(rPins[i]))
            self.col.append( digitalio.DigitalInOut(cPins[i]))
        
        self.grid = [ [False, False, False], 
                      [False, False, False], 
                      [False, False, False] ]
        
    def get_n(self, r, c):
        n = r*3 + c
        return n
    
    def lightRC(self, r, c, col=(100,0,0)):
        n = self.get_n(r,c)
        self.light(n, col)

    def check_sensor(self, r, c):
        check = False
        n = self.get_n(r,c)
        self.col[c].direction = digitalio.Direction.OUTPUT
        self.col[c].value = True
        self.row[r].direction = digitalio.Direction.INPUT
        self.row[r].pull = digitalio.Pull.UP
        if self.row[r].value:
            check = True
        else:
            check = False
        self.col[c].value = False   
        return (check, n)
    
    def check_grid(self, l_light=True ):
        for r in range(3):
            for c in range(3):
                self.grid[r][c], n = self.check_sensor(r,c)
                if l_light and self.grid[r][c]:
                    self.light(n, (200,200,0))
                else:
                    self.light(n, (200,0,0))
                
        return self.grid
    
    def gameStart(self):
        self.game = uTicTacToe()
        
    def gameShowBoard(self):
        for r in range(3):
            for c in range(3):
                if self.game.board[r][c] == "X":
                    self.lightRC(r,c, (200,0,0))
                elif self.game.board[r][c] == "O":
                    self.lightRC(r,c, (0,200,0))
                else:
                    self.lightRC(r,c, (100,100,0))
                    
    def gameDetectMove(self):
        l_empty = True
        for r in range(3):
            for c in range(3):
                if not (self.game.board[r][c] in "XO"):
                    l_empty, n = self.check_sensor(r,c)
                    self.grid[r][c] = l_empty
                    if l_empty == False:
                        return l_empty, r, c
        return l_empty, None, None
                    
    def getMagMove(self):
        l_check = True
        while l_check:
            l_empty, r, c = self.gameDetectMove()
            if l_empty == False:
                l_check = False
                self.game.makeMove(r,c)
                self.game.printBoard()
                self.gameShowBoard()
                
    def playMagGame(self):
        while not self.game.l_win:
            self.getMagMove()
                

        
if __name__ == '__main__':

    board = TicTacToeBoardPico()
    board.gameStart()
    board.gameShowBoard()
    board.playMagGame()


# for i in range(500):
#     print(i)
#     g = board.check_grid()
#     for r in range(2, -1, -1):
#         print(g[r])
#     
#     
#     time.sleep(0.5)



