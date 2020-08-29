#########################################################
# Class of functions determining the status of the game #
#########################################################

class Logic():
    def __init__(self, squares):
        self.squareNr = 9
        self.board = squares
        self.won = False

    def getRowNumbers(self, row):
        rowNumbers = list()
        for i in range(self.squareNr):
            rowNumbers.append(self.board[(row, i)].getNumber())

        return rowNumbers

    def getColNumbers(self, col):
        colNumbers = list()
        for i in range(self.squareNr):
            colNumbers.append(self.board[(i, col)].getNumber())

        return colNumbers

    # Refactor
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
                squareNumbers.append(self.board[(row, col)].getNumber())

        return squareNumbers

    # Refactor
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
            return True

    # Refactor 
    def isGameWon(self):
        for row in range(self.squareNr):
            if(not self.isValidRow(row)):
                return False
        for col in range(self.squareNr):
            if(not self.isValidCol(col)):
                return False
        for square in range(self.squareNr):
            if(not self.isValidSquare(square)):
                return False

        self.won = True
        return True
