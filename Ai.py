from PossibleMoves import *
from Captures_Checks import *
from InitialBoard import *
import copy
import math
import random


def is_queen_captured(chessBoard, side):

    QueenGone = True

    if side == "wQ":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wQ":
                    QueenGone = False

    else:

        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "bQ":
                    QueenGone = False

    return QueenGone

def is_rook_captured(chessBoard, side):

    RookGone = True
    num_rook = 0

    if side == "wR":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wR":
                    num_rook += 5

    else:

        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "bR":
                    num_rook += 5

    return 10 - num_rook

def is_knight_captured(chessBoard, side):

    knightGone = True
    num_knight = 0

    if side == "wN":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wN":
                    num_knight += 3

    else:

        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "bN":
                    num_knight += 3

    return 6 - num_knight

def is_bishop_captured(chessBoard, side):

    BishopGone = True
    num_bishop = 0

    if side == "wB":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wB":
                    num_bishop += 3

    else:

        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "bB":
                    num_bishop += 3

    return 6 - num_bishop

def is_pawn_captured(chessBoard, side):

    PawnGone = True
    num_pawns = 0
    if side == "wP":
        
        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "wP":
                    num_pawns += 1

    else:

        for i in range(0, 8):
            for j in range(0, 8):
                if chessBoard[i][j].name == "bP":
                    num_pawns += 1

    return 8 - num_pawns

def calculate_scores(chessBoard, side):
    score = 0

    if(side == "white"):

        #For Checkmate
        blackKing = find_king(chessBoard, "bK")
        isCheckmated = is_king_checkmate(chessBoard, blackKing)
        if(isCheckmated):
            score += 1000

        isCheck = is_king_checked(chessBoard, blackKing)
        if(isCheck):
            score += 500

        #For Capturing Queen
        isQueenCaptured = is_queen_captured(chessBoard, "bQ")
        if(isQueenCaptured):
            score += 9

        #For Capturing Rook
        isRookCaptured = is_rook_captured(chessBoard, "bR")
        score += isRookCaptured

        #For Capturing Bishop
        isBishopCaptured = is_bishop_captured(chessBoard, "bB")
        score += isBishopCaptured

        #For Capturing Knight
        isKnightCaptured = is_knight_captured(chessBoard, "bN")
        score += isKnightCaptured

        #For Capturing Pawn
        totalPawnCaptured = is_pawn_captured(chessBoard, "bP")
        score += totalPawnCaptured
        

    elif(side == "black"):

        #For Checkmate
        whiteKing = find_king(chessBoard, "wK")
        isCheckmated = is_king_checkmate(chessBoard, whiteKing)
        if(isCheckmated):
            score -= 1000

        isCheck = is_king_checked(chessBoard, whiteKing)
        if(isCheck):
            score -= 500

        #For Capturing Queen
        isQueenCaptured = is_queen_captured(chessBoard, "wQ")
        if(isQueenCaptured):
            score -= 9

        #For Capturing Rook
        isRookCaptured = is_rook_captured(chessBoard, "wR")
        score -= isRookCaptured

        #For Capturing Bishop
        isBishopCaptured = is_bishop_captured(chessBoard, "wB")
        score -= isBishopCaptured

        #For Capturing Knight
        isKnightCaptured = is_knight_captured(chessBoard, "wN")
        score -= isKnightCaptured

        #For Capturing Pawn
        totalPawnCaptured = is_pawn_captured(chessBoard, "wP")
        score -= totalPawnCaptured

    return score

def get_all_boards_for_minimax(chess_board, side):
    chess_boards = []

    if(side):
        for i in range(0, 8):
            for j in range(0, 8):

                if chess_board[i][j].name == "bP":
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                if chess_board[i][j].name == "bR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "bN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()

                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "bB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "bQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "bK":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                        
                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)
    else:
        for i in range(0, 8):
            for j in range(0, 8):

                if chess_board[i][j].name == "wP":
                    possible_moves = pawn_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                if chess_board[i][j].name == "wR":
                    possible_moves = rook_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "wN":
                    possible_moves = knight_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()

                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "wB":
                    possible_moves = bishop_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "wQ":
                    possible_moves = queen_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])

                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

                elif chess_board[i][j].name == "wK":
                    possible_moves = king_moves(chess_board, chess_board[i][j])
                    for move in possible_moves:
                        new_chess_board = copy.deepcopy(chess_board)
                        new_chess_board[move[0]][move[1]] = copy.deepcopy(new_chess_board[i][j])
                        
                        new_chess_board[move[0]][move[1]].alphaPosition = move[0]
                        new_chess_board[move[0]][move[1]].numericPosition = move[1]

                        new_chess_board[i][j].clear()
                        chess_boards.append(new_chess_board)

    random.shuffle(chess_boards)
    return chess_boards


BESTMOVE = create_chess_board()
DEPTH = 3
PRUNINGSCORE = 99999

def perform_AI_turn(chess_board):
    global BESTMOVE
    minimax(chess_board, "Ai", DEPTH, -PRUNINGSCORE, PRUNINGSCORE)
    return BESTMOVE

def minimax(board, playerTurn, depth, alpha, beta):
    global BESTMOVE
    global DEPTH

    # print("board")
    # print_board(BESTMOVE)

    if(depth == 0):
        if(playerTurn == "Ai"):
            return calculate_scores(board, "black")

        elif(playerTurn == "Enemy"):
            return calculate_scores(board, "white")

    # For White
    if(playerTurn == "Enemy"):
        maxScore = -PRUNINGSCORE
        moves = get_all_boards_for_minimax(board, False)
        for move in moves:
            board = copy.deepcopy(move)
            # print_board(move)

            score = minimax(board, "Ai", depth-1, alpha, beta)

            if(score > maxScore):
                maxScore = score
                if(depth == DEPTH):
                    BESTMOVE = copy.deepcopy(move)
            alpha = max(maxScore, alpha)
            if(beta <= alpha):
                break

        return maxScore

    # For Black
    elif(playerTurn == "Ai"):

        minScore = PRUNINGSCORE
        moves = get_all_boards_for_minimax(board, True)
        for move in moves:
            board = copy.deepcopy(move)
            # print_board(move)
            #newMoves = get_all_boards_for_minimax(move, True)
            score = minimax(board, "Enemy", depth-1, alpha, beta)

            if(score < minScore):
                minScore = score
                if(depth == DEPTH):
                    BESTMOVE = copy.deepcopy(move)

            beta = min(minScore, beta)
            if (beta <= alpha):
                break

        return minScore