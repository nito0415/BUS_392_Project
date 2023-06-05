## First Test Case

Lanzix 2
Objective: Escape.
You wake up in a dark cave.
You cannot see anything in the darkness.
New run start: 
- *What do you do? go*
You take a step forward...
You still cannot see anything in the darkness
- *Do you look around for light? y*
You look around for light...
You do not see anything.
You hear a human scream deeper in the tunnel.
1: Approach quietly
2: Approach
- *Do you go towards the scream? 2*
You approach the scream.
You see the killer walking further into the cave.
- *Do you follow the figure? n*
The killer spots you! He runs over to you!
Quickly, you prepare for battle
The Killer says: "Don't even try to escape!"
You take 581 damage.
Health: -481
- *New run start:*
What do you do? 

### Working as expected

## Second Test Case

Connected to pydev debugger (build 231.9011.38)
Lanzix 2
Objective: Escape.
You wake up in a dark cave.
You cannot see anything in the darkness.
New run start: 
- What do you do? >? run
You decide to run
Suddenly two torches light up two opposite ends of the cave you're in.
You notice three pressure plates in addition to the two torches.
Many vines and plants cover the walls of the room you're in.
- Do you investigate the room further? >? Yes
Upon further investigation you notice a mysterious liquid leaking from the ceiling into a rough stone basin in the middle of the room.
Everything is silent.
What do you do?
1 = Wait and do not move
2 = Investigate the pressure plates
3 = Investigate the plants
4 = sleep
5 = Investigate the liquid and stone basin 
- What do you do? >? 5
You approach the stone basin and it's strange contents.
As you get closer a rancid stench confronts you.
There are puddles around the stone basin.
You notice steam around the basin now that you are directly in front of it.
You peer into the bottom of the basin and see a golden ring.
- Do you attempt to take the ring? >? y
You got the Golden ring
Inventory Includes:
{'Golden ring': 1}
What do you do?
1 = Wait and do not move
2 = Investigate the pressure plates
3 = Investigate the plants
4 = sleep
5 = Investigate the liquid and stone basin 
- What do you do? >? 1
You wait for sometime.
Nothing happens.
Still, nothing happens.
You continue on your journey.
What do you do?
1 = Wait and do not move
2 = Investigate the pressure plates
3 = Investigate the plants
4 = sleep
5 = Investigate the liquid and stone basin 
- What do you do? >? 1
You wait for sometime.
You have encountered a goblin!
Goblin: "What are you doing in my swamp!"
You have no weapon!
You can only run!
You failed to run away!
The beast attacks!
>The goblin deals 3 damage.
> 
>Health: 100
>
-  ### *Not working as expected*
What do you do?
1 = Wait and do not move
2 = Investigate the pressure plates
3 = Investigate the plants
4 = sleep
5 = Investigate the liquid and stone basin 
- What do you do? >? 2
You approach the pressure plates.
Pressure plate 1: picture of a wolf.
Pressure plate 2: picture of a flower.
Pressure plate 3: picture of a ring with a blue ribbon.
- Which pressure plate do you choose? >? 2
You decide to stand on pressure plate 2
A loud grating noise explodes around the cave as you step on pressure plate 2
The ground below the pressure plate gives way and you fall into a pit
You're still falling!
You land in a lake.
You survived thanks to the golden ring you have!
You swim to the edge of the lake and notice a campfire with a wizard sitting beside it.
- Do you approach the wizard? >? y
You approach the wizard...
You sit down beside the campfire.
The wizards says, "I have been waiting for you."
"I'm sure you have many questions" says the wizard.
What do you ask the wizard?
1 = Where am I?
2 = Who are you?
3 = What's going on.
4 = I have no further questions.
- What do you ask the Wizard? >? 1
"You are in a dark cave."
"You're in the land of Lanzix."
"A land under the corruption of the Twelve."
What do you ask the wizard?
1 = Where am I?
2 = Who are you?
3 = What's going on.
4 = I have no further questions.
- What do you ask the Wizard? >? 2
"I am a wizard! Don't you remember me?"
"You have successfully completed your first task."
"That being, finding me."
"Your second task is to stop the killer that wonders these caves."
"He is one of the Twelve."
What do you ask the wizard?
1 = Where am I?
2 = Who are you?
3 = What's going on.
4 = I have no further questions.
- What do you ask the Wizard? >? 3
"Many things."
"You may have noticed that you have two choices from your starting position in time."
What do you ask the wizard?
1 = Where am I?
2 = Who are you?
3 = What's going on.
4 = I have no further questions.
- What do you ask the Wizard? >? 4
"I will send you back in time so that you may be able to complete your second task." Says the wizard
"Keep the ring close!"
> The killer hears you! He runs over to you!
Quickly, you prepare for battle
The Killer says: "Don't even try to escape!"
You take 590 damage.
Health: -493
>
- ## *Not working as expected*
New run start: 
What do you do? 

- Loop resets to the beginning of the game
- ## *Working as expected*

## Third Test Case

- What do you do? >? Run
You decide to Run
Suddenly two torches light up two opposite ends of the cave you're in.
You notice three pressure plates in addition to the two torches.
Many vines and plants cover the walls of the room you're in.
- Do you investigate the room further? >? n
The killer hears you! He rushes over to you!
Quickly, you prepare for battle
The Killer says: Die!
You take 760 damage.
Health: -660
New run start: 
What do you do? 

- Killer kills the player if they do not investigate the room
- ## *Working as expected*