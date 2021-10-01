# Weapons
default abduls_sword = item(
    _("Abdul's sword"),
    _("A very normal sword."),
    "abduls_sword",
    2100,
    ["Hand", "Weapon"],
    )

default small_sword = item(
    _("Small sword"),
    _("It's more like a dagger."),
    "small_sword",
    2100,
    ["Hand", "Weapon"],
    )

default bow = item(
    _("Bow"),
    _("The vendor says: it Gives you 15 agility."),
    "bow",
    4200,
    ["Hand", "Weapon"],
    )

default arrows = item(
    _("Arrows"),
    _("Normal looking arrows."),
    "arrows",
    40,
    ["Hand"],
    )

default list_of_weapons = [
    abduls_sword, small_sword, arrows, bow, arrows,
]

# Equipment
default bracers_of_agility = item(
    _("Bracers of agility"),
    _("The vendor says: it Gives you 15 agility."),
    "bracers_of_agility",
    1200,
    ["Wrist", "Armor"],
    )

default simple_hat = item(
    _("Hat"),
    _("A test hat with icon like bow."),
    "simple_hat",
    4200,
    ["Hat"],
    )

default left_sandal = item(
    _("Left sandal"),
    _("A pair of sandals, well the left one."),
    "left_sandal",
    4200,
    ["Left Foot"],
    )

default right_sandal = item(
    _("Right sandal"),
    _("A pair of sandals, well the right one."),
    "right_sandal",
    4200,
    ["Right Foot"],
    )

default simple_shirt = item(
    _("Simple shirt"),
    _("White shows you're clean."),
    "simple_shirt",
    4200,
    ["Top"],
    )

default simple_pants = item(
    _("Simple pants"),
    _("White and baggy, good for hot climate."),
    "simple_pants",
    4200,
    ["Bottom"],
    )

default list_of_equipments = [
    bracers_of_agility, simple_hat, left_sandal, right_sandal, simple_shirt, simple_pants, 
]

# Accessories
default silver_ring = item(
    _("Silver ring"),
    _("It has some value."),
    "silver_ring",
    4200,
    ["Finger", "jewelry"],
    )

default gold_ring = item(
    _("Gold ring"),
    _("A wedding ring if you wear it on your left ring finger."),
    "gold_ring",
    4200,
    ["Finger", "jewelry"],
    )

default prayer_beads = item(
    _("Prayer beads"),
    _("Hold this in your hand and show people you pray a whole lot."),
    "prayer_beads",
    4200,
    ["Neckless", "Hand", "Wrist"],
    )

default list_of_accessories = [
    silver_ring, gold_ring, prayer_beads, 
]

# Tools
default axe = item(
    _("Axe"),
    _("A simple wood cutting axe."),
    "axe",
    1400,
    ["tools", "weapon"],
    )

default saw = item(
    _("Saw"),
    _("A single handle saw."),
    "saw", ##
    1600,
    ["tools"],
    )

default list_of_tools = [
    axe, saw,
]


