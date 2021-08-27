
# Exists
default cooper_mine_snake_pass = pnco(
    "Snake's pass",
    None,
    (400, 500),
    Jump('snakes_pass'),
    )


default cooper_mine_map = pncs("Roc pass",
    [
        cooper_mine_snake_pass,
    ], night = "bg/roc_pass/night.webp"
    )
image bg cooper_mine = "bg/roc_pass/bg.webp"
label cooper_mine:
    scene 
    show bg cooper_mine onlayer bg
    show screen pnc(abdul, cooper_mine_map)
    with dissolve
    pause
    jump cooper_mine
