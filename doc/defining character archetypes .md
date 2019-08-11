An archetype or combat class is a list of percentages specifying what stat the character's points should be spent on.
A Wizard invests heavily into mana and power while a Guard invests in health and agility.

the format is: "Name": [health, mana, stamina, power, agility] and they go in the "arcDic" dictionary.

```python
define arcDic = {
    "Peasant": [30, 35, 65, 80, 95],
    "Wizard": [14, 54, 62, 90, 100],
    "Dancer": [21, 28, 63, 73, 100],
    "Princess": [14, 21, 33, 49, 64],
    "Beast": [28, 29, 38, 67, 73],
}
```

You, might have noticed that those percentages add up to something lots more than a hundred. The reason is: each one of them is a position on the line from zero to a hundred.
For example a peasant have:
            30 percent chance to gain health
30 to 35 =  5 percent chance to gain mana
35 to 65 =  30 percent chance to gain stamina
65 to 80 =  15 percent to gain attack
80 to 95 =  15 percent to gain agility
            and since they end at 95 percent there is 5 percent chance left for wasted potential

The logic behind the numbers is: a peasant does lots of manual labor and that improves their stamina and their health.

### Tools:
Since only programmers enjoy tweaking numbers, I wrote the archetype generator tool to help us generate different types (classes) of characters in a visual way,
See the video here: https://www.youtube.com/watch?v=LWMm5YgXXC0

If you’re interested in participating in character generation, you can download this tool here:
PC: https://drive.google.com/open?id=12vS0h6t5WXUGVSaKsxpc_yHF8um6h1Yd
Mac: https://drive.google.com/open?id=1ELSCX6IuQ5mYdv5aRHqtJp9jhXpZnCbi

The way it works is: you can tweak the amount of chance for each point to go to a stat, give it a name and copy it to paste in the comments.
It would help to explain the reasons why this class should be in the game and why the point distribution should be like that for that class but not necessary. I’ll take whatever you give. Just keep in mind that there’s a limited number of classes we can put in the game and your suggestion might have a slim chance to make the cut.

This tool will be included in the later demos of the game.