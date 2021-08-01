default ruins_0 = pnco(
    "thorns",
    "bg/roc_pass/01.png",
    (188, 598),
    items = [[thorns, 1]],
    )
default ruins_1 = pnco(
    "thorns",
    "bg/roc_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    )
default ruins_2 = pnco(
    "thorns",
    "bg/roc_pass/03.png",
    (173, 842),
    items = [[thorns, 1]],
    )
default ruins_3 = pnco(
    "thorns",
    "bg/roc_pass/04.png",
    (411, 729),
    items = [[thorns, 1]],
    )
default ruins_back = pnco(
    "Back",
    None,
    (611, 729),
    Jump('beduins_camp'),
    )
# items


# Fights
default ogre = unit(
    "Ogre",
    "char/foes/ogre",
    lvl = 5,
    type = "Demon",
    items = [(coal, 11)]
    )
default ruins_ogre = pnco(
    "thorns",
    "bg/ruins/ogre.png",
    (182, 660),
    Jump('ruins_ogre'),
    )
label ruins_ogre:
    call screen btl_scr(team([abdul]), team([ogre]))
    jump ruins



default ruins_loc = pncs("Roc pass",
    [
        ruins_0,
        ruins_1,
        ruins_2,
        ruins_3,
        ruins_back,
        ruins_ogre,

    ], night = "bg/ruins/night.webp"

    )

image bg ruins = "bg/ruins/bg.webp"
label ruins:
    if not ruins_loc in all_places:
        $ all_places.append(ruins_loc)
    scene 
    show bg ruins onlayer bg
    show screen pnc(abdul, ruins_loc)
    with dissolve
    pause
    jump ruins
