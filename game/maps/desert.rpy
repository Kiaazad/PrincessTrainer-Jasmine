default desert_roc_pass_loc = pnco(
    "Roc pass",
    "bg/desert/roc pass.png",
    (1600, 576),
    Jump('desert_0'),
    )
default desert_agrabah_loc = pnco(
    "Agrabah",
    "bg/desert/agrabah.png",
    (900, 800),
    Jump('agrabah'),
    )

default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass_loc,
        desert_agrabah_loc,

    ]
    )

label desert:
    scene
    show bg bg1 onlayer bg
    show screen pnc(abdul, desert_map)
    pause
    jump desert
