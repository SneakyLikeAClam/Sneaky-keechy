import sys
import time
import os




def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)                        

char = {'lvl': 1,
        'xp' : 0,
        'lvlnext' : 10}

stats = {'ATK': 10,
         'DEF': 5,
         'HP' : 10}

def level(char, stats):
    nATK, nDEF, nHP = 0, 0, 0
    while char['xp'] >= char['lvlnext']:
        char['lvl'] += 1
        char['xp'] = char['xp'] - char['lvlnext']
        char['lvlnext'] = round(char['lvlnext'] * 1.2)
        nATK += 1
        nDEF += 1
        nHP += 1
        if char["xp"] < char["lvlnext"]:
            print("You have reached level " + str(char["lvl"]))
            print("Current XP             " + str(char["xp"]))
            print("XP to next level       " + str(char["lvlnext"]))
            print("HP                   ^ " + str(stats["HP"]))
            print("Attack               ^ " + str(stats["ATK"]))
            print("Defense              ^ " + str(stats["DEF"]))

            
            #print("You have reached level "+ str(char["lvl"]))
    


char['xp'] +=10

level(char, stats)

print (char["lvl"])



char['xp'] +=12

level(char, stats)

print (char["lvl"])


char['xp'] +=50

level(char, stats)

print (char["lvl"])



char['xp'] +=50

level(char, stats)

print (char["lvl"])



char['xp'] +=6000

level(char, stats)

print (char["lvl"])

print(stats)
print(char)
#typing ("Current Level EXP:         " + str(round(xp / lvlnext,2)*100)+"%\n") #my original code - one below looks cleaner
#typing ("Current level EXP:         {}%\n" .format(int((xp / lvlnext)*100)))
#typing ("EXP needed for next Level: " + str(lvlnext)+"\n")
#typing ("Health                     " + str(health )+"\n")
#typing ("Stamina                    " + str(stamina )+"\n")
#typing ("Stealth                    " + str(stealth )+"\n")
#typing ("Strength                   " + str(strength )+"\n")