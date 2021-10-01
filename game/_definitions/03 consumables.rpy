

# drugs
default beer = item(
    _("Bread beer"),
    _("A home made bear, it is made from very stale and unedible bread."),
    "beer",
    70,
    ["drug", "drink"],

    food = 3,
    water = 45,
    )
default beer_keg = item(
    _("Beer keg"),
    _("A keg of beer containing around 40 pints of beer."),
    "beer_keg",
    2400,
    ["drug"],

    )

default liquor = item(
    _("Doggy liquor"),
    _("A very bitter moonshine made by distilling raisin's wine."),
    "liquor",
    1590,
    ["drug", "drink"],
    water = 10,
    )

default wine = item(
    _("Red wine"),
    _("You can be arrested for having this."),
    "wine",
    550,
    ["drug", "drink"],
    food = 4,
    water = 45,
    )

default opium = item(
    _("Opium"),
    _("Using this drug causes constipation."),
    "opium",
    200,
    ["drug", "hard drug"],
    )

default hashish = item(
    _("Hashish"),
    _("Good for smoking pipes. Careful not to get attached to this."),
    "hashish",
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
    "rice",
    75,
    ["food", "raw"],
    food = 50,
    water = -60,
    )

default bread = item(
    _("Naan bread"),
    _("Almost fresh flat bread."),
    "bread",
    50,
    ["food"],
    food = 140,
    )

default water = item(
    _("Water"),
    _("Clean drinkable water from the qanat."),
    "water",
    10,
    ["food"],
    water = 180,
    )

default crackers = item(
    _("Naan crackers"),
    _("A dried small bread."),
    "crackers",
    10,
    ["food"],
    food = 65,
    water = -5,
    )

default damp_crackers = item(
    _("Damp naan crackers"),
    _("Crackers you kept in your pants."),
    "damp_crackers",
    10,
    ["food"],
    food = 65,
    water = 5,
    )

default salt = item(
    _("Salt"),
    _("A spoon of salt."),
    "salt",
    10,
    ["food"],
    water = -100,
    )

default saffron = item(
    _("Saffron"),
    _("A very expensive spice that cause a happy feeling."),
    "saffron",
    1000,
    ["food"],
    food = 2,
    water = -5,
    )

default fish = item(
    _("Fish"),
    _("An ordinary fish."),
    "fish_med",
    250,
    ["food", "raw"],
    food = 120,
    water = 30,
    )

default small_fish = item(
    _("Small fish"),
    _("A small one."),
    "fish_small",
    50,
    ["food", "raw"],
    food = 50,
    water = 10,
    )

default big_fish = item(
    _("Big fish"),
    _("The big one."),
    "fish_big",
    350,
    ["food", "raw"],
    food = 160,
    water = 40,
    )


# Fruits
default dates = item(
    _("Dates"),
    _("Dried dates."),
    "dates",
    10,
    ["food"],
    food = 115,
    water = -10,
    )

default cantaloupe = item(
    _("Cantaloupe"),
    _("Not enough for a breakfast, specially half of it."),
    "cantaloupe",
    80,
    ["food"],
    food = 40,
    water = 100,
    )

default watermelon = item(
    _("Watermelon"),
    _("A sweet sensational taste."),
    "watermelon",
    90,
    ["food"],
    food = 30,
    water = 150,
    )

default pomegranate = item(
    _("Pomegranate"),
    _("n/a."),
    "pomegranate",
    30,
    ["food"],
    food = 22,
    water = 42,
    )

default apple = item(
    _("Apple"),
    _("n/a."),
    "apple",
    40,
    ["food"],
    food = 41,
    water = 45,
    )

default list_of_foods = [
    bread, water, dates, cantaloupe, watermelon, pomegranate, apple, crackers, damp_crackers, salt, saffron,
]

# remedy
default snake_bite_remedy = item(
    _("Snake bite remedy"),
    _("Cures snake bite."),
    "snake_bite_remedy",
    200,
    ["remedy", "bottled"],
    )

default scorpion_bite_remedy = item(
    _("Scorpion bite remedy"),
    _("Cures scorpion bite."),
    "scorpion_bite_remedy",
    200,
    ["remedy", "bottled"],
    )

default list_of_remedies = [
    snake_bite_remedy, scorpion_bite_remedy,
]

# Remedy ingredients
default scorpion_tail = item(
    _("Scorpion's tail"),
    _("The pointy end of scorpion."),
    "scorpion_tail",
    100,
    ["remedy"],
    )

default dead_snake = item(
    _("Dead snake"),
    _("It's dead."),
    "dead_snake",
    100,
    ["remedy"],
    )


