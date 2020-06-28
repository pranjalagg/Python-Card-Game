import tkinter as tk
from tkinter import *
from knight import *
import keyboard
import random
from score import *
from playsound import playsound

list = [0, 1, 2, 3]

#Knight1 Fight
def knight1_fight(b):
    b.place(x=600, y=400, anchor='center')


#Knight2 Fight
def knight2_fight(b):
    b.place(x=900, y=400, anchor='center')

#Return Knight1 to its initial position
def knight1_replace(list1, ind1, x1, y1):
    list1[ind1].place(x = x1[ind1], y = y1, anchor='nw')

#Return Knight2 to its initial position
def knight2_replace(list2, ind2, x2, y2):
    list2[ind2].place(x = x2[ind2], y = y2, anchor='se')

#Random Knight Selection
def comp_card():
    x = random.choice(list)
    return x

#Compare
def clear(list1, list2, ind1, ind2, x1, x2, y1, y2, score1, score2, situation, start, b, f):
    score1.destroy()
    score2.destroy()
    situation.destroy()
    start.destroy()
    if knight1[ind1].get_health() == 0 or knight2[ind2].get_health() == 0:
        if knight1[ind1].get_health() == 0:
            list1[ind1].destroy()
            if knight2[ind2].get_health() != 0:
                knight2_replace(list2, ind2, x2, y2)
            s1 = "SCORE = {}".format(sc.in_scorec())
            list2[4].config(text = s1)

        if knight2[ind2].get_health() == 0:
            list2[ind2].destroy()
            if knight1[ind1].get_health() != 0:
                knight1_replace(list1, ind1, x1, y1)
            list.remove(ind2)
            s1 = "SCORE = {}".format(sp.in_scorep())
            list1[4].config(text = s1)
       # return

    elif knight1[ind1].get_health() > knight2[ind2].get_health():
        knight1_replace(list1, ind1, x1, y1)
        knight2_replace(list2, ind2, x2, y2)
        s1 = "SCORE = ".format(sp.in_scorep())
        list1[4].config(text=s1)

    elif knight1[ind1].get_health() < knight2[ind2].get_health():
        knight1_replace(list1, ind1, x1, y1)
        knight2_replace(list2, ind2, x2, y2)
        s1 = "SCORE = ".format(sc.in_scorec())
        list2[4].config(text=s1)

    else:
        knight1_replace(list1, ind1, x1, y1)
        knight2_replace(list2, ind2, x2, y2)


    if  sp.score_player == 4 and sc.score_comp == 4:
        f.destroy()
        frame = Frame(root, height=1000, width=1000, bg='white')
        frame.pack(fill=BOTH, expand=True)
        l2 = Label(root, text="Tie", font=("Chiller", 100, "bold"),
                   background="#ffffff")
        l2.place(relx=0.2, rely=0.4)

        l3 = Label(root, image=f3_img, relief="flat", border=0)
        l3.place(relx=0.5, rely=0.3)

    elif  sp.score_player == 4 or sc.score_comp == 4:
        f.destroy()
        frame = Frame(root, height=1000, width=1000, bg='white')
        frame.pack(fill=BOTH, expand=True)
        if sp.score_player == 4:
            l2 = Label(root, text="Player Wins", font=("Chiller", 50, "bold"), background="#ffffff")
            l2.place(relx=0.2, rely=0.4)

            l3 = Label(root, image=f_img, relief="flat", border=0)
            l3.place(relx=0.5, rely=0.3)

        else:
            l2 = Label(root, text="Computer Wins", font=("Chiller", 50, "bold"), background="#ffffff")
            l2.place(relx=0.2, rely=0.4)

            l3 = Label(root, image=f2_img, relief="flat", border=0)
            l3.place(relx=0.5, rely=0.3)

    else:
        b.place(x=710, y=500)

#Fight
def match(ind1, ind2, situ, score1, score2, start, list1, list2, x1, x2, y1, y2, f, situation, b):
    if knight1[ind1].get_skill() == sit[situ] and knight2[ind2].get_skill() != sit[situ]:
        knight1[ind1].dec_health()
        knight2[ind2].dec_health_sp()
        knight2[ind2].dec_armour()

    elif knight1[ind1].get_skill() != sit[situ] and knight2[ind2].get_skill() == sit[situ]:
        knight1[ind1].dec_health_sp()
        knight2[ind2].dec_health()
        knight1[ind1].dec_armour()

    else:
        knight1[ind1].dec_health()
        knight2[ind2].dec_health()

    str1 = "Health = {}\nArmour = {}\nSkill = {}".format(knight1[ind1].get_health(), knight1[ind1].get_armour(),
                                                         knight1[ind1].get_skill())
    score1.destroy()
    # score1 = Button(f, height=20, width=30, text=str1)
    score1 = Button(f, height=10, width=30, font=("Calibri", 10, "bold"), relief="flat", border=0, text=str1)#, background="purple", foreground="white")
    score1.place(x=0, y=300, anchor='nw')

    str2 = "Health = {}\nArmour = {}\nSkill = {}".format(knight2[ind2].get_health(), knight2[ind2].get_armour(),
                                                         knight2[ind2].get_skill())
    score2.destroy()
    # score2 = Button(f, height=20, width=30, text=str2)
    score2 = Button(f, height=10, width=30, font=("Calibri", 10, "bold"), relief="flat", border=0, text=str2)#, background="purple", foreground="white")
    score2.place(x=1350, y=300, anchor='nw')

    start.destroy()

    start = Button(f, height=3, width=10, text="Clear", command=lambda: clear(list1, list2, ind1, ind2, x1, x2, y1, y2, score1, score2, situation, start, b, f))
    start.place(relx=0.465, rely=0.5)

#Select KNIGHT
def set_k(list1, list2, b, f, x1, x2, y1, y2):
    ret = comp_card()
    ind=0
    knight2_fight(list2[ret])
    while True:
        if keyboard.is_pressed('1'):
            ind=0
            break
        elif keyboard.is_pressed('2'):
            ind=1
            break
        elif keyboard.is_pressed('3'):
            ind=2
            break
        elif keyboard.is_pressed('4'):
            ind=3
            break

    knight1_fight(list1[ind]) #Brings first Knight in centre
    str1 = "Health = {}\nArmour = {}\nSkill = {}".format(knight1[ind].get_health(), knight1[ind].get_armour(), knight1[ind].get_skill())
    # score1 = Button(f, height=20, width=30, text=str1)
    score1 = Button(f, height=10, width=30, font=("Calibri", 10, "bold"), relief="flat", border=0, text=str1)#, background="purple", foreground="white")
    score1.place(x=0, y=300, anchor='nw')

    str2 = "Health = {}\nArmour = {}\nSkill = {}".format(knight2[ret].get_health(), knight2[ret].get_armour(),knight2[ret].get_skill())
    score2 = Button(f, height=10, width=30, font=("Calibri", 10, "bold"), relief="flat", border=0, text=str2)#, background="purple", foreground="white")
    score2.place(x=1550, y=300, anchor='ne')

    situ = comp_card() #To select situation
    situation = Button(f, height=5, width=30, text=sit[situ], relief="flat", border=0)#, foreground="white", bg="#613c6e")
    situation.place(x=750, y=500, anchor='n')


    start = Button(f, height=3, width=10, text="Start", command=lambda: match(ind, ret, situ, score1,
                                                                                  score2, start, list1, list2, x1, x2,
                                                                                  y1, y2, f, situation, b))
    start.place(relx=0.465, rely=0.5)


# Start Gameplay
def start_gameplay(f1):
    f1.destroy()

    frame = Frame(root, height=1000, width=1000, bg='#613c6e')
    frame.pack(fill=BOTH, expand=True)

    bg_l = Label(frame, image=bg)
    bg_l.pack()

    p1y=20
    p2y=820

    #Player 1 Knights
    k1b = Button(frame,image=knight_f, relief="flat", text="Knight 1")
    k1b.place(x=30, y=p1y)

    k2b = Button(frame, image=knight_du, relief="flat", text="Knight 2")
    k2b.place(x=220, y=p1y)

    k3b = Button(frame, image=knight_de, text="Knight 3")
    k3b.place(x=410, y=p1y)

    k4b = Button(frame, image=knight_s, text="Knight 4")
    k4b.place(x=600, y=p1y)

    str1="Score = 0"
    s1 = Button(frame, height=10, width=20, text=str1, font=("Calibri", 10, "bold"), relief="flat", bg="#3d3e42", fg="white")# background="#b8a233")
    s1.place(relx=0.966, rely=0.055, anchor='ne')

    list_p1 = [k1b, k2b, k3b, k4b, s1]
    list_x1 = [30, 220, 410, 600]
    y1 = 20

    #Player 2 Knights
    k5b = Button(frame, image=knight_f, text="Knight 1")
    k5b.place(x=920, y=p2y, anchor='se')

    k6b = Button(frame, image=knight_du, text="Knight 2")
    k6b.place(x=1120, y=p2y, anchor='se')

    k7b = Button(frame, image=knight_de, text="Knight 3")
    k7b.place(x=1320, y=p2y, anchor='se')

    k8b = Button(frame, image=knight_s, text="Knight 4")
    k8b.place(x=1510, y=p2y, anchor='se')

    str2 = "Score = 0"
    s2 = Button(frame, height=10, width=20, text=str1, font=("Calibri", 10, "bold"), relief="flat", bg="#3d3e42", fg="white")
    s2.place(relx=0.055, rely=0.966, anchor='sw')

    list_p2 = [k5b, k6b, k7b, k8b, s2]
    list_x2 = [920, 1120, 1320, 1510]
    y2 = 820

    set = Button(frame, height=3, width=10, text='Select Card',
                     command=lambda: set_k(list_p1, list_p2, set, frame, list_x1, list_x2, y1, y2))
    set.place(x=710, y=500)

    playsound('harry.mp3', False)

# Instruction Function
def instructions():
    root.config(background="sky blue")
    frame_1 =Frame(root)
    frame_1.pack(fill=BOTH, expand=True)
    frame_1.config(bg="sky blue")
    l3 = Label(frame_1, text="Instructions", font=("Chiller", 50, "bold"), background="sky blue")
    l3.pack()

    #Create label for instruction
    rules = "\nGOAL-\n-The one who saves the princess wins the game\nSETUP-\n-Being a wizard you need to defeat computer's " \
            "knights and earn reward points\n. A wizard is given four knights each having different skills. The battle could be on" \
            "Desert, Dungeons, Ship or Forest.\n If the location of battle matches with the skill of Knight then the Knight wins" \
            "and gets a point. The one who gets upto 4 points wins\nRULES-\n- Press-1 to choose KNIGHT-1\n" \
            "- Press-2 to choose KNIGHT-2\n- Press-3 to choose KNIGHT-3\n- Press-4 to choose KNIGHT-4\n-Once destroyed do not " \
            "select the card\nSCORING-\n- Wizard scores 1 point for a win\n"
    l_ins = Label(frame_1, text=rules, font=("Gabriola", 20, "bold"), background="sky blue")
    l_ins.pack()

    #Next Button5
    n_img = PhotoImage(file="next.png")
    nb = Button(frame_1, image=n_img, relief="flat", border=0, background="sky blue", command=lambda: start_gameplay(frame_1))
    nb.place(relx=0.899, rely=0.799)
    nb.image = n_img




# Start Button
def start():
    l1.destroy()
    l2.destroy()
    b1.destroy()
    instructions()


# Display
root = tk.Tk()
root.title("A Wizard Did It ...")
root.geometry("1080x1920")
root.config(background="#ffffff")

# Logo
wiz_img = PhotoImage(file="img.png")
l1 = Label(root, image=wiz_img, background="#000000")
l1.place(x=300, y=0, anchor='nw')

# Title
l2 = Label(root, text="A Wizard Did It ...", font=("Chiller", 100, "bold"), background="#ffffff")
l2.place(x=638, y=100, anchor='nw')

# Button
b1_img = PhotoImage(file="b1.png")
bg = PhotoImage(file="bg_1.png")
b1 = Button(root, image=b1_img, relief="flat", background="#ffffff", border=0, command=start)
b1.pack(pady=(450, 0))
knight_f = PhotoImage(file="knight_f.png")
knight_du = PhotoImage(file="knight_du.png")
knight_de = PhotoImage(file="knight_de.png")
knight_s = PhotoImage(file="knight_s.png")
f_img=PhotoImage(file="f2.png")
f2_img=PhotoImage(file="f3_c.png")
f3_img=PhotoImage(file="cry.png")

k1 = Knight("Forest")
k2 = Knight("Dungeon")
k3 = Knight("Desert")
k4 = Knight("Ship")
knight1 = [k1, k2, k3, k4]
count1 = 0

k5 = Knight("Forest")
k6 = Knight("Dungeon")
k7 = Knight("Desert")
k8 = Knight("Ship")
knight2 = [k5, k6, k7, k8]
count2 = 0

sp = Score()
sc = Score()

sit = ["Forest", "Dungeon", "Desert", "Ship"]

mainloop()