from tkinter import Tk, Canvas, PhotoImage, Label
from time import sleep
from random import randint as rand
from threading import Thread


def checkCollision():
    dolphin_coords = canvas.coords(dolphin)
    if dolphin_coords[1] == 24.0:
        canvas.move(dolphin, 0, 8)
    elif dolphin_coords[1] == 576.0:
        canvas.move(dolphin, 0, -8)

def upKey(event):
    canvas.move(dolphin, 0, -8)
    checkCollision()

def downKey(event):
    canvas.move(dolphin, 0, 8)
    checkCollision()

def enemyMotion():
    global danger
    enemyNumber = rand(0, (len(danger)-1))
    enemyX = 990
    enemyY = rand(10, 550)
    print(danger[enemyNumber])
    if danger[enemyNumber] == crab or danger[enemyNumber] == spikes:
        enemy = canvas.create_image(enemyX, 590, image=danger[enemyNumber][0])
    elif danger[enemyNumber] != spikes:
        enemy = canvas.create_image(enemyX, enemyY, image=danger[enemyNumber][0])
    enemy_coords = canvas.coords(enemy)
    while enemy_coords[0] > 300 :
        for i in range(len(danger[enemyNumber])):
            enemy_coords = canvas.coords(enemy)
            sleep(0.1)
            canvas.delete(enemy)
            enemy = canvas.create_image(enemy_coords[0], enemy_coords[1], image=danger[enemyNumber][i])
            window.update()
            canvas.move(enemy, -20, 0)

def spawnEnemy():
    global danger, enemyNumber
    enemyNumber = rand(0, (len(danger)-1))
    enemyX = 990
    enemyY = rand(10, 550)
    sleep(2)
    enemy_coords = canvas.coords(enemy)
    while enemy_coords[0] > 300 :
        enemyNumber = rand(0, (len(danger)-1))
        enemyY = rand(10, 550)
        if danger[enemyNumber] == crab or danger[enemyNumber] == spikes:
            enemy = canvas.create_image(enemyX, 590, image=danger[enemyNumber][0])
        elif danger[enemyNumber] != spikes:
            enemy = canvas.create_image(enemyX, enemyY, image=danger[enemyNumber][0])
    return enemy


window = Tk()
window.title("Splashy Dolphin")
window.geometry("1280x720")
canvas = Canvas(window, bg = '#383838',width = 1280, height = 720)
canvas.create_rectangle(280, 0, 1000, 720, fill="#006994")
canvas.create_rectangle(280, 600, 1000, 720, fill="#c2b280")
canvas.create_rectangle(0, 650, 1280, 720, fill="#ffb101")
canvas.pack()

text_bg = canvas.create_text(640, 680, text="S    P    L    A    S    H    Y        D    O    L    P    H    I    N", font=("Bookshelf Symbol", 40, "bold"), fill='white')
text_fg = canvas.create_text(642, 682, text="S    P    L    A    S    H    Y        D    O    L    P    H    I    N", font=("Bookshelf Symbol", 40, "bold"), fill='red')

canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.focus_set()

dolphinImg = PhotoImage(file="images/dolphin/0-0.png")
dolphin = canvas.create_image(500, 360, image=dolphinImg)
dolphins = []
dolphins.append(PhotoImage(file="images/dolphin/0-0.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-1.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-2.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-3.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-4.png"))
dolphins.append(PhotoImage(file="images/dolphin/0-5.png"))

spikes = []
spikes.append(PhotoImage(file="images/spikes/0-0.png"))
spikes.append(PhotoImage(file="images/spikes/0-2.png"))
spikes.append(PhotoImage(file="images/spikes/0-4.png"))
spikes.append(PhotoImage(file="images/spikes/0-6.png"))

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

pf_danger = []
pf_danger.append(pufferfish[4])
pf_danger.append(pufferfish[5])
pf_danger.append(pufferfish[6])

danger = []
danger.append(spikes)
danger.append(shark)
danger.append(orca)
danger.append(ph_jelly)
danger.append(jellyfish)
danger.append(crab)
danger.append(pf_danger)

t = 0
gameOver = False
enemies = []
i = 0
j = 0
while True:
    enemyNumber = 0
    if i == len(dolphins)-1:
        i = 0
    dolphin_coords = canvas.coords(dolphin)
    canvas.delete(dolphin)
    dolphin = canvas.create_image(dolphin_coords[0], dolphin_coords[1], image=dolphins[i])
    window.update()
    sleep(0.05)
    i += 1
    if t % 60 == 0:
        enemyNumber = rand(0, (len(danger)-1))
        enemyX = 990
        enemyY = rand(10, 550)
        enemyNumber = rand(0, (len(danger)-1))
        enemyY = rand(10, 550)
        if danger[enemyNumber] == crab or danger[enemyNumber] == spikes:
            enemy = canvas.create_image(enemyX, 590, image=danger[enemyNumber][0])
            enemies.append(enemy)
        elif danger[enemyNumber] != spikes:
            enemy = canvas.create_image(enemyX, enemyY, image=danger[enemyNumber][0])
            enemies.append(enemy)
    if len(enemies) != 0:
        for a in range(len(enemies)):
            canvas.move(enemies[a], -6, 0)
            enemy_coords = canvas.coords(enemies[a])
            if enemy_coords[0] < 300:
                canvas.delete(enemies[a])
                enemies.remove(enemies[a])
                break
    t += 1
    window.update()


window.mainloop()
