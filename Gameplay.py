from InitialBoard import *
from PossibleMoves import *
from Ai import *
from Piece import *
from Captures_Checks import *
import random
import copy
from gui import *

def gameplay():

    chess_board = create_chess_board()
    chess_board = fill_initial_population(chess_board)

    # Printing the Board
    print("Initial Board")
    print_board(chess_board)

    board(True, chess_board)

    print("Select piece to move(white)")
    curr_i = int(input("Enter i (Y - axis) = "))
    curr_j = int(input("Enter j (X - axis) = "))

    print("Valid moves ", end=" ")
    curr_valid_moves = get_valid_moves(chess_board, chess_board[curr_i][curr_j])
    print(curr_valid_moves)
    print("Select position to move")

    new_i = int(input("Enter i (Y - axis) = "))
    new_j = int(input("Enter j (X - axis) = "))

    curr_move = (new_i, new_j)

    while curr_move not in curr_valid_moves:
        print("PLEASE ENTER A VALID MOVE!!!")

        new_i = int(input("Enter i (Y - axis) = "))
        new_j = int(input("Enter j (X - axis) = "))

        curr_move = (new_i, new_j)


    chess_board[new_i][new_j] = copy.deepcopy(chess_board[curr_i][curr_j])

    chess_board[new_i][new_j].alphaPosition = new_i
    chess_board[new_i][new_j].numericPosition = new_j

    chess_board[curr_i][curr_j].clear()
    while 1:

        board(True, chess_board)

        whiteKing = find_king(chess_board, "wK")
        blackKing = find_king(chess_board, "bK")

        whiteChecked = is_king_checked(chess_board, whiteKing)
        if whiteChecked:
            print("WHITE KING IS CHECKED!!!")

        blackChecked = is_king_checked(chess_board, blackKing)
        if blackChecked:
            print("BLACK KING IS CHECKED!!!")

        whiteCheckedmated = is_king_checkmate(chess_board, whiteKing)
        if whiteCheckedmated:
            print("Black Wins!")
            break

        blackCheckedmated = is_king_checkmate(chess_board, blackKing)
        if blackCheckedmated:
            print("White Wins!")
            break

        print("\n\n")
        print("New Board")
        print_board(chess_board)

        print("\n\n")
        print("Performing AI turn...")
        print("New Board")

        chess_boards = perform_AI_turn(chess_board)
        chess_board = copy.deepcopy(chess_boards)

        board(True, chess_board)


        print_board(chess_board)

        print("\n\n")
        print("Player Turn")
        print("Select piece to move")
        curr_i = int(input("Enter i (Y - axis) = "))
        curr_j = int(input("Enter j (X - axis) = "))

        print("Valid moves ", end=" ")
        print("Valid moves ", end=" ")
        curr_valid_moves = get_valid_moves(chess_board, chess_board[curr_i][curr_j])
        print(curr_valid_moves)
        print("Select position to move")

        new_i = int(input("Enter i (Y - axis) = "))
        new_j = int(input("Enter j (X - axis) = "))

        curr_move = (new_i, new_j)

        while curr_move not in curr_valid_moves:
            print("PLEASE ENTER A VALID MOVE!!!")

            new_i = int(input("Enter i (Y - axis) = "))
            new_j = int(input("Enter j (X - axis) = "))

            curr_move = (new_i, new_j)

        chess_board[new_i][new_j] = copy.deepcopy(chess_board[curr_i][curr_j])
        chess_board[new_i][new_j].alphaPosition = new_i
        chess_board[new_i][new_j].numericPosition = new_j
        chess_board[curr_i][curr_j].clear()

        board(True, chess_board)
