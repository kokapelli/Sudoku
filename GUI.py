from tkinter import *
from Square import Square

hardcodeTest = ((0, 0), (7, 7), (3, 6), (6, 3))

testGame = [[9,0,0,3,0,5,0,0,0],
            [0,3,0,0,0,7,0,0,6],
            [0,7,5,4,1,0,9,3,9],
            [0,0,0,6,4,2,0,0,0],
            [1,0,0,0,0,0,0,0,4],
            [0,0,0,1,3,8,0,0,0],
            [0,1,9,0,7,3,2,4,0],
            [3,0,0,2,0,0,0,6,0],
            [0,0,0,9,0,4,0,0,7]]

class GUI():
    def __init__(self):
        self.width = 540
        self.height = 540
        self.squareNr = 9
        self.squareDim = self.width // self.squareNr

        self.createBoard()
        self.setSquares()
        self.board.pack()
        self.board.bind("<Key>", self.keyboardInput)
        self.board.bind("<Button-1>", self.squareClick)

        self.highlightedSquare = None
        self.draw()

    def createBoard(self):        
        self.master = Tk()
        self.master.resizable(False, False)
        self.master.title("Sewdewko")
        self.master.configure(background="black")
        self.board = Canvas(self.master, bg="white", highlightthickness=0, width = self.width, height = self.height)

    def setSquares(self):
        self.squares = {}
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                x1 = self.squareDim*col
                y1 = self.squareDim*row
                x2 = self.squareDim*(col+1)
                y2 = self.squareDim*(row+1)

                textX = x1 + self.squareDim/2
                textY = y1 + self.squareDim/2
                
                # Crude solution, will be refactored.
                if((row, col) in hardcodeTest):
                    self.squares[(row, col)] = Square(x1, y1, x2, y2, textX, textY, (row, col), self)
                
                else:
                    self.squares[(row, col)] = Square(x1, y1, x2, y2, textX, textY, (row, col), self)

                #Enter random number sudoku "inputter"
                self.board.create_rectangle(x1, y1, x2, y2, fill="white")
                
                self.setThickSquareLine()

        
        self.assignBoardNumbers()
        
    def draw(self):
        self.board.delete("all")

        self.isValidRow(0)
        self.isValidCol(1)
        self.isValidSquare(0)

        for row in range(self.squareNr):
            for col in range(self.squareNr):
                currSquare = self.squares[(row, col)]
                number = currSquare.getNumber()
                x1, y1, x2, y2, textX, textY = currSquare.getGUISquareCoords()
                
                if (self.highlightedSquare is not None and self.highlightedSquare == (row, col) and not currSquare.getHardcoded()):
                    self.board.create_rectangle(x1, y1, x2, y2, fill="beige")
                    if(number):
                        self.board.create_text(textX, textY, font=("Purisa", 30), text=number)
                else:
                    if(currSquare.getHardcoded()):
                        self.board.create_rectangle(x1, y1, x2, y2, fill="#e6e6e6")
                    else:
                        self.board.create_rectangle(x1, y1, x2, y2, fill="white")
                    if(number):
                        self.board.create_text(textX, textY, font=("Purisa", 30), text=number)

        self.setThickSquareLine()

    def squareClick(self, event):
        selected_column = int(event.x / self.squareDim)
        selected_row    = int(event.y / self.squareDim)
        try:
            self.board.focus_set()
            self.highlightedSquare = (selected_row, selected_column)
            print(f"Clicked:  {self.highlightedSquare}")
        except:
            pass

        self.draw()

    def keyboardInput(self, event):
        try:
            print(f"Pressed: {repr(event.char)}")
            self.squares[self.highlightedSquare].setNumber(int(event.char))
        except:
            pass

        self.draw()

    def setThickSquareLine(self):
        # Three thick boxes on each row
        boxSpacing = self.width / 3
        for col in range(1, 4):
            self.board.create_line(boxSpacing*col, 0, boxSpacing*col, self.height, width=3)
        for row in range(1, 4):
            self.board.create_line(0, boxSpacing*row, self.width, boxSpacing*row, width=3)


    def getRowNumbers(self, row):
        rowNumbers = list()
        for i in range(self.squareNr):
            rowNumbers.append(self.squares[(row, i)].getNumber())

        return rowNumbers

    def getColNumbers(self, col):
        colNumbers = list()
        for i in range(self.squareNr):
            colNumbers.append(self.squares[(i, col)].getNumber())

        return colNumbers

    def getSquareNumbers(self, square):
        squareNumbers = list()
        boxSize = int(self.squareNr / 3)
        rowLevel = 0

        # Consider revising this solution, better solutions exist
        if(2 < square <= 5):
            rowLevel = 1

        elif(5 < square <= 8):
            rowLevel = 2
                
        colLevel = square % 3
        
        for row in range(boxSize*rowLevel, boxSize*rowLevel + boxSize):
            for col in range(boxSize*colLevel, boxSize*colLevel + boxSize):
                squareNumbers.append(self.squares[(row, col)].getNumber())

        return squareNumbers

    # Consider creating superclasses for the three checks
    def isValidSquare(self, square):
        n = set(self.getSquareNumbers(square))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            print(n)
            return True

    def isValidRow(self, row):
        n = set(self.getRowNumbers(row))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            print(n)
            return True

    def isValidCol(self, col):
        n = set(self.getColNumbers(col))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            print(n)
            return True

    def assignBoardNumbers(self):
        game = self.createRandomGame()
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                currVal = game[row][col]
                if(currVal == 0):
                    self.squares[(row, col)].setNumber(game[row][col])
                else:
                    self.squares[(row, col)].setHardCodedNumber(game[row][col])



    # Will create randomized games in the future
    def createRandomGame(self):
        return testGame

def main():
    board = GUI()
    board.master.mainloop()

if __name__ == "__main__":
    main()
