default poor_bazaar = pnco(
    "Bazaar",
    None,
    (780, 980),
    Jump('bazaar'),
    )
default poor_thief = pnco(
    "Ahmad",
    "bg/poor/thief.png",
    (1294, 601),
    Jump('poor_thief'),
    shifts = [[100,180], [190, 250]]
    )
default poor_barracks = pnco(
    "Barracks",
    None,
    (800, 600),
    Jump('barracks'),
    )
default petros_shop = pnco(
    "Shady Figure",
    "bg/poor/petros.png",
    (136, 330),
    Jump('petros_shop'),
    hidden = False, hoffset = (20,-80),
    )


default poor_map = pncs(
    "Poor section",
    [
        poor_bazaar,
        poor_thief,
        poor_barracks,
        petros_shop,
    ], night = "bg/poor/night.jpg"
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


# Shady alley
define pet = Character("Petros", color="#4ff", what_text_color="#dff")
image petros normal = "char/petros/normal.png"



default petros_u = unit(
    "Petros",
    "char/petros",

    3410,
    [
        (beer, 1),
        (liquor, 1),
        (wine, 1),
    ],
    1.2,

    8,
    "Peasant",
    interests = [],
    reject = ["Weapon", "armor", "lamp"]
    )
label petros_shop:
    scene
    if not "first" in petros_u.flags:
        show petros normal at right
        pet "Hey... Dabul... know any women to hook me up with?"
        show abd normal at left
        abd "It's Abdul, and no."
        pet "Came here to sin then? What's your choice?"
        $ petros_u.add_flag("first")
    else:
        show petros normal at right
        pet "Abully the sinner. What do you need this time?"
        show abd normal at left
    if qlog.has(beer_for_the_viking) and beer_for_the_viking.stat == "Active":
        abd "I need a keg of beer."
        pet "Ohohohoh, what for? having friends over?"
        pet "Any women? I'm coming too."
        abd "It's for somebody."
        pet "Ah, the guy at oasis?"
        abd "Yes."
        pet "I was wondering when he'll run out."
        pet "A keg costs 2400 Dinars."
        $ hero.paidcash(2400)
        $ petros_u.gotcash(2400)
        abd "Here."
        pet "Alright, wait here."
        hide petros with moveoutright
        pause 4
        show petros normal at right with moveinright
        pet "Here you go, a keg of the best beer in Agrabah."
        $ hero.got(beer_keg)
        $ beer_for_the_viking.complete()
        pet "Don't get caught."
        abd "Thanks"
        pet "And you don't know me if they catch you."
        "..."
        jump bazaar

    call screen shop(s = petros_u)
    jump poor
