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
