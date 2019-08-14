init python:
    class item:
        def __init__(self, name, val, icon, inf = "", type = None):
            self.name = name
            self.val = val
            self.inf = inf
            self.icon = icon
            self.hov = False
            self.type = type


# ingredient
default thorns = item(
    "Camelthorns",
    10,
    "items/thorns.png",
    ""
    )

default wood = item(
    "Wood",
    40,
    "items/wood.png",
    ""
    )

default feather = item(
    "Feather",
    1,
    "items/feather.png",
    ""
    )

default stick = item(
    "Stick",
    1,
    "items/stick.png",
    ""
    )

default string = item(
    "String",
    1,
    "items/string.png",
    ""
    )

default arrowhead = item(
    "Arrowhead",
    5,
    "items/arrowhead.png",
    ""
    )

default sand_bottle = item(
    "A bottle on a rope",
    500,
    "items/sand_bottle.png",
    "Now let's go hang it in the lamp.",
    )

default bottle = item(
    "Empty bottle",
    400,
    "items/bottle.png",
    "There's so many uses for an empty bottle.",
    )

default rope = item(
    "Rope",
    90,
    "items/rope.png",
    "A good sturdy rope.",
    )

default cork = item(
    "Cork",
    10,
    "items/cork.png",
    "A normal cork.",
    )



# drugs
default beer = item(
    "Bread beer",
    70,
    "items/beer.png",
    "A home made bear, it is made from very stale and unedible bread."
    )

default liquor = item(
    "Doggy liquor",
    590,
    "items/liquor.png",
    "A very bitter moonshine made by distilling raisin's wine."
    )

default wine = item(
    "Red wine",
    550,
    "items/wine.png",
    "You can be arrested for having this."
    )

default opium = item(
    "Opium",
    200,
    "items/opium.png",
    "Using this drug causes constipation."
    )

default hashish = item(
    "Hashish",
    200,
    "items/opium.png",
    ""
    )

# food
default bread = item(
    "Naan bread",
    50,
    "items/bread.png"
    )

default water = item(
    "Water",
    10,
    "items/water.png",
    "Clean drinkable water from the qanat."
    )

default dates = item(
    "Dates",
    10,
    "items/dates.png",
    "Dried dates."
    )

default crackers = item(
    "Naan crackers",
    10,
    "items/crackers.png",
    "A dried small bread."
    )

default damp_crackers = item(
    "Damp naan crackers",
    10,
    "items/damp_crackers.png",
    "Crackers you kept in your pants."
    )

default salt = item(
    "Salt",
    10,
    "items/damp_crackers.png",
    "A soon of salt."
    )

default saffron = item(
    "Saffron",
    1000,
    "items/damp_crackers.png",
    "A very expensive spice that cause a happy feeling."
    )



# remedy
default snake_bite_remedy = item(
    "Snake bite remedy",
    200,
    "items/snake_bite_remedy.png",
    "Cures snake bite."
    )

default scorpion_bite_remedy = item(
    "Scorpion bite remedy",
    200,
    "items/scorpion_bite_remedy.png",
    "Cures scorpion bite."
    )


# Equipment
default abduls_sword = item(
    "Abdul's sword",
    2100,
    "items/abduls_sword.png",
    "A very normal sword."
    )

default small_sword = item(
    "Small sword",
    2100,
    "items/small_sword.png",
    "It's more like a dagger."
    )

default bracers_of_agility = item(
    "Bracers of agility",
    1200,
    "items/bracers_of_agility.png",
    "The vendor says: it Gives you 15 agility."
    )

default arrows = item(
    "Arrows",
    40,
    "items/arrows.png",
    "Normal looking arrows."
    )

default bow = item(
    "Bow",
    4200,
    "items/bow.png",
    "The vendor says: it Gives you 15 agility."
    )

# Books
default book1 = item(
    "Red book",
    3100,
    "items/book1.png",
    "It's a red book."
    )

default book2 = item(
    "Book of Err",
    5300,
    "items/book2.png",
    "The facetting tale of Err."
    )

default book3 = item(
    "Book of Eep",
    6500,
    "items/book3.png",
    "The most amazing book about Eep and it's miraculous effect."
    )

default book4 = item(
    "An old book",
    2200,
    "items/book4.png",
    "This book looks old."
    )

# sex
default coconut_oil = item(
    "Coconut  oil",
    942,
    "items/_frm.png",
    "There's no domain that can't be conquered with a bit of spit. But in the dry desert, Hakim's coconut  oil saves you from an embarrassing situation when you're too thirsty to spit."
    )

default nuru_gel = item(
    "Nuru gel",
    1956,
    "items/_frm.png",
    "From the far east, slippery, sticky, stringy lubrication. It's used in full body massage."
    )

# Other
default black_lamp = item(
    "Black lamp",
    2100,
    "items/bracers_of_agility.png",
    "An oil lamp used for illumination."
    )


# Tools
default axe = item(
    "Axe",
    1400,
    "items/bracers_of_agility.png",
    "A simple wood cutting axe.",
    type = "tools"
    )

default saw = item(
    "Saw",
    1600,
    "items/bracers_of_agility.png",
    "A single handle saw.",
    type = "tools"
    )
