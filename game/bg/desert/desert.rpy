default desert_roc_pass = pnco(
    "Roc pass",
    "bg/desert/roc pass.png",
    (1600, 576),
    Jump('desert_0'),
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
default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass,
        desert_agrabah,
        desert_heaven_oasis,
        desert_beduins_camp,
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




