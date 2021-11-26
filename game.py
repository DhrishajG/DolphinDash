from tkinter import Tk, Canvas, PhotoImage, Label, Button, Text
from time import sleep
from random import randint as rand

def overlapping(a, b):
    a_dim = canvas.coords(a)
    b_dim = canvas.coords(b)
    if a_dim[0] >= b_dim[0]-15 and a_dim[0] <= b_dim[0]+15 and a_dim[1] >= b_dim[1]-20 and a_dim[1] <= b_dim[1]+20:
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

def menuMain():
    global menu, gameImg, game_text, start_button, customise_button, restart_btn, resume_btn, leaderboard_btn
    menu = canvas.create_rectangle(0, 0, 1280, 720, fill="#4B0082")
    game_text = canvas.create_image(640, 100, image=gameImg, anchor='c')
    start_button = Button(window, text="new game", font="Bookshelf 20 bold", height=2, width=26, command=getUsername, anchor='c')
    start_button.place(x=440, y=300)
    customise_button = Button(window, text="customise", font="Bookshelf 20 bold", height=2, width=26, command=customise, anchor='c')
    customise_button.place(x=440, y=400)
    resume_btn = Button(window, text="resume", font="Bookshelf 20 bold", height=2, width=26, command=reload, anchor='c')
    resume_btn.place(x=440, y=500)
    leaderboard_btn = Button(window, text="leaderboard", font="Bookshelf 20 bold", height=2, width=26, command=showLeaderboard, anchor='c')
    leaderboard_btn.place(x=440, y=600)

def game_over():
    global isRestart, restart_btn, t, gameOver, isPause, isBoss, isRestart, i, j, score, lives, dolphin, dolphinImg, enemies, fish_arr, isTurtle, gameOver_btn, gameover, livesDisplay, lives_arr, score_txt, score_display, gameProgress, leaderboard
    canvas.delete(gameover)
    gameProgress = open("db/progress.txt", "w")
    gameProgress.close()
    leaderboard = open("db/leaderboard.txt", "a")
    lb_txt = "\n"+str(score)+","+username
    leaderboard.write(lb_txt)
    gameOver = False
    isPause = False
    isBoss = False
    gameOver_btn.destroy()
    isRestart = False
    t = 0
    i = 0
    j = 0
    score = 0
    lives = 3
    canvas.delete(score_display)
    canvas.delete(livesDisplay)
    score_txt = "Score:"+str(score)
    score_display = canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))
    livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])
    canvas.delete(dolphin)
    dolphin = canvas.create_image(550, 360, image=dolphinImg, anchor='e')
    if len(enemies) != 0:
        for a in range(0, len(enemies), 3):
            canvas.delete(enemies[a])
    if len(fish_arr) != 0:
        for a in range(0, len(fish_arr)):
            canvas.delete(fish_arr[a])
    if len(isTurtle) != 0:
        for a in range(0, len(isTurtle), 2):
            canvas.delete(isTurtle[a])
    enemies.clear()
    fish_arr.clear()
    isTurtle.clear()
    canvas.pack()
    window.update()
    menuMain()

def restart():
    global isRestart, restart_btn, t, gameOver, isPause, isBoss, isRestart, i, j, score, lives, dolphin, dolphinImg, enemies, fish_arr, isTurtle, livesDisplay, lives_arr, score_txt, score_display, saveAndQuit_btn
    isRestart = True
    gameOver = False
    isPause = False
    isBoss = False
    saveAndQuit_btn.destroy()
    restart_btn.destroy()
    motion()
    isRestart = False
    t = 0
    i = 0
    j = 0
    score = 0
    lives = 3
    canvas.delete(score_display)
    canvas.delete(livesDisplay)
    score_txt = "Score:"+str(score)
    score_display = canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))
    livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])
    canvas.delete(dolphin)
    dolphin = canvas.create_image(550, 360, image=dolphinImg, anchor = 'e')
    if len(enemies) != 0:
        for a in range(0,len(enemies),3):
            canvas.delete(enemies[a])
    if len(fish_arr) != 0:
        for a in range(0, len(fish_arr)):
            canvas.delete(fish_arr[a])
    if len(isTurtle) != 0:
        for a in range(0, len(isTurtle), 2):
            canvas.delete(isTurtle[a])
    enemies.clear()
    fish_arr.clear()
    isTurtle.clear()
    canvas.pack()
    window.update()
    isRestart = False
    menuMain()

def saveAndQuit():
    global gameProgress, score, username, lives, dolphin, dolphins, dolphin1, dolphin2, dolphin3, saveAndQuit_btn, restart_btn, isRestart, restart_btn, t, gameOver, isPause, isBoss, isRestart, i, j, dolphinImg, enemies, fish_arr, isTurtle, gameOver_btn, gameover, livesDisplay, lives_arr, score_txt, score_display
    gameProgress = open("db/progress.txt", "w")
    which_dolphin = 0
    if dolphins == dolphin1:
        which_dolphin = 1
    elif dolphins == dolphin2:
        which_dolphin = 2
    elif dolphins == dolphin3:
        which_dolphin = 3
    dol_coords = canvas.coords(dolphin)
    data = (username+"\n"+str(score)+"\n"+str(lives)+"\n"+str(which_dolphin)+"\n"+str(dol_coords[0])+"\n"+str(dol_coords[1])).split("\n")
    for a in range(len(data)):
        output_str = data[a]+"\n"
        gameProgress.write(output_str)
    gameProgress.close()
    saveAndQuit_btn.destroy()
    restart_btn.destroy()
    gameOver = False
    isPause = False
    isBoss = False
    gameOver_btn.destroy()
    isRestart = False
    t = 0
    i = 0
    j = 0
    score = 0
    lives = 3
    canvas.delete(score_display)
    canvas.delete(livesDisplay)
    score_txt = "Score:"+str(score)
    score_display = canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))
    livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])
    canvas.delete(dolphin)
    dolphin = canvas.create_image(550, 360, image=dolphinImg, anchor='e')
    if len(enemies) != 0:
        for a in range(0, len(enemies), 3):
            canvas.delete(enemies[a])
    if len(fish_arr) != 0:
        for a in range(0, len(fish_arr)):
            canvas.delete(fish_arr[a])
    if len(isTurtle) != 0:
        for a in range(0, len(isTurtle), 2):
            canvas.delete(isTurtle[a])
    enemies.clear()
    fish_arr.clear()
    isTurtle.clear()
    canvas.pack()
    window.update()
    menuMain()

def pause(event):
    global isPause, restart_btn, saveAndQuit_btn
    if isPause is True:
        restart_btn.destroy()
        saveAndQuit_btn.destroy()
        isPause = False
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)
        canvas.bind("<t>", turtleCheat)
        canvas.bind("<i>", invisibleCheat)
        canvas.focus_set()
        motion()
    elif isPause is False:
        restart_btn = Button(window, text="restart", font="Bookshelf 20 bold", height=2, width=26, command=restart, anchor='c')
        restart_btn.place(x=440, y=300)
        saveAndQuit_btn = Button(window, text="save & quit", font="Bookshelf 20 bold", height=2, width=26, command=saveAndQuit, anchor='c')
        saveAndQuit_btn.place(x=440, y=400)
        isPause = True
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")
        canvas.unbind("<t>")
        canvas.unbind("<i>")
        canvas.focus_set()

def turtleCheat(event):
    global turtlee, isTurtle, turtle
    turtlee = canvas.create_image(990, 570, image=turtle[0], anchor='n')
    isTurtle.append(turtlee)
    isTurtle.append(0)

def bossKey(event):
    global isBoss, boss_canvas, bossImg
    if isBoss is False:
        boss_canvas = canvas.create_image(640, 360, image=bossImg, anchor='c')
        isBoss = True
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")
        canvas.unbind("<t>")
        canvas.unbind("<space>")
        canvas.unbind("<i>")
        canvas.focus_set()
    elif isBoss is True:
        canvas.delete(boss_canvas)
        isBoss = False
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)
        canvas.bind("<t>", turtleCheat)
        canvas.bind("<space>", pause)
        canvas.bind("<i>", invisibleCheat)
        canvas.focus_set()
        motion()

def invisibleCheat(event):
    global isInvisible, iCount, invinsibleImg, invinsibleTxt
    invinsibleTxt = canvas.create_image(640, 50, image=invinsibleImg, anchor='c')
    isInvisible = True
    iCount = 0

def getUsername():
    global username, start_button, game_text, menu, customise_button, username_textbox, submit_btn, resume_btn, leaderboard_btn
    canvas.delete(menu)
    canvas.delete(game_text)
    customise_button.destroy()
    start_button.destroy()
    resume_btn.destroy()
    leaderboard_btn.destroy()
    canvas.pack()
    username_textbox = Text(window, height=2, width=28, font="Bookshelf 20 bold")
    username_textbox.place(x=440, y=300)
    submit_btn = Button(window, height=2, width=26, text="start!", font="Bookshelf 20 bold", command=startGame)
    submit_btn.place(x=440, y=400)

def startGame():
    global start_button, game_text, menu, customise_button, username_textbox, submit_btn, username, gameProgress
    gameProgress = open("db/progress.txt", "w")
    username = username_textbox.get('1.0', 'end-1c')
    username_textbox.destroy()
    submit_btn.destroy()
    motion()

def reload():
    global username, lives, score, dolphin, dolphins, dolphin1, dolphin2, dolphin3, menu, game_text, start_button, customise_button, resume_btn, score_display, livesDisplay, lives_arr, leaderboard_btn
    gProg = open("db/progress.txt", "r")
    data_reload = []
    lines = gProg.readlines()
    for line in lines:
        data_reload.append(line.strip())
    username = data_reload[0]
    score = int(data_reload[1])
    lives = int(data_reload[2])
    dolph = int(data_reload[3])
    dolphX = float(data_reload[4])
    dolphY = float(data_reload[5])
    canvas.delete(dolphin)
    dolphin_used = []
    if dolph == 1:
        dolphin_used = dolphin1
    if dolph == 2:
        dolphin_used = dolphin2
    if dolph == 3:
        dolphin_used = dolphin3
    dolphin = canvas.create_image(dolphX, dolphY, image=dolphin_used[0], anchor='e')
    canvas.delete(menu)
    canvas.delete(game_text)
    start_button.destroy()
    customise_button.destroy()
    resume_btn.destroy()
    leaderboard_btn.destroy()
    canvas.delete(score_display)
    canvas.delete(livesDisplay)
    score_txt = "Score:"+str(score)
    score_display = canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))
    livesDisplay = canvas.create_image(350, 50, image=lives_arr[lives])
    motion()

def dolph1_set():
    global dolphins, dolphin1
    dolphins = dolphin1

def dolph2_set():
    global dolphins, dolphin2
    dolphins = dolphin2

def dolph3_set():
    global dolphins, dolphin3
    dolphins = dolphin3

def cusToStart():
    global custom_canvas, dolph3_btn, dolph2_btn, dolph1_btn, cus_to_start, custom_text, game_text, gameImg
    custom_canvas.pack_forget()
    dolph1_btn.destroy()
    dolph2_btn.destroy()
    dolph3_btn.destroy()
    cus_to_start.destroy()
    canvas.delete(custom_text)
    game_text = canvas.create_image(640, 100, image=gameImg, anchor='c')

def customise():
    global dolphins, dolphin1, dolphin2, dolphin3, game_text, start_button, customise_button, custom_canvas, dolph3_btn, dolph2_btn, dolph1_btn, cus_to_start, custom_text
    canvas.delete(game_text)
    custom_canvas = Canvas(window, bg="#4B0082", width=1280, height=720)
    custom_canvas.pack()
    custom_text = canvas.create_text(640, 100, text="Choose your dolphin", font="Bookshelf 30 bold", fill="white", anchor='c')
    custom_canvas.pack()
    dolph1_btn = Button(window, text="Gary: joyful dolphin who loves his home", font="Bookshelf 20 bold", height=2, width=60, command=dolph1_set, anchor='c')
    dolph1_btn.place(x=250, y=200)
    dolph2_btn = Button(window, text="Azuki: an alien dolphin who is here to kidnap Gary", font="Bookshelf 20 bold", height=2, width=60, command=dolph2_set, anchor='c')
    dolph2_btn.place(x=250, y=300)
    dolph3_btn = Button(window, text="Suido: a stingray who is scared of Gary", height=2, width=60, font="Bookshelf 20 bold", command=dolph3_set, anchor='c')
    dolph3_btn.place(x=250, y=400)
    cus_to_start = Button(window, text="back", height=2, width=60, font="Bookshelf 20 bold", command=cusToStart, anchor='c')
    cus_to_start.place(x=250, y=500)

def motion():
    canvas.bind("<Up>", upKey)
    canvas.bind("<Down>", downKey)
    canvas.bind("<space>", pause)
    canvas.bind("<t>", turtleCheat)
    canvas.bind("<b>", bossKey)
    canvas.bind("<i>", invisibleCheat)
    canvas.focus_set()
    global t, isPause, enemies, fish_arr, i, j, gameOver, dolphin, dolphins, spikes, crab, danger, lives, score, score_txt, score_display, isInvisible, iCount, livesDisplay, lives_arr, invinsibleImg, invinsibleTxt, gameoverImg, gameover, gameOver_btn
    canvas.bind("<Up>", upKey)
    canvas.bind("<Down>", downKey)
    canvas.bind("<space>", pause)
    canvas.bind("<t>", turtleCheat)
    canvas.bind("<b>", bossKey)
    canvas.bind("<i>", invisibleCheat)
    canvas.focus_set()
    while isPause is False and lives > 0 and isBoss is False and isRestart is False:
        enemyNumber = 0
        if i == len(dolphins)-1:
            i = 0
        if isInvisible == True and iCount <= 100:
            dolphin_coords = canvas.coords(dolphin)
            canvas.delete(dolphin)
            dolphin = canvas.create_image(dolphin_coords[0], dolphin_coords[1], image=dolphins[i], anchor = 'e')
            iCount += 1
        else:
            isInvisible = False
            canvas.delete(invinsibleTxt)
            dolphin_coords = canvas.coords(dolphin)
            canvas.delete(dolphin)
            dolphin = canvas.create_image(dolphin_coords[0], dolphin_coords[1], image=dolphins[i], anchor='e')
        window.update()
        sleep(0.06)
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
                enemy = canvas.create_image(enemyX, 590, image=danger[enemyNumber][0], anchor='n')
                enemies.append(enemy)
                enemies.append(enemyNumber)
                enemies.append(0)
            elif danger[enemyNumber] != spikes:
                enemy = canvas.create_image(enemyX, enemyY, image=danger[enemyNumber][0], anchor='w')
                enemies.append(enemy)
                enemies.append(enemyNumber)
                enemies.append(0)
        if len(enemies) != 0:
            for a in range(0, len(enemies), 3):
                enemies[a+2] += 1
                canvas.move(enemies[a], -20, 0)
                if enemies[a+2] == len(danger[enemies[a+1]]):
                    enemies[a+2] = 0
                enemy_coords = canvas.coords(enemies[a])
                canvas.delete(enemies[a])
                enemies[a] = canvas.create_image(enemy_coords[0], enemy_coords[1], image=danger[enemies[a+1]][enemies[a+2]], anchor='w')
                if enemy_coords[0] < 280:
                    canvas.delete(enemies[a])
                    del enemies[0:3]
                    a -= 3
                    break
                if overlapping(dolphin, enemies[a]) and isInvisible is False:
                    lives -= 1
                    if lives == 0:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[0])
                    elif lives == 1:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[1])
                    elif lives == 2:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[2])
                    elif lives == 3:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])
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
                    score_txt="Score:"+str(score)
                    canvas.delete(score_display)
                    score_display=canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))
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
                    del isTurtle[0:2]
                    a -= 2
                    break
                if overlapping(dolphin, isTurtle[a]):
                    lives += 1
                    canvas.delete(isTurtle[a])
                    del isTurtle[0:2]
                    a -= 2
                    if lives > 3:
                        lives = 3
                    if lives == 0:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[0])
                    elif lives == 1:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[1])
                    elif lives == 2:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[2])
                    elif lives == 3:
                        canvas.delete(livesDisplay)
                        livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])
                    break
        t += 1
        window.update()
    if lives == 0:
        gameover = canvas.create_image(640, 250, image=gameoverImg, anchor='c')
        gameOver_btn = Button(window, text="restart", font="Bookshelf 20 bold", height=2, width=26, command=game_over, anchor='c')
        gameOver_btn.place(x=440, y=350)
        canvas.unbind("<Up>")
        canvas.unbind("<Down>")
        canvas.unbind("<t>")
        canvas.unbind("<space>")
        canvas.unbind("<i>")
        canvas.focus_set()

def sortList():
    global leaderboard
    lblist = []
    leaderboard = open("db/leaderboard.txt", "r")
    lines = leaderboard.readlines()
    for line in lines:
        if line != "\n":
            item = line.split(",")
            player = []
            player.append(int(item[0].strip()))
            player.append(item[1].strip())
            lblist.append(player)
    lblist.sort(reverse=True)
    return lblist

def showLeaderboard():
    lbwindow = Tk()
    lbwindow.title("Leader Board")
    lbwindow.geometry("1280x720")
    lbcanvas = Canvas(lbwindow, bg = '#4B0082', width = 1280, height = 720)
    lbmenu = lbcanvas.create_rectangle(0, 0, 1280, 720, fill="#4B0082")
    lbtxt = lbcanvas.create_text(640, 50, text="LEADERBOARD", font="Bookshelf 30 bold", fill="white", anchor='c')
    lbcanvas.pack()
    lbwindow.update()
    lb_names = sortList()
    board = ""
    pos = 1
    textY = 150
    for i in range(len(lb_names)):
        name = lb_names[i]
        if name[0] != "\n" and pos <= 10:
            board = str(pos)+". "+name[1]+" - "+str(name[0])
            lbcanvas.create_text(640, textY, text=board, font = "Bookshelf 20", fill="white", anchor='c')
            textY += 50
            pos += 1
    lbwindow.mainloop()

window = Tk()
window.title("Dolphin Dash")
window.geometry("1280x720")
canvas = Canvas(window, bg = '#383838',width = 1280, height = 720)
canvas.create_rectangle(280, 0, 1000, 720, fill="#006994")
canvas.create_rectangle(280, 600, 1000, 720, fill="#c2b280")
canvas.create_rectangle(0, 650, 1280, 720, fill="#ffb101")
canvas.pack()

text_bg = canvas.create_text(640, 680, text="D    O    L    P    H    I    N                       D    A    S    H", font=("Bookshelf Symbol", 40, "bold"), fill='white')
text_fg = canvas.create_text(642, 682, text="D    O    L    P    H    I    N                       D    A    S    H", font=("Bookshelf Symbol", 40, "bold"), fill='red')

dolphinImg = PhotoImage(file="images/dolphin/0-0.png")
dolphin = canvas.create_image(550, 360, image=dolphinImg, anchor = 'e')
dolphin1 = []
dolphin1.append(PhotoImage(file="images/dolphin/0-0.png"))
dolphin1.append(PhotoImage(file="images/dolphin/0-1.png"))
dolphin1.append(PhotoImage(file="images/dolphin/0-2.png"))
dolphin1.append(PhotoImage(file="images/dolphin/0-3.png"))
dolphin1.append(PhotoImage(file="images/dolphin/0-4.png"))
dolphin1.append(PhotoImage(file="images/dolphin/0-5.png"))

dolphin2 = []
dolphin2.append(PhotoImage(file="images/trellia/1-0.png"))
dolphin2.append(PhotoImage(file="images/trellia/1-1.png"))
dolphin2.append(PhotoImage(file="images/trellia/1-2.png"))
dolphin2.append(PhotoImage(file="images/trellia/1-3.png"))
dolphin2.append(PhotoImage(file="images/trellia/1-4.png"))
dolphin2.append(PhotoImage(file="images/trellia/1-5.png"))

dolphin3 = []
dolphin3.append(PhotoImage(file="images/stingray/1-0.png"))
dolphin3.append(PhotoImage(file="images/stingray/1-1.png"))
dolphin3.append(PhotoImage(file="images/stingray/1-2.png"))
dolphin3.append(PhotoImage(file="images/stingray/1-3.png"))
dolphin3.append(PhotoImage(file="images/stingray/1-4.png"))
dolphin3.append(PhotoImage(file="images/stingray/1-5.png"))

dolphins = dolphin1

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

lives_arr = []
lives_arr.append(PhotoImage(file="images/lives/0.png"))
lives_arr.append(PhotoImage(file="images/lives/1.png"))
lives_arr.append(PhotoImage(file="images/lives/2.png"))
lives_arr.append(PhotoImage(file="images/lives/3.png"))
livesDisplay = canvas.create_image(350, 50, image=lives_arr[3])

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
isBoss = False
isRestart = False
enemies = []
fish_arr = []
i = 0
j = 0

score = 0
lives = 3

gameProgress = open("db/progress.txt")
leaderboard = open("db/leaderboard.txt")
leaderboard.close()

username = ""
username_textbox = Text(window, height=2, width=26, font="Bookshelf 20 bold")
submit_btn = Button(window, height=2, width=26, text="start!", command=startGame)

score_txt = "Score:"+str(score)
score_display = canvas.create_text(900, 40, text=score_txt, fill="white", font=("Times New Roman", 20, "bold", "italic"))

iCount = 0
isInvisible = False
invinsibleImg = PhotoImage(file="images/invinsible.png")
invinsibleTxt = canvas.create_image(640, 50, image=invinsibleImg, anchor='c')
canvas.delete(invinsibleTxt)

isTurtle = []
menu = canvas.create_rectangle(0, 0, 1280, 720, fill="#4B0082")
canvas.delete(menu)
gameImg  = PhotoImage(file="images/game_name.png")
start_button = Button(window, text="new game", font="Bookshelf 20 bold", height = 2, width = 26, command=getUsername, anchor='c')
customise_button = Button(window, text="customise", font="Bookshelf 20 bold", height=2, width=26, command=customise, anchor='c')
restart_btn = Button(window, text="restart", font="Bookshelf 20 bold", height=2, width=26, command=restart, anchor='c')
gameoverImg = PhotoImage(file="images/gameover.png")
gameover = canvas.create_image(640, 300, image=gameoverImg, anchor='c')
canvas.delete(gameover)
gameOver_btn = Button(window, text="restart", font="Bookshelf 20 bold", height=2, width=26, command=game_over, anchor='c')
saveAndQuit_btn  = Button(window, text="save & quit", font="Bookshelf 20 bold", height=2, width=26, command=saveAndQuit, anchor='c')
resume_btn = Button(window, text="resume", font="Bookshelf 20 bold", height=2, width=26, command=reload, anchor='c')
leaderboard_btn = Button(window, text="leaderboard", font="Bookshelf 20 bold", height=2, width=26, command=showLeaderboard, anchor='c')

menuMain()

window.mainloop()
