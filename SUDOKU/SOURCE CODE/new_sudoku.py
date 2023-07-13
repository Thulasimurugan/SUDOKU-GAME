import pygame
import numpy as np

pygame.init()
buffer = 5
grid = [[0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,4,0,0,0,0,0,0,0]]

def isEmpty(num):
    if num == 0:
        return True
    return False
def isValid(position,num):
    for i in range(0,len(grid[0])):
        if grid[position[0]][i] == num:
            return False
    for i in range(0,len(grid[0])):
        if grid[i][position[1]] == num:
            return False
        
    x = position[0]//3*3
    y = position[1]//3*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x+i][y+j] == num:
                return False
    return True
    
solved = 0
def solve():
    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if (isEmpty(grid[i][j])):
                for k in range(1,10):
                    if (isValid((i,j),k)):
                        grid[i][j] = k
                        pygame.draw.rect(win,"brown", ((j+1)*60 + buffer, (i+1)*60+ buffer,60 -7,60 -7))
                        grid_auto = font1.render(str(k),True,"white")
                        win.blit(grid_auto,((j+1) * 60 + 25,(i+1) * 60 + 25))
                        pygame.time.delay(25)
                        pygame.display.update()
                        solve()
                        #Exit condition
                        global solved
                        if(solved == 1):
                            return
                        #if sudoku_solver returns, there's a mismatch
                        grid[i][j] = 0
                        pygame.draw.rect(win, "brown", ((j+1)*60 + buffer, (i+1)*60+ buffer,60 -2*buffer , 60 - 2*buffer))
                        pygame.display.update()
                        pygame.time.delay(50)
                return
    solved = 1
    
def insert(win,position):
    global running
    global Home
    j = position[0]
    i = position[1]
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid[i-1][j-1] != 0:
                    return
                if (event.key == 48):
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win,"green",(position[0]*60 + buffer,position[1]* 60 + buffer,60-buffer,60-buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):
                    value_np = np.array(event.key - 48)
                    grid_text = font1.render(str(value_np),True,(255,255,255))
                    pygame.draw.rect(win,"green",(position[0]*60 + buffer,position[1] * 60 + buffer,60 - 7,60 - 7))
                    win.blit(grid_text,(position[0]*60 + 25,position[1]*60 + 25))
                    pygame.display.update()
                    return
                return            
            if event.type == pygame.QUIT:
                return
            
def user_play():
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//60, pos[1]//60))
            if event.type == pygame.QUIT:
                pygame.quit()
                return  
                 
def user_click():
    erase = pygame.draw.rect(win,"navy",(650,388,120,40),0,9)
    pygame.draw.rect(win,"white",(650,388,120,40),3,9)
    home_btn_text = font2.render("ERASE",True,"white")
    win.blit(home_btn_text,(680,400))
    if erase.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        print("erased successfuly")
    hint = pygame.draw.rect(win,"navy",(650,538,120,40),0,9)
    pygame.draw.rect(win,"white",(650,538,120,40),3,9)
    home_btn_text = font2.render("HINT",True,"white")
    win.blit(home_btn_text,(688,550))
    if hint.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        print("hint is updated successfully")

def click():
    global thulasi
    home_btn = pygame.draw.rect(win,"navy",(650,150,120,40),0,9)
    pygame.draw.rect(win,"white",(650,150,120,40),3,9)
    home_btn_text = font2.render("EXIT",True,"white")
    win.blit(home_btn_text,(680,162))
    if home_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        exit()
    user = pygame.draw.rect(win,"navy",(640,450,140,40),0,9)
    pygame.draw.rect(win,"white",(640,450,140,40),3,9)
    home_btn_text = font2.render("USER PLAY",True,"white")
    win.blit(home_btn_text,(660,462))
    if user.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
         user_play()
    else:
        thulasi = False
def Play_game():
    image = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405832584 (1).png")
    win.blit(image,(10,10))
    thulasi = font2.render("THULASI MURUGAN",True,"navy")
    win.blit(thulasi,(70,35))
    mistake_text = font2.render("MISTAKE",True,"navy")
    win.blit(mistake_text,(290,35))
    mistake_text1 = font2.render("/3",True,"navy")
    win.blit(mistake_text1,(390,35))
    timer_text = font2.render("TIMER",True,"navy")
    win.blit(timer_text,(470,35))
    click()
    for i in range(0,10):
            if (i%3 == 0):
                pygame.draw.line(win,"yellow",(60,60 + 60 * i),(600,60 + 60 * i),5)
                pygame.draw.line(win,"yellow",(60+60 * i,60),(60 + 60 * i,600),5)
            pygame.draw.line(win,"deepskyblue",(60,60+60 * i),(600,60+60 * i),2)
            pygame.draw.line(win,"deepskyblue",(60+60 * i,60),(60+60 * i,600),2)
    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if (0 < grid[i][j] < 10):
                grid_text = font1.render(str(grid[i][j]),True,(0,0,0))
                win.blit(grid_text,((j+1)*60+25,(i+1)*60+25))
    
    auto = pygame.draw.rect(win,"navy",(640,300,140,40),0,9)
    pygame.draw.rect(win,"white",(640,300,140,40),3,9)
    home_btn_text = font2.render("AUTO FILL",True,"white")
    win.blit(home_btn_text,(660,312))
    if auto.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        solve()
    pygame.display.update()

def home():
    global main_Play
    image = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405832584 (1).png")
    win.blit(image,(10,20))
    image1 = pygame.image.load("C:/Users/bobmu/Music/SUDOKU GAME/1687405726205 (1).png")
    win.blit(image1,(100,100))
    home_btn = pygame.draw.rect(win,"red",(80,25,140,40),0,5)
    pygame.draw.rect(win,"yellow",(80,25,140,40),5,5)
    text = font.render("PLAY",True,"white")
    win.blit(text,(113,34))
    how_to_play_btn = pygame.draw.rect(win,"red",(230,25,240,40),0,5)
    pygame.draw.rect(win,"yellow",(230,25,240,40),5,5)
    text = font.render("HOW TO PLAY",True,"white")
    win.blit(text,(263,34))
    if how_to_play_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        print("baskaran")
    exit_btn = pygame.draw.rect(win,"red",(480,25,140,40),0,5)
    pygame.draw.rect(win,"yellow",(480,25,140,40),5,5)
    text = font.render("EXIT",True,"white")
    win.blit(text,(518,34))
    if exit_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        exit()
    pygame.display.update()
    if home_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        main_Play = True
    else:
        main_Play = False
    return main_Play
if __name__ in "__main__":
    win = pygame.display.set_mode((800,650))
    pygame.display.set_caption("My Sudoku")
    font = pygame.font.Font('freesansbold.ttf', 24)
    font1 = pygame.font.Font('freesansbold.ttf', 25)
    font2 = pygame.font.Font('freesansbold.ttf', 18)
    back_ground = "green"
    main_Play = False
    main_Play = False
    thulasi = False
    running = True
    while running:
        win.fill((255,0,255))
        if main_Play == True:
            Play = Play_game()
        else:
            Play = home()
        def murugan():
            if thulasi == True:
                user_play()
            else:
                home()
                print("hello")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
