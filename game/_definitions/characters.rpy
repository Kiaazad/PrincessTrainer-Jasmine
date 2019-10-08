﻿default abdul = unit(
    name = "Abdul", # Name
    dir = "char/abdul", # Asset directory

    # Inventory
    cash = 40, # Cash ##(optional - default is: 0)
    items = [], # A list of items in (item, quantity) format [(wood, 20), (bow, 1), etc...] ##(optional - default is: Empty list)
    markup = 1, # Price markup ##(optional - default is: 1)

    # fight
    lvl = 1, # Level ##(optional - default is: 1)
    type = "Peasant", # Archetype ##(optional - default is: Peasant)
    )

default jafar = unit(
    "Jafar",
    "char/jafar",

    lvl = 650,
    type = "Wizard"
    )
default harem_girl_1 = unit(
    "Harem Girl",
    "char/harem_girl_1",

    lvl = 2,
    type = "Dancer"
    )
default jasmine = unit(
    "Jasmine",
    "char/jasmine",

    lvl = 3,
    type = "Princess"
    )
default snake = unit(
    "Snake",
    "char/snake",

    lvl = 2,
    type = "Beast"
    )


default akbar = unit(
    "Akbar",
    "char/akbar",

    210,
    [
        (wood, 20),
        (snake_bite_remedy, 2),
        (scorpion_bite_remedy, 5),
        (small_sword, 1),
        (bow, 1),
        (book1, 1),
        (book4, 1),
        (book2, 1),
        (book3, 1),
        (arrows, 6),
    ],
    1.1,

    8,
    "Peasant",
    )

# -------- teams
default snake_dancer = unit(
    "Snake",
    "char/snake",

    lvl = 2,
    type = "Dancer"
    )


