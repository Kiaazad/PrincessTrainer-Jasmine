# A Roc or Rukh is a very big bird that could lift elephants to the sky, probably an eagle that got embellished in the stories.
# https://en.wikipedia.org/wiki/Roc_(mythology)

default des_0_1 = pnco(
    "thorns",
    "bg/rock_pass/01.png",
    (188, 598),
    items = [[thorns, 1]],
    )
default des_0_2 = pnco(
    "thorns",
    "bg/rock_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    )
default des_0_3 = pnco(
    "thorns",
    "bg/rock_pass/03.png",
    (173, 842),
    items = [[thorns, 1]],
    tut = True,
    )
default des_0_4 = pnco(
    "thorns",
    "bg/rock_pass/04.png",
    (411, 729),
    items = [[thorns, 1]],
    tut = True,
    )
default des_0_5 = pnco(
    "thorns",
    "bg/rock_pass/05.png",
    (1222, 634),
    items = [[thorns, 1]],
    )
default des_0_6 = pnco(
    "thorns",
    "bg/rock_pass/06.png",
    (1658, 774),
    items = [[thorns, 1]],
    tut = True,
    )
default des_0_7 = pnco(
    "thorns",
    "bg/rock_pass/07.png",
    (632, 612),
    items = [[thorns, 1]],
    )

default empty_chest = item(
    _("Empty chest"),
    _("It's too beat up to keep stuff."),
    "items/wood.png",
    220,
    )
default des_0_chest = pnco(
    "Empty chest",
    "bg/rock_pass/chest.png",
    (1524, 744),
    items = [[empty_chest, 1]],
    )

default rusty_sword = item(
    _("Rusty sword"),
    _("Can it be restored?"),
    "items/wood.png",
    220,
    )
default des_0_sword = pnco(
    "Rusty sword",
    "bg/rock_pass/sword.png",
    (1399, 715),
    items = [[rusty_sword, 1]],
    )
default des_0_return = pnco(
    "Return",
    None,
    (300, 800),
    Jump('desert'),
    )
image des_0_shine:
    "bg/ev/shine.png"
    ease .3 zoom .1 rotate -20
    ease .3 zoom 1 rotate 20
    repeat

default des_0_col = pncs("Roc pass",
    [
        des_0_1,
        des_0_2,
        des_0_3,
        des_0_4,
        des_0_5,
        des_0_6,
        des_0_7,
        des_0_chest,
        des_0_sword,
    ],
    cond = [
        [[des_0_3, des_0_4, des_0_6], Jump("intro_0_1")]
    ]
    )
image bg rock_pass = "bg/rock_pass/bg.jpg"
label desert_0:
    scene 
    show bg rock_pass onlayer bg
    show screen pnc(abdul, des_0_col)
    with dissolve
    pause
    jump desert_0
