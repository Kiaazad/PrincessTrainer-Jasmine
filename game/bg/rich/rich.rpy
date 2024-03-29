﻿default rich_agrabah = pnco(
    "Street",
    None,
    (1270, 1009),
    Jump('street'),
    )
default rich_vantage_point = pnco(
    "Go up the mountain",
    None,
    (139, 956),
    Jump('vantage_point'),
    )




# Haji's son
default hajis_son = pnco(
    "Haji's son",
    "bg/rich/hajis_son.png",
    (670, 764),
    Jump('hajis_son'),
    hidden = False, hoffset = (35,203),
    )
define hajis = Character("Haji's son", color="#4ff", what_text_color="#dff")
image hajis normal = "char/pedestrians/hajis_son.png"
define hajis_slave = Character("Haji's slave", color="#4ff", what_text_color="#dff")
image hajis_slave normal = "char/pedestrians/hajis_slave.png"

label hajis_son:
    scene
    show hajis normal at right with dissolve
    show abd normal at left with dissolve
    "..."
    hajis "Slave! more food!"
    hajis_slave "Yes master."
    show hajis normal at midright with move
    show hajis_slave normal at right with moveinright
    hajis_slave "Here you go."
    "..."
    hajis "What?"
    abd "Nothing..."

    jump rich

# Kaneez
default rich_laila = pnco(
    "Laila",
    "bg/rich/laila.png",
    (1437, 733),
    Jump('rich_laila'),
    hidden = False, hoffset = (35,203),
    )
define lai = Character("Laila", color="#4ff", what_text_color="#dff")
define kam = Character("Kamal", color="#4ff", what_text_color="#dff")
image laila normal = "char/pedestrians/laila.png"
image kamal normal = "char/pedestrians/kamal.png"

label rich_laila:
    scene

    if not "kamal's warning" in abdul.flags:
        show laila normal at right
        lai "New slave?"
        show abd normal at left with dissolve
        abd "What?"
        lai "I've never seen you around here, you must be a new slave."
        abd "I'm not a slave."
        lai "Ow, just poor then?"
        abd "ermmm..."
        lai "You should leave before...{nw}"
        show laila normal at midright with move
        show kamal normal at right with moveinright
        kam "Making friends? slave?"
        lai "Sorry master."
        kam "Go!"
        kam "Yes master."
        hide laila
        "..."
        kam "Delivering something?"
        abd "No."
        kam "Then you have no business being here."
        "..."
        kam "Go!"
        kam "Before I report you to the guards."
        abd "alright..."
        $ abdul.flags.append("kamal's warning")
        jump rich
    elif not "kamal's second warning" in abdul.flags:
        show laila normal at right with dissolve
        show abd normal at left with dissolve
        show kamal normal at midright with moveinright
        kam "What did I tell you?"
        kam "Get lost!"
        $ abdul.flags.append("kamal's second warning")
        jump rich
    elif not "got arrested" in abdul.flags:
        show laila normal at right with dissolve
        show abd normal at left with dissolve
        show kamal normal at midright with moveinright
        kam "{size=44}Guard!"
        show laila normal at right
        show kamal normal at midright
        with move
        show ras normal at center with dissolve
        ras "Is this the guy?"
        kam "Yes."
        ras "Move it buddy!"
        show abd normal at left with dissolve
        abd "Where to?"
        ras "Jail."
        abd "But...{w=.2}{nw}"
        ras "{size=44}Move!{w=.2}{nw}" with hpunch
        "{nw}"
        $ abdul.flags.append("got arrested")
        jump rasoul_arc_1
    else:
        show laila normal at right with dissolve
        show abd normal at left with dissolve
        show kamal normal at midright with moveinright
        kam "You're here again?"
        kam "Rasoul will pay for this."
        jump rich



default rich_map = pncs(
    "Rich section",
    [
        rich_agrabah,
        rich_laila,
        rich_vantage_point,
        hajis_son,

    ], night = "bg/rich/night.webp"
    )

image bg rich = "bg/rich/bg.webp"
label rich:
    scene
    show bg rich onlayer bg
    show screen pnc(abdul, rich_map)
    pause
    jump rich