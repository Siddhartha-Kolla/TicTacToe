import pygame as pg 
import time

def run():
    pg.init()
    pg.font.init()
    pg.mouse.set_cursor(*pg.cursors.broken_x)

    global width,height
    width, height = 600,600
    global screen
    screen = pg.display.set_mode((width, height))

    pg.display.set_icon(pg.image.load('images/logo.png'))
    pg.display.set_caption('Tic Tac Toe')

    global rows , cols
    rows , cols = 3,3
    
    global game
    game = []

    for i in range(rows):
        game.append([])
        for x in range(cols):
            game[i].append("-")

    global kreuz
    kreuz = True
    global done
    done = False
    global win_text_showed
    win_text_showed = False

    global fps
    fps = 30
    global clock
    clock = pg.time.Clock()

def placing_the_figure():
    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] == "X":
                screen.blit(pg.transform.smoothscale(pg.image.load('images/cross.png'),(134,134)),(col*(600/3)+30,row*(600/3)+30))
            if game[row][col] == "O":
                screen.blit(pg.image.load('images/circle.png'),(col*(600/3)+30,row*(600/3)+30))

def check():
    for i in range(len(game)):
        com = ""
        for x in range(len(game[i])):
            com += game[i][x]
        if com == "XXX" or com == "OOO": return com[0]
    for i in range(3):
        com = ""
        for l in game:
            com += l[i]
        if com == "XXX" or com == "OOO": return com[0]
    if game[0][2]=="X" and game[1][1]=="X" and game[2][0]=="X":
        return "X"
    elif game[0][2]=="O" and game[1][1]=="O" and game[2][0]=="O":
        return "X"
    
    com = ""
    for i in range(3):
        com += game[i][i]
    if com == "XXX" or com == "OOO": return com[0]

    com = ""
    for i in range(3):
        com += game[i][2-i]
    if com == "XXX" or com == "OOO": return com[0]

    return "0"
def drawcheck():
    c = ""
    for i in game:
        for x in i:
            c += x
    if "-" in c: return "0"
    return "U"

def reset():
    run()

run()

while not done:
    clock.tick(fps)
    screen.fill((255,255,255))
    grid = pg.image.load('images/grid.png')
    grid = pg.transform.smoothscale(grid,(600,600))
    screen.blit(grid,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            Xpos,Ypos = pg.mouse.get_pos()
            if game[Ypos//200][Xpos//200] == "-":
                if kreuz:
                    game[Ypos//200][Xpos//200]= "X"
                    kreuz = False
                    pg.mouse.set_cursor(*pg.cursors.diamond)
                else:
                    game[Ypos//200][Xpos//200]= "O"
                    kreuz = True
                    pg.mouse.set_cursor(*pg.cursors.broken_x)
                    

    placing_the_figure()

    if not check()[0].isdecimal() and not win_text_showed:
        screen.blit(pg.font.SysFont("Comic Sans MS",100).render(f"{check()} gewinnt",True,(0,0,255)), (75, 230))
        # pg.draw.line(screen,(0,255,0),(50,50),(100,50),width=15)
        # (col*(600/3)+30+67,row*(600/3)+30+67)67
        pg.display.flip()
        time.sleep(2)
        win_text_showed = True
        reset()
    
    if not drawcheck().isdecimal() and not win_text_showed:
        screen.blit(pg.font.SysFont("Comic Sans MS",150).render("Draw",True,(0,0,255)), (140, 190))
        pg.display.flip()
        time.sleep(2)
        win_text_showed = True
        reset()
    pg.display.flip() 

pg.quit()
