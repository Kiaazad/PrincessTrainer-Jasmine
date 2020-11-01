default ruins_0 = pnco(
    "thorns",
    "bg/rock_pass/01.png",
    (188, 598),
    items = [[thorns, 1]],
    )
default ruins_1 = pnco(
    "thorns",
    "bg/rock_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    )
default ruins_2 = pnco(
    "thorns",
    "bg/rock_pass/03.png",
    (173, 842),
    items = [[thorns, 1]],
    )
default ruins_3 = pnco(
    "thorns",
    "bg/rock_pass/04.png",
    (411, 729),
    items = [[thorns, 1]],
    )
default ruins_back = pnco(
    "Back",
    None,
    (611, 729),
    Jump('desert'),
    )
# items


default ruins_loc = pncs("Roc pass",
    [
        ruins_0,
        ruins_1,
        ruins_2,
        ruins_3,
        ruins_back,

    ],

    )


label ruins:
    scene 
    show bg ruins onlayer bg
    show screen pnc(abdul, ruins_loc)
    with dissolve
    pause
    jump ruins
