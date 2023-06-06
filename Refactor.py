import random
import time

user_yes = ["yes", "yeah", "yep", "y", "ye", "yea", "ok", "okay", "affirmative", "sounds good", "you got it",
            "whatever", "sure", "if i have to", "yeh", "yah"]
user_no = ["no", "no way", "that's stupid", "why would i do that?", "that's really dumb", "nope", "i don't think so",
           "that won't fly"]
inventory = {}
active_effects = {}
achievements = []


# opening screen function
def opening_screen():
    print("Lanzix 2")
    # time.sleep(3)
    print("Objective: Escape.")
    # time.sleep(5)
    print("You wake up in a dark cave.")
    # time.sleep(5)
    print("You cannot see anything in the darkness.")


def get_achievements_length(achievements_param):
    length = len(achievements_param)
    return length


def get_achievements(achievements_param):
    achievements_param = achievements_param
    return achievements_param


# define a function that will check the player's inventory to see if they have a weapon, and if they do, what weapon
def weapon_check(inventory_param):
    if "knife" in inventory_param:
        return True
    else:
        return False


def feather_check(inventory_param):
    if "feather" in inventory_param:
        return True
    else:
        return False


def powerful_energy_check(active_effects_param):
    if "powerful energy" in active_effects_param:
        return True
    else:
        return False


# define a function that will check the player's inventory to see if they have the invulnerability items
def invulnerability_check(inventory_param, active_effects_param):
    if "feather" in inventory_param or "powerful energy" in active_effects_param:
        return True
    else:
        return False


# function for user achievements
# changed parameter to achievements_param
# 6/4/2023
def achievement_unlocked(award, achievements_param):
    if award not in achievements_param:
        # time.sleep(3)
        print(f'''You have been awarded the achievement "{award}."''')
        # time.sleep(3)
        print("You should be proud, these achievements are very difficult to acquire!")
        # time.sleep(3)
        print("How many are there?")
        # time.sleep(3)
        print("That's for you to discover!")
        achievements_param.append(award)
        # time.sleep(3)
        print("Achievements:")
        print(achievements_param)
        # time.sleep(3)
        pass
    else:
        pass


# we need to write a function that will handle the user fighting beasts
# we will need to pass in the user's health as a parameter as well as the loop variable
# we will return a tuple with the user's health and the loop variable
def fight_beast(health_param, loop_param, inventory_param, active_effects_param, achievements_param):
    beasts_humanoid = ["troll", "giant", "bandit", "orc", "goblin", "draugr"]
    beasts_animal = ["wolf", "bear", "sabre cat", "troll", "giant", "dragon"]
    quote_during_battle_humanoid = ["Never should have come here!", "What are you doing in my swamp!", "*Low Growl*",
                                    "You're going to die!"]
    quote_during_battle_animal = ["Howl", "Roar", "Growl", "Snarl"]
    # we need to return a random beast from either the humanoid or animal list
    if random.randint(0, 1) == 0:
        beast = random.choice(beasts_humanoid)
        quote_during_battle = random.choice(quote_during_battle_humanoid)
        # time.sleep(3)
    else:
        beast = random.choice(beasts_animal)
        quote_during_battle = random.choice(quote_during_battle_animal)
        # time.sleep(3)
    print(f"You have encountered a {beast}!")
    # time.sleep(3)
    print(f'''{beast.capitalize()}: "{quote_during_battle}"''')
    if invulnerability_check(inventory_param, active_effects_param):
        print("You are invulnerable!")
        # time.sleep(3)
        print("You continue on your journey.")
        # time.sleep(3)
        loop_param = loop_param
        return health_param, loop_param
    else:

        if weapon_check(inventory_param):
            print("You have a weapon!")
            # time.sleep(3)
            print("You have two options:")
            # time.sleep(3)
            print("1. Fight")
            # time.sleep(3)
            print("2. Run")
            user_choice = input("What do you choose? ")
            if user_choice == "1":
                print("Before you are able to attack the beast hits you!")
                # time.sleep(3)
                damage = random.randint(0, 20)
                health_param -= damage
                if damage == 0:
                    print(f"You dodged the attack!")
                    # time.sleep(3)
                    print("You continue on your journey.")
                    # time.sleep(3)
                    loop_param = loop_param
                    return health_param, loop_param
                if health_param > 0:
                    print(random.choice(quote_during_battle))
                    # time.sleep(3)
                    print(f"The {beast} deals {str(damage)} damage.")
                    # time.sleep(3)
                    print("Health: " + str(health_param))
                    # time.sleep(3)
                    print("You attack the beast!")
                    # time.sleep(3)]
                    print("The beast flees!")
                    # time.sleep(3)
                    loop_param = loop_param
                    return health_param, loop_param
                else:
                    chance_to_run = random.randint(0, 7)
                    if chance_to_run != 3:
                        print("You ran away!")
                        # time.sleep(3)
                        print("You continue on your journey.")
                        # time.sleep(3)
                        loop_param = loop_param
                        return health_param, loop_param
                    else:
                        print("You failed to run away!")
                        # time.sleep(3)
                        print("The beast attacks!")
                        # time.sleep(3)
                        damage = random.randint(0, 20)
                        health_param -= damage
                        result = handle_death(health_param, loop_param)
                        health_param = result[0]
                        loop_param = result[1]
                        return health_param, loop_param

        else:
            print("You have no weapon!")
            # time.sleep(3)
            print("You can only run!")
            # time.sleep(3)

            chance_to_run = random.randint(0, 1)
            if chance_to_run == 0:
                print("You ran away!")
                # time.sleep(3)
                print("You continue on your journey.")
                # time.sleep(3)
                loop_param = loop_param
                return health_param, loop_param
            else:
                print("You failed to run away!")
                # time.sleep(3)
                print("The beast attacks!")
                # time.sleep(3)
                damage = random.randint(0, 20)
                print(f"The {beast} deals {damage} damage.")
                # time.sleep(3)
                health_param -= damage
                print(f"Health: {health_param}")
                result = handle_death(health_param, loop_param)
                health_param = result[0]
                loop_param = result[1]
                return health_param, loop_param


# we will need to define a function to handle the killer's battle sequence
def fight_killer(health_param, loop_param, inventory_param, active_effects_param, achievements_param, wizard_param):
    if wizard_param == 1:
        # time.sleep(3)
        print("Inventory:", inventory_param)
        battle_quote = ['''"You never should have come here!"''', '''"I've got you now!"''',
                        '''"Don't even try to escape!"''', '''Die!''']
        quote_during_battle = random.choice(battle_quote)
        killer = "alive"
        global inventory
        global active_effects
        global achievements

        # time.sleep(1)
        print(f"The Killer says: {quote_during_battle}")
        # time.sleep(3)
        if weapon_check(inventory_param):
            # time.sleep(3)
            print("You have a weapon!")
            if feather_check(inventory_param):
                # time.sleep(3)
                print("You are undefeatable because you carry the killers feather!")
                # time.sleep(3)
                print("You are able to fight because you carry the knife!")
                # time.sleep(3)
                count = 1
                while killer == "alive":

                    rand_chance = random.randint(1, 3)
                    if rand_chance == 2:
                        # time.sleep(3)
                        print("You defeat the killer!")
                        # time.sleep(3)
                        print("The killer lies motionless on the cave floor.")
                        # time.sleep(3)
                        print("You have completed Lanzix 2.")
                        # time.sleep(3)
                        print("Thank you for playing!")
                        # time.sleep(3)
                        print(f"You have completed {get_achievements_length(achievements_param)} achievements!")
                        # time.sleep(3)
                        print("Achievements:")
                        print(get_achievements(achievements_param))
                        # time.sleep(3)
                        time_stop_win = time.perf_counter()
                        print(f"It took this much time to complete the game: {time_stop_win}")
                        killer = "dead"
                        user_answer = input("Do you want to play again? (y/n)")
                        if user_answer in user_yes:
                            health_param = 100
                            loop_param = 1
                            return health_param, loop_param
                        else:
                            exit()
                    else:
                        # time.sleep(3)
                        print("The killer dodged your attack!")
                        count += 1
                        # time.sleep(3)
                        print("You prepare for your next attack!")
                        # time.sleep(3)
                        killer_run = random.randint(3, 5)
                        if count == killer_run:
                            # time.sleep(3)
                            print("The killer runs away!")
                            # time.sleep(3)
                            print("You are left in the darkness as you were.")
                            # time.sleep(3)
                            loop_param = loop_param
                            return health_param, loop_param
                        else:
                            continue
            elif powerful_energy_check(active_effects_param):
                # time.sleep(3)
                print("The killer cannot kill you because of your powerful energy.")
                # time.sleep(3)
                print("You attack with your weapon, but it does not seem to do any damage.")
                # time.sleep(3)
                print("The killer seeing that you are immune to his attacks runs off into the darkness.")
                # time.sleep(3)
                return health_param, loop_param
            '''else:
                print("You cannot kill the killer because you don't have a weapon!")
                # time.sleep(3)
                print("The killer lunges forth")
                damage = random.randint(120, 999)
                health_param -= damage
                # time.sleep(3)
                print(f"You take {damage} damage.")
                print("Health: " + str(health))
                # time.sleep(3)
                loop_param = 1
                return health_param, loop_param'''
        elif powerful_energy_check(active_effects_param):
            print("The killer cannot kill you because of your powerful energy.")
            # time.sleep(3)
            print("However, you cannot kill the killer because you don't have a weapon.")
            # time.sleep(3)
            print("The killer seeing that you are immune to his attacks runs off into the darkness.")
            # time.sleep(3)
            loop_param = loop_param
            return health_param, loop_param
        elif feather_check(inventory_param):
            print("You cannot be killed because you have the feather!")
            # time.sleep(3)
            print("However, you cannot kill the killer because you don't have a weapon.")
            # time.sleep(3)
            print("You gaze into the killer's eyes.")
            # time.sleep(3)
            print("It became uncomfortable to stare so long, so the killer flees.")
            achievement_unlocked("Scare the killer", achievements)
            loop_param = loop_param
            return health_param, loop_param
        else:
            print("You don't have a weapon!")
            damage = random.randint(120, 999)
            health_param -= damage
            # time.sleep(3)
            print(f"You take {damage} damage.")
            print("Health: " + str(health_param))
            # time.sleep(3)
            loop_param = 1
            return health_param, loop_param
    else:
        return health_param, loop_param


# wait sequence function
# get a random good event or a random bad event or nothing
# the good event will increase the user's health to a maximum of 100
# or the user may get a knife
# the bad event will have the player encounter a beast
# we will define a function for each event
# we will return a tuple with the user's health and the loop variable
def wait_sequence(health_param, loop_param, inventory_param, active_effects_param, achievements_param):
    rand_good_event = ["max health", "knife"]
    rand_bad_event = ["beast"]
    rand_nothing_event = ["nothing"]
    # time.sleep(3)
    print("You wait for sometime.")
    # time.sleep(3)
    rand_num = random.randint(1, 8)
    if rand_num == 2:
        choice = random.choice(rand_good_event)
        if choice == "max health":
            print("Suddenly a powerful energy touches you.")
            # time.sleep(3)
            print("Your health is restored!")
            # time.sleep(3)
            health_param += 20
            # time.sleep(3)
            print(f"Health: {health_param}")
            loop_param = loop_param
            return health_param, loop_param
        else:
            # I don't think we get the knife in our
            # inventory here.
            # TODO: Pass the global inventory dictionary
            # TODO: Append the global inventory dictionary
            print("You sit alone with your thoughts.")
            # time.sleep(3)
            print("Out of the corner of your eye, you see a knife.")
            # time.sleep(3)
            print("You pick it up.")
            # time.sleep(3)
            inventory_param["knife"] = 1
            print("You continue on your journey.")
            inventory_display(inventory_param)
            loop_param = loop_param
            return health_param, loop_param
    else:
        number = random.randint(0, 7)
        if number == 3:
            choice = random.choice(rand_bad_event + rand_nothing_event)
            if choice == "beast":
                result = fight_beast(health_param, loop_param, inventory_param, active_effects_param,
                                     achievements_param)
                health_param = result[0]
                loop_param = result[1]
                return health_param, loop_param
            else:
                print("Nothing happens.")
                # time.sleep(3)
                print("Still, nothing happens.")
                # time.sleep(3)
                print("You continue on your journey.")
                # time.sleep(3)
                loop_param = loop_param
                return health_param, loop_param


def death(health_param, loop_param):
    global inventory
    global active_effects
    global achievements
    # time.sleep(3)
    print("You died.")
    # time.sleep(3)
    print("Debug statement - Testing death")
    # time.sleep(3)
    print("Health: " + str(health_param))
    time_stop_death = time.perf_counter()
    print(f"{time_stop_death}")
    inventory = {}
    active_effects = {}
    achievements = []
    # time.sleep(3)
    # loop_param being 1, returns the player to the beginning
    loop_param = 1
    health_param = health_param
    return health_param, loop_param


# the handle_death function is a function that checks if the player's health is 0 or below, and if it is,
# it calls the death function

def handle_death(health_param, loop_param):
    if health_param <= 0:
        death(health_param, loop_param)
        loop_param = 1
        return health_param, loop_param
    else:
        health_param = health_param
        loop_param = loop_param
        return health_param, loop_param


def battle_killer_start(wizard_param):
    if wizard_param == 1:
        # time.sleep(3)
        killer = ["The killer sees you!", "The killer hears you!", "The killer spots you!"]
        killer_2 = ["He runs over to you!", "He rushes over to you!", "The killer is on your tail!"]
        choice = random.choice(killer)
        choice_2 = random.choice(killer_2)
        # time.sleep(3)
        print(f"{choice} {choice_2}")
        # time.sleep(3)
        print("Quickly, you prepare for battle")
    else:
        pass


def inventory_display(inventory_param):
    print("Inventory Includes:")
    print(inventory_param)


def effects_display(active_effects_param):
    print("Active effects:")
    print(active_effects_param)


def explore_message():
    print("You take a step forward...")
    # time.sleep(5)
    print("You still cannot see anything in the darkness")
    # time.sleep(5)


def explore_message_b():
    print("You look around for light...")
    # time.sleep(5)
    print("You do not see anything.")
    # time.sleep(5)
    # time.sleep(5)
    print("You hear a human scream deeper in the tunnel.")
    # time.sleep(3)


def explore_message_b_2():
    # time.sleep(5)
    print("You approach the scream.")
    # time.sleep(3)
    print("You see the killer walking further into the cave.")
    # time.sleep(3)


def explore_message_b_1():
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
    # broke this string into two lines for better readability
    print("Upon further investigation you notice a mysterious liquid leaking from the ceiling into a rough stone basin "
          "in the middle of the room.")
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
    print('''The Wizard calls out to you, "over here Aaron."''')
    # time.sleep(3)
    print('''"That's right" you think to yourself, "My name is Aaron."''')
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


def plants_6(hidden_passage_killer_param):
    # time.sleep(3)
    print(f"You decide to {hidden_passage_killer_param}.")
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


def main():
    wizard = 1
    loop = 1
    opening_screen()
    while loop == 1:
        global inventory
        global active_effects
        global achievements

        inventory = {}
        active_effects = {}
        achievements = []
        health = 100
        wizard = 1
        # loop 1 is the loop you get sent back to if you die at any point
        print("New run start: ")
        time.perf_counter()
        # time.sleep(5)

        # loop 2 is the loop where you get sent back by the wizard
        loop = 2
        while loop == 2:
            intro_a = input("What do you do? ")
            wizard = 1

            if intro_a.lower() == "explore" or intro_a.lower() == "go":
                explore_message()

                explore_a = input("Do you look around for light? ")
                if explore_a.lower() in user_yes:
                    explore_message_b()

                    print("1: Approach quietly")
                    # time.sleep(3)
                    print("2: Approach")
                    # time.sleep(3)

                    explore_b = input("Do you go towards the scream? ")

                    if explore_b.lower() == "1":
                        explore_message_b_1()
                        result = fight_beast(health, loop, inventory, active_effects, achievements)
                        health = result[0]
                        loop = result[1]
                        continue

                    if explore_b.lower() == "2":
                        explore_message_b_2()

                        explore_c = input("Do you follow the figure? ")

                        if explore_c.lower() in user_yes:
                            explore_message_killer_yes()
                            battle_killer_start(wizard)
                            result = fight_killer(health, loop,  inventory, active_effects, achievements, wizard)
                            health = result[0]
                            loop = result[1]
                            continue

                    else:
                        explore_message_c()

                        active_effects["powerful energy"] = 1
                        # time.sleep(3)
                        print(active_effects)
                        # time.sleep(3)
                        print("With your new found power you will be able to resist any foe!")
                        # time.sleep(3)
                        continue

                if explore_a.lower() in user_no:
                    explore_message_killer_no()
                    explore_b = input("What do you do? ")
                    print("You decide to " + explore_b)
                    battle_killer_start(wizard)
                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                    health = result[0]
                    loop = result[1]
                    continue
                else:
                    # This is regarding looking for light.
                    # This else is for if the user does not type a user_yes or user_no.
                    battle_killer_start(wizard)
                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                    health = result[0]
                    loop = result[1]
                    continue

            # wait sequence and battle code sequence are defined for life_loop and death_loop
            if intro_a.lower() == "wait":
                result = wait_sequence(health, inventory, active_effects, achievements, loop)
                health = result[0]
                loop = result[1]
                continue

            if intro_a.lower() == "juan" or intro_a.lower() == "spencer":
                inventory["knife"] = 1
                inventory["feather"] = 1
                inventory["golden ring"] = 1
                active_effects["powerful energy"] = 1
                inventory_display(inventory)
                loop = 2
                continue

            # if loop != 2:
                # break

            else:
                print("You decide to " + intro_a)
                choice_5_a()

                inspect_a = input("Do you investigate the room further? ")
                if inspect_a.lower() in user_yes:
                    choice_5_b()
                    # loop 3 is the loop that lets you make choices to explore the room
                    loop = 3
                    while loop == 3:
                        choice_5_c()

                        choice_a = input("What do you do? ")
                        if choice_a.lower() == "1":
                            # loop = 3
                            result = wait_sequence(health, loop, inventory, active_effects, achievements)
                            health = result[0]
                            loop = result[1]
                            continue

                        if choice_a.lower() == "2":
                            approach_pressure_plates()

                            choice_plate1 = input("Which pressure plate do you choose? ")
                            if choice_plate1.lower() == "1":
                                pressure_plate_1()

                                choice_plate1_a = input("What do you try now? ")
                                if (choice_plate1_a.lower() == "look for a clue" or
                                        choice_plate1_a.lower() == "look for clue" or
                                        choice_plate1_a.lower() == "look"):

                                    achievement_unlocked("Look for clue", achievements)

                                    pressure_plate_1_clue()
                                    loop = 3
                                    continue

                                else:
                                    # time.sleep(3)
                                    print("You decide to " + choice_plate1_a)
                                    # time.sleep(3)
                                    print(f"Unfortunately, {choice_plate1_a} does not work. ")
                                    # time.sleep(3)
                                    loop = 3
                                    continue

                            if choice_plate1.lower() == "2":
                                pressure_plate_2()

                                if "golden ring" in inventory:
                                    pressure_plate_2_survive()
                                    # this loop allows you to approach the wizard
                                    loop = 4
                                    while loop == 4 and loop != 1:
                                        lake_wizard = input("Do you approach the wizard? ")
                                        if lake_wizard.lower() in user_yes:
                                            pressure_plate_2_wizard()
                                            # this loop lets you choose an option from the wizard
                                            loop = 5
                                            while loop == 5 and loop != 1:
                                                wizard_ask()

                                                wizard_questions = input("What do you ask the Wizard? ")
                                                if wizard_questions.lower() == "1":
                                                    wizard_question_1()
                                                    loop = 5
                                                    continue

                                                if wizard_questions.lower() == "2":
                                                    wizard_question_2()
                                                    loop = 5
                                                    continue

                                                if wizard_questions.lower() == "3":
                                                    wizard_question_3()

                                                    if "knife" in inventory:
                                                        wizard_question_3a()
                                                        loop = 5
                                                        continue
                                                    else:
                                                        pass
                                                        loop = 5
                                                        continue

                                                if wizard_questions.lower() == "4":
                                                    wizard_question_4()
                                                    # TODO: revise the loops and fix
                                                    loop = 2
                                                    # break
                                                    # break
                                                    # break
                                                    wizard = 2
                                                    continue

                                                    # Yeah, we need 3 breaks. CRAZY right????!!!?!?!?!
                                                else:
                                                    # time.sleep(3)
                                                    loop = 5
                                                    achievement_unlocked("Starting the rebellion.", achievements)
                                                    # TODO: possibly revise print statement
                                                    print("Nice! Now please choose a valid response!")
                                                    continue

                                        else:
                                            approach_wizard_no()
                                            achievement_unlocked("Learn your name", achievements)
                                            # time.sleep(3)
                                            continue

                                else:
                                    wizard_fall()
                                    # reset lists and dictionaries
                                    inventory = {}
                                    active_effects = {}
                                    achievements = []
                                    achievement_unlocked("Humpty Dumpty had a great fall.", achievements)
                                    wizard = 2
                                    loop = 1
                                    continue

                            if choice_plate1.lower() == "3":
                                knife_chance = random.randint(0, 5)
                                achievement_unlocked("Examine pressure plate #3!", achievements)

                                if knife_chance == 2 or knife_chance == 3:
                                    inventory["knife"] = 1
                                    print("You find a knife as you stepped on the pressure plate!")
                                    # time.sleep(3)
                                    inventory_display(inventory)
                                else:
                                    battle_killer_start(wizard)
                                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                                    health = result[0]
                                    loop = result[1]
                                    continue

                        if choice_a.lower() == "3":
                            plants_1()

                            hidden_passage = input("Do you attempt to go through the passageway? ")
                            if hidden_passage.lower() in user_yes and "golden ring" in inventory:
                                plants_2()
                                # this loop is for acquiring the feather
                                loop = 6
                                while loop == 6:
                                    # time.sleep(3)
                                    if "feather" not in inventory:
                                        hidden_passage_feather = input("Do you take the feather? ")

                                        if hidden_passage_feather.lower() in user_yes:
                                            plants_3()
                                            inventory["feather"] = 1
                                            # time.sleep(3)
                                            print(inventory)
                                            battle_killer_start(wizard)
                                            result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                                            health = result[0]
                                            loop = result[1]
                                            continue
                                        else:
                                            print("Are you sure you don't want the feather?")
                                            # time.sleep(3)
                                            battle_killer_start(wizard)
                                            result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                                            health = result[0]
                                            loop = result[1]
                                            continue
                                    else:
                                        # time.sleep(3)
                                        print("The killer is walking through the room when he spots you!")
                                        # time.sleep(3)
                                        battle_killer_start(wizard)
                                        result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                                        health = result[0]
                                        loop = result[1]
                                        continue

                            if hidden_passage.lower() in user_no:
                                achievement_unlocked("Don't go in the passageway!", achievements)
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

                        if choice_a.lower() == "4":
                            achievement_unlocked("Sleep", achievements)
                            # time.sleep(3)
                            print("You awake.")
                            # time.sleep(3)
                            continue
                        if choice_a.lower() == "5" and "golden ring" not in inventory:
                            basin_1()

                            basin = input("Do you attempt to take the ring? ")
                            if basin.lower() in user_yes:
                                # time.sleep(3)
                                basin_random = random.randint(0, 4)
                                if basin_random == 1 or basin_random == 2 or basin_random == 3:
                                    # time.sleep(1)
                                    print("You got the Golden ring")
                                    # time.sleep(3)
                                    inventory["golden ring"] = 1
                                    inventory_display(inventory)
                                    continue
                                else:
                                    # time.sleep(3)
                                    battle_killer_start(wizard)
                                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                                    health = result[0]
                                    loop = result[1]
                                    continue

                        if choice_a.lower() == "5" and "golden ring" in inventory:
                            # time.sleep(3)
                            print("You've already been here.")
                            # time.sleep(3)
                            achievement_unlocked("Thorough explorer", achievements)
                        else:
                            # time.sleep(3)
                            continue

                if inspect_a.lower() in user_no:
                    inspect_no()
                    battle_killer_start(wizard)
                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                    health = result[0]
                    loop = result[1]
                    continue

                else:
                    # time.sleep(3)
                    battle_killer_start(wizard)
                    result = fight_killer(health, loop, inventory, active_effects, achievements, wizard)
                    health = result[0]
                    loop = result[1]
                    continue
        #  if loop != 1:
            # break
main()
