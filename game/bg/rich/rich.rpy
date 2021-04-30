default rich_agrabah = pnco(
    "Agrabah",
    None,
    (924, 77),
    Jump('agrabah'),
    )

default rich_laila = pnco(
    "Laila",
    "bg/rich/laila.png",
    (1437, 733),
    Jump('rich_laila'),
    hidden = False, hoffset = (35,203),
    )


default rich_map = pncs(
    "Rich section",
    [
        rich_agrabah,
        rich_laila,
    ]
    )

image bg rich = "bg/rich/bg.png"
label rich:
    scene
    show bg rich onlayer bg
    show screen pnc(abdul, rich_map)
    pause
    jump rich

# Kaneez
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
        jump street
    elif not "kamal's second warning" in abdul.flags:
        show laila normal at right with dissolve
        show abd normal at left with dissolve
        show kamal normal at midright with moveinright
        kam "What did I tell you?"
        kam "Get lost!"
        $ abdul.flags.append("kamal's second warning")
        jump street
    else:
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
        jump rasoul_arc_1


