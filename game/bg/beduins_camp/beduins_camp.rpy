
default beduins_camp_back = pnco(
    "Back",
    None,
    (911, 729),
    Jump('desert'),
    hidden = False, hoffset = (83,-40),
    )

default beduins_camp_loc = pncs(
    "Main street",
    [
        beduins_camp_back,

    ]
    )

image bg beduins_camp = "bg/beduins_camp/bg.jpg"
label beduins_camp:
    scene
    show bg beduins_camp onlayer bg
    show screen pnc(abdul, beduins_camp_loc)
    pause
    jump beduins_camp

