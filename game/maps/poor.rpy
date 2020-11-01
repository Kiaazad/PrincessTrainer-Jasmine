default poor_agrabah = pnco(
    "Agrabah",
    None,
    (924, 77),
    Jump('agrabah'),
    )




default poor_map = pncs(
    "Poor section",
    [
        poor_agrabah,
    ]
    )

image bg poor = "bg/poor/bg.jpg"
label poor:
    scene
    show bg poor onlayer bg
    show screen pnc(abdul, poor_map)
    pause
    jump rich




