# Leveling and Experience
To level up our character we need to know what level it is and how much experience it needs to reach the next level. There are many ways to calculate experience curve, but for this game we're making it simple for the players.

Instead of raising the experience requirement per level, each unit requires 1000 experience points to reach the next level.

To discourage the players from grinding weaker enemies, the enemies that are lower level than the player yield less XP when killed/defeated and to encourage the players the enemies that are a higher level yield more XP. Here's an initial calculation (subject to change at a later time).

-5 levels or lower:     1xp
-4 levels:              2xp
-3 levels:              4xp
-2 levels:              8xp
-1 level:               12xp
same level:             16xp
+1 level:               20xp
+2 levels:              24xp
+3 levels:              32xp
+4 levels:              40xp
+5 levels or more:      48xp

The highest level in the party would be considered the current level (subject to change).

### Learning points
With each level-up, the unit is rewarded learning points that can be spent on stats or learning a new skill.

### Level cap
There will be no level cap, the player can level-up units to any level desired but the learning points rewarded per level are on a decaying curve and after some level each level only rewards one learning point.