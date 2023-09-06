#################################
#Python Code by Siddhartha Kolla
# From 2022
# My Github Account: https://www.github.com/SiddharthaKolla
#################################

import pygame as pg
import time
from tkinter import *
from tkinter import messagebox as mb
def name_extract(player1,player2):

	root = Tk()
	root.geometry("675x400")
	root.resizable(False, False)
	root.title("Tic Tac Toe")
	root.iconbitmap(default="images/logo.ico")

	wel_lbl = Label(root,text="Welcome to Tic Tac Toe game. Please enter your names.",font=('Arial', 13,"bold"))
	wel_lbl.place(relx=0.5,rely=0.1,anchor=CENTER)

	pler_lbl = Label(root,text="Players :",font=('Times New Roman', 13,"bold"))
	pler_lbl.place(relx=0.12+0.075,rely=0.4,anchor=CENTER)

	en_t1 = StringVar()
	en_box1 = Entry(root,textvariable=en_t1,font=('Times New Roman', 12))
	en_box1.place(relx=0.15+0.075+0.2,rely=0.4,anchor=CENTER)
	en_t1.set(player1)

	en_t2 = StringVar()
	en_box2 = Entry(root,textvariable=en_t2,font=('Times New Roman', 12))
	en_box2.place(relx=0.45+0.075+0.2,rely=0.4,anchor=CENTER)
	en_t2.set(player2)

	def submit():
		global name1,name2
		name1 = en_t1.get().strip()
		name1 = name1.replace(" ","")
		name2 = en_t2.get().strip()
		name2 = name2.replace(" ","")
		root.destroy()

	ok_btn = Button(root,text="Submit",font=("Arial",12,"bold"),command=submit)
	ok_btn.place(relx=0.5,rely=0.675,anchor=CENTER,width=100,height=35)


	root.mainloop()
	return (name1[:15],name2[:15])

oldnm1,oldnm2 = "Player1","Player2"

def inititialize():

    pg.init()
    pg.font.init()



    global width , height
    width , height = 600,600

    global rows , cols
    rows , cols = 3,3

    global name1,name2
    name1,name2 = "",""
    name1,name2 = name_extract(oldnm1,oldnm2)
    if name1 == "" and name2 == "":
    	quit()

    global basefont
    basefont = pg.font.Font(None,80)

    global screen
    screen = pg.display.set_mode((width, height))
    
    global xcurs,ocurs
    xcurs,ocurs = pg.cursors.broken_x , pg.cursors.diamond

    pg.display.set_icon(pg.image.load('images/logo.ico'))
    pg.display.set_caption('Tic Tac Toe')

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

    global game
    game = []

    global xct,yct
    xct,yct = 10+((width//rows-20)//2),10+((height//cols-20)//2)

    global x_win , o_win
    x_win , o_win = "XXX","OOO"

    for i in range(rows):
        game.append([])
        for x in range(cols):
            game[i].append("-")

inititialize()

def draw():

    global linex,liney
    linex , liney = width//rows , height//cols

    for i in range(rows-1):
        pg.draw.line(screen,(0,0,0),(linex,0),(linex,height),width=10)
        linex += width//rows
    for i in range(cols-1):
        pg.draw.line(screen,(0,0,0),(0,liney),(width,liney),width=10)
        liney += height//cols

def placing_the_figure():
    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] == "X":
                screen.blit(pg.transform.smoothscale(pg.image.load('images/cross.png'),(width//rows-20,height//cols-20)),(col*(height//cols)+10,row*(width//rows)+10))
            if game[row][col] == "O":
                screen.blit(pg.transform.smoothscale(pg.image.load('images/circle.png'),(width//rows-20,height//cols-20)),(col*(height//cols)+10,row*(width//rows)+10))


def check():
    for i in range(len(game)):
        com = ""
        for x in range(len(game[i])):
            com += game[i][x]
        if x_win in com or o_win in com: return (name1 if x_win in com else name2,(0*(width//rows)+xct,i*(height//cols)+yct),((len(x_win)-1)*(width//rows)+xct,i*(height//cols)+yct))
    for i in range(cols):
        com = ""
        for l in game:
            com += l[i]
        if x_win in com or o_win in com: return (name1 if x_win in com else name2,(i*(width//rows)+xct,0*(height//cols)+yct),(i*(width//rows)+xct,(len(x_win)-1)*(height//cols)+yct))
    
    com = ""
    for i in range(min(rows,cols)):
        com += game[i][i]
    if x_win in com or o_win in com: return (name1 if x_win in com else name2,(0*(width//rows)+xct,0*(height//cols)+yct),((len(x_win)-1)*(width//rows)+xct,(len(x_win)-1)*(height//cols)+yct))

    com = ""
    for i in range(min(rows,cols)):
        com += game[i][(min(rows,cols)-1)-i]
    if x_win in com or o_win in com: return (name1 if x_win in com else name2,((min(rows,cols)-1)*(width//rows)+xct,0*(height//cols)+yct),((rows-len(x_win))*(width//rows)+xct,(len(x_win)-1)*(height//cols)+yct))

    return (0,0)
def drawcheck():
    c = ""
    for i in game:
        for x in i:
            c += x
    if "-" in c: return "0"
    return "U"

def reset():
    master = Tk()
    master.withdraw()
    pg.quit()
    res = mb.askquestion('Game Reset', 'Do you want to reset the game?')
    def rest1():
        global oldnm1,oldnm2
        oldnm1,oldnm2 = name1,name2
        inititialize()
    if res == "yes":
        master.destroy()
        rest1()
    else:
        mb.showinfo('Thank you', 'Thank you for playing the game')
        quit()


while not done:
    clock.tick(fps)
    screen.fill((255,255,255))
    draw()
    if kreuz:
        pg.mouse.set_cursor(xcurs)
    else:
        pg.mouse.set_cursor(ocurs)
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            Xpos,Ypos = event.pos
            if game[Ypos//(height//cols)][Xpos//(width//rows)] == "-":
                if kreuz:
                    game[Ypos//(height//cols)][Xpos//(width//rows)]= "X"
                    kreuz = False
                else:
                    game[Ypos//(height//cols)][Xpos//(width//rows)]= "O"
                    kreuz = True
    placing_the_figure()

    che = check()

    if not che[0] == 0 and not win_text_showed:
        pg.draw.line(screen,(0,255,0),che[1],che[2],width=15)
        na = basefont.render(che[0],True,(0,255,0))
        na_rect = na.get_rect(center=(width//2,height//2))
        screen.blit(na,na_rect)

        gewnn = basefont.render("gewinnt",True,(0,255,0))
        ge_rect = gewnn.get_rect(center=(width//2,height//2+80))
        screen.blit(gewnn,ge_rect)
        pg.display.flip()
        time.sleep(2)
        win_text_showed = True
    if not drawcheck().isdecimal() and not win_text_showed:
        dr = basefont.render("Draw",True,(0,255,0))
        dr_rect = dr.get_rect(center=(width//2,height//2))
        screen.blit(dr,dr_rect)
        pg.display.flip()
        time.sleep(2)
        win_text_showed = True
    if win_text_showed:
        reset()

    pg.display.flip()
pg.quit()