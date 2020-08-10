from tkinter import *


class GUI():
    def __init__(self):
        self.width = 900
        self.height = 900
        self.squareNr = 9
        self.squareDim = self.width // self.squareNr

        self.createBoard()
        self.setSquares()
        self.board.pack()
        self.board.bind("<Button-1>", self.squareClick)

        self.highlightedSquare = None

    def createBoard(self):        
        self.master = Tk()
        self.master.resizable(False, False)
        self.master.title("Sewdewko")
        self.master.configure(background="black")
        self.board = Canvas(self.master, bg="white", highlightthickness=0, width = self.width, height = self.height)

    def setSquares(self):
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                x1 = self.squareDim*col
                y1 = self.squareDim*row
                x2 = self.squareDim*(col+1)
                y2 = self.squareDim*(row+1)

                self.board.create_rectangle(x1, y1, x2, y2, fill="white")   

    def draw(self):
        for row in range(self.squareNr):
            for col in range(self.squareNr):
                x1 = col * self.squareDim
                y1 = row * self.squareDim
                x2 = x1 + self.squareDim
                y2 = y1 + self.squareDim
                if (self.highlightedSquare is not None and self.highlightedSquare == (row, col)):
                    self.board.create_rectangle(x1, y1, x2, y2,
                                                 fill="beige",
                                                 tags="area")
                else:
                    self.board.create_rectangle(x1, y1, x2, y2, fill="white",
                                                 tags="area")

    def squareClick(self, event):
        selected_column = int(event.x / self.squareDim)
        selected_row    = int(event.y / self.squareDim)
        try:
            self.highlightedSquare = (selected_row, selected_column)
            print(self.highlightedSquare)
        except:
            pass
        self.draw()

def main():
    board = GUI()
    board.master.mainloop()

if __name__ == "__main__":
    main()
