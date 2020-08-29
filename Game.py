#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################
# Creates boards and initiates games of Sudoku #
################################################

import random
import copy
from datetime import datetime
from GUI import GUI

initBoard = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]


# THE RANGE CAN BE CHANGED FROM len(board[0]) TO SOMETHING ELSE
class Game():
    def __init__(self):
        # The amount of initial numbers in the Sudoku
        # Works as a difficulty gauge
        self.providedNumbers = 30
        self.solution = list()
        self.startGame()

    def startGame(self):
        play = True
        while(play):
            self.board = self.createBoard()
            self.game = GUI(self.board, self.solution)
            self.game.master.mainloop()

    def createBoard(self):
        random.seed(datetime.now())

        # bypassing Python's value by reference
        board = copy.deepcopy(initBoard)
        for i in range(self.providedNumbers):
            board = self.setRandomNumbers(board)
            
        # bypassing Python's value by reference
        originBoard = copy.deepcopy(board)
        if(self.solveBoard(board)):
            self.solution = board
            return originBoard
        else:
            return self.createBoard()
    
    def setRandomNumbers(self, board):
            randRow = random.randint(0, 8)
            randCol = random.randint(0, 8)
            randNum = random.randint(1, 9)
            board[randRow][randCol] = randNum

            if(self.checkValidPlacement(board, randRow, randCol)):
                return board
            else:
                board[randRow][randCol] = 0
                return self.setRandomNumbers(board)
            
    def checkValidPlacement(self, board, row, col):
        rowValid = self.checkDuplicate(board[row])
        colValid = self.checkDuplicate(self.getColVals(board, col))
        squareValid = self.checkDuplicate(self.getSquareVals(board, row, col))
        if(rowValid and colValid and squareValid):
            return True
        else:
            return False

    def checkDuplicate(self, vals):
        seen = set()
        for num in vals:
            if num not in seen:
                seen.add(num)
            elif num != 0:
                return False

        return True

    def getColVals(self, board, col):
        colVals = list()
        for i in range(len(board[0])):
            colVals.append(board[i][col])

        return colVals

    # Dirty solution, will have to be refactored
    def getSquareVals(self, board, row, col):
        squareVals = list()
        boxSize = int(len(board[0]) / 3)

        rowLevel = 0
        colLevel = 0

        if(2 < row <= 5):
            rowLevel = 1

        elif(5 < row <= 8):
            rowLevel = 2

        if(2 < col <= 5):
            colLevel = 1

        elif(5 < col <= 8):
            colLevel = 2

        for row in range(boxSize*rowLevel, boxSize*rowLevel + boxSize):
            for col in range(boxSize*colLevel, boxSize*colLevel + boxSize):
                squareVals.append(board[row][col])

        return squareVals

    def solveBoard(self, board):
        find = self.findEmpty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.validSolution(board, i, (row, col)):
                board[row][col] = i

                if self.solveBoard(board):
                    return True

                board[row][col] = 0

        return False


    def validSolution(self, board, num, pos):
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        boxY = pos[0] // 3
        boxX = pos[1] // 3

        for row in range(boxY*3, boxY*3 + 3):
            for col in range(boxX*3, boxX*3 + 3):
                if board[row][col] == num and (row, col) != pos:
                    return False

        return True

    def findEmpty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j)  # row, col

        return None

if __name__ == "__main__":
    game = Game()