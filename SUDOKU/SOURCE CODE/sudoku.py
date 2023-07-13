import pygame
import pygame.sysfont
import numpy as np


grid = [[0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,4,0,0,0,0,0,0,0]]
background_color = "green"
background_color1 = "deeppink"
pygame.init()
#for image
font = pygame.font.Font('freesansbold.ttf', 24)
font1 = pygame.font.Font('freesansbold.ttf', 15)
num_text = pygame.font.Font("freesansbold.ttf", 30)
win = pygame.display.set_mode((750,700))
pygame.display.set_caption("MY SUDOKU GAME")
fps = 60
timer = pygame.time.Clock()
PLAY = False
HOME = True
EXIT = True
HOW = 1
buffer = 5
solved = 0

def isEmpty(num):
    if num == 0:
        return True
    return False

def isValid(position, num):
     #Check for Column, row and sub-grid
    
    #Checking row
    for i in range(0, len(grid[0])):
        if(grid[position[0]][i] == num):
            return False
    
    #Checking column
    for i in range(0, len(grid[0])):
        if(grid[i][position[1]] == num):
            return False
    
    #Check sub-grid  
    x = position[0]//3*3
    y = position[1]//3*3
    #Gives us the box number
    
    for i in range(0,3):
        for j in range(0,3):
            if(grid[x+i][y+j]== num):
                return False
    return True


solved = 0
def sudoku_solver(win):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0,len(grid[0])):
        for j in range(0, len(grid[0])):
            if(isEmpty(grid[i][j])): 
                for k in range(1,10):
                    if isValid((i,j), k):                   
                        grid[i][j] = k
                        pygame.draw.rect(win, background_color, ((j+1)*65 + buffer, (i+1)*65+ buffer,65 -2*buffer , 65 - 2*buffer))
                        value = myfont.render(str(k), True, (0,0,0))
                        win.blit(value, ((j+1)*65+15,(i+1)*65))
                        pygame.display.update()
                        pygame.time.delay(25)
                        sudoku_solver(win)
                        
                        #Exit condition
                        global solved
                        if(solved == 1):
                            return
                        
                        #if sudoku_solver returns, there's a mismatch
                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, ((j+1)*65 + buffer, (i+1)*65+ buffer,65 -2*buffer , 65 - 2*buffer))
                        pygame.display.update()
                        #pygame.time.delay(50)
                return               
    solved = 1
def solve_sudoku(num):
    def empty(num):
        global grid     
        if (num == 0):
            print("Danica")
            return True
        return False
    def valid(position,num):
        global grid
        print(grid[position[0]])
        for i in range(0, len(grid[0])):
            if(grid[position[0]][i] == num):
                return False
        
        #Checking column
        for i in range(0, len(grid[0])):
            if(grid[i][position[1]] == num):
                return False
        
        #Check sub-grid  
        x = position[0]//3*3
        y = position[1]//3*3
        #Gives us the box number
        
        for i in range(0,3):
            for j in range(0,3):
                if(grid[x+i][y+j]== num):
                    return False
        return True

        
    def sudoku():
        print(num)
        for i in range(0,9):
            for j in range(0,9):
                if empty(num):
                    if valid((i,j),num):
                        grid[i][j] = num
                        sudoku()
                        grid[i][j] = 0
                return
    sudoku()     
def play_game():
    global running
    global HOME
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    image = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405832584 (1).png")
    win.blit(image,(6,7))
    home_btn = pygame.draw.rect(win,"lime",[501,10,150,40],0,5)
    pygame.draw.rect(win,"white",[501,10,150,40],5,5)
    text = font1.render("HOME",True,"white")
    win.blit(text,(551,25))
    undo_btn = pygame.draw.rect(win,"lime",(300,10,190,40), 0, 5)
    pygame.draw.rect(win,"white",[300,10,190,40], 5, 5)
    text1 = font1.render("AUTO FILL",True,"white")
    win.blit(text1,(341,25))
    if undo_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed():
        print("hai")
    myfont = pygame.font.SysFont("Comic Sans Ms",23)
    def insert(win,position):
        i,j = position[1], position[0]
        myfont = pygame.font.SysFont('Comic Sans MS', 35)
        sudoku_solver(win)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if(grid[i-1][j-1] != 0):
                        return 
                    if(event.key == 48): #checking with 0
                        grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(win,"green",(position[0]*65 + buffer,position[1]*65 + buffer,65-buffer,65-buffer))
                        pygame.display.update()
                        return
                    if(0 < event.key - 48 <10):
                        value_np = np.array(event.key - 48)
                        value1 = myfont.render(str(value_np), True, (0,0,0))
                        pygame.draw.rect(win,background_color1,(position[0]*65 + buffer,position[1]*65+buffer,65-buffer,65-buffer))
                        win.blit(value1,(position[0]*65+buffer,position[1] *65)) 
                        grid[i-1][j-1] = event.key - 48
                        solve_sudoku(value_np)
                        pygame.display.update()
                        return
                    return   
    for i in range(0,10):
            if (i*3 == 0):
                pygame.draw.line(win, (0,0,0), (65 + 65*i, 65), (65 + 65*i ,650 ), 4 )
                pygame.draw.line(win, (0,0,0), (65, 65 + 65*i), (650, 65 + 65*i), 4 )
            pygame.draw.line(win,"black",(65+65*i,65),(65+65*i,650),2)
            pygame.draw.line(win,"black",(65,65+65*i),(650,65+65*i),2)
    pygame.display.update()
    if home_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed():
        print("hai")
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = num_text.render(str(grid[i][j]), True, (0,0,0))
                win.blit(value, ((j+1)*65+15, (i+1)*67))
    pygame.display.update()
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//65, pos[1]//65))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    
def draw_game():
    global HOW
    image = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405832584 (1).png")
    image1 = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405726205 (1).png")
    play_btn = pygame.draw.rect(win, "deeppink",[80, 30, 150, 40], 0, 5)
    pygame.draw.rect(win, "red",[80,30, 150, 40], 5, 5)
    text = font.render("PLAY",True,'white')
    exit_btn = pygame.draw.rect(win,"deeppink",[240,30,150,40], 0, 5)
    pygame.draw.rect(win,"red",[240,30,150,40],5,5)
    text1=font.render("EXIT",True,"white")
    how_btn = pygame.draw.rect(win,"deeppink",[400,30,300,40], 0, 5)
    pygame.draw.rect(win,"red",[400,30,300,40],5,5)
    text2=font.render("HOW TO PLAY",True,"white")
    if how_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        print("how to play")
    win.blit(image,(25,25))
    win.blit(image1,(170,100))
    win.blit(text,(120,39))
    win.blit(text1,(285,39))
    win.blit(text2,(450,39))
    
    if exit_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        EXIT = True
        print(EXIT)
        exit()
    else:
        EXIT = False
    if play_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        PLAY = True
    else:
        PLAY = False
    return PLAY


   


running = True
while running:
    timer.tick(fps)
    win.fill((0, 255, 255))
    def home():
        global HOME,PLAY
        print("HAI WELCOME TO THE HOME I AM HAPPY TO MEET YOU")
        if HOME == True:
            HOME = True
            PLAY = False
        else:
            HOME = False
            PLAY = True
    if PLAY == True:
        play_game()
    else:
        PLAY = draw_game()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.QUIT
pygame.display.update()
 