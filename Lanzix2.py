import random
import time

inventory = {}
active_effects = {}
achievements = []

time_chase = random.randint(10, 60)
health = 100
quote_during_battle = ["Test Quote", "Test Quote 2", "Test Quote 3"]

user_yes = ["yes", "yeah", "yep", "y", "ye", "yea", "ok", "okay", "affirmative", "sounds good", "you got it",
            "whatever", "sure", "if i have to", "yeh", "yah"]
user_no = ["no", "no way", "that's stupid", "why would i do that?", "that's really dumb", "nope", "i don't think so",
           "that won't fly"]


def achievement_unlocked(award):
    if (award not in achievements):
        # time.sleep(3)
        print(f'''You have been awarded the achievement "{award}."''')
        # time.sleep(3)
        print("You should be proud, these achievements are very difficult to acquire!")
        # time.sleep(3)
        print("How many are there?")
        # time.sleep(3)
        print("That's for you to discover!")
        achievements.append(award)
        # time.sleep(3)
        print("Achievements:")
        print(achievements)
        # time.sleep(3)
    else:
        pass


def battle_code_lite(health):
    beasts = ["Werewolf", "Bat", "Zombie"]
    rand_beast = random.choice(beasts)

    print(f"Suddenly a {rand_beast} attacks you!")
    # time.sleep(3)
    print(f"You have no choice but to face {rand_beast} in combat.")
    # time.sleep(3)

    user_life = 1
    if("feather" in inventory or "Powerful energy" in active_effects):
        print("You cannot be harmed in battle!")
        # time.sleep(3)
        print("The beast runs away.")
        # time.sleep(3)
    else:
        damage = random.randint(0, 20)
        health -= damage
        if (damage == 0):
            print(f"You dodged the attack!")
            # time.sleep(3)
            print("You continue on your journey.")
            # time.sleep(3)
        if (health > 0):
            print(random.choice(quote_during_battle))
            # time.sleep(3)
            print(f"The {rand_beast} deals {str(damage)} damage.")
            user_life = 1
            # time.sleep(3)
            print("Health: " + str(health))
        else:
            user_life = 0
            print("You died.")
            # time.sleep(3)
            print("Health: " + health)
        return health


def battle_code_killer(health):
    user_life = 1
    if("feather" in inventory or "Powerful energy" in active_effects):
        # time.sleep(1)
        print(quote_during_battle)
        # time.sleep(3)
        print("The killer cannot stop you, you have the upper hand!")
        # time.sleep(3)
        if ("Knife" in inventory and "Feather" in inventory):
            # time.sleep(3)
            print("You are undefeatable because you carry the killers feather!")
            # time.sleep(3)
            print("You are able to fight because you carry the knife!")
            # time.sleep(3)
            print("You defeat the killer!")
            #time.sleep(3)
        else:
            # time.sleep(3)
            print("The killer cannot kill you because of your powerful energy.")
            # time.sleep(3)
            print("However, you cannot kill the killer because you don't have a weapon.")
            # time.sleep(3)
            print("The killer seeing that you are immune to his attacks runs off into the darkness.")
            # time.sleep(3)

    else:
        damage = random.randint(120, 999)
        health -= damage
        # time.sleep(3)
        print(f"You take {damage} damage.")
        print("Health: " + str(health))
        # time.sleep(3)
        print("You died.")
        return health

def battle_killer_start():
    # time.sleep(3)
    killer = ["The killer sees you!", "The killer hears you!", "The killer spots you!"]
    killer_2 = ["He runs over to you!", "He rushes over to you!", "The killer is on your tail!"]
    choice = random.choice(killer)
    choice_2 = random.choice(killer_2)
    # time.sleep(3)
    print(f"{choice} {choice_2}")
    #time.sleep(3)
    print("Quickly, you prepare for battle")

# inventory display function

def inventory_display():
    print("Inventory Includes:")
    print(inventory)

def effects_display():
    print("Active effects:")
    print(active_effects)

def wait_sequence(health, inventory, active_effects):
    rand_good = ["Max health", "Knife"]
    rand_bad = ["Killer interaction", "Enemy interaction"]
    # time.sleep(3)
    print("You wait for sometime.")
    # time.sleep(3)
    rand_num = random.randint(1,8)
    if (rand_num == 2):
        choice = random.choice(rand_good)
        if (choice == "Max health"):
            health = 100
            # time.sleep(3)
            print(f"Health: {health}")
        if (choice == "Knife"):
            # time.sleep(3)
            print("You find a knife in the corner of the room!")
            # time.sleep(3)
            inventory["Knife"] = 1
            inventory_display()

    else:
        choice = random.choice(rand_bad)
        if (choice == "Killer interaction"):
            # time.sleep(3)
            battle_killer_start()
            battle_code_killer(health)
        if (choice == "Enemy interaction"):
            # time.sleep(3)
            battle_code_lite(health)


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
    print("Because you quietly approach you did not alert the figure to yourself.")
    # time.sleep(3)
    print("The figure walks away from you leaving you in the darkness.")
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

def choice_5_a():
    # time.sleep(3)
    print("Suddenly two torches light up two opposite ends of the cave you're in.")
    # time.sleep(3)
    print("You notice three pressure plates in addition to the two torches.")
    # time.sleep(3)
    print("Many vines and plants cover the walls of the room you're in.")
    # time.sleep(3)

def choice_5_b():
    # time.sleep(4)
    print("Upon further investigation you notice a mysterious liquid leaking from the ceiling into a rough stone basin in the middle of the room.")
    # time.sleep(4)
    print("Everything is silent.")

def choice_5_c():
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

def approach_pressure_plates():
    # time.sleep(3)
    print("You approach the pressure plates.")
    # time.sleep(3)
    print("Pressure plate 1: picture of a wolf.")
    # time.sleep(3)
    print("Pressure plate 2: picture of a flower.")
    # time.sleep(3)
    print("Pressure plate 3: picture of a ring with a blue ribbon.")
    # time.sleep(3)

def pressure_plate_1():
    # time.sleep(1)
    print("You approach the pressure plate and the smell of the wilderness wafts your way.")
    # time.sleep(3)
    print("You cautiously step on the pressure plate.")
    # time.sleep(6)
    print("nothing happens.")
    # time.sleep(3)
    print("you step on it again, hoping something will happen.")
    # time.sleep(6)
    print("Again, nothing happens.")
    # time.sleep(2)
    print("Frustrated, you step away from the pressure plate and eye the room for a clue.")
    # time.sleep(3)

def pressure_plate_1_clue():
    # time.sleep(3)
    print("You come up with nothing to help you with the pressure plate")
    # time.sleep(3)
    print("You double back to the center of the room.")

def pressure_plate_2():
    # time.sleep(1)
    print("You decide to stand on pressure plate 2")
    # time.sleep(4)
    print("A loud grating noise explodes around the cave as you step on pressure plate 2")
    # time.sleep(3)
    print("The ground below the pressure plate gives way and you fall into a pit")
    # time.sleep(4)
    print("You're still falling!")
    # time.sleep(4)
    print("You land in a lake.")
    # time.sleep(3)

def pressure_plate_2_survive():
    # time.sleep(1)
    print("You survived thanks to the golden ring you have!")
    # time.sleep(3)
    print("You swim to the edge of the lake and notice a campfire with a wizard sitting beside it.")
    # time.sleep(3)

def pressure_plate_2_wizard():
    # time.sleep(3)
    print("You approach the wizard...")
    # time.sleep(3)
    print("You sit down beside the campfire.")
    # time.sleep(3)
    print('''The wizards says, "I have been waiting for you."''')
    # time.sleep(3)
    print('''"I'm sure you have many questions" says the wizard.''')
    # time.sleep(3)

def wizard_ask():
    print("What do you ask the wizard?")
    # time.sleep(1)
    print("1 = Where am I?")
    # time.sleep(3)
    print("2 = Who are you?")
    # time.sleep(3)
    print("3 = What's going on.")
    # time.sleep(3)
    print("4 = I have no further questions.")

def wizard_question_1():
    # time.sleep(1)
    print('''"You are in a dark cave."''')
    # time.sleep(3)
    print('''"You're in the land of Lanzix."''')
    # time.sleep(3)
    print('''"A land under the corruption of the Twelve."''')
    # time.sleep(3)

def wizard_question_2():
    # time.sleep(1)
    print('''"I am a wizard! Don't you remember me?"''')
    # time.sleep(3)
    print('''"You have successfully completed your first task."''')
    # time.sleep(3)
    print('''"That being, finding me."''')
    # time.sleep(3)
    print('''"Your second task is to stop the killer that wonders these caves."''')
    # time.sleep(3)
    print('''"He is one of the Twelve."''')
    # time.sleep(3)

def wizard_question_3():
    # time.sleep(1)
    print('''"Many things."''')
    # time.sleep(5)
    print('''"You may have noticed that you have two choices from your starting position in time."''')
    # time.sleep(3)

def wizard_question_3a():
    # time.sleep(1)
    print('''"I see you have already acquired a weapon."''')
    # time.sleep(3)
    print('''"You must stop the killer."''')
    # time.sleep(3)
    print('''"You have the means."''')
    # time.sleep(3)
    print('''"Make sure to take the feather."''')
    # time.sleep(3)

def wizard_question_4():
    # time.sleep(3)
    print('''"I will send you back in time so that you may be able to complete your second task." Says the wizard''')
    # time.sleep(3)
    print('''"Keep the ring close!"''')

def approach_wizard_no():
    # time.sleep(3)
    print('''The Wizard calls out to you,"over here Aaron."''')
    # time.sleep(3)
    print('''"That's right" you think. "My name is Aaron."''')
    # time.sleep(3)

def wizard_fall():
    # time.sleep(1)
    print("You die from the fall.")
    # time.sleep(3)
    print("As you fell you saw something interesting.")
    # time.sleep(3)

def plants_1():
    # time.sleep(3)
    print("You investigate the plants.")
    # time.sleep(3)
    print("You notice a hidden passageway behind the plants.")
    # time.sleep(3)
    print("The hidden passageway has a keyhole in the shape of a ring.")
    # time.sleep(3)

def plants_2():
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

def plants_3():
    # time.sleep(3)
    print("You take the feather!")
    # time.sleep(3)
    print("You hear a killer enter through the tunnel behind you.")
    # time.sleep(3)

def plants_4():
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

def plants_5():
    # time.sleep(3)
    print("You start running!")
    # time.sleep(3)
    print("The killer catches up to you!")
    # time.sleep(3)

def plants_6():
    # time.sleep(3)
    print(f"You decide to {hidden_passage_killer}.")
    # time.sleep(3)
    print("The killer catches up to you!")
    # time.sleep(3)

def basin_1():
    # time.sleep(3)
    print("You approach the stone basin and it's strange contents.")
    # time.sleep(5)
    print("As you get closer a rancid stench confronts you.")
    # time.sleep(3)
    print("There are puddles around the stone basin.")
    # time.sleep(3)
    print("You notice steam around the basin now that you are directly in front of it.")
    # time.sleep(3)
    print("You peer into the bottom of the basin and see a golden ring.")
    # time.sleep(4)

def inspect_no():
    # time.sleep(1)
    print("You don't investigate the room any more.")
    # time.sleep(3)
    print("A figure steps into the light.")
    # time.sleep(3)
    print('''The figure says, "Good luck getting out of here fool!"''')
    # time.sleep(3)
    battle_code_killer(health)





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

            if (explore_b.lower() == "2"):
                explore_message_b_2()

                explore_c = input("Do you follow the figure? ")

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
            explore_message_killer_no()
            explore_b = input("What do you do? ")
            print("You decide to " + explore_b)
            battle_killer_start()
            battle_code_killer(health)
            continue
        else:
            # This is regarding looking for light. This else is for if the user does not type a user_yes or user_no.
            battle_killer_start()
            battle_code_killer(health)
            continue

    if (intro_a.lower() == "wait"):
        wait_sequence(health, inventory, active_effects)
        continue

    # if (intro_a.lower() == "2386"):
        # time.sleep(1)
        # print("You think about the numbers.")
        # time.sleep(3)
        # print("You know '2386' means something important.")
        # time.sleep(3)
        # print("Maybe you should go further into the darkness.")
        # continue

    # if (intro_a.lower() == "listen"):
        # time.sleep(1)
        # print("You hear a person scream in the distance")
    else:
        print("You decide to " + intro_a)
        choice_5_a()

        inspect_a = input("Do you investigate the room further? ")
        if (inspect_a.lower() in user_yes):
            choice_5_b()

            while True:
                choice_5_c()

                choice_a = input("What do you do? ")
                if (choice_a.lower() == "1"):
                    wait_sequence(health, inventory, active_effects)
                    continue

                if (choice_a.lower() == "2"):
                    approach_pressure_plates()

                    choice_plate1 = input("Which pressure plate do you choose? ")
                    if (choice_plate1.lower() == "1"):
                        pressure_plate_1()

                        choice_plate1_a = input("What do you try now? ")
                        if (choice_plate1_a.lower() == "look for a clue" or choice_plate1_a.lower() == "look for clue" or choice_plate1_a.lower() ==  "look"):
                            pressure_plate_1_clue()

                            continue
                        else:
                            # time.sleep(3)
                            print("You decide to " + choice_plate1_a)
                            # time.sleep(3)
                            print(f"Unfortunately, {choice_plate1_a} does not work. ")
                            # time.sleep(3)
                            continue

                            # can we even define the above because we use the user input "choice_plate1_a"

                    if (choice_plate1.lower() == "2"):
                        pressure_plate_2()

                        if ("Golden ring" in inventory):
                            pressure_plate_2_survive()

                            while True:
                                lake_wizard = input("Do you approach the wizard? ")
                                if (lake_wizard.lower() in user_yes):
                                    pressure_plate_2_wizard()

                                    while True:
                                        wizard_ask()

                                        wizard_questions = input("What do you ask the Wizard? ")
                                        if (wizard_questions.lower() == "1"):
                                            wizard_question_1()

                                            continue

                                        if (wizard_questions.lower() == "2"):
                                            wizard_question_2()

                                            continue


                                        if (wizard_questions.lower() == "3"):
                                            wizard_question_3()

                                            if ("knife" in inventory):
                                                wizard_question_3a()
                                                continue
                                            else:
                                                pass
                                            continue


                                        if (wizard_questions.lower() == "4"):
                                            wizard_question_4()
                                            break
                                            break
                                            break
                                            continue

                                            # Yeah we need 3 breaks. CRAZY right????!!!?!?!?!
                                        else:
                                            # time.sleep(3)
                                            continue

                                else:
                                    approach_wizard_no()
                                    achievement_unlocked("Learn your name")
                                    # time.sleep(3)
                                    continue


                        else:
                            wizard_fall()

                            achievement_unlocked("Fall to your death")
                            inventory = {}
                            active_effects = {}
                            break
                            continue

                    if (choice_plate1.lower() == "3"):
                        # time.sleep(1)
                        rand_num = random.randint(1,2)
                        if (rand_num == 1):
                            random_good_occurance()

                            achievement_unlocked("Look at pressure plate #3")
                            # Just to add more stuff to the achievements!

                        else:
                            random_bad_occurance()
                        continue

                if (choice_a.lower() == "3"):
                    plants_1()

                    hidden_passage = input("Do you attempt to go through the passageway? ")
                    if (hidden_passage.lower() in user_yes and "Golden ring" in inventory):
                        plants_2()

                        while True:
                            # time.sleep(3)
                            if ("Feather" not in inventory):
                                hidden_passage_feather = input("Do you take the feather? ")

                                if (hidden_passage_feather.lower() in user_yes):
                                    plants_3()
                                    inventory["Feather"] = 1
                                    # time.sleep(3)
                                    print(inventory)

                                    hidden_passage_killer = input("What do you do(Run or Hide)? ")

                                    if (hidden_passage_killer.lower() == "hide"):
                                        plants_4()

                                        battle_code_killer(health)



                                    if (hidden_passage_killer.lower() == "run"):
                                        plants_5()

                                        battle_code_killer(health)



                                    else:
                                        # time.sleep(3)
                                        achievement_unlocked("Ignore the parameters!")

                                        plants_6()

                                        battle_code_killer(health)




                                else:
                                    print("Are you sure you don't want the feather?")
                                    time.sleep(3)
                                    continue

                            if ("Feather" in inventory and "Knife" in inventory):
                                # time.sleep(3)
                                print("You are prepared for battle.")
                                # time.sleep(3)
                                print("The killer is walking through the room when he spots you!")
                                # time.sleep(3)
                                battle_code_killer(health)
                            else:
                                # time.sleep(3)
                                print("The killer is walking through the room when he spots you!")
                                # time.sleep(3)
                                battle_code_killer(health)

                        break

                    if (hidden_passage.lower() in user_no):
                        achievement_unlocked("Don't go in the passageway!")
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
                    achievement_unlocked("Sleep")
                    continue

                if (choice_a.lower() == "5" and "Golden ring" not in inventory):
                    basin_1()

                    basin = input("Do you attempt to take the ring? ")
                    if (basin.lower() in user_yes):
                        # time.sleep(3)
                        basin_random = random.randint(0, 4)
                        if (basin_random == 1 or basin_random == 2 or basin_random == 3):
                            # time.sleep(1)
                            print("You got the Golden ring")
                            # time.sleep(3)
                            inventory["Golden ring"] = 1
                            inventory_display()
                            continue
                        else:
                            # time.sleep(3)
                            print("While you were reaching in to get the golden ring the killer confronts you.")
                            # time.sleep(3)
                            battle_code_killer(health)
                if (choice_a.lower() == "5" and "Golden ring" in inventory):
                    # time.sleep(3)
                    print("You've already been here.")
                    # time.sleep(3)
                    achievement_unlocked("Thorough explorer")
                else:
                    # time.sleep(3)
                    continue

        if (inspect_a.lower() in user_no):
            inspect_no()

            battle_killer_start()

            battle_code_killer(health)

        else:
            # time.sleep(3)
            battle_killer_start()
            battle_code_killer(health)
            continue


