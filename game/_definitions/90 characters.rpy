﻿default abdul = unit(
    name = "Abdul", # Name
    dir = "char/abdul", # Asset directory

    # Inventory
    cash = 40, # Cash ##(optional - default is: 0)
    items = [], # A list of items in (item, quantity) format [(wood, 20), (bow, 1), etc...] ##(optional - default is: Empty list)
    markup = 1, # Price markup ##(optional - default is: 1)

    # fight
    lvl = 2, # Level ##(optional - default is: 1)
    type = "Peasant", # Archetype ##(optional - default is: Peasant)
    )
default hero = abdul # Set our hero to someone
default halia = unit(
    "Halia",
    "char/halia",
    lvl = 2,
    type = "Dancer"
    )
default training_dummy = unit(
    "Training dummy",
    "char/foes/training_dummy",
    lvl = 1,
    type = "Dummy",
    cant = ["Parry", "Dodge", "Block"]
    )
default rasoul = unit(
    "Rasoul",
    "char/rasoul",
    lvl = 24,
    type = "Warrior"
    )

default jafar = unit(
    "Jafar",
    "char/jafar",
    lvl = 650,
    type = "Wizard"
    )
default jasmine = unit(
    "Jasmine",
    "char/jasmine",
    lvl = 3,
    type = "Princess"
    )



default snake_dancer = unit(
    "Snake",
    "char/snake",

    lvl = 100,
    type = "Dancer"
    )

default snake_dancing_girl_1 = unit(
    "Snake Dancer",
    "char/snake_dancing_girl_1",

    lvl = 8,
    type = "Dancer"
    )

default scorpion_mistress = unit(
    "Snake Dancer",
    "char/scorpion_mistress",

    lvl = 2,
    type = "Dancer"
    )

default orphans_and_monkeys = unit(
    "Orphan",
    "char/orphans_and_monkeys",

    lvl = 2,
    type = "Peasant"
    )



default warrior_man = unit(
    "Desert warrior",
    "char/warrior_man",

    lvl = 12,
    type = "Warrior"
    )

default warrior_woman = unit(
    "Desert warrior",
    "char/warrior_woman",

    lvl = 11,
    type = "Warrior"
    )

default undead_guard = unit(
    "Ancient undead guard",
    "char/undead_guard",

    lvl = 18,
    type = "Warrior"
    )

















