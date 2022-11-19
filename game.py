import pygame
import numpy as np
import random
import time

WHITE = (255,255,255)

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

height = 50
width = 50

x = 0
y = 0

SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

pygame.init()

clockobject = pygame.time.Clock()

game_board = np.zeros([height,width], dtype=int)

box_height = WINDOW_HEIGHT/len(game_board)
box_width = WINDOW_WIDTH/len(game_board[0])

def random_board(board):
    count = 0
    rand_x = 0
    rand_y = 0
    for i in board:
        rand_x = 0
        for n in i:
            if count == 2:
                game_board[rand_x][rand_y] = random.randint(0,1)
                count = 0
            else:
                count+=1
            rand_x+=1
        rand_y +=1

print(game_board)

def draw_grid(pos_x,pos_y,grid):
    x = pos_x
    y = pos_y
    for i in grid:
        x=0
        for n in i:
            rect = pygame.Rect(x*box_height, y*box_width, box_height, box_width)
            if n == 1:
                pygame.draw.rect(SCREEN, WHITE, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
            x+=1
        y+=1

random_board(game_board)
print(game_board)

while True:
    print("loop")
    SCREEN.fill((0,0,0))
    time.sleep(0.5)
    x_board = 0
    y_board = 0
    original_board = game_board
    #game_board = np.zeros([height,width], dtype=int)
    for i in original_board:
        x_board = 0
        for n in i:
            neighbors = 0

            try:
                if original_board[x_board+1][y_board] == 1:
                    neighbors +=1
                if original_board[x_board][y_board+1] == 1:
                    neighbors += 1
                if original_board[x_board+1][y_board+1] == 1:
                    neighbors += 1
                if original_board[x_board-1][y_board] == 1:
                    neighbors += 1
                if original_board[x_board+1][y_board-1] == 1:
                    neighbors += 1
                if original_board[x_board-1][y_board-1] == 1:
                    neighbors += 1
            except:
                pass
            if n == 1:
                if neighbors >= 4:
                    game_board[x_board][y_board] = 0
                    print("blanking")
                if neighbors <= 1:
                    game_board[x_board][y_board] = 0
                    print("blanking")
            if neighbors == 3:
                game_board[x_board][y_board] = 1
                print("life")
            x_board +=1
        y_board += 1
    draw_grid(x,y,game_board)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

