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
default desert_water_front_loc = pnco(
    "Water front",
    None,
    (300, 500),
    Jump('desert_water_front'),
    )
default desert_ruins_loc = pnco(
    "The ruins",
    None,
    (670, 200),
    Jump('desert_ruins'),
    )

default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass_loc,
        desert_agrabah_loc,
        desert_water_front_loc,
        desert_ruins_loc,
    ]
    )

label desert:
    scene
    show bg bg1 onlayer bg
    show screen pnc(abdul, desert_map)
    pause
    jump desert

# The viking



define vik = Character("The Viking", color="#4ff", what_text_color="#dff")
image viking normal = "char/viking/normal.png"

label desert_water_front:
    scene
    show bg water_front
    show viking normal at right
    vik "Abdul the wood collector... have you came here to take my boat apart?"
    show abd normal at left
    abd "Do you have to mention that every time? I thought it was abandoned."
    vik "Alright alright... Came to buy what I've fished out from my sunken cargo?"
    abd "What do you have."
    vik "Nothing yer, but soon."
    abd "Alright I'll visit later."
    jump desert

label desert_ruins:
    scene
    show bg desert_ruins
    "Nothing here yet"
    jump desert


