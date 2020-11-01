

# drugs
default beer = item(
    _("Bread beer"),
    _("A home made bear, it is made from very stale and unedible bread."),
    "items/beer.png",
    70,
    ["drug", "drink"],
    )

default liquor = item(
    _("Doggy liquor"),
    _("A very bitter moonshine made by distilling raisin's wine."),
    "items/liquor.png",
    1590,
    ["drug", "drink"],
    )

default wine = item(
    _("Red wine"),
    _("You can be arrested for having this."),
    "items/wine.png",
    550,
    ["drug", "drink"],
    )

default opium = item(
    _("Opium"),
    _("Using this drug causes constipation."),
    "items/opium.png",
    200,
    ["drug", "hard drug"],
    )

default hashish = item(
    _("Hashish"),
    _("Good for smoking pipes. Careful not to get attached to this."),
    "items/opium.png",
    200,
    ["drug"],
    )

default list_of_drugs = [
    beer, liquor, wine, opium, hashish,
]


# food
default rice = item(
    _("White rice"),
    _("Can you cook rice the right way?."),
    "items/bread.png",
    75,
    ["food", "raw"],
    )

default bread = item(
    _("Naan bread"),
    _("Almost fresh flat bread."),
    "items/bread.png",
    50,
    ["food"],
    )

default water = item(
    _("Water"),
    _("Clean drinkable water from the qanat."),
    "items/water.png",
    10,
    ["food"],
    )

default crackers = item(
    _("Naan crackers"),
    _("A dried small bread."),
    "items/crackers.png",
    10,
    ["food"],
    )

default damp_crackers = item(
    _("Damp naan crackers"),
    _("Crackers you kept in your pants."),
    "items/damp_crackers.png",
    10,
    ["food"],
    )

default salt = item(
    _("Salt"),
    _("A spoon of salt."),
    "items/damp_crackers.png",
    10,
    ["food"],
    )

default saffron = item(
    _("Saffron"),
    _("A very expensive spice that cause a happy feeling."),
    "items/damp_crackers.png",
    1000,
    ["food"],
    )

# Fruits
default dates = item(
    _("Dates"),
    _("Dried dates."),
    "items/dates.png",
    10,
    ["food"],
    )

default cantaloupe = item(
    _("Cantaloupe"),
    _("Not enough for a breakfast, specially half of it."),
    "items/dates.png",
    80,
    ["food"],
    )

default watermelon = item(
    _("Watermelon"),
    _("A sweet sensational taste."),
    "items/dates.png",
    90,
    ["food"],
    )

default pomegranate = item(
    _("Pomegranate"),
    _("n/a."),
    "items/dates.png",
    30,
    ["food"],
    )

default apple = item(
    _("Apple"),
    _("n/a."),
    "items/dates.png",
    40,
    ["food"],
    )

default list_of_foods = [
    bread, water, dates, cantaloupe, watermelon, pomegranate, apple, crackers, damp_crackers, salt, saffron,
]

# remedy
default snake_bite_remedy = item(
    _("Snake bite remedy"),
    _("Cures snake bite."),
    "items/snake_bite_remedy.png",
    200,
    ["remedy", "bottled"],
    )

default scorpion_bite_remedy = item(
    _("Scorpion bite remedy"),
    _("Cures scorpion bite."),
    "items/scorpion_bite_remedy.png",
    200,
    ["remedy", "bottled"],
    )

default list_of_remedies = [
    snake_bite_remedy, scorpion_bite_remedy,
]

