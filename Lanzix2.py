def battle_code_lite(health):

    user_life = 1
    if("feather" in inventory or "Powerful energy" in active_effects):
        time.sleep(3)
        print(quote_during_battle)
    else:
        damage = random.randint(0, 20)
        health -= damage
        if (damage == 0):
            print(f"You dodged the attack!")
        if (health > 0):
            print(random.choice(quote_during_battle))
            user_life = 1
            print("Health: " + str(health))
        else:
            user_life = 0
            print("Health: " + health)

def battle_code_killer(health):
    user_life = 1
    if("feather" in inventory or "Powerful energy" in active_effects):
        time.sleep(0)
        print(quote_during_battle)
    else:
        damage = random.randint(0, 20)
        health -= damage
        if (damage == 0):
            print(f"You dodged the attack!")
        if (health > 0):
            print(random.choice(quote_during_battle))
            user_life = 1
            print("Health: " + str(health))
        else:
            user_life = 0
            print("Health: " + health)

# inventory display function

def inventory_display():
    print("Inventory Includes:")
    print(inventory)

def effects_display():
    print("Active effects:")
    print(active_effects)

# opening screen
def opening_screen():
    print("Lanzix 2")
    #time.sleep(3)
    print("Objective: Escape.")
    #time.sleep(5)
    print("You wake up in a dark cave.")
    #time.sleep(5)
    print("You cannot see anything in the darkness.")

def explore_message():
    print("You take a step forward...")
    #time.sleep(5)
    print("You still cannot see anything in the darkness")
    #time.sleep(5)

def explore_message_b():
    print("You look around for light...")
    #time.sleep(5)
    print("You do not see anything.")
    #time.sleep(5)
    #print("But you hear something.")
    # time.sleep(5)
    print("You hear a human scream deeper in the tunnel.")
    # time.sleep(3)

def explore_message_b_1():
    # time.sleep(5)
    print("You approach the scream.")
    # time.sleep(3)
    print("The killer hears you!")
    # time.sleep(3)
    print("The killer pulls out a knife.")

def explore_message_b_2():
    # time.sleep(2)
    print("You used stealth to approach the scream.")
    # time.sleep(3)
    print("Once you get there...")
    # time.sleep(3)
    print("You see a figure holding a torch standing over a dead body.")
    # time.sleep(3)
    print("Because you quietly approach you did not alert the figure to youself.")
    # time.sleep(3)
    print("The figure walks away from you leaving you in the darkess.")
    # time.sleep(3)
    print("With the dead body.")
    # time.sleep(3)

def explore_message_c():
    # time.sleep(3)
    print("You do not follow the figure.")
    # time.sleep(3)
    print("You feel a powerful blast of energy hit you from behind.")
    # time.sleep(3)
    print("You feel empowered.")

def explore_message_killer_yes():
    # time.sleep(2)
    print("You walk behind the figure.")
    # time.sleep(3)
    print("The figure hears you!")
    # time.sleep(3)
    print("The figure turns around and pulls out a knife!")
    # time.sleep(3)


def explore_message_killer_no():
    # time.sleep(3)
    print("You stay put.")
    # time.sleep(3)
    print("You notice a faint light in the distance towards the direction of the scream.")
    # time.sleep(3)



import random
import time

inventory = {}
active_effects = {}

time_chase = random.randint(10, 60)
health = 100
quote_during_battle = ["Test Quote", "Test Quote 2", "Test Quote 3"]

user_yes = ["yes", "yeah", "yep", "y", "ye", "yea", "ok", "okay", "affirmative", "sounds good", "you got it",
            "whatever", "sure", "if i have to", "yeh", "yah"]
user_no = ["no", "no way", "that's stupid", "why would i do that?", "that's really dumb", "nope", "i don't think so",
           "that won't fly"]

opening_screen()

while True:

    # time.sleep(5)
    intro_a = input("What do you do? ")

    if (intro_a.lower() == "explore" or intro_a.lower() == "go"):
        explore_message()

        explore_a = input("Do you look around for light? ")
        if (explore_a.lower() in user_yes):
            explore_message_b()

            print("1: Approach quietly")
            # time.sleep(3)
            print("2: Approach")
            # time.sleep(3)

            explore_b = input("Do you go towards the scream? ")

            if (explore_b.lower() == "1"):
                explore_message_b_2()
                battle_code_lite(health)
                continue
                continue
            # maybe make this an option between 1 approach and 2 quietly approach

            if (explore_b.lower() == "2"):
                explore_message_b_2()

                explore_c = input("Do you follow the figure, he is your only source of light? ")

                if (explore_c.lower() in user_yes):
                    explore_message_killer_yes()
                    battle_code_killer(health)
                    continue

                else:
                    explore_message_c()

                    active_effects["Powerful energy"] = 1
                    # time.sleep(3)
                    print(active_effects)
                    # time.sleep(3)
                    print("With your new found power you will be able to face any foe!")
                    # time.sleep(3)
                    continue

            if (explore_b.lower() in user_no):
                # time.sleep(3)
                print("You stay put.")
                # time.sleep(3)
                print("You notice a faint light in the distance towards the direction of the scream.")
                # time.sleep(3)
                explore_b = input("What do you do? ")
                print("You decide to " + explore_b)
                # time.sleep(3)
                print("Given the nature of " + explore_b + " You are forced to hold off for a moment.")
                # time.sleep(3)
                print("A figure leaps out of the dark!")
                # time.sleep(3)
                print("The figure pulls out a knife.")
                # time.sleep(3)
                if ("feather" in inventory or "Powerful energy" in active_effects):
                    # time.sleep(3)
                    print("You live!")
                    # time.sleep(3)
                    print("You survived the attack!")
                    # time.sleep(3)
                    print("You quickly rush back the way you came.")
                    continue
                else:
                    # time.sleep(3)
                    print("You die.")
                    # time.sleep(3)
                    print("RESPAWN")
                    continue

        else:
            continue

    if (intro_a.lower() == "wait"):
        print("You wait for sometime.")
        # time.sleep(3)
        print("You grow restless.")
        # time.sleep(3)
        print("You think to yourself that '2386' is a code to something, but you cannot remember why you think so.")
        # time.sleep(5)
        continue

    if (intro_a.lower() == "2386"):
        # time.sleep(1)
        print("You think about the numbers.")
        # time.sleep(3)
        print("You know '2386' means something important.")
        # time.sleep(3)
        print("Maybe you should go further into the darkness.")
        continue

    if (intro_a.lower() == "listen"):
        # time.sleep(1)
        print("You hear a person scream in the distance")
    else:
        print("You decide to " + intro_a)
        # time.sleep(3)
        print("Suddenly two torches light up two opposite ends of the cave you're in.")
        # time.sleep(3)
        print("You notice three pressure plates in addition to the two torches.")
        # time.sleep(3)
        print("Many vines and plants cover the walls of the room you're in.")
        # time.sleep(3)

        inspect_a = input("Do you investigate the room further? ")
        if (inspect_a.lower() in user_yes):
            # time.sleep(6)
            print("Upon further investigation you notice a mysterious liquid leaking from the ceiling into a rough stone basin in the middle of the room.")
            # time.sleep(6)
            print("Everything is silent.")
            while True:
                # time.sleep(1)
                print("What do you do?")
                # time.sleep(1)
                print("1 = Wait and do not move")
                # time.sleep(1)
                print("2 = Investigate the pressure plates")
                # time.sleep(1)
                print("3 = Investigate the plants")
                # time.sleep(1)
                print("4 = sleep")
                # time.sleep(1)
                print("5 = Investigate the liquid and stone basin ")
                # time.sleep(1)

                choice_a = input("What do you do? ")
                if (choice_a.lower() == "1"):
                    # time.sleep(3)
                    print("You wait...")
                    # time.sleep(6)
                    print("You wait...")
                    # time.sleep(6)
                    print("You hear a scream off in the distance...")
                    # time.sleep(3)
                    print("The scream says, 'I don't know about the wizard.'")
                    # time.sleep(3)
                    print("You think to yourself, 'What wizard?'")
                    # time.sleep(2)
                    continue

                if (choice_a.lower() == "2"):
                    # time.sleep(3)
                    print("You approach the pressure plates.")
                    # time.sleep(3)
                    print("Pressure plate 1: picture of a wolf.")
                    # time.sleep(3)
                    print("Pressure plate 2: picture of a flower.")
                    # time.sleep(3)
                    print("Pressure plate 3: picture of a ring with a blue ribbon.")
                    # time.sleep(3)

                    choice_plate1 = input("Which pressure plate do you choose? ")
                    if (choice_plate1.lower() == "1"):
                        # time.sleep(1)
                        print("You aproach the pressure plate and the smell of the wilderness wafts your way.")
                        # time.sleep(3)
                        print("You cautiously step on the pressure plate")
                        # time.sleep(6)
                        print("nothing happens")
                        # i want something to happen when you put a special code in this option
                        # time.sleep(3)
                        print("you step on it again, hoping something will happen")
                        # time.sleep(6)
                        print("Again, nothing happens.")
                        # time.sleep(2)
                        print("frustrated, you step away from the pressure plate and eye the room for a clue")
                        # time.sleep(3)

                        choice_plate1_a = input("What do you try now? ")
                        if (choice_plate1_a.lower() == "look for a clue" or "look for clue" or "look"):
                            # time.sleep(3)
                            print("you come up with nothing to help you with the pressure plate")
                            # time.sleep(3)
                            continue

                    if (choice_plate1.lower() == "2"):
                        # time.sleep(1)
                        print("you decide to stand on pressure plate 2")
                        # time.sleep(4)
                        print("a loud grating noise explodes around the cave as you step on pressure plate 2")
                        # time.sleep(3)
                        print("the ground below the pressure plate gives way and you fall into a pit")
                        # time.sleep(4)
                        print("You're still falling!")
                        # time.sleep(4)
                        print("You land in a lake.")
                        # time.sleep(3)

                        if ("Golden ring" in inventory):
                            # time.sleep(1)
                            print("You survived thanks to the golden ring you have!")
                            # time.sleep(3)
                            print(
                                "You swim to the edge of the lake and notice a campfire with a wizard sitting beside it.")
                            # time.sleep(3)
                            lake_wizard = input("Do you approach the wizard? ")

                            if (lake_wizard.lower() in user_yes):
                                # time.sleep(3)
                                print("You approach the wizard...")
                                # time.sleep(3)
                                print("You sit down beside the campfire.")
                                # time.sleep(3)
                                print("The wizards says, 'I have been waiting for you.'")
                                # time.sleep(3)
                                print("'I'm sure you have many questions' says the wizard.")
                                # time.sleep(3)

                                while True:
                                    print("What do you ask the wizard?")
                                    # time.sleep(1)
                                    print("1 = Where am I?")
                                    # time.sleep(3)
                                    print("2 = Who are you?")
                                    # time.sleep(3)
                                    print("3 = What's going on.")
                                    # time.sleep(3)
                                    print("4 = I have no further questions.")

                                    wizard_questions = input("What do you ask the Wizard? ")
                                    if (wizard_questions.lower() == "1"):
                                        # time.sleep(1)
                                        print("You are in a dark cave.")
                                        # time.sleep(3)
                                        print("You're in the land of Lanzix.")
                                        # time.sleep(3)
                                        print("A land under the corruption of the Twelve.")
                                        # time.sleep(3)
                                        continue

                                    if (wizard_questions.lower() == "2"):
                                        # time.sleep(1)
                                        print("I am a wizard! Don't you remember me?")
                                        # time.sleep(3)
                                        print("You have successfully completed your first task.")
                                        # time.sleep(3)
                                        print("That being finding me.")
                                        # time.sleep(3)
                                        print("Your second task is to stop the killer that wonders these caves.")
                                        # time.sleep(3)
                                        print("'He is one of the Twelve.'")
                                        # time.sleep(3)
                                        print("'Now go'.")
                                        # time.sleep(3)
                                        print(
                                            "'I will send you back in time so that you may be able to complete your second task.' Says the wizard")
                                        # time.sleep(3)
                                        print("Keep the ring close!")
                                        break



                                    if (wizard_questions.lower() == "3"):
                                        # time.sleep(1)
                                        print("Many things...")
                                        # time.sleep(3)
                                        continue
                                    else:
                                        # time.sleep(3)
                                        continue
                        else:
                            # time.sleep(1)
                            print("You die from the fall.")
                            # time.sleep(3)
                            print("As you were falling you heard a voice mention something about a wizard and a wolf.")
                            # time.sleep(3)
                            continue

                        # pit opens up and swallows you, you fall for a long time and land into a lake
                    if (choice_plate1.lower() == "3"):
                        #time.sleep(1)
                        pass
                    # easter egg
                    if (choice_plate1.lower() == "4"):
                        # time.sleep(1)
                        print("a passage way opens up to your right")
                        # time.sleep(3)
                        print("as you walk down the passage a wolf appears")
                        # time.sleep(3)
                        print("you look down at the wolf, suprised")
                        # time.sleep(3)
                        print("the wolf looks back at you, it seems to be grinning")
                        # time.sleep(3)
                        print("'what do you need assistance with'")
                        # time.sleep(3)
                        # option to ask for help with whatever here

                if (choice_a.lower() == "3"):
                    # time.sleep(3)
                    print("You investigate the plants.")
                    # time.sleep(3)
                    print("You notice a hidden passageway behind the plants.")
                    # time.sleep(3)
                    print("The hidden passageway has a keyhole in the shape of a ring.")
                    # time.sleep(3)

                    hidden_passage = input("Do you attempt to go through the passageway? ")
                    if (hidden_passage.lower() in user_yes):
                        # time.sleep(1)
                        print("You insert the golden ring into the keyhole of the passage.")
                        # time.sleep(3)
                        print("The door of the passage swings open.")
                        # time.sleep(3)
                        print("You take the golden ring from the keyhole and continue through the passageway.")
                        # time.sleep(3)
                        print("You wind up in a room with tables and notes and papers on those tables.")
                        # time.sleep(5)
                        print("You see a feather on a table.")

                        while True:
                            # time.sleep(3)
                            hidden_passage_feather = input("Do you take the feather? ")

                            if (hidden_passage_feather.lower() in user_yes):
                                # time.sleep(3)
                                print("You take the feather!")
                                # time.sleep(3)
                                inventory["Feather"] = 1
                                print(inventory)
                                # time.sleep(3)
                                print("You hear a killer enter through the tunnel behind you.")
                                # time.sleep(3)

                                hidden_passage_killer = input("What do you do(Run or Hide)? ")

                                if (hidden_passage_killer.lower() == "hide"):
                                    # time.sleep(6)
                                    print("You hide.")
                                    # time.sleep(3)
                                    print("You hear the killer enter into the room that you're in.")
                                    # time.sleep(3)
                                    print("The killer shouts, 'where is my feather!'")
                                    # time.sleep(3)
                                    print("The killer searches all around the room for his feather.")
                                    # time.sleep(3)
                                    print("The killer is a mortal without his feather.")
                                    # time.sleep(3)

                                    if ("feather" and "knife" in inventory):
                                        kill = input("Do you killer the killer? ")
                                        if (kill.lower() in user_yes):
                                            # time.sleep(3)
                                            print("you kill the killer.")
                                    else:
                                        print("You think, 'if only I had a weapon to bring the killer to his end.'")
                                        # time.sleep(3)
                                        print("The killer sees you!")
                                        # time.sleep(3)

                                        print(f"You have about {time_chase} seconds to escape.")
                                        # time.sleep(3)



                                if (hidden_passage_killer.lower() == "run"):
                                    print("You start running!")
                                    print(time_chase)
                                    time.sleep(3)
                                    for i in range(time_chase, 0):
                                        print(f"You have {i} seconds left!")
                                        time.sleep(1)
                                        #2% chance of immediate death every iteration.
                                        if time_chase >= 30 or "Powerful energy" in active_effects:
                                            time.sleep(3)
                                            print("You escaped the killer!")
                                            time.sleep(3)
                                            break

                                        else:
                                            if ("feather" in inventory or "Powerful energy" in active_effects):
                                                # time.sleep(3)
                                                print("You live!")
                                                # time.sleep(3)
                                                print("You survived the attack!")
                                                # time.sleep(3)
                                                print("You quickly rush back the way you came.")
                                                continue
                                            else:
                                                # time.sleep(3)
                                                print("You die.")
                                                # time.sleep(3)
                                                print("RESPAWN")
                                                continue


                                else:
                                    print(f"You {hidden_passage_killer}")
                                    break

                            else:
                                print("Are you sure you don't want the feather?")
                                time.sleep(3)
                                continue

                        break

                    if (hidden_passage.lower() in user_no):
                        # time.sleep(3)
                        print("You double back to the center of the room.")
                        # time.sleep(3)
                        continue
                    else:
                        # time.sleep(3)
                        print("The door won't budge!")
                        # time.sleep(3)
                        print("You double back to the center of the room.")
                        # time.sleep(3)
                        continue

                if (choice_a.lower() == "4"):
                    pass
                    # time.sleep(3)

                if (choice_a.lower() == "5"):
                    print("")
                    # time.sleep(3)
                    print("You approach the stone basin and it's strange contents.")
                    # time.sleep(5)
                    print("As you get closer a rancid stench confronts you.")
                    # time.sleep(3)
                    print("There are puddles around the stone basin.")
                    # time.sleep(3)
                    print("You notice steam around the basin now that you are directly in fron of it.")
                    # time.sleep(3)
                    print("You peer into the bottom of the basin and see a golden ring.")
                    # time.sleep(4)

                    basin = input("Do you attempt to take the ring? ")
                    if (basin.lower() in user_yes):
                        # time.sleep(3)
                        basin_random = random.randint(0, 4)
                        if (basin_random == 1 or 2 or 3):
                            # time.sleep(1)
                            print("You got the Golden ring")
                            # time.sleep(3)
                            inventory["Golden ring"] = 1
                            inventory_display()
                        else:
                            # time.sleep(3)
                            print("You failed to retrive the golden ring.")
                            # time.sleep(3)
                            basin_random = random.randint(1, 4)
                            if (basin_random == "2"):
                                # time.sleep(3)
                                print("The figure approaches you.")
                                # time.sleep(10)
                                print("The figure pulls out a knife.")
                                # time.sleep(8)
                                print("You no longer live")
                                # time.sleep(4)
                                print("As the figure killed you, he muttered about the eleven others.")
                                # time.sleep(12)
                                continue
                            else:
                                # time.sleep(3)
                                print("You failed to retrive the golden ring.")
                                continue

        else:
            # time.sleep(3)
            continue
        if (inspect_a.lower() in user_no):
            # time.sleep(1)
            print("You don't investigate the room any more.")
            # time.sleep(3)
            print("A figure steps into the light.")
            # time.sleep(3)
            print('''The figure says, "Good luck getting out of here fool!"''')
            # time.sleep(3)

            reply_a = input("What do you say to the figure? ")
            if (reply_a.lower() == "go away"):
                # time.sleep(2)
                print("'No!' says the figure.")
                # time.sleep(3)
                print("The figure pulls out a knife.")
                if ("feather" in inventory or "Powerful energy" in active_effects):
                    # time.sleep(3)
                    print("You live!")
                    # time.sleep(3)
                    print("You survived the attack!")
                    # time.sleep(3)
                    print("You quickly rush back the way you came.")
                    continue
                else:
                    # time.sleep(3)
                    print("You die.")
                    # time.sleep(3)
                    print("RESPAWN")
                    continue



            else:
                # time.sleep(3)
                print("The figure pulls out a knife.")
                if ("feather" in inventory or "Powerful energy" in active_effects):
                    # time.sleep(3)
                    print("You live!")
                    # time.sleep(3)
                    print("You survived the attack!")
                    # time.sleep(3)
                    print("You quickly rush back the way you came.")
                    continue
                else:
                    # time.sleep(3)
                    print("You die.")
                    # time.sleep(3)
                    print("RESPAWN")
                    continue

        else:
            continue


