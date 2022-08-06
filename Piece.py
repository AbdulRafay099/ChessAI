import copy


class Piece:
    name = "--"
    points = 0
    alphaPosition = 0  # X-Axis
    numericPosition = 0  # Y-Axis
    firstMove = True # checking if first move for pawn

    def __init__(self, name, points, alphaPosition, numericPosition,firstMove):
        self.name = name
        self.points = points
        self.alphaPosition = alphaPosition
        self.numericPosition = numericPosition
        self.firstMove = firstMove

    def clear(self):
        self.name = "--"
        self.points = 0
        self.alphaPosition = 0  # X-Axis
        self.numericPosition = 0  # Y-Axis
        self.firstMove = True  # checking if first move for pawn

    def copy(self, original):
        self.name = original.name
        self.points = original.points
        self.alphaPosition = original.alphaPosition
        self.numericPosition = original.numericPosition
        self.firstMove = original.firstMove


def find_king(chessBoard, side):

    if side == "wK":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wK":

                    newKing = copy.deepcopy(chessBoard[i][j])
                    return newKing

    else:

        for i in range(0, 8):
            for j in range(0, 8):

                if chessBoard[i][j].name == "bK":
                    newKing = copy.deepcopy(chessBoard[i][j])
                    return newKing

