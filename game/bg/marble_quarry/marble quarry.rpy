# Exists
default marble_quarry_ruins = pnco(
    "Ruins",
    None,
    (171, 952),
    Jump('ruins'),
    )
default marble_quarry_roc_pass = pnco(
    "Roc pass",
    None,
    (1781, 550),
    Jump('roc_pass'),
    )

default marble_quarry_map = pncs(
    "Marble quarry",
    [
        marble_quarry_ruins,
        marble_quarry_roc_pass,
    ], night = "bg/marble_quarry/night.webp"
    )
image bg marble_quarry = "bg/marble_quarry/bg.webp"
label marble_quarry:

    scene 
    show bg marble_quarry onlayer bg
    show screen pnc(abdul, marble_quarry_map)
    with dissolve
    pause
    jump marble_quarry
