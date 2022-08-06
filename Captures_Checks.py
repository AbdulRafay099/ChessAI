from InitialBoard import print_board
from Piece import *
from PossibleMoves import *
from PossibleBoards import *
import copy


def is_king_checked(chessboard, king):
    all_enemy_moves = []
    under_check = False

    if king.name == "wK":

        all_enemy_moves = get_all_check_moves(chessboard, "white")
      
        for move in all_enemy_moves:
        
            if move[0] == king.alphaPosition and move[1] == king.numericPosition:
                under_check = True

    elif king.name == "bK":
        all_enemy_moves = get_all_check_moves(chessboard, "black")

        for move in all_enemy_moves:
            if move[0] == king.alphaPosition and move[1] == king.numericPosition:
                under_check = True

    return under_check


def is_king_checkmate(chessboard, king):

    all_king_boards = king_moved_boards(chessboard, king)
    checkmate = True

    if (len(all_king_boards) > 0):

        for board in all_king_boards:

            newKing = find_king(board, king.name)
            isChecked = is_king_checked(board, newKing)

            if (isChecked == False):
                checkmate = False

    elif(len(all_king_boards)==0 and is_king_checked(chessboard, king)):
        checkmate = True
    else:
        checkmate = False

    return checkmate


def is_piece_under_attack(chessboard, piece):
    all_enemy_moves = []
    under_attack = False

    if piece.name[0] == "w":
        all_enemy_moves = get_all_enemy_moves(chessboard, "white")

        for move in all_enemy_moves:
            if move[0] == piece.alphaPosition and move[1] == piece.numericPosition:
                under_attack = True

    if piece.name[0] == "b":
        all_enemy_moves = get_all_enemy_moves(chessboard, "black")

        for move in all_enemy_moves:
            if move[0] == piece.alphaPosition and move[1] == piece.numericPosition:
                under_attack = True

    return under_attack


def king_moved_boards(chess_board, king):
    chess_boards = []

    possible_moves = king_moves1(chess_board, chess_board[king.alphaPosition][king.numericPosition])

    for move in possible_moves:
        new_chess_board = copy.deepcopy(chess_board)
        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[king.alphaPosition][king.numericPosition])
        new_chess_board[king.alphaPosition][king.numericPosition].clear()

        # Check if that new board is checked position   
        newKing = find_king(new_chess_board, king.name)
        check = is_king_checked(new_chess_board, newKing)
        if (check == False):
            chess_boards.append(new_chess_board)

    return chess_boards
