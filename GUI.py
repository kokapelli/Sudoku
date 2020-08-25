################################################
# Contains all GUI elements of the Sudoku game #
################################################

from tkinter import *
from Square import Square
from Logic import Logic

class GUI():
    def __init__(self, game, solution):
        self.game = game
        self.solution = solution

        self.width = 540
        self.height = 540
        self.squares = dict()
        self.squareNr = 9
        self.squareDim = self.width // self.squareNr

        self.createBoard()
        self.setSquares()
        self.board.pack()
        self.board.bind("<Key>", self.keyboardInput)
        self.board.bind("<Button-1>", self.squareClick)

        self.logic = Logic(self.squares)
        self.highlightedSquare = None

        self.draw()

    def createBoard(self):        
        self.master = Tk()
        self.master.resizable(False, False)
        self.master.title("Falk: Sudoku")
        self.master.configure(background="black")
        self.board = Canvas(self.master, bg="white", highlightthickness=0, width = self.width, height = self.height)

    def setSquares(self):
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                x1 = self.squareDim*col
                y1 = self.squareDim*row
                x2 = self.squareDim*(col+1)
                y2 = self.squareDim*(row+1)

                textX = x1 + self.squareDim/2
                textY = y1 + self.squareDim/2

                self.squares[(row, col)] = Square(x1, y1, x2, y2, textX, textY, (row, col), self)
                self.board.create_rectangle(x1, y1, x2, y2, fill="white")
        
        self.assignBoardNumbers()
        
    def draw(self):
        self.resetBoard()

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

        self.setThickSquareLines()
        
        if(self.logic.isGameWon()):
            self.winner()

    def assignBoardNumbers(self):
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                currVal = self.game[row][col]
                if(currVal == 0):
                    self.squares[(row, col)].setNumber(self.game[row][col])
                else:
                    self.squares[(row, col)].setHardCodedNumber(self.game[row][col])

    def winner(self):
            l = Label(self.master, bg="#d0ffba", text="Sudoku Completed!", font=("Helvetica", 30)) 
            l.place(relx = 0.5, rely = 0.5, anchor = 'center')
            l.config(width=self.width)

    def newGame(self):
        destroy(self.master)


    def resetBoard(self):
        self.board.delete("all")

    def setThickSquareLines(self):
        # Three thick boxes on each row
        boxSpacing = self.width / 3
        for col in range(1, 4):
            self.board.create_line(boxSpacing*col, 0, boxSpacing*col, self.height, width=3)
        for row in range(1, 4):
            self.board.create_line(0, boxSpacing*row, self.width, boxSpacing*row, width=3)

    ##################################
    ###    User input functions    ###
    ##################################

    def squareClick(self, event):
        selected_column = int(event.x / self.squareDim)
        selected_row    = int(event.y / self.squareDim)
        try:
            if(not self.logic.won):
                self.board.focus_set()
                self.highlightedSquare = (selected_row, selected_column)
                #print(f"Clicked:  {self.highlightedSquare}")
            else:
                self.master.destroy()
        except:
            pass

        self.draw()

    def keyboardInput(self, event):
        try:
            #print(f"Pressed: {repr(event.char)}")
            self.squares[self.highlightedSquare].setNumber(int(event.char))
        except:
            pass

        self.draw()
