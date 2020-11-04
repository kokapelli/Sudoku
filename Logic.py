#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################################
# Class of functions determining the status of the game #
#########################################################

class Logic():
    def __init__(self, squares: list):
        self.squareNr = 9
        self.board    = squares
        self.won      = False

    def getRowNumbers(self, row: int) -> list:
        rowNumbers = list()
        for i in range(self.squareNr):
            rowNumbers.append(self.board[(row, i)].getNumber())

        return rowNumbers

    def getColNumbers(self, col: int) -> list:
        colNumbers = list()
        for i in range(self.squareNr):
            colNumbers.append(self.board[(i, col)].getNumber())

        return colNumbers

    def getSquareNumbers(self, square: int) -> list:
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

    # Consider creating superclasses for the three checks
    def isValidSquare(self, square: int) -> bool:
        n = set(self.getSquareNumbers(square))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            return True

    def isValidRow(self, row: int) -> bool:
        n = set(self.getRowNumbers(row))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            return True

    def isValidCol(self, col: int) -> bool:
        n = set(self.getColNumbers(col))
        try:
            n.remove(0)
        except:
            pass
        
        if(len(n) < 9):
            return False
        else:
            return True


    def isGameWon(self) -> bool:
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
