from tkinter import *
from tkinter import messagebox
import os
import pygame

##import cv2
##import pyglet


#Register

def register():
    global register_screen
    register_screen =Toplevel(main_screen)
    register_screen.title("Thai General Election 2020")
    register_screen.geometry("900x600")
 
    global username
    global password
    global username_entry
    global password_entry
    global district
    global district_entry
    global job
    global job_entry
    global MALE
    global MALE_tick
    global FEMALE
    global FEMALE_tick
    global photo3
    username = StringVar()
    password = StringVar()
    district = StringVar()
    job = StringVar()
    MALE = IntVar()
    FEMALE = IntVar()
 
    Label(register_screen, text="Please Enter your information below for registration", bg="orange",width="50", height="2", font=("Calibri", 13)).pack() 
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Your Name")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen,text ="").pack()
    gender_label = Label(register_screen, text ="Your Gender")
    gender_label.pack()
    MALE_tick = Checkbutton(register_screen, text="Male", selectcolor ="red",onvalue = 1, offvalue = 0,variable = MALE)
    MALE_tick.pack()
    FEMALE_tick = Checkbutton(register_screen, text ="Female", selectcolor = "blue", onvalue = 1, offvalue = 0, variable = FEMALE)
    FEMALE_tick.pack()
    Label(register_screen,text ="").pack()
    password_lable = Label(register_screen, text="Thai Identification Numbers")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password)
    password_entry.pack()
    Label(register_screen, text="").pack()
    district_label = Label(register_screen, text = "Current District")
    district_label.pack()
    district_entry = Entry(register_screen, textvariable = district)
    district_entry.pack()
    Label(register_screen, text ="").pack()
    job_label = Label(register_screen, text = "Current Occupation")
    job_label.pack()
    job_entry = Entry(register_screen, textvariable = job)
    job_entry.pack()
    Label(register_screen, text = "").pack()
    Button(register_screen, text="Register", width=30, height=1, bg="Green",font = ("Calibri",12), command = register_user).pack()
    
    Label(register_screen, text ="").pack()
    photo3 = PhotoImage(file = 'police.png')
    labelphoto3 = Label(register_screen, image = photo3,justify = LEFT)
    labelphoto3.pack()
    
 
 
#Login
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Thai General Election 2020")
    login_screen.geometry("600x400")
    Label(login_screen, text="Please Enter your Thai Identification Number and your Name", bg ="pink",width ="50", height = "2", font = ("Calibri",13)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    global photo
   
    Label(login_screen, text="Your Name").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Thai Identification Number").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify)
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    Label(login_screen, text = "").pack()
    photo = PhotoImage(file = 'office.png')
    labelphoto = Label(login_screen, image = photo)
    labelphoto.pack()
    
   

def menuVoting():
    global menuvoting_screen
    global photo4
    global photo5
    global photo6
    menuvoting_screen = Toplevel(main_screen)
    menuvoting_screen.title("Thai General Election 2020")
    menuvoting_screen.geometry("600x410")
    Label(menuvoting_screen, text = "Thailand General Election Main Menu", bg = "Orange", width = "100", height = "2", font = ("Calibri",13)).pack()
    Label(menuvoting_screen, text = "").pack()
    Button(menuvoting_screen,text="Prime Minister Candidates", height="2", width="30",command = prime_minister).pack()
    Label(menuvoting_screen, text ="").pack()
    Label(menuvoting_screen,text="===List of Prime Minister Candidates profiles and achievements===",bg="Yellow",width="100",height="1",font=("New Courier",10)).pack()
    Label(menuvoting_screen, text ="").pack()
    Button(menuvoting_screen,text="General Election Voting Ballot", height="2", width="30", command = election).pack()
    Label(menuvoting_screen, text ="").pack()
    Label(menuvoting_screen,text="===You are allowed to vote only onces===",bg="Yellow",width="100",height="1",font=("New Courier",10)).pack()
    Label(menuvoting_screen, text ="").pack()
    photo4 = PhotoImage(file = 'senator.png')
    labelphoto = Label(menuvoting_screen, image = photo4)
    labelphoto.pack(side = LEFT, padx = 20)
    photo5 = PhotoImage(file = 'Royal standard.png')
    labelphoto4 = Label(menuvoting_screen, image = photo5)
    labelphoto4.pack(side = LEFT, padx = 85)
    photo6 = PhotoImage(file = 'senator.png')
    labelphoto6 = Label(menuvoting_screen, image = photo4)
    labelphoto6.pack(side = RIGHT, padx = 20)

#Menu Candidate
def prime_minister():
    global prime_minister_screen  
    global pacharat
    global prayut
    global pheu
    global suda
    global future
    global torn
    global anutin
    global pumchai

    prime_minister_screen = Toplevel(main_screen)
    prime_minister_screen.title("Thai General Election 2020")
    prime_minister_screen.geometry("1000x800")
    Label(prime_minister_screen, text = "=== All Candidates from each political parties ===", bg = "light green", width = "150", height = "2", font = ("Arial",13)).pack()
    pacharat = PhotoImage(file = 'phacarat.png')
    labelphoto7 = Label(prime_minister_screen, image = pacharat)
    labelphoto7.place(x = 0,y = 100)
    prayut = PhotoImage(file = 'prayut chan o cha.png')
    labelphoto8 = Label(prime_minister_screen, image = prayut)
    labelphoto8.place(x = 200,y = 70)
    PP = Label(prime_minister_screen, text = "Palang Pracharath Party",bg = "light blue", width = "20", height = "2",fg = "Blue")
    PP.place(x = 110, y = 240)
    btpp = Button(prime_minister_screen,text="Click me to see the Information!", width=30, height=1,command = Chan, fg = "Blue")
    btpp.place(x = 75, y = 285)
    pheu = PhotoImage(file = 'pheu.png')
    labelphoto9 = Label(prime_minister_screen,image = pheu)
    labelphoto9.place(x = 580, y = 110)
    suda = PhotoImage(file = 'suda.png')
    labelphoto10 = Label(prime_minister_screen, image = suda)
    labelphoto10.place(x = 800, y = 90)
    ph = Label(prime_minister_screen, text = "Pheu Thai Party", bg = "pink", width = "20", height = "2", fg = "Red")
    ph.place(x = 700, y = 245)
    btph = Button(prime_minister_screen,text="Click me to see the Information!", width=30, height=1,command = Ying, fg = "Red")
    btph.place(x = 670, y = 285)
    future = PhotoImage(file = 'future.png')
    labelphoto1 = Label(prime_minister_screen, image = future)
    labelphoto1.place(x = 10, y = 450)
    torn = PhotoImage(file = 'speaker thanatorn.png')
    labelphoto2 = Label(prime_minister_screen, image = torn)
    labelphoto2.place(x = 190, y = 450)
    ff = Label(prime_minister_screen, text = "Future Forward Party", bg = "yellow", width = "20", height = "2", fg = "Orange")
    ff.place(x= 110, y = 620)
    btff = Button(prime_minister_screen,text="Click me to see the Information!", width=30, height=1,command = Future, fg = "Orange")
    btff.place(x = 75, y = 660)
    pumchai = PhotoImage(file = 'weed.png')
    labelphoto3 = Label(prime_minister_screen, image = pumchai)
    labelphoto3.place(x = 592, y = 410)
    anutin = PhotoImage(file = 'anutin.png')
    labelphoto4 = Label(prime_minister_screen, image = anutin)
    labelphoto4.place(x = 770, y = 440)
    anu = Label(prime_minister_screen, text = "Bhumjaithai Party", bg = "light green", width = "20", height = "2", fg = "Dark Green")
    anu.place(x = 680, y = 620)
    btanu = Button(prime_minister_screen,text="Click me to see the Information!", width=30, height=1,command = Bhum, fg = "Green")
    btanu.place(x = 645, y = 660)

#First Candidate Profile
def Chan():
    global prayut_screen  
    global Prayut
    global paca
    prayut_screen = Toplevel(main_screen)
    prayut_screen.title("Thai General Election 2020")
    prayut_screen.geometry("800x500")
    Label(prayut_screen, text = "General Prayut Chan-Oh-Cha", bg = "light blue", width = "100", height = "2", font = ("Courier",13)).pack()
    Prayut = PhotoImage(file = 'prayut.png')
    labelphoto7 = Label(prayut_screen, image = Prayut)
    labelphoto7.place(x = 30,y = 100)
    PP = Label(prayut_screen, text = "Candidate from Phalang Pracharat Party", bg = "light blue", width = "35", height = "2")
    PP.place(x = 30, y = 370)
    paca = PhotoImage(file = 'phacarat.png')
    labelphotoa = Label(prayut_screen, image = paca)
    labelphotoa.place(x = 600, y = 50)
    name = Label(prayut_screen, text = "Name: Prayut Chan-Oh-Cha",bg = "Light Blue",fg = "Dark Blue", width = "25", height = "2", font = ("Courier",13))
    name.place(x = 290, y = 100)
    age = Label(prayut_screen, text = "Age: 65", fg = "Dark Blue", bg = "Light Blue",width = "8", height = "2", font = ("Courier",13))
    age.place(x = 290, y = 155)
    job = Label(prayut_screen, text = "Occupation: Military General", fg = "Dark Blue", bg = "Light Blue", width = "28", height = "2", font = ("Courier",13))
    job.place(x = 289, y = 209)
    school = Label(prayut_screen, text = "Education: National Defence College of Thailand", fg = "Dark Blue", bg = "Light Blue", width = "48", height = "2", font = ("Courier",13))
    school.place(x = 287, y = 268)
    goal = Label(prayut_screen, text = "Achievements: No Corruption and Anti-Rebellion", fg = "Dark Blue", bg = "Light Blue", width = "47", height = "2", font = ("Courier",13))
    goal.place(x = 285, y = 329)

#Second Candidate Profile
def Ying():
    global Ying_screen  
    global YING
    global THAI
    Ying_screen = Toplevel(main_screen)
    Ying_screen.title("Thai General Election 2020")
    Ying_screen.geometry("800x500")
    Label(Ying_screen, text = "Ms. Sudarat Keyuraphan", bg = "Pink",fg = "Red", width = "100", height = "2", font = ("Courier",13)).pack()
    YING = PhotoImage(file = 'Su.png')
    labelphoto7 = Label(Ying_screen, image = YING)
    labelphoto7.place(x = 20,y = 80)
    suradat = Label(Ying_screen, text = "Candidate from Pheu Thai Party", bg = "Pink",fg = "Red", width = "27", height = "2")
    suradat.place(x = 30, y = 290)
    THAI = PhotoImage(file = 'pheu.png')
    PhotoPheu = Label(Ying_screen, image = THAI)
    PhotoPheu.place(x = 620, y = 50)
    name = Label(Ying_screen, text = "Name: Sudarat Keyuraphan",bg = "Pink",fg = "Dark Red", width = "25", height = "2", font = ("Courier",13))
    name.place(x = 260, y = 100)
    age = Label(Ying_screen, text = "Age: 58", fg = "Dark Red", bg = "Pink",width = "8", height = "2", font = ("Courier",13))
    age.place(x = 260, y = 155)
    job = Label(Ying_screen, text = "Occupation: Politician", fg = "Dark Red", bg = "Pink", width = "23", height = "2", font = ("Courier",13))
    job.place(x = 260, y = 209)
    school = Label(Ying_screen, text = "Education: Chulalongkorn University of Thailand", fg = "Dark Red", bg = "Pink", width = "48", height = "2", font = ("Courier",13))
    school.place(x = 260, y = 268)
    goal = Label(Ying_screen, text = "Achievements: More Public Health-Care and Culture ", fg = "Dark Red", bg = "Pink", width = "51", height = "2", font = ("Courier",13))
    goal.place(x = 260, y = 329)

#Third Candidate Profile
def Future():
    global Future_screen  
    global FUTURE
    global Tana
    Future_screen = Toplevel(main_screen)
    Future_screen.title("Thai General Election 2020")
    Future_screen.geometry("800x500")
    Label(Future_screen, text = "Mr. Thanathorn Juangroongruangkit", bg = "Yellow",fg = "dark orange", width = "100", height = "2", font = ("Courier",13)).pack()
    Tana = PhotoImage(file = 'thanatorn.png')
    labelphoto7 = Label(Future_screen, image = Tana)
    labelphoto7.place(x = 20,y = 80)
    suradat = Label(Future_screen, text = "Candidate and Leader Future Forward Party", bg = "Yellow",fg = "dark orange", width = "35", height = "2")
    suradat.place(x = 30, y = 270)
    FUTURE = PhotoImage(file = 'future.png')
    labelphotoa = Label(Future_screen, image = FUTURE)
    labelphotoa.place(x = 70, y = 330)
    name = Label(Future_screen, text = "Name: Thanathorn Juangroongruangkit",bg = "Yellow",fg = "dark orange", width = "35", height = "2", font = ("Courier",13))
    name.place(x = 300, y = 90)
    age = Label(Future_screen, text = "Age: 41", fg = "dark orange", bg = "Yellow",width = "8", height = "2", font = ("Courier",13))
    age.place(x = 300, y = 145)
    job = Label(Future_screen, text = "Occupation: Businessman", fg = "dark orange", bg = "Yellow", width = "23", height = "2", font = ("Courier",13))
    job.place(x = 300, y = 200)
    school = Label(Future_screen, text = "Education: Thammasat University of Thailand", fg = "dark orange", bg = "Yellow", width = "44", height = "2", font = ("Courier",13))
    school.place(x = 298, y = 260)
    goal = Label(Future_screen, text = "Achievements: Inflation of Economy and Corporate ", fg = "dark orange", bg = "yellow", width = "49", height = "2", font = ("Courier",13))
    goal.place(x = 300, y = 315)

#Fourth Candidate Profile
def Bhum():
    global Bhum_screen  
    global BHUMJAI
    global ANUtin
    Bhum_screen = Toplevel(main_screen)
    Bhum_screen.title("Thai General Election 2020")
    Bhum_screen.geometry("800x500")
    Label(Bhum_screen, text = "Dr. Anutin Charnvirakul", bg = "light green",fg = "dark green", width = "100", height = "2", font = ("Courier",13)).pack()
    ANUtin = PhotoImage(file = 'anu.png')
    labelphoto7 = Label(Bhum_screen, image = ANUtin)
    labelphoto7.place(x = 20,y = 80)
    jai = Label(Bhum_screen, text = "Candidate and Leader Bhumjaithai Party", bg = "light green",fg = "dark green", width = "32", height = "2")
    jai.place(x = 20, y = 330)
    BHUMJAI = PhotoImage(file = 'weed.png')
    labelphotoa = Label(Bhum_screen, image = BHUMJAI)
    labelphotoa.place(x = 640, y = 50)
    name = Label(Bhum_screen, text = "Name: Anutin Charnvirakul",bg = "light green",fg = "dark green", width = "26", height = "2", font = ("Courier",13))
    name.place(x = 270, y = 90)
    age = Label(Bhum_screen, text = "Age: 53", fg = "dark green", bg = "light green",width = "8", height = "2", font = ("Courier",13))
    age.place(x = 270, y = 145)
    job = Label(Bhum_screen, text = "Occupation: Engineer", fg = "dark green", bg = "light green", width = "21", height = "2", font = ("Courier",13))
    job.place(x = 270, y = 200)
    school = Label(Bhum_screen, text = "Education: Hofstra University of U.S.A", fg = "dark green", bg = "light green", width = "39", height = "2", font = ("Courier",13))
    school.place(x = 270, y = 260)
    goal = Label(Bhum_screen, text = "Achievements: Increase Education and Researching ", fg = "dark green", bg = "light green", width = "49", height = "2", font = ("Courier",13))
    goal.place(x = 270, y = 320)

def election():
    global election_screen
    global VOTE
    global voteLabel
    global SEAL
    global defence
    global se
    global party1
    global party2
    global VOTEA
    global VOTEAB
    global VOTEABC
    global voteLabel2
    global voteLabel123
    global voteLabel1234
    global party3
    global party4
    

    election_screen = Toplevel(main_screen)
    VOTE = 0
    VOTEA = 0
    VOTEAB = 0
    VOTEABC = 0
    election_screen.title("Who's going to be our next Prime Minister 2020")
    election_screen.geometry("1100x900")
    SEAL = PhotoImage(file = 'seal of pm.png')
    labelphotoSEAL = Label(election_screen, image = SEAL)
    labelphotoSEAL.place(x = 10, y = 70)
    Title = Label(election_screen, text = "Thailand General Election 2020 After the Dissolution of National Council Peace and Order of Kingdom Of Thailand", width = "120", height= "2", bg = "Orange", fg = "Dark Blue", font = ("Calibri",15))
    Title.pack()
    se = PhotoImage(file = 'senator.png')
    labelphotose = Label(election_screen, image = se)
    labelphotose.place(x = 960, y = 70)
    defence = PhotoImage(file = 'defence.png')
    labelphoto_defence = Label(election_screen, image = defence)
    labelphoto_defence.place(x = 440,y = 70)
    Title2 = Label(election_screen, text = "You are allow to vote only once", width = "30", height = "1", bg = "Yellow", fg = "Dark Red", font = ("New Courier",17))
    Title2.place(x = 20,y = 250)
    Title3 = Label(election_screen, text = "Choose your next Government", width = "30", height = "1", bg = "Yellow", fg = "Dark Red", font = ("New Courier",17))
    Title3.place(x = 700, y = 250)
    Title4 = Label(election_screen, text = "First Party", width = "10", height = "2", bg = "Light Blue", fg = "Dark Blue", font = ("New Courier",13))
    Title4.place(x = 50 ,y = 300)
    Title5 = Label(election_screen, text = "Palang Pracharath Party", width = "20", height = "2", bg = "Light Blue", fg = "Dark Blue", font = ("New Courier",13))
    Title5.place(x = 160, y = 300)
    Title6 = Label(election_screen, text = "Second Party", width = "15", height = "2", bg = "light pink", fg = "Dark Red", font = ("New Courier",13))
    Title6.place(x = 720, y = 300)
    Title7 = Label(election_screen, text = "Pheu Thai Party", width = "20", height = "2", bg = "light pink", fg = "Dark Red", font = ("New Courier",13))
    Title7.place(x = 870, y = 300)
    party1 = PhotoImage(file = 'phacarat.png')
    labelphotoparty1 = Label(election_screen, image = party1)
    labelphotoparty1.place(x = 70 ,y = 370)
    btvote1 = Button(election_screen, text = "Press to Vote Party1", fg = "Dark Blue", width = "20", command = vote1)
    btvote1.place(x = 20, y = 490)
    voteLabel= Label(election_screen, text = VOTE, width = "20", height = "2", fg = "Dark Blue")
    voteLabel.place(x = 190, y = 485)
    party2 = PhotoImage(file = 'pheu.png')
    labelphotoparty2 = Label(election_screen, image = party2)
    labelphotoparty2.place(x = 790, y = 370)
    btvote2 = Button(election_screen, text = "Press to Vote Party2", fg = "Dark Red", width = "20", command = vote2)
    btvote2.place(x = 700, y = 490)
    voteLabel2 = Label(election_screen, text = VOTEA, width = "20", height = "2", fg = "Dark Red")
    voteLabel2.place(x = 900, y = 485)
    Title8 = Label(election_screen, text = "Future Forward Party", width = "20", height = "2", bg = "Yellow", fg = "Dark orange", font = ("New Courier",13))
    Title8.place(x = 150, y = 580)
    Title9 = Label(election_screen, text = "Third Party", width = "10", height = "2", bg = "Yellow", fg = "dark orange", font = ("New Courier",13))
    Title9.place(x = 40, y = 580) 
    party3 = PhotoImage(file = 'future.png')
    labelphotoparty3 = Label(election_screen, image = party3)
    labelphotoparty3.place(x = 90 , y = 630)
    btvote3 = Button(election_screen, text = "Press to Vote Party3", fg = "Dark Red", width = "20", command = vote3)
    btvote3.place(x = 20, y = 800)
    voteLabel123 = Label(election_screen, text = VOTEAB, width = "20", height = "2", fg= "Dark Orange")
    voteLabel123.place(x = 200,y = 800)
    Titlea = Label(election_screen, text = "Fourth Party", width = "20", height = "2", bg = "light green", fg = "dark green", font = ("New Courier",13))
    Titlea.place(x = 700, y = 580)
    Titleb = Label(election_screen, text = "Bhumjaithai Party", width = "20", height = "2", bg = "light green", fg = "dark green", font = ("New Courier",13))
    Titleb.place(x = 900, y = 580)
    party4 = PhotoImage(file = 'weed.png')
    labelphotoparty4 = Label(election_screen, image = party4)
    labelphotoparty4.place(x = 800, y = 630)
    btvote4 = Button(election_screen, text = "Press to Vote Party4", fg = "Dark Green", width = "20", command = vote4)
    btvote4.place(x = 700, y = 850)
    voteLabel1234 = Label(election_screen, text = VOTEABC, width = "20", height = "2", fg= "Dark Green")
    voteLabel1234.place(x = 900,y = 850)
    bt5 = Button(election_screen, text = "End the Vote", fg = "Black", width = "20", command = counting)
    bt5.place(x = 450, y = 800)

#Updating plus 1 for each parties votes
def vote1():
    global VOTE
    global voteLabel
    VOTE = VOTE + 1
    voteLabel["text"] = VOTE


def vote2():
    global VOTEA
    global voteLabel2
    VOTEA = VOTEA + 1
    voteLabel2["text"] = VOTEA

def vote3():
    global VOTEAB
    global voteLabel123
    VOTEAB = VOTEAB + 1
    voteLabel123["text"] = VOTEAB

def vote4():
    global VOTEABC
    global voteLabel1234
    VOTEABC = VOTEABC + 1
    voteLabel1234["text"] = VOTEABC


#Count Voting
def counting():
    if (VOTE > VOTEA) and (VOTE > VOTEAB) and (VOTE > VOTEABC):
        PrayutWin()
    elif (VOTEA > VOTE) and (VOTEA > VOTEAB) and (VOTEA > VOTEABC):
        SudaWin()
    elif (VOTEAB > VOTE) and (VOTEAB > VOTEA) and (VOTEAB > VOTEABC):
        TornWin()
    elif (VOTEABC > VOTE) and (VOTEABC > VOTEA) and (VOTEABC > VOTEAB):
        AnuWin()

#Party1 Win
def PrayutWin():
    global Prayutwin_screen
    global Winner1
    global text1

    Prayutwin_screen = Toplevel(main_screen)
    Prayutwin_screen.title("General Prayut Chan-O-Cha Win!")
    Prayutwin_screen.geometry("400x300")

    Winner1 = PhotoImage(file = 'phacarat.png')
    labelwinner1 = Label(Prayutwin_screen, image = Winner1)
    labelwinner1.pack()
    Label(Prayutwin_screen,text = "Palang Pracharath Party has won the election", bg = "light Blue", fg = "Dark blue", width = "50", height = "2", font = ("New Courier",13)).pack()
    
#Party2 Win    
def SudaWin():
    global sudaWin_screen
    global Winner2

    sudaWin_screen = Toplevel(main_screen)
    sudaWin_screen.title("Ms. Sudarat Keyuraphan Win!")
    sudaWin_screen.geometry("400x300")

    Winner2 = PhotoImage(file = 'pheu.png')
    labelwinner2 = Label(sudaWin_screen, image = Winner2)
    labelwinner2.pack()
    Label(sudaWin_screen, text = "Pheu Thai Party has won the election", bg = "light pink", fg = "Dark Red", width = "50", height = "2", font = ("New Courier",13)).pack()

#Party3 Win
def TornWin():
    global TornWin_screen
    global Winner3

    TornWin_screen = Toplevel(main_screen)
    TornWin_screen.title("Mr. Thanathorn Juangroongruangkit Win!")
    TornWin_screen.geometry("400x300")

    Winner3 = PhotoImage(file = 'future.png')
    labelwinner3 = Label(TornWin_screen, image = Winner3)
    labelwinner3.pack()
    Label(TornWin_screen, text = "Future Forward Party has won the election", bg = "yellow", fg = "Dark orange", width = "50", height = "2", font = ("New Courier",13)).pack()

#Party4 Win
def AnuWin():
    global AnuWin_screen
    global Winner4

    AnuWin_screen = Toplevel(main_screen)
    AnuWin_screen.title("Dr. Anutin Charnvirakul Win!")
    AnuWin_screen.geometry("400x300")

    Winner4 = PhotoImage(file = 'weed.png')
    labelwinner4 = Label(AnuWin_screen, image = Winner4)
    labelwinner4.pack()
    Label(AnuWin_screen, text = "Bhumjaithai Party has won the election", bg = "light green", fg = "Dark Green", width = "50", height = "2", font = ("New Courier",13)).pack()
    
    
#File Regisiter save info
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open("username.txt", "w")
    file.write(username_info + " " + password_info + "\n")
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    job_entry.delete(0, END)
    district_entry.delete(0, END)
    
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    messagebox.showinfo("Thailand General Election 2020","Registration Successful!")
 
#Connect Register to Login check.
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    global user_info
 
    file1 = open("username.txt", "r")
    verify = file1.read().splitlines()
    file1.close()
        
    for lines in verify:
        user_info = lines.split()
        
        user_name = user_info[0]
        user_password = user_info[1]

        if username1 == user_name:
            messagebox.showwarning("Thai General Election 2020","Welcome" + str(user_info))
            menuVoting()
            break
 
        else:
            messagebox.showwarning("Thailand General Election 2020","User or Password not recognised")
            
 
#Check succeed login
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 

#Not Found User
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
#Delete
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def close_window():
    main_screen.destroy()

def playmusic():
    pygame.mixer.music.load("meditation.mp3") 
    pygame.mixer.music.play()

def mutemusic():
    pygame.mixer.music.stop()


def main_screen():
    global main_screen
    
    main_screen = Tk()
    pygame.init()
    main_screen.title("Thailand General Election 2020")
    main_screen.call('wm', 'iconphoto', main_screen._w,PhotoImage(file='seal of PM.png'))
    main_screen.geometry("900x600")
 
    label = Label(text="Access this page for voting new representatives batch of government", bg="Orange", width="100", height="2", font=("Calibri", 13)).pack() 
            
    btlogin = Button(text="Thai Citizenship Login Form", height="2", width="30" ,command = login).pack()
    label = Label(main_screen, text ="").pack()
    label = Label(text="===Use your Thai citizen ID to Login===",bg="Yellow",width="100",height="1",font=("New Courier",10)).pack()
    label = Label(main_screen, text ="").pack()
    btreg = Button(text="Registration Form of Thai Citizenship", height="2", width="30",command = register).pack()
    label = Label(main_screen, text ="").pack()
    label = Label(text="<><><>You must reach a qualification of being thai citizen to register<><><>",bg="Yellow",width="100",height="1",font=("New Courier",10)).pack()
    label = Label(main_screen,text = "").pack()
    label = Label(main_screen, text = "").pack()
    photo = PhotoImage(file = 'thai flag.png')
    labelphoto = Label(main_screen, image = photo)
    labelphoto.pack()
    label = Label(main_screen, text = "").pack()
    btmusic = Button(text = "Play some Music", height = "2", width = "30",command = playmusic, font = ("calibri",10)).pack()
    label = Label(main_screen, text = "").pack()
    btmute = Button(text = "Mute your Music", height = "2", width = "30",command = mutemusic, font = ("calibri",10)).pack()
    label = Label(main_screen, text = "").pack()
    btquit = Button(text = "Quit the Program",height = "2", width= "30",command = close_window, font = ("calibri",10)).pack()
    main_screen.mainloop()
    

main_screen()