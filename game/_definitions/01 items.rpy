# Ingredient
default thorns = item(
    name = _("Tumbleweed"),         # Name
    inf = _(""),                    # Description [optional]
    icon = "items/thorns.png",      # Icon [optional]
    val = 10,                       # Value [optional] [Default = 0]
    type = None,                    # Type [optional] [default = None]
    use_event = None,               # Event happening when used [optional] [default = None]
    )

default wood = item(
    _("Wood"),
    _(""),
    "items/wood.png",
    40,
    )

default feather = item(
    _("Feather"),
    _(""),
    "items/feather.png",
    1,
    )

default stick = item(
    _("Stick"),
    _("Behold the mighty stick!"),
    "items/stick.png",
    1,
    )

default string = item(
    _("String"),
    _(""),
    "items/string.png",
    1,
    )

default arrowhead = item(
    _("Arrowhead"),
    _(""),
    "items/arrowhead.png",
    5,
    )

default bottle = item(
    _("Empty bottle"),
    _("There's so many uses for an empty bottle."),
    "items/bottle.png",
    400,
    )

default rope = item(
    _("Rope"),
    _("A good sturdy rope."),
    "items/rope.png",
    90,
    )

default cork = item(
    _("Cork"),
    _("A normal cork."),
    "items/cork.png",
    10,
    )

default list_of_ingredients = [
    thorns, wood, feather, stick, string, arrowhead, bottle, rope, cork,
]


# Books
default book1 = item(
    _("Red book"),
    _("It's a red book."),
    "items/book1.png",
    3100,
    )

default book2 = item(
    _("Book of Err"),
    _("The facetting tale of Err."),
    "items/book2.png",
    5300,
    )

default book3 = item(
    _("Book of Eep"),
    _("The most amazing book about Eep and it's miraculous effect."),
    "items/book3.png",
    6500,
    )

default book4 = item(
    _("An old book"),
    _("This book looks old."),
    "items/book4.png",
    2200,
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
    "items/bracers_of_agility.png",
    2100,
    )

default sand_bottle = item(
    _("A bottle on a rope"),
    _("Now let's go hang it in the lamp."),
    "items/sand_bottle.png",
    500,
    )

default magic_ring = item(
    _("Magic ring"),
    _("A ring with a Genie in it."),
    "items/sand_bottle.png",
    500,
    )

default list_of_lamp_items = [
    black_lamp, sand_bottle, magic_ring,
]