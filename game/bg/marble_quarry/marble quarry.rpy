# Exists
default marble_quarry_shard = pnco(
    "Quartz shard",
    None,
    (400, 500),
    Jump('marble_quarry'),
    )


default marble_quarry_map = pncs("marble_quarry",
    [
        cooper_mine_snake_pass,
    ], night = "bg/roc_pass/night.webp"
    )
image bg marble_quarry = "bg/roc_pass/bg.webp"
label marble_quarry:
    scene 
    show bg marble_quarry onlayer bg
    show screen pnc(abdul, marble_quarry_map)
    with dissolve
    pause
    jump marble_quarry
