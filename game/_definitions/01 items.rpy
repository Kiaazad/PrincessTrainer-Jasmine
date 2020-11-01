# Ingredient
default thorns = item(
    name = _("Tumbleweed"),         # Name
    inf = _("A round-shaped plant that are wrapped by dead plants."), #Descriptions optional
    icon = "items/thorns.png",      # Icon [optional]
    val = 10,                       # Value [optional] [Default = 0]
    tags = ["fuel"],                      # tags [optional] [default = empty list]
    use_event = None,               # Event happening when used [optional] [default = None]
    )

default wood = item(
    _("Wood"),
    _("A piece of wood that can be used to make fire."),
    "items/wood.png",
    40,
    ["fuel"],
    )

default coal = item(
    _("Coal"),
    _("A lump of coal."),
    "items/wood.png", ##
    100,
    ["fuel"],
    )

default feather = item(
    _("Feather"),
    _("You can tickle someobody's feet with it."),
    "items/feather.png",
    1,
    )

default stick = item(
    _("Stick"),
    _("Behold the mighty stick! You can whack someone or you can STICK it in a hole somewhere!"),
    "items/stick.png",
    1,
    ["fuel"],
    )

default string = item(
    _("String"),
    _("Not as strong as the rope, but it's useful for something else."),
    "items/string.png",
    1,
    )

default arrowhead = item(
    _("Arrowhead"),
    _("A sharp tip of an arrow. Not sure what else is used for."),
    "items/arrowhead.png",
    5,
    )

default bottle = item(
    _("Empty bottle"),
    _("There's so many uses for an empty bottle. It can help with my private business and etc."),
    "items/bottle.png",
    400,
    )

default rope = item(
    _("Rope"),
    _("A good sturdy rope. Can be use for varies of things such as tying people up."),
    "items/rope.png",
    90,
    )

default cork = item(
    _("Cork"),
    _("A normal cork... Why don't you put a cork in it!"),
    "items/cork.png",
    10,
    )

default list_of_ingredients = [
    thorns, wood, feather, stick, string, arrowhead, bottle, rope, cork,
]


# Books
default book1 = item(
    _("Red book"),
    _("It's a red book. I'm sure it's one of Jafar's works."),
    "items/book1.png",
    3100,
    ["book"],
    )

default book2 = item(
    _("Book of Err"),
    _("The facetting tale of Err. It's about an errrr man that went errrr."),
    "items/book2.png",
    5300,
    ["book"],
    )

default book3 = item(
    _("Gold covered book"),
    _("It seems to be written in code."),
    "items/book3.png",
    9500,
    ["book"],
    )

default book4 = item(
    _("An old book"),
    _("This book looks old. The cover the worn out and the papers are completely brown"),
    "items/book4.png",
    2200,
    ["book"],
    )

default list_of_books = [
    book1, book2, book3, book4,
]


# sex
default coconut_oil = item(
    _("Coconut  oil"),
    _("There's no domain that can't be conquered with a bit of spit. But in the dry desert, Hakim's coconut  oil saves you from an embarrassing situation when you're too thirsty to spit."),
    "items/_frm.png",
    942,
    )

default nuru_gel = item(
    _("Nuru gel"),
    _("From the far east, slippery, sticky, stringy lubrication. It's used in full body massage."),
    "items/_frm.png",
    1956,
    )

default list_of_sex_items = [
    coconut_oil, nuru_gel, 
]

# Lamp
default black_lamp = item(
    _("Black lamp"),
    _("An oil lamp used for illumination."),
    "items/black_lamp.png",
    2100,
    ["magic", "lamp"],
    )

default sand_bottle = item(
    _("A bottle on a rope"),
    _("Now let's go hang it in the lamp."),
    "items/sand_bottle.png",
    500,
    ["magic", "junk"],
    )

default magic_ring = item(
    _("Magic ring"),
    _("A ring with a Genie engraved on it."),
    "items/sand_bottle.png",
    500,
    ["magic"],
    )

default list_of_lamp_items = [
    black_lamp, sand_bottle, magic_ring,
]
