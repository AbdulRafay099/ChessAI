from Piece import *


# Creation of the chess board
def create_chess_board():
    chess_board = []
    for i in range(0, 8):
        chess_board.append([])
        for j in range(0, 8):
            chess_board[i].append(Piece("--", 0, 0, 0, False))

    return chess_board


def print_board(chess_board):
    for i in range(0, 8):
        for j in range(0, 8):
            print(chess_board[i][j].name, end=" ")
        print()
    print("\n")


def fill_initial_population(chess_board):
    # For white pawns
    for index in range(0, 8):
        chess_board[6][index].name = "wP"
        chess_board[6][index].points = 1
        chess_board[6][index].alphaPosition = 6
        chess_board[6][index].numericPosition = index
        chess_board[6][index].firstMove = True

    # For black pawns

    for index in range(0, 8):
        chess_board[1][index].name = "bP"
        chess_board[1][index].points = 1
        chess_board[1][index].alphaPosition = 1
        chess_board[1][index].numericPosition = index
        chess_board[1][index].firstMove = True


    # For White rooks
    chess_board[7][0].name = "wR"
    chess_board[7][0].points = 5
    chess_board[7][0].alphaPosition = 7
    chess_board[7][0].numericPosition = 0
    chess_board[7][0].firstMove = False

    chess_board[7][7].name = "wR"
    chess_board[7][7].points = 5
    chess_board[7][7].alphaPosition = 7
    chess_board[7][7].numericPosition = 7
    chess_board[7][7].firstMove = False

    # For Black rooks
    chess_board[0][0].name = "bR"
    chess_board[0][0].points = 5
    chess_board[0][0].alphaPosition = 0
    chess_board[0][0].numericPosition = 0
    chess_board[0][0].firstMove = False

    chess_board[0][7].name = "bR"
    chess_board[0][7].points = 5
    chess_board[0][7].alphaPosition = 0
    chess_board[0][7].numericPosition = 7
    chess_board[0][7].firstMove = False

    # For White knight
    chess_board[7][1].name = "wN"
    chess_board[7][1].points = 3
    chess_board[7][1].alphaPosition = 7
    chess_board[7][1].numericPosition = 1
    chess_board[7][1].firstMove = False

    chess_board[7][6].name = "wN"
    chess_board[7][6].points = 3
    chess_board[7][6].alphaPosition = 7
    chess_board[7][6].numericPosition = 6
    chess_board[7][6].firstMove = False

    # For Black knight
    chess_board[0][1].name = "bN"
    chess_board[0][1].points = 3
    chess_board[0][1].alphaPosition = 0
    chess_board[0][1].numericPosition = 1
    chess_board[0][1].firstMove = False

    chess_board[0][6].name = "bN"
    chess_board[0][6].points = 3
    chess_board[0][6].alphaPosition = 0
    chess_board[0][6].numericPosition = 6
    chess_board[0][6].firstMove = False

    # For White Bishop
    chess_board[7][2].name = "wB"
    chess_board[7][2].points = 3
    chess_board[7][2].alphaPosition = 7
    chess_board[7][2].numericPosition = 2
    chess_board[7][2].firstMove = False

    chess_board[7][5].name = "wB"
    chess_board[7][5].points = 3
    chess_board[7][5].alphaPosition = 7
    chess_board[7][5].numericPosition = 5
    chess_board[7][5].firstMove = False

    # For Black Bishop
    chess_board[0][2].name = "bB"
    chess_board[0][2].points = 3
    chess_board[0][2].alphaPosition = 0
    chess_board[0][2].numericPosition = 2
    chess_board[0][2].firstMove = False

    chess_board[0][5].name = "bB"
    chess_board[0][5].points = 3
    chess_board[0][5].alphaPosition = 0
    chess_board[0][5].numericPosition = 5
    chess_board[0][5].firstMove = False

    # For White Queen
    chess_board[7][3].name = "wQ"
    chess_board[7][3].points = 9
    chess_board[7][3].alphaPosition = 7
    chess_board[7][3].numericPosition = 3
    chess_board[7][3].firstMove = False

    # For Black Queen
    chess_board[0][3].name = "bQ"
    chess_board[0][3].points = 9
    chess_board[0][3].alphaPosition = 0
    chess_board[0][3].numericPosition = 3
    chess_board[0][3].firstMove = False

    # For White King
    chess_board[7][4].name = "wK"
    chess_board[7][4].points = 1000
    chess_board[7][4].alphaPosition = 7
    chess_board[7][4].numericPosition = 4
    chess_board[7][4].firstMove = False

    # For Black King
    chess_board[0][4].name = "bK"
    chess_board[0][4].points = 1000
    chess_board[0][4].alphaPosition = 0
    chess_board[0][4].numericPosition = 4
    chess_board[0][4].firstMove = False
    
    return chess_board
