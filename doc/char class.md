Defining a character can be as easy as a name and directory.

```
default abdul = unit(
    "Abdul", # Name
    "0001", # Asset directory
    )
```
Everything else is optional but for the seek of clarity here's a list:

## inventory
### cash = 0
The amount of money this character is carrying, if killed, all of the cash is lootable.


### items = []
A list of items that this character possess, these items can be bought or looted.
the items need to be a list of stacks:

```
    items = [stack(wood, 20),
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


