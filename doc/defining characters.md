Defining a character can be as easy as a name and directory.

```
default abdul = unit(
    "Abdul", # Name
    "0001", # Asset directory
    )
```
Everything else is optional but for the seek of clarity here's a list:

### Name =  "Abdul"
The name of this character. Must be a string. this doesn't replace the character definition though, you still have to define a character `define me = Character("Abdul", color="#44f")` if you want your character to talk.

### dir = "char/abdul"
The directory that holds all of the assets related to this character, icon, images, fight animation, etc...
for this game, we keep the character assets inside `game/char` folder, to find them easier we try to keep the character name the same as the instance name name: `"char/abdul"`

## inventory
### cash = 0
The amount of money this character is carrying, if killed, all of the cash is lootable.


### items = []
A list of items that this character possess, these items can be bought or looted.
the items need to be a list of stacks:

```
    items = [
        stack(wood, 20),
        stack(snake_bite_remedy, 2),
        stack(scorpion_bite_remedy, 5),
        stack(small_sword, 1),
        stack(bow, 1),
        ]
```
A stack requires the item instance name and the number of items in that stack.

### mup = 1.1
The markup price the vendor sells at, in this case the vendor sells everything at 110 percent of the base item value.


## Fight
### lvl = 1
The starting level of this character.

### type = "Peasant"
The character's archetype, it effects how the points for this character are spent and which stats of this character are reinforced.

## The big example
Now let's make a shop keeper named "Akbar" and give him some items to sell.

```
default akbar = unit(
    "Akbar",
    "char/akbar",

    210,
    [
        stack(wood, 20),
        stack(snake_bite_remedy, 2),
        stack(scorpion_bite_remedy, 5),
        stack(small_sword, 1),
        stack(bow, 1),
        stack(book1, 1),
        stack(book4, 1),
        stack(book2, 1),
        stack(book3, 1),
        stack(arrows, 6),
    ],
    1.1,

    8,
    "Peasant",
    )
```

As you might have noticed, there is no indicator if "Akbar" is friendly or enemy. That's because everybody in the game starts as neutral but they have the capability to fight if necessary. for example if you try to steal something from him and he notices, he will cut your hand off, or at least try to.

it would be a good practice to specify your inputs:

```
default akbar = unit(
    "Akbar",
    "char/akbar",

    cash = 210,
    items = [
        stack(wood, 20),
        stack(snake_bite_remedy, 2),
        stack(scorpion_bite_remedy, 5),
        stack(small_sword, 1),
        stack(bow, 1),
        stack(book1, 1),
        stack(book4, 1),
        stack(book2, 1),
        stack(book3, 1),
        stack(arrows, 6),
    ],
    mup = 1.1,

    lvl = 8,
    type = "Peasant",
    )
```
it makes it more readable and prevents accidental miss assignment, plus in some cases you don't need to enter everything ad skipping some inputs would be a time saver:

```
default dog = unit(
    "Wild Dog",
    "char/dog",

    lvl = 1,
    type = "Beast",
    )
```
