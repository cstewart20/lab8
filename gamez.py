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

def first_left():   # Two different options and one bad
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
    elif decision in option_B:        #Deadend
        print("It was a vialient effort, but the big seemed to crush your little companion. All for nothing tsk tsk.")
        time.sleep(1)
        print("GAME OVER")
    elif decision in option_C:        #Leads to overheating challenge
        print("OK. I phoned Nortan, and hes on his way. I met him years ago while wondering the mainframe. I tried to convince him to escape with me, but hes happy here. Better here than with the wife he says ahahah.")
        time.sleep(5)
        print("There he is! Just the sight of good ol' Nortan sends em running. Something to do with his last name - AnTivrs? Either way he just saved our life!    Lets go further.")
        over_heat
    else: 
        print("Whoops, musta been the wrong input, don't forget your quotes ;). Give me a second to rewind, don't worry.")
        time.sleep(4)
        first_left()

def first_right():  #One good option and one bad
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
    elif decision in option_B:   #Going to bypass the bug problem completely and connect to overheating challenge
        print("Good call turning back mate! This looks a lot better. Oh and I think we just missed a nasty bug, you see those droppings? Luckily you took us the wrong way or that would have been a dousey. Let's keep going before it comes back.")
        time.sleep(3)
        over_heat()
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
        fork_in_road()
    elif decision in option_B:        # Dead end
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
    else:
        print("I'm confused, there's only two options here... Maybe you didn't hear me correctly")
        time.sleep(2)
        print("Lets do that over...")
        ignite_comp()


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
    elif decision in option_B:    # Takes you to next function 
        print("It's getting hotter and hotter, but I'll keep going if you say so. Man I don't think I've sweat this much since the summer of '09!")
        time.sleep(3)
        print("It's a lot cooler down here, I'm glad we kept going. Hopefully the exit is somewhere around here.")
        fork_in_road() 
    elif decision in option_C:    # Either keeps going or gives player option literallly tells them game over. 
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
            fork_in_road()
        if decision in no:
            print("Wise choice, I see you have some humanity.")
            print("I'll keep that in mind for next game, maybe you'll have better luck! ")
            time.sleep(2)
            print("GAMEOVER")
    else:    # for false inputs, starts them over
        print("Sorry... I didn't get that. Must have been a problem")
        print("lets start again")
        over_heat()


def fork_in_road():     # One of the final functions
    time.sleep(3)
    print("The air is getting a lot better in here, and there seems to be less and less machine hum.")
    print("Either I'm going crazy, or we are almost out of here!")
    time.sleep(5)
    print("Theres a fork in the road up above. I've never gotten this far before so you're gonna have to choose!")
    time.sleep(2)
    print("Should I go left or right...?")
    decision = input(">")
    if decision in right:   # Takes them through one more obstacle before final round!! 
        time.sleep(2)
        print("It looks like we are in the memory. Don't want to stay here too long, we could get sucked in!")
        print("Quick, lets go into this duct before we are here forever.")
        # ADD FUNCTION
    elif decision in left:        # Takes them to final round!
        time.sleep(1)
        print("That was it! I can see the opening through the port!")
        time.sleep(2)
        print("I'm so excited, I can't wait, lets go!!!!")
        final_round()
    else:  # for false inputs, starts them over
        print("Not an option :((( sorry )")
        fork_in_road()


def locked_in():
    print("We managed to escape from the memory, but the hatch to the duct isn't opening!")
    time.sleep(2)
    print("I guess they repaired these parts, ugh what a shame!")
    time.sleep(1)
    print("Okay. I might be able to jimmy the repair and get us out of here but I don't know if they put anti-break software on here.")
    print("If they did, this could get ugly. What do you think I should do?")
    time.sleep(5)
    print("A. Jimmy it")
    print("B. Call for help again")
    print("C. cry :( )")
    decision = input(">")
    if decision in option_A: # DEAD END
        print("Okay, I'll go for it.")
        time.sleep(3)
        print("Oh no! It was booby trapped! The anti-break software smushed him...")
        time.sleep(1)
        print("Rest in peace")
        time.sleep(1)
        print("THE END")
    elif decision in option_B:    # TAKES TO FINAL ROUND
        print("Okay... I just called Norton and he said he'll disable any traps... ")
        time.sleep(10)
        print("Should be good to go....")
        time.sleep(2)
        print("Yes! We made it out!")
        print("And i can see the end! We are almost out of here man!")
        final_round()
    elif decision in option_C:    # GOES TO FINAL ROUND 
        print("Oh! My tears seem to be frying the anti-break!")
        time.sleep(1)
        print("I think I'll be able to get through!")
        time.sleep(2)
        print('Yes! It worked... and I have no idea how...')
        print("Oh well, at least we made it! I can see the end...")
        final_round()
    else:   # for false inputs, starts them over
        print("That wasn't an option!!!")
        locked_in()

def final_round():
    time.sleep(1)
    print("Do you think I should...")
    print("A. Just go for it, jump out!")
    print("B. Play the safe route and use a rope to go down.")
    decision = input(">")
    if decision in option_A:        # Wins
        print("If you say so, my life is in your hands ...")
        time.sleep(2)
        print("Here i go...")
        time.sleep(2)
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        time.sleep(10)
        print("HE SURVIVED THE FALL! HE MADE IT OUT! CONGRATS YOU WON THE GAME!!! YOU BEAT ALL ODDS!!!")
        print("With how many way there are to lose this, I am very impressed with you right now!")
        print("Enjoy life knowing you liberated the little computer guy !!")
    elif decision in option_B:  # LOses 
        print("Good call, let me wrap my good old rope around this part here and we'll be on our way.")
        time.sleep(3)
        print("I'm going to start my decent!")
        time.sleep(5)
        print("W-whats that noise?!?!")
        time.sleep(3)
        print("the rope!")
        time.sleep(1)
        print("it's snapping!")
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        time.sleep(10)
        print("He.... he didn't survive the fall...")
        time.sleep(2)
        print("After all this time... you did so well too... Almost there...")
        print("THE END")
    else:  # false input (restarts)
        print("At this point, I have no idea how you are messing up the inputs but I guess we all slip up...")
        time.sleep(2)
        print("I'll start you over :) ")
        final_round()
