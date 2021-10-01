





# 0.24
added the start of `learn_pick_pocket` quest chain, it's a bit obscure though
`make_a_copper_ring` can be finished now
added: `a_diamond_to_sell` quest line
Moved items and spells icons into the image folder to future proof the game in case we want to swap them with webp format (it is likely that this will happen to other images as well)
Abdul no longer holds unto `wine` in the `planted_evidence` quest
made fleeing a fight chancy, hard and dangerous, some fights are even harder to flee from
No more walking fleeing corps (can't cast spells after death)
you can add spells to the empty slots on your spell bar while in the middle of fight now
No more free experience after fights
can't be too generous with the beggar anymore
your health now regenerates when resting
your stamina and mana now regenerates out of combat

# 0.23
the `cash_in_hand` quest should be fixed now
minor improvement to the quest list
frequently used screens have their buttons on the top of interface
fixed the errors at the end of `to_do_list` quest, also the item change added
you will level up every 100 exp you gain
the combat text now differentiates between damage dealt and damage taken
the training dummy doesn't kill you anymore
managing the team and arranging the spells is a bit more coherent now
you gain experience for defeating enemies now
skipping the fights is an ability now
Fixed getting stuck after battling the training dummy
Migrated to renpy version 7.4.8


# 0.22
This month I couldn't keep track of all changes, the majority of changes where focused on the fighting system though.
A number of fights are added to the game to work as test cases, I'm still working on how to handle the amount of exp given by the enemies so there's no level-up yet, but the new fights yield loot now, basically you can take anything that the enemies had in their inventory.
A number of new locations and characters are added, you can continue Rasoul's quest chain to unlock the widow's house, it will become a new source of quests and fun soon.
You can nap

# 0.21
revamped how the fight system calculates attacks, it should be easier to vail on an enemy now, specially the defenseless ones
the training dummy cant "Parry", "Dodge" or "Block" anymore
fixed double layered images in characters causing alpha problem in semi transparent areas, and hopefully save some resources
removed some of unused code
removed some of the unused files
converted some of bigger images to webp format to reduce the size of the game
the night placeholders are added to the places that didn't have them
The inside places no longer get dark if there isn't any windows
save background for the lamp tour fixed
new CG
new characters (The virgin hunter, Ali)
new quest (stolen_spyglass)
new items (2 spyglasses)
new locations (caravanserai, vantage point)

# 0.20
the planted evidence quest is done and can be completed
Petros relocated to the poor section
We have a new jailer
added quest notification animations
some new items for future quests
fixed the return stack error (appearing in the middle of the screen)
The fights are back (not sure what caused the lags, I assume it was my computer)
you can see your quests inside the lamp now

# 0.19.1
Errors while pressing [F], [Q], [R], or [T] keys are fixed
The shine error fixed

# 0.19
beer delivery quest is done, now we have a fully functional quest system
the small bug with the shops is fixed
improvement in the bag system that was necessary for some of the future features
The start if Rasoul's arc is added
No more annoying bombardment of notifications "You've died of xx" either
Adjusted the food and hunger to the rule of 3's, it takes roughly 3 days without water to die, and a week without food
Bag options are visible by default now
Fishing minigame, no more free fish!

# 0.18
New characters (not available in the story line yet)
Added few temporary night version of the main locations
CG scenes are spiced up with some interactivity
The first animated CG is converted into live2D
Migrating to renpy version 7.4.4
Live2D integration for CG scenes
Live2D integration into the point and click system
Migrating to renpy version 7.4.3


# 0.17
Disabled clicking on things while speaking (this caused a small bug with shops that will b fixed later)
you can complete one quest with no rewards as a test (the rest will be added soon)
now you can return to the lamp
Added drinking from pounds and wheels
You can't eat the lamp, or non food items anymore
added a rudimentary day/night cycle
Migrating to renpy version 7.4.2

# 0.16
You can eat / drink
Hunger and thirst bars added
Migrating to renpy version 7.4.1
CG scenes are skipped one per click now, instead of all at once
You can sleep to pass time
Hunger and thirst are added
Collected resources can be regenerated over night depending on their chance to regen
Time keeping added