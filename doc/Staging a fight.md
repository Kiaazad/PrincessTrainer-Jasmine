# How to stage a fight


## Fighters
The first things you will need are two or more units to fight, you can create units inside `game/_definitions/100 characters.rpy` file. Follow the examples and comments in the same file.

## Spells and skills
For the newly created characters, you need to give them some moves or spells to use in the fight, I will add a method to give those newly created characters a set of skills based on their archetype and level, but for now here's how you add spells to your characters skill list.
```python
$ abdul.gotskill(kick)
```
To see a list or create your own skills check: `game/_definitions/` directory inside `10 effects.rpy, 11 spells.rpy and 12 skills.rpy` files.

## Teams
You need to add your characters to two teams to fight against each other before calling the fight screen, you can do it in two ways:
### permanent teams
The data of these teams are kept and they can be used in multiple fights. You can define these teams inside `game/_definitions/101 teams.rpy.rpy` file. and pass them to the battle screen.
```python
show screen btl_scr(me_team, en_team)
```
### Temporary teams
You can also create teams on the fly.
```python
show screen btl_scr(team([abdul]), team([snake, orphan])
```

## Managing the teams
Right now there's no method to add the spells into the the fighters fast action bar, I will write one since the enemies would need them, but till then, the player can use the team manager screen to manage the team members and their spell list. There will be a button to open the team manager inside the fight screen, and sending a team into a fight without this step can be a gimmick of sending people to fight unprepared, they have to manage their skill set while being attacked.

## WIP
The fight system is still in early development, the name of methods, attributes and screens can change as they are improved.


