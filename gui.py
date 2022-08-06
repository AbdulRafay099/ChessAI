import pygame
import copy


def board(running, chessBoard): 
    
    board_positions = []

    bP = pygame.image.load("Graphics/Black/bP.png")
    wP = pygame.image.load("Graphics/White/wP.png")
    bK = pygame.image.load("Graphics/Black/bK.png")
    wK = pygame.image.load("Graphics/White/wK.png")
    bR = pygame.image.load("Graphics/Black/bR.png")
    wR = pygame.image.load("Graphics/White/wR.png")
    bB = pygame.image.load("Graphics/Black/bB.png")
    wB = pygame.image.load("Graphics/White/wB.png")
    bQ = pygame.image.load("Graphics/Black/bQ.png")
    wQ = pygame.image.load("Graphics/White/wQ.png")
    bN = pygame.image.load("Graphics/Black/bN.png")
    wN = pygame.image.load("Graphics/White/wN.png")

    bP = pygame.transform.scale(bP, (50, 50)) 
    wP = pygame.transform.scale(wP, (50, 50)) 
    bK = pygame.transform.scale(bK, (50, 50)) 
    wK = pygame.transform.scale(wK, (50, 50)) 
    bR = pygame.transform.scale(bR, (50, 50)) 
    wR = pygame.transform.scale(wR, (50, 50)) 
    bB = pygame.transform.scale(bB, (50, 50)) 
    wB = pygame.transform.scale(wB, (50, 50)) 
    bQ = pygame.transform.scale(bQ, (50, 50)) 
    wQ = pygame.transform.scale(wQ, (50, 50)) 
    bN = pygame.transform.scale(bN, (50, 50)) 
    wN = pygame.transform.scale(wN, (50, 50)) 

    
    def flipColor(color):
        white = (240,240,240)
        black = (0,166,172)
        if not color or color == white:
            color = black
        else: 
            color = white
        return color

    def Display_wK(x,y):
        window.blit(wK, (x,y))

    def Display_wR(x,y):
        window.blit(wR, (x,y))

    def Display_wQ(x,y):
        window.blit(wQ, (x,y))

    def Display_wB(x,y):
        window.blit(wB, (x,y))

    def Display_wN(x,y):
        window.blit(wN, (x,y))

    def Display_wP(x,y):
        window.blit(wP, (x,y))

    def Display_bK(x,y):
        window.blit(bK, (x,y))

    def Display_bR(x,y):
        window.blit(bR, (x,y))

    def Display_bQ(x,y):
        window.blit(bQ, (x,y))

    def Display_bB(x,y):
        window.blit(bB, (x,y))

    def Display_bN(x,y):
        window.blit(bN, (x,y))

    def Display_bP(x,y):
        window.blit(bP, (x,y))

    width=480         # measurements for the window
    height=480
    block_size= 60  
    window = pygame.display.set_mode((width,height))
    background_color = (0,0,0)     # This is how I make the lines
    window.fill(background_color)
    c = None
    pygame.draw.rect(window,(255,0,0),pygame.Rect(0,0,width,height)) # red background
    for y in range(0,height,block_size): 
        c = flipColor(c)
        for x in range(0,width,block_size):
            c = flipColor(c)
            rect = pygame.Rect(x , y , x+block_size , y+block_size ) 
            pygame.draw.rect(window, c , rect, 0)   # Leaves space for lines to be visible.

            board_positions.append((x+5, y+3))

    for i in range(0,height+1,block_size):  
        pygame.draw.line(window,(0,0,0),(i,0),(i,width),2)
        pygame.draw.line(window,(0,0,0),(0,i),(height,i),2)

    pygame.draw.line(window,(0,0,0),(height-2,0),(height-2,width),2) # fix for out of window line
    pygame.draw.line(window,(0,0,0),(0,width-2),(height,width-2),2) # fix for out of wondow line

    for i in range(0, 8):
        for j in range(0, 8):

            if(chessBoard[i][j].name == "wK"):
                Display_wK(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "wQ"):
                Display_wQ(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "wR"):
                Display_wR(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "wB"):
                Display_wB(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "wN"):
                Display_wN(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "wP"):
                Display_wP(board_positions[i*8 + j][0], board_positions[i*8 + j][1])

            elif(chessBoard[i][j].name == "bK"):
                Display_bK(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "bQ"):
                Display_bQ(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "bR"):
                Display_bR(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "bB"):
                Display_bB(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "bN"):
                Display_bN(board_positions[i*8 + j][0], board_positions[i*8 + j][1])
            elif(chessBoard[i][j].name == "bP"):
                Display_bP(board_positions[i*8 + j][0], board_positions[i*8 + j][1])

    pygame.display.flip()
