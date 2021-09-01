# Known issues:
Lamp Tour Menu:
- Nothing is labeled.
- The Jar Room is closed.
- The Menu Room is closed.
- The Setting Room is closed.

- The “Cash in Hand” quest turn in is bugged. When you reload a save, other than the first auto one, you can no longer turn in the quest to Jafar.
>> the qlog.has returns False after a load.

"Thanks. It was so dark that I couldn't see where to click to go back to the tower! Admittedly my eyesight isn't very good."
>> we need ease of access options

- The Barracks’ guard is hard to see/can’t be seen at night.  When he is no longer a shadow, he might be easier to see.
>>> the darkness at night is intentional but the severity of this issue will be reduced with the finalized art and L2D models

- The duel wielding sword woman can be seen and even clicked on at the start of the game, before you even find the lamp.  Should she be hidden until a return visit?
>> all enemies will be scheduled soon, though rubbing the lamp should not effect how dangerous the desert is.

- Scorpion opponent doesn’t do any damage.  Mana/the blue bar goes down, even into the negatives, during the fight.  Left in from combat testing?
>>> sometimes the beast archetype will cast growl spell too many times, it will be fixed once we balance the spells and fights


# Explained:
- You can miss getting the quest “Books for Jafar” if you decided to view the lamp on your own. Is there another way to start the quest?
>> Missing quests are intentional

- “Books for School” and “Planted Evidence” don’t show up under the [Filter: All] tab in the quest log.
>> The list can be dragged up

What’s the difference between a “Finished” quest and a “Completed” quest?
>> A finished quest is delivered and done

Combat:
- Does the [Add] button do anything while in the manage settings?
>> It's for adding more fighters to the team if you have any

- How many attacks are supposed to be on the combat toolbar at the start? Without a sword, two show up automatically, “Punch” and “Kick”. With a sword, only “Punch” shows up automatically.
>> Depends on the level and it's somehow random

- Sleazy Ahmad, isn’t always in the Poor Section. He seems to vanish from time to time, and you can’t click on him/talk to him.
>> It's the result of shifts system, the characters can go to eat, sleep or travel and wouldn't always be there

- The way to exit menus is inconsistent. Sometimes you click the button on the right, sometimes it’s on the left. The same issues extends to the Bazaar location, instead of exiting by clicking down, you exit the street by clicking up.
>> The placement of buttons differs for each location since they lead into each other and there's multiple ways to exit

- When speaking to Soodeh her name is not displayed when she speaks.  Instead, “???” show up where her name should be.  It seems to happen when you shut down the game completely and then reload a save where you already spoke to/met her.
>> Her name being unknown at first is intentional, I will look at the problem after loading if it pops up again

Quest Planted Evidence:
- Rasoul can throw you in jail forever if you ask for your money back.  A game over screen/an option to restart/or a way to get out would be nice.
>>> rotting in the jail is always a possibility, the players should be careful what they choose and what they do

- I’ve always wondered about the "2" on the days passed display.  I finally found out what it means.  It’s an indicator for how fast or slow time is set to pass in game.  You can increase or decrease how fast time goes by clicking right or left of it.  Did you mean to leave it in the game?
>>> it is a test feature but it's highly possible to leave it in the game as a feature





# Can't duplicate
- Your mouse pointer can vanish if you tab out while in combat. To make it reappear you have to move it around and try to click on a button or combat toolbar.
>> it is possible that the mouse pointer disappears because of inactivity,in that case it's an engine thing andd happens anywhere in the game


