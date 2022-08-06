from Piece import find_king
from PossibleMoves import *
from Captures_Checks import *
import copy

def get_all_boards(chess_board):
    chess_boards = []

    for i in range(0, 8):
        for j in range(0, 8):
            
            if chess_board[i][j].name == "wP":        
                possible_moves = pawn_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
                
                
            elif chess_board[i][j].name == "wR":
                possible_moves = rook_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
               
            elif chess_board[i][j].name == "wN":
                possible_moves = knight_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
               
            elif chess_board[i][j].name == "wB":
                possible_moves = bishop_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
               
            elif chess_board[i][j].name == "wQ":
                possible_moves = queen_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
               
            elif chess_board[i][j].name == "wK":
                possible_moves = king_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
                


    for i in range(0, 8):
        for j in range(0, 8):
            
            if chess_board[i][j].name == "bP":        
                possible_moves = pawn_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
                
                
            elif chess_board[i][j].name == "bR":
                possible_moves = rook_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)

            elif chess_board[i][j].name == "bN":
                possible_moves = knight_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)

            elif chess_board[i][j].name == "bB":
                possible_moves = bishop_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)

            elif chess_board[i][j].name == "bQ":
                possible_moves = queen_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)

            elif chess_board[i][j].name == "bK":
                possible_moves = king_moves(chess_board, chess_board[i][j])
                for move in possible_moves:
                    new_chess_board = copy.deepcopy(chess_board)
                    new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                    new_chess_board[i][j].clear()
                    chess_boards.append(new_chess_board)
              
    return chess_boards