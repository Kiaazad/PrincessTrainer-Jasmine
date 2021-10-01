# Ingredient
default thorns = item(
    name = _("Tumbleweed"),         # Name
    inf = _("A round-shaped plant that are wrapped by dead plants."), #Descriptions optional
    icon = "thorns",      # Icon [optional]
    val = 10,                       # Value [optional] [Default = 0]
    tags = ["fuel"],                      # tags [optional] [default = empty list]
    use_event = None,               # Event happening when used [optional] [default = None]
    )

default wood = item(
    _("Wood"),
    _("A piece of wood that can be used to make fire."),
    "wood",
    40,
    ["fuel"],
    )

default coal = item(
    _("Coal"),
    _("A lump of coal."),
    "coal", ##
    100,
    ["fuel"],
    )

default feather = item(
    _("Feather"),
    _("You can tickle someobody's feet with it."),
    "feather",
    1,
    )

default stick = item(
    _("Stick"),
    _("Behold the mighty stick! You can whack someone or you can STICK it in a hole somewhere!"),
    "stick",
    1,
    ["fuel"],
    )

default string = item(
    _("String"),
    _("Not as strong as the rope, but it's useful for something else."),
    "string",
    1,
    )

default arrowhead = item(
    _("Arrowhead"),
    _("A sharp tip of an arrow. Not sure what else is used for."),
    "arrowhead",
    5,
    )

default bottle = item(
    _("Empty bottle"),
    _("There's so many uses for an empty bottle. It can help with my private business and etc."),
    "bottle",
    400,
    )

default rope = item(
    _("Rope"),
    _("A good sturdy rope. Can be use for varies of things such as tying people up."),
    "rope",
    90,
    )

default cork = item(
    _("Cork"),
    _("A normal cork... Why don't you put a cork in it!"),
    "cork",
    10,
    )

default fish_spirit = item(
    _("Spirit fish"),
    _("Amazing astral creature. A rare trophy for the luckiest fishermen."),
    "fish_spirit",
    5000,
    )
default quartz_bit = item(
    _("White gem stone"),
    _("Is it a diamond?."),
    "quartz_bit",
    0,
    )
default big_quartz = item(
    _("White gem stone"),
    _("Is it a diamond?."),
    "big_quartz",
    800,
    )
default list_of_ingredients = [
    thorns, wood, feather, stick, string, arrowhead, bottle, rope, cork, fish_spirit,
]


# Books
# default book1 = item(
#     _("Red book"),
#     _("It's a red book. I'm sure it's one of Jafar's works."),
#     "book1",
#     3100,
#     ["Book"],
#     )

default book2 = item(
    _("Book of Err"),
    _("The facetting tale of Err. It's about an errrr man that went errrr."),
    "book2",
    5300,
    ["Book"],
    )

default book3 = item(
    _("Gold covered book"),
    _("It seems to be written in code."),
    "book3",
    9500,
    ["Book"],
    )

default book4 = item(
    _("An old book"),
    _("This book looks old. The cover the worn out and the papers are completely brown"),
    "book4",
    2200,
    ["Book"],
    )

default list_of_books = [
    book2, book3, book4,
]


# sex
default coconut_oil = item(
    _("Coconut  oil"),
    _("There's no domain that can't be conquered with a bit of spit. But in the dry desert, Hakim's coconut  oil saves you from an embarrassing situation when you're too thirsty to spit."),
    "coconut_oil",
    942,
    )

default nuru_gel = item(
    _("Nuru gel"),
    _("From the far east, slippery, sticky, stringy lubrication. It's used in full body massage."),
    "nuru_gel",
    1956,
    )

default list_of_sex_items = [
    coconut_oil, nuru_gel, 
]

# Lamp
default black_lamp = item(
    _("Black lamp"),
    _("An oil lamp used for illumination."),
    "black_lamp",
    2100,
    ["magic", "lamp"],
    )

default sand_bottle = item(
    _("A bottle on a rope"),
    _("Now let's go hang it in the lamp."),
    "sand_bottle",
    500,
    ["magic", "junk"],
    )

default magic_ring = item(
    _("Magic ring"),
    _("A ring with a Genie engraved on it."),
    "magic_ring",
    500,
    ["magic"],
    )

default list_of_lamp_items = [
    black_lamp, sand_bottle, magic_ring,
]
