from tkinter import *


class GUI():
    def __init__(self):
        self.width = 900
        self.height = 900
        self.squareNr = 9
        self.squareDim = self.width // self.squareNr

        self.master = Tk()
        self.createBoard()
        self.board.pack()
        self.board.bind("<Button-1>", self.squareClick)

    def createBoard(self):
        self.board = Canvas(self.master, bg="white", highlightthickness=0, width = self.width, height = self.height)
        self.squares = {}
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                x1 = self.squareDim*col
                y1 = self.squareDim*row
                x2 = self.squareDim*(col+1)
                y2 = self.squareDim*(row+1)

                self.board.create_rectangle(x1, y1, x2, y2, fill="white")
                
    def squareClick(self, event):
        selected_column = int(event.x / self.squareDim)
        selected_row    = int(event.y / self.squareDim)
        try:
            pass
        except:
            pass
