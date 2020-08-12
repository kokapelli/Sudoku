
class Square():
    def __init__(self, x1, y1, x2, y2, textX, textY, coord, board):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.textX = textX
        self.textY = textY
        self.coord = coord

        self.board = board
        self.number = 0
        self.hardCoded = False


    def __repr__(self):
        return f'Coords {self.coord}: {self.x1}, {self.y1}, {self.x2}, {self.y2}: {self.number}'

    def getGUISquareCoords(self):
        return self.x1, self.y1, self.x2, self.y2, self.textX, self.textY

    def getSquareCoords(self):
        return self.x1, self.y1, self.x2, self.y2

    def getSquareNumberCoords(self):
        return self.textX, self.textY

    def getNumber(self):
        return self.number
        
    def getHardcoded(self):
        return self.hardCoded

    def setHardCodedNumber(self, number):
        self.number = number
        self.hardCoded = True

    def setNumber(self, number):
        if(self.hardCoded):
            return
        else:
            self.number = number
