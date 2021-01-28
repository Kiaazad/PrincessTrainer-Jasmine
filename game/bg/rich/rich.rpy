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
    show laila normal at right
    lai "New slave?"
    show abd normal at left
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
    jump street


