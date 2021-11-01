# A Roc or Rukh is a very big bird that could lift elephants to the sky, probably an eagle that got embellished in the stories.
# https://en.wikipedia.org/wiki/Roc_(mythology)

# Exists
default roc_pass_snakes_pass = pnco(
    "Snake's pass",
    None,
    (400, 500),
    Jump('snakes_pass'),
    hidden = True,
    )
default roc_pass_agrabahs_gate = pnco(
    "Agrabah's gate",
    None,
    (1343, 1002),
    Jump('agrabahs_gate'),
    hidden = True,
    )
default roc_pass_marble_quarry = pnco(
    "Marble quarry",
    None,
    (41, 805),
    Jump('marble_quarry'),
    hidden = True,
    )

# objects
default des_0_1 = pnco(
    "thorns",
    "bg/roc_pass/01.png",
    (188, 598),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_0_2 = pnco(
    "thorns",
    "bg/roc_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_0_3 = pnco(
    "thorns",
    "bg/roc_pass/03.png",
    (173, 842),
    items = [[thorns, 1]],
    tut = True,
    regen = 10,
    )
default des_0_4 = pnco(
    "thorns",
    "bg/roc_pass/04.png",
    (411, 729),
    items = [[thorns, 1]],
    tut = True,
    regen = 10,
    )
default des_0_5 = pnco(
    "thorns",
    "bg/roc_pass/05.png",
    (1222, 634),
    items = [[thorns, 1]],
    regen = 10,
    )
default des_0_6 = pnco(
    "thorns",
    "bg/roc_pass/06.png",
    (1658, 774),
    items = [[thorns, 1]],
    tut = True,
    regen = 10,
    )
default des_0_7 = pnco(
    "thorns",
    "bg/roc_pass/07.png",
    (632, 612),
    items = [[thorns, 1]],
    regen = 10,
    )

# Chest item
default empty_chest = item(
    _("Empty chest"),
    _("It's too beat up to keep stuff."),
    "empty_chest",
    220,
    )
default des_0_chest = pnco(
    "Empty chest",
    "bg/roc_pass/chest.png",
    (1524, 744),
    items = [[empty_chest, 1]],
    )

# Sword item
default rusty_sword = item(
    _("Rusty sword"),
    _("Can it be restored?"),
    "rusty_sword",
    220,
    )
default des_0_sword = pnco(
    "Rusty sword",
    "bg/roc_pass/sword.png",
    (1399, 715),
    items = [[rusty_sword, 1]],
    )

# Fights
default little_thief = unit(
    "Little thief",
    "char/foes/little_thief",
    lvl = 5,
    type = "Demon",
    items = [(small_sword, 2), (water, 1)],
    )
default roc_pass_little_thief = pnco(
    "Little thief",
    "bg/roc_pass/little_thief.png",
    (152 , 586),
    Jump('roc_pass_little_thief'),
    hidden = True,
    aggressive = True,
    )
label roc_pass_little_thief:
    call screen btl_scr(team([abdul]), team([little_thief]))
    jump roc_pass


# Lamp shine
image des_0_shine:
    "bg/roc_pass/Glimmer.png"
    ease .3 zoom .1 rotate -20
    ease .3 zoom 1 rotate 20
    repeat

default roc_pass_map = pncs("Roc pass",
    [
        roc_pass_marble_quarry,
        roc_pass_snakes_pass,
        roc_pass_agrabahs_gate,

        des_0_1,
        des_0_2,
        des_0_3,
        des_0_4,
        des_0_5,
        des_0_6,
        des_0_7,
        des_0_chest,
        des_0_sword,
        roc_pass_little_thief,
    ],
    cond = [
        [[des_0_3, des_0_4, des_0_6], Jump("intro_0_1")]
    ], night = "bg/roc_pass/night.webp"
    )
image bg roc_pass = "bg/roc_pass/bg.webp"
label roc_pass:
    scene 
    show bg roc_pass onlayer bg
    show screen pnc(abdul, roc_pass_map)
    with dissolve
    pause
    jump roc_pass
