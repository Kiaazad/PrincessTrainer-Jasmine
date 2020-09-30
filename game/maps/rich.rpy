default rich_agrabah = pnco(
    "Agrabah",
    None,
    (924, 77),
    Jump('agrabah'),
    )




default rich_map = pncs(
    "Rich section",
    [
        rich_agrabah,
    ]
    )

image bg rich = "bg/rich.png"
label rich:
    scene
    show bg rich onlayer bg
    show screen pnc(abdul, rich_map)
    pause
    jump rich




