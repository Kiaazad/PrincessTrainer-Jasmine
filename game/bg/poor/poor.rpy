default poor_bazaar = pnco(
    "Bazaar",
    None,
    (700, 700),
    Jump('bazaar'),
    )
default poor_thief = pnco(
    "Ahmad",
    "bg/poor/thief.png",
    (1294, 601),
    Jump('poor_thief'),
    )




default poor_map = pncs(
    "Poor section",
    [
        poor_bazaar,
        poor_thief,
    ]
    )

image bg poor = "bg/poor/bg.png"
label poor:
    scene
    show bg poor onlayer bg
    show screen pnc(abdul, poor_map)
    pause
    jump poor

default ahmad_u = unit(
    "Sleazy Ahmad",
    "char/ahmad",

    490,
    [

    ],
    1.1,

    8,
    "Peasant",
    interests = ["jewelry"],
    reject = ["fuel"]
    )

define ahm = Character("Sleazy Ahmad", color="#4ff", what_text_color="#dff")
image ahmed normal = "char/ahmad/normal.png"
label poor_thief:
    scene
    if not "first" in ahmad_u.flags:
        $ ahmad_u.pick_pocket_skill = 80
        show ahmed normal at right
        ahm "Hey baddy!"
        ahm "Do you want to play coins?"
        show abd normal at left
        abd "You seem the wrong type to gamble with."
        ahm "Come on buddy... What's the harm?"
        abd "I don't know..."
        $ ahmad_u.pick_pocket(abdul)
        ahm "Alright buddy... I'm here if you want to have some fun."
        $ ahmad_u.add_flag("first")
    else:
        show ahmed normal at right
        ahm "Came to play buddy?"
        show abd normal at left
        menu:
            "sure!":
                abd "Sure..."
                ahm "..."
                ahm "Oh that's odd, I can't find my lucky coin. let's do it later."
                $ ahmad_u.pick_pocket(abdul)
                ahm "let's do it later."
            "No!":
                ahm "Come on buddy..."
                ahm "Don't be like that."
                abd "NO!"
                ahm "..."
                $ ahmad_u.pick_pocket(abdul)
                ahm "Alright, you'll be back."
    jump poor
