#file import
import time
import os
import sys


#defineds presets
def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
def clrscrn():
	if os.name == 'posix':
		_=os.system("clear")
	else:
		_=os.system('cls')


def prologue():
    #write into a function???????
    #base stats prior to class selection
    HP = 10
    ATK = 10
    DEF = 10
    pcclass = "villager"

    #get a PC name logged and recorded
    typing ("Welcome adventurer.\n")
    time.sleep(1)
    typing ("Where should we begin?\n")
    time.sleep(1)

    #player title
    typing ("First off, how about your title, do you prefer mr, miss or something else?\n")
    pcpronoun = input()
    time.sleep(1)

    #player name
    typing ("And now, how about a name, what should i call you?\n")
    pcname = input()

    time.sleep(1)
    typing ("So you're "+pcpronoun+" "+ pcname+".\nIs that correct?\n")
    time.sleep(1)
    question1 = input()

    #checking name is correct and fucking with the players name 
    if question1 == "no" or question1 == "No":
        typing ("Oh is that so, then what is your name then?")
        pcname = input()
        typing ("So its "+ pcname+". Your sure this time? Well i dont really care anymore.\nI'm going to call you "+pcpronoun+" Indecisive for wasting my time\n")
        pcname = pcpronoun+" Indecisive"
    elif question1 == "yes" or question1 == "Yes":
        typing ("Okay, glad we got that right straight off the bat, you wouldnt believe how many people get their own name wrong.\nIts embarresing to be honest\n")
    elif question1 != "yes" or question1 !="Yes" or question1 !="no" or question1 !="No" :
        typing("What? thats not quite the answer to my question is it. I think im going to call you "+pcpronoun+" Ignoramus.\n")
        pcname = pcpronoun+" Ignoramus"
    time.sleep(1)
    clrscrn()

    #class selection
    typing("next question for you then " + pcname + ", what is your class?\n1.Warrior\n2.Thief\n3.Soilder\n\n\n")
    question2 = input()

    #warrior stats
    if question2 == "Warrior" or question2 == "warrior" or question2 == "1":
        HP = HP * 5
        DEF = DEF * 3
        ATK = ATK * 3
        pcclass = "Warrior" #add to all player classes
        typing ("You are a warrior! \nYou can go all night with your health and stamina.\nI wouldnt try sneaking around though too much if i were you.\n")

    #thief stats   he is black hashahahaha
    elif question2 == "Thief" or question2 == "thief" or question2 == "2":
        HP = HP * 2
        DEF = DEF * 2
        ATK = ATK * 4
        pcclass = "Thief"
        typing ("You are a thief!\nHiding in the shadows and striking unseen.\nUnfortuanately for you though, you are very squishy.\n")
        #soilder stats
    elif question2 == "Soilder" or question2 == "soilder" or question2 == "3":
        HP = HP * 100
        DEF = DEF * 100
        ATK = ATK * 100
        pcclass = "Soilder"
        typing ("You are a soilder.\nTake hits and hit back harder, you can do that.\nJust like a dwarf your a natural sprinter, no marathons for you.\n")
        
    typing ("Well then my new " + pcclass + ", I hope you are happy with the results you have here as you cant change them.\n")
    time.sleep(2)
    print("Health:     " + str(HP))
    print("Attack:    " + str(ATK))
    print("Defence:    " + str(DEF))

    time.sleep(5)
    clrscrn()

    typing("So are you ready for an adventure then? \nOf course you are why else would you be here " + pcname + ".\n")
    room1()


prologue()