default desert_roc_pass = pnco(
    "Roc pass",
    "bg/desert/roc pass.png",
    (1600, 576),
    Jump('desert_0'),
    )
default desert_agrabah = pnco(
    "Agrabah",
    "bg/desert/agrabah.png",
    (900, 800),
    Jump('agrabah'),
    )
default desert_heaven_oasis = pnco(
    "Heaven oasis",
    None,
    (300, 500),
    Jump('heaven_oasis'),
    )
default desert_ruins = pnco(
    "The ruins",
    None,
    (670, 200),
    Jump('ruins'),
    )
default desert_beduins_camp = pnco(
    "Beduins camp",
    None,
    (370, 600),
    Jump('beduins_camp'),
    )
default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass,
        desert_agrabah,
        desert_heaven_oasis,
        desert_ruins,
        desert_beduins_camp,
    ]
    )

label desert:
    scene
    show bg bg1 onlayer bg
    show screen pnc(abdul, desert_map)
    pause
    jump desert




