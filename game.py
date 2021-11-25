from tkinter import Tk, Canvas, PhotoImage, Label
from time import sleep
from random import randint as rand
from threading import Thread

def overlapping(a,b):
    a_dim = canvas.coords(a)
    b_dim = canvas.coords(b)
    if a_dim[0] >= b_dim[0]-15 and a_dim[0] <= b_dim[0]+15 and a_dim[1] >= b_dim[1]-20 and a_dim[1] <=b_dim[1]+20:
        return True
    return False

def checkCollision():
    dolphin_coords = canvas.coords(dolphin)
    if dolphin_coords[1] == 24.0:
        canvas.move(dolphin, 0, 8)
    elif dolphin_coords[1] == 584.0:
        canvas.move(dolphin, 0, -8)

def upKey(event):
    canvas.move(dolphin, 0, -8)
    checkCollision()

def downKey(event):
    canvas.move(dolphin, 0, 8)
    checkCollision()

def pause(event):
    global isPause
    if isPause == True:
        isPause = False
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)
        canvas.bind("<t>", turtleCheat)
        canvas.focus_set()
        motion()
    elif isPause == False:
        isPause = True
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")
        canvas.unbind("<t>")
        canvas.focus_set()

def turtleCheat(event):
    global turtlee, isTurtle, turtle
    turtlee = canvas.create_image(990, 570, image=turtle[0], anchor = 'n')
    isTurtle.append(turtlee)
    isTurtle.append(0)

def bossKey(event):
    global isPause, boss_canvas, bossImg
    if isPause == False:
        boss_canvas = canvas.create_image(640, 360, image=bossImg, anchor = 'c')
        isPause = True
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")
        canvas.unbind("<t>")
        canvas.unbind("<space>")
        canvas.focus_set()
    elif isPause == True:
        canvas.delete(boss_canvas)
        isPause = False
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)
        canvas.bind("<t>", turtleCheat)
        canvas.bind("<space>", pause)
        canvas.focus_set()
        motion()

def motion():
    global t, isPause, enemies, fish_arr, i, j, gameOver, dolphin, dolphins, spikes, crab, danger, lives, score
    while isPause == False and lives > 0:
        enemyNumber = 0
        if i == len(dolphins)-1:
            i = 0
        dolphin_coords = canvas.coords(dolphin)
        canvas.delete(dolphin)
        dolphin = canvas.create_image(dolphin_coords[0], dolphin_coords[1], image=dolphins[i], anchor = 'e')
        window.update()
        sleep(0.07)
        i += 1
        if t % 5 == 0:
            fishNumber = rand(0, (len(fish)-1))
            fishX = 990
            fishY = rand(200, 550)
            fishy = canvas.create_image(fishX, fishY, image=fish[fishNumber])
            fish_arr.append(fishy)
        if t % 5 == 0:
            enemyNumber = rand(0, (len(danger)-1))
            enemyX = 990
            enemyY = rand(200, 550)
            if danger[enemyNumber] == crab or danger[enemyNumber] == spikes:
                enemy = canvas.create_image(enemyX, 590, image=danger[enemyNumber][0], anchor = 'n')
                enemies.append(enemy)
                enemies.append(enemyNumber)
                enemies.append(0)
            elif danger[enemyNumber] != spikes:
                enemy = canvas.create_image(enemyX, enemyY, image=danger[enemyNumber][0], anchor = 'w')
                enemies.append(enemy)
                enemies.append(enemyNumber)
                enemies.append(0)
        if len(enemies) != 0:
            for a in range(0,len(enemies),3):
                enemies[a+2] += 1
                canvas.move(enemies[a], -20, 0)
                if enemies[a+2] == len(danger[enemies[a+1]]):
                    enemies[a+2] = 0
                enemy_coords = canvas.coords(enemies[a])
                canvas.delete(enemies[a])
                enemies[a] = canvas.create_image(enemy_coords[0], enemy_coords[1], image=danger[enemies[a+1]][enemies[a+2]], anchor = 'w')
                if enemy_coords[0] < 280:
                    canvas.delete(enemies[a])
                    del enemies[0:3]
                    a -= 3
                    break
                if overlapping(dolphin, enemies[a]):
                    lives -= 1
                    print(lives)
        if len(fish_arr) != 0:
            for a in range(0, len(fish_arr)):
                canvas.move(fish_arr[a], -20, 0)
                fish_coords = canvas.coords(fish_arr[a])
                if fish_coords[0] < 280:
                    canvas.delete(fish_arr[a])
                    del fish_arr[0]
                    a -= 1
                    break
                if overlapping(fish_arr[a], dolphin):
                    score += 10
                    print(score)
                    canvas.delete(fish_arr[a])
                    del fish_arr[a]
                    a -= 1
                    break
        if len(isTurtle) != 0:
            for a in range(0, len(isTurtle), 2):
                canvas.move(isTurtle[a], -10, 0)
                turtle_coords = canvas.coords(isTurtle[a])
                if isTurtle[a+1] == (len(turtle)-1):
                    isTurtle[a+1] = 0
                canvas.delete(isTurtle[a])
                isTurtle[a] = canvas.create_image(turtle_coords[0], turtle_coords[1], image=turtle[isTurtle[a+1]], anchor = 'n')
                if turtle_coords[0] < 280:
                    canvas.delete(isTurtle[a])
                    print(score)
                    del isTurtle[0:2]
                    a -= 2
                    break
                if overlapping(dolphin, isTurtle[a]):
                    lives += 1
                    canvas.delete(isTurtle[a])
                    del isTurtle[0:2]
                    a -= 2
                    break
        t += 1
        window.update()

window = Tk()
window.title("Dolphin Dive")
window.geometry("1280x720")
canvas = Canvas(window, bg = '#383838',width = 1280, height = 720)
canvas.create_rectangle(280, 0, 1000, 720, fill="#006994")
canvas.create_rectangle(280, 600, 1000, 720, fill="#c2b280")
canvas.create_rectangle(0, 650, 1280, 720, fill="#ffb101")
canvas.pack()

text_bg = canvas.create_text(640, 680, text="D    O    L    P    H    I    N                       D    I    V    E", font=("Bookshelf Symbol", 40, "bold"), fill='white')
text_fg = canvas.create_text(642, 682, text="D    O    L    P    H    I    N                       D    I    V    E", font=("Bookshelf Symbol", 40, "bold"), fill='red')

canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind("<space>", pause)
canvas.bind("<t>", turtleCheat)
canvas.bind("<b>", bossKey)
canvas.focus_set()

dolphinImg = PhotoImage(file="images/dolphin/0-0.png")
dolphin = canvas.create_image(550, 360, image=dolphinImg, anchor = 'e')
dolphins = []
dolphins.append(PhotoImage(file="images/dolphin/0-0.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-1.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-2.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-3.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-4.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-5.png"))

spikes = []
spikes.append(PhotoImage(file="images/spikes/0-0.png"))

shark = []
shark.append(PhotoImage(file="images/shark/2-0.png"))
shark.append(PhotoImage(file="images/shark/2-1.png"))
shark.append(PhotoImage(file="images/shark/2-2.png"))
shark.append(PhotoImage(file="images/shark/2-3.png"))

ph_jelly = []
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-0.png"))
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-1.png"))
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-2.png"))
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-3.png"))
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-4.png"))
ph_jelly.append(PhotoImage(file="images/prehistoric-jelly/0-5.png"))

orca = []
orca.append(PhotoImage(file="images/orca/0-0.png"))
orca.append(PhotoImage(file="images/orca/0-1.png"))
orca.append(PhotoImage(file="images/orca/0-2.png"))
orca.append(PhotoImage(file="images/orca/0-3.png"))

jellyfish = []
jellyfish.append(PhotoImage(file="images/jellyfish/3-0.png"))
jellyfish.append(PhotoImage(file="images/jellyfish/3-1.png"))
jellyfish.append(PhotoImage(file="images/jellyfish/3-2.png"))
jellyfish.append(PhotoImage(file="images/jellyfish/3-3.png"))
jellyfish.append(PhotoImage(file="images/jellyfish/3-4.png"))
jellyfish.append(PhotoImage(file="images/jellyfish/3-5.png"))

crab = []
crab.append(PhotoImage(file="images/crab/0-0.png"))
crab.append(PhotoImage(file="images/crab/0-1.png"))

turtle = []
turtleImg = PhotoImage(file="images/unused-turtle/0-0.png")
turtlee = canvas.create_image(990, 500, image=turtleImg, anchor = 'n')
canvas.delete(turtlee)

turtle.append(PhotoImage(file="images/unused-turtle/0-0.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-1.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-2.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-3.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-4.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-5.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-6.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-7.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-8.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-9.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-10.png"))
turtle.append(PhotoImage(file="images/unused-turtle/0-11.png"))

fish = []
fish.append(PhotoImage(file="images/fish/0-0.png"))
fish.append(PhotoImage(file="images/fish/0-1.png"))
fish.append(PhotoImage(file="images/fish/0-2.png"))
fish.append(PhotoImage(file="images/fish/0-3.png"))
fish.append(PhotoImage(file="images/fish/0-4.png"))
fish.append(PhotoImage(file="images/fish/0-5.png"))
fish.append(PhotoImage(file="images/fish/0-6.png"))
fish.append(PhotoImage(file="images/fish/0-7.png"))
fish.append(PhotoImage(file="images/fish/1-0.png"))
fish.append(PhotoImage(file="images/fish/1-1.png"))
fish.append(PhotoImage(file="images/fish/1-2.png"))
fish.append(PhotoImage(file="images/fish/1-3.png"))
fish.append(PhotoImage(file="images/fish/1-4.png"))
fish.append(PhotoImage(file="images/fish/1-5.png"))
fish.append(PhotoImage(file="images/fish/1-6.png"))
fish.append(PhotoImage(file="images/fish/1-7.png"))
fish.append(PhotoImage(file="images/fish/2-0.png"))
fish.append(PhotoImage(file="images/fish/2-1.png"))
fish.append(PhotoImage(file="images/fish/2-2.png"))
fish.append(PhotoImage(file="images/fish/2-3.png"))
fish.append(PhotoImage(file="images/fish/2-4.png"))
fish.append(PhotoImage(file="images/fish/2-5.png"))
fish.append(PhotoImage(file="images/fish/2-6.png"))
fish.append(PhotoImage(file="images/fish/2-7.png"))
fish.append(PhotoImage(file="images/fish/3-0.png"))
fish.append(PhotoImage(file="images/fish/3-1.png"))
fish.append(PhotoImage(file="images/fish/3-2.png"))

pufferfish = []
pufferfish.append(PhotoImage(file="images/pufferfish/0-0.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-1.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-2.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-3.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-4.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-5.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-4.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-3.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-2.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-1.png"))
pufferfish.append(PhotoImage(file="images/pufferfish/0-0.png"))

danger = []
danger.append(spikes)
danger.append(shark)
danger.append(orca)
danger.append(ph_jelly)
danger.append(jellyfish)
danger.append(crab)
danger.append(pufferfish)

bossImg = PhotoImage(file="images/bosskey.png")
boss_canvas = canvas.create_image(640, 360, image=bossImg, anchor = 'c')
canvas.delete(boss_canvas)

t = 0
gameOver = False
isPause = False
enemies = []
fish_arr = []
i = 0
j = 0

score = 0
lives = 3

isTurtle = []

motion()
window.mainloop()
