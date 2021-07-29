# Exits
default desert_roc_pass = pnco(
    "Roc pass",
    "bg/desert/roc pass.png",
    (1600, 576),
    Jump('roc_pass'),
    )
default desert_agrabah = pnco(
    "Agrabah",
    "bg/desert/agrabah.png",
    (720, 880),
    Jump('street'),
    )
default desert_heaven_oasis = pnco(
    "Heaven oasis",
    None,
    (932, 601),
    Jump('heaven_oasis'),
    )
default desert_beduins_camp = pnco(
    "Beduins camp",
    None,
    (111, 796),
    Jump('beduins_camp'),
    )

# Fights
default black_scorpion = unit(
    "Black scorpion",
    "char/foes/black_scorpion",
    lvl = 6,
    type = "Beast",
    )
default desert_black_scorpion = pnco(
    "Black scorpion",
    "bg/desert/black_scorpion.png",
    (182, 660),
    Jump('desert_black_scorpion'),
    )
label desert_black_scorpion:
    call screen btl_scr(team([abdul]), team([black_scorpion]))
    jump desert



default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass,
        desert_agrabah,
        desert_heaven_oasis,
        desert_beduins_camp,
        desert_black_scorpion,
    ], night = "bg/desert/night.webp"
    )
"""
Background design notes:
This background is the desert immediately outside of the city's gate, it can be few pathways towards different places. 3 should suffice.
"""
image bg desert = "bg/desert/bg.webp"
label desert:
    if not desert_map in all_places:
        $ all_places.append(desert_map)
    scene
    show bg desert onlayer bg
    show screen pnc(abdul, desert_map)
    pause
    jump desert




