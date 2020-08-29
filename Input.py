import sys

class Input():
    def __init__(self, GUI):
        self.GUI = GUI

        self.GUI.board.bind("<Key>", self.keyboardInput)
        self.GUI.board.bind("<Button-1>", self.squareClick)
        self.GUI.board.bind('<Escape>', self.exit)
        self.GUI.board.bind('<Return>', self.solve)
        self.GUI.board.bind('<Left>', self.leftKey)
        self.GUI.board.bind('<Right>', self.rightKey)
        self.GUI.board.bind('<Up>', self.upKey)
        self.GUI.board.bind('<Down>', self.downKey)

    def squareClick(self, event):
        selected_column = int(event.x / self.GUI.squareDim)
        selected_row    = int(event.y / self.GUI.squareDim)
        try:
            if(not self.GUI.logic.won):
                self.GUI.board.focus_set()
                self.GUI.highlightedSquare = (selected_row, selected_column)
                #print(f"Clicked:  {self.GUI.highlightedSquare}")
            else:
                self.GUI.master.destroy()
        except:
            pass

        self.GUI.draw()

    def keyboardInput(self, event):
        try:
            #print(f"Pressed: {repr(event.char)}")
            self.GUI.squares[self.GUI.highlightedSquare].setNumber(int(event.char))
        except:
            pass

        self.GUI.draw()

    def exit(self, event):
        sys.exit()

    def solve(self, event):
        try:
            self.GUI.board.focus_set()
            self.GUI.solveGame()
        except:
            pass
    
        self.GUI.draw()

    def leftKey(self, event):
        try:
            self.GUI.board.focus_set()
            self.squareMove((0, -1))
        except:
            pass
        
        self.GUI.draw()
    
    def rightKey(self, event):    
        try:
            self.GUI.board.focus_set()
            self.squareMove((0, 1))
        except:
            pass

        self.GUI.draw()

    def upKey(self, event):
        try:
            self.GUI.board.focus_set()
            self.squareMove((-1, 0))
        except:
            pass
        
        self.GUI.draw()

    def downKey(self, event):    
        try:
            self.GUI.board.focus_set()
            self.squareMove((1 ,0))
        except:
            pass
        
        self.GUI.draw()

    def insideBoundary(self, loc):
        if(0 <= loc[0] < 9 and 0 <= loc[1] < 9):
            return True
        else:
            return False

    def squareMove(self, direction):
        newHighlight = tuple(map(lambda i, j: i + j, self.GUI.highlightedSquare, direction))
        if(self.insideBoundary(newHighlight)):
            self.GUI.highlightedSquare = newHighlight