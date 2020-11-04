#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# Defines the state of every square in a Sudoku game #
######################################################

from typing import Tuple

class Square():
    def __init__(self, 
                    x1: int, 
                    y1: int, 
                    x2: int, 
                    y2: int, 
                    textX: str, 
                    textY: str, 
                    coord: str, 
                    board: str):
        self.x1    = x1
        self.y1    = y1
        self.x2    = x2
        self.y2    = y2
        self.textX = textX
        self.textY = textY
        self.coord = coord

        self.board     = board
        self.number    = 0
        self.hardCoded = False


    def __repr__(self) -> str:
        return f'Coords {self.coord}: {self.x1}, {self.y1}, {self.x2}, {self.y2}: {self.number}'

    def getGUISquareCoords(self) -> Tuple[int, int, int, int, str, str]:
        return self.x1, self.y1, self.x2, self.y2, self.textX, self.textY

    def getSquareCoords(self) -> Tuple[int, int, int, int]:
        return self.x1, self.y1, self.x2, self.y2

    def getSquareNumberCoords(self) -> Tuple[str, str]:
        return self.textX, self.textY

    def getNumber(self) -> int:
        return self.number
        
    def getHardcoded(self) -> bool:
        return self.hardCoded

    def setHardCodedNumber(self, number: int) -> None:
        self.number    = number
        self.hardCoded = True

    def setNumber(self, number: int) -> None:
        if(self.hardCoded):
            return
        else:
            self.number = number
