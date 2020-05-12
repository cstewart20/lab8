# gamez.py
#Chloe Stewart 
# 2020

#So that it can seem like the npc is thinking 
import time    

#To make up for input variability 
option_A = ["A","a"]
option_B = ["B","b"]
option_C = ["C","c"]
left = ["Left","left","L","l"]
right = ["Right","right","R","r"]
yes = ["Yes","yes","y","Y"]
no = ["No", "no", "N", "n"]


def start():  #Set up the story and get player name 
    player_name = input("Wh-Who is this??? > ")
    print("Hello "+ player_name + " I haven't had anyone on here in a long time! I'm so so so thankful you came. Do you think you could help me?? Yes or no?")
    decision = input (">")
    if decision in yes:
        print("Oh I knew you'd say yes!") 
        part_1()
    elif decision in no:
        print("Oh so so so rude. Well goodbye Mr. Loser " + player_name + ", hope you DON'T have a wonderful day") #End of the game for them 
    else:
        print("Bro, yes or no!!! AS IF i'd care about anything else you'd say. Lets start ALL over")
        start() #Makes them start all over again
def part_1():
    print("Now that I know you'll help, Let me tell you whats up. I've been stuck in this computer for years now, and I can't get out. ")
    print("You see, I have this fear of making decisions, one choice that could decide my fate. I need you to make the choices for me. That way my life is in your hands! :))")
    time.sleep(10) #gives people time to read
    print("Perfect, no objections, lets get to the first crossroads. I have to get to the output port! Goodluck")
    time.sleep(5)
    print(" ... Well this is embarrasing. I seem to have forgetten the way. What do you say, left or right?")
    decision = input(">")
    if decision in left:
        first_left()
    elif decision in right: 
        first_right()
    else:
        print('OH.')
        time.sleep(1)
        print('MY')
        time.sleep(1)
        print('GOD')
        time.sleep(1)
        print('Cannot follow the rules huh. I cant take this anymore Ill do it myself.')
        time.sleep(5)
        print('They went off on their own and ended up falling into the computer fan. You just killed someone. Nice! Good gaming!')
        time.sleep(1)
        print('THE END')

def first_left():
    print("On no! This is the right way, b-but - there seems to be a bug! And we ran right into it! I forgot theyre seasonal UGHHHHHH")
    time.sleep(3)
    print("Should we...")
    time.sleep(1)
    print("A. Spray it with the strongest raid i have until it suffocates")
    print("B. Try to sneak around it")
    print("C. Phone a friend for help")
    decision = input(">")
    if decision in option_A:
        print("The wires around it seem to be melting! But theres a gap! I'm going thru.")
        # INPUT ANOTHER FUNCTION 
    if decision in option_B:
        print("It was a vialient effort, but the big seemed to crush your little companion. All for nothing tsk tsk.")
        time.sleep(1)
        print("GAME OVER")
    if decision in option_C:
        print("OK. I phoned Nortan, and hes on his way. I met him years ago while wondering the mainframe. I tried to convince him to escape with me, but hes happy here. Better here than with the wife he says ahahah.")
        time.sleep(5)
        print("There he is! Just the sight of good ol' Nortan sends em running. Something to do with his last name - AnTivrs? Either way he just saved our life!    Lets go further.")
        # INPUT ANOTHER FUNCTION

def first_right():
    print ("right test")
