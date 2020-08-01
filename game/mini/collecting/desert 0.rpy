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
default des_0_chest = pnco(
    "Empty chest",
    "bg/rock_pass/chest.png",
    (1524, 744),
    items = [[thorns, 1]],
    )
default des_0_sword = pnco(
    "Rusty sword",
    "bg/rock_pass/sword.png",
    (1399, 715),
    items = [[thorns, 1]],
    )

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

label desert_0:
    scene black
    show bg rock_pass
    show screen pnc(abdul, des_0_col)
    with dissolve
    pause
    return
