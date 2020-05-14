# gamez.py
#Chloe Stewart 
# 2020

#So that it can seem like the npc is thinking. Adds a lot of dramatics. 
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
    if decision in left:    # leads to bug problem
        first_left()
    elif decision in right:     # the 'wrong' way but can still lead back 
        first_right()
    else:       # Deadend for wrong inputs. Just unlucky if this is the one they mess up. 
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
    if decision in option_A:        #Leads to ignite comp
        print("The wires around it seem to be melting! But theres a gap! I'm going thru.")
        ignite_comp()
    if decision in option_B:        #Deadend
        print("It was a vialient effort, but the big seemed to crush your little companion. All for nothing tsk tsk.")
        time.sleep(1)
        print("GAME OVER")
    if decision in option_C:        #Leads to 
        print("OK. I phoned Nortan, and hes on his way. I met him years ago while wondering the mainframe. I tried to convince him to escape with me, but hes happy here. Better here than with the wife he says ahahah.")
        time.sleep(5)
        print("There he is! Just the sight of good ol' Nortan sends em running. Something to do with his last name - AnTivrs? Either way he just saved our life!    Lets go further.")
        # INPUT ANOTHER FUNCTION    
    else: 
        print("Whoops, musta been the wrong input, don't forget your quotes ;). Give me a second to rewind, don't worry.")
        time.sleep(4)
        first_left()

def first_right():
    print("Hmmmmm. This definitely isn't the right way, i've never seen those wires. ")
    time.sleep(1)
    print("Should we just keep going or turn back?")
    print("A. Keep Going")
    print("B. Turn Back")
    decision = input(">")
    if decision in option_A:    #Deadend 
        print("Okay, it's been a while now and I really don't know where we are.")
        time.sleep(4)
        print("Oh, no! I think we are near the cooling duct! The fan, it's too strong, I'm being sucked in! Tell my mom i love he-")
        time.sleep(5)
        print("... It was a quick death - definitely not clean or pretty - but quick. RIP to the best little unnamed companion you'll ever know.")
        print("THE END")
    if decision in option_B:   #Going to bypass the bug problem completely and connect to after Nortan's option
        print("Good call turning back mate! This looks a lot better. Oh and I think we just missed a nasty bug, you see those droppings? Luckily you took us the wrong way or that would have been a dousey. Let's keep going before it comes back.")
        time.sleep(3)
        # ADD FUNCTION LEADING TO After NORTANS OPTION
    else:       #for wrong inputs, starts function over 
        print("I'm confused, there's only two options here... Maybe you didn't hear me correctly")
        time.sleep(2)
        first_right()


def ignite_comp():      # Either blows up or sleeps to continue playing the game. 
    print("We made it. I'm glad that worked, you really seem to know what you are doing.")
    time.sleep(3)
    print("We've been walking for a bit now and the air seems to be getting thicker around me. Maybe we shouldn't have sprayed that big spray, it's so much harder to breathe.")
    time.sleep(3)
    print("Should I... ")
    print("A. Just turn every thing off and sleep for the night")
    print("B. Crank the power, maybe the fan will help air out this place.")
    decision = input(">")
    if decision in option_A: #Survives! 
        print("Goodnight!")
        time.sleep(10)
        print("g--goodmorning! The bugfog seems to have cleared during the night, good call on just sleeping! Wish I could solve all my problems like that!")
        # LEADS TO FUNCTION - myabe Norton's maybe another depending on how much you get done next time
    if decision in option_B:        # Dead end
        print("Here let me just flip this...")
        time.sleep(1)
        print("turn this over...")
        time.sleep(1)
        print("yank this out...")
        time.sleep(1)
        print("AND THERE! Power should be turning up any second now")
        time.sleep(5)
        print("Wait, thats a spark. The bug spray! and the power! Were gonna explode!")
        time.sleep(2)
        print("BADABOOM")
        time.sleep(1)
        print("BADABING")
        time.sleep(4)
        print(". And with one little choice, the game is over for you friend")
        print("THE END")


def over_heat():        # Two ways to lose and two ways to continue 
    print("Bugs really are nasty, so be glad thats over. I think it's just a little further. Shouldn't be too bad from now on!")
    time.sleep(5)
    print("May have spoke too soon, it's getting hotter in here.")
    print("That's not good. The owner must be playing games right now, the computer usually overheats. I try to stay near the fans, and strap down so I don't burn but we might be too far now. ")
    time.sleep(3)
    print("Should we...")
    print("A. Turn back and search for the fans. Don't want to risk overheating.")
    print("B. Keep going, a little sweat doesn't hurt.")
    print("C. Just wait here and see if the heat wave passes. What are the odds he plays for that long right?")
    decision = input(">")
    if decision in option_A:    #Gets lost and loses game
        print("Okay we'll go back this way...")
        time.sleep(2)
        print("Maybe we took this turn")
        time.sleep(2)
        print("Or this one...")
        time.sleep(2)
        print("I CANT REMEMBER!")
        time.sleep(1)
        print("This is useless.")
        print("I'll never be good enough to find my way out, what would my mom think of me! Oh - ")
        time.sleep(3)
        print("-")
        print("-")
        print("It seems that they got a little too emotional with all of this drama and had a temper tantrum. I don't think they'll be back soon.")
        print("Probably best if you just left")
        print("Game over :()")
    if decision in option_B:    # Takes you to next function 
        print("It's getting hotter and hotter, but I'll keep going if you say so. Man I don't think I've sweat this much since the summer of '09!")
        time.sleep(3)
        print("It's a lot cooler down here, I'm glad we kept going. Hopefully the exit is somewhere around here.")
        # ADD FUNCTION HERE YA 
    if decision in option_C:    # Either keeps going or gives player option literallly tells them game over. 
        time.sleep(5)
        print("So we've been here for about 5 hours now...")
        print("They don't seem to be slowing down on the gaming,")
        print("and I think someone just delivered some pizza. It's going to be a long night here. I'm not sure we'll make it.")
        time.sleep(3)
        print("The poor little guy ended up over heatting and fried all of his brain. Maybe you'll still be able to lead him out.")
        print("Do you want to keep going? Yes or No?")
        decision = input(">")
        if decision in yes:
            print("Poor little man, looks like a puppet. But I guess we'll keep going")
            # CONNECT TO OPTION B FUCTION 
        if decision in no:
            print("Wise choice, I see you have some humanity.")
            print("I'll keep that in mind for next game, maybe you'll have better luck! ")
            time.sleep(2)
            print("GAMEOVER")
