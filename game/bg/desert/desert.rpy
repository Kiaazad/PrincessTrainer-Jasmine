# Exits
default desert_roc_pass = pnco(
    "Roc pass",
    "bg/desert/roc pass.png",
    (1600, 576),
    Jump('roc_pass'),
    )
default desert_agrabah = pnco(
    "Agrabah",
    "bg/desert/agrabah.png",
    (720, 880),
    Jump('street'),
    )
default desert_heaven_oasis = pnco(
    "Heaven oasis",
    None,
    (932, 501),
    Jump('heaven_oasis'),
    )
default desert_beduins_camp = pnco(
    "Beduins camp",
    None,
    (111, 796),
    Jump('beduins_camp'),
    )

# Random
default desert_nasim = pnco(
    "Trap",
    "bg/desert/nasim.png",
    (1057, 628),
    Jump('desert_nasim'),
    )
define nasim = Character("Nasim", color="#4ff", what_text_color="#dff")
image nasim normal dark = "char/nasim/normal dark.png"

label desert_nasim:
    scene
    show nasim normal dark at right
    nasim "Hey there strong man!"
    show abd normal at left with dissolve
    abd "Huh? hey..."
    nasim "Come on daddyo, why the hesitance? I won't bite..."
    nasim "Unless you want me to."
    abd "Ummm... I...{w=.2}{nw}"
    $ msg.msg("You've received a piece of paper.")
    nasim "Here."
    abd "What's this?"
    nasim "An invitation."
    abd "Invitation? To what?"
    nasim "My lady is camping nearby, and you're invited to meet her."
    abd "Where?"
    nasim "It's written on the invitation. The southern trade route."
    abd "Ummm..."
    abd "Who's your lady?"
    nasim "That's a secret."
    abd "Sounds suspicious... Are you going to lore me there and jump me?"
    nasim "I can jump you here if you want?"
    abd "I meant mug me."
    nasim "What's the fun in that?"
    "..."
    nasim "Listen, I love to stay and chat you up, but I have to bounce before some guard shows up."
    nasim "Come over tomorrow if you want to meet my lady. She has something that you'll definitely want."
    abd "What is it that I want?"
    nasim "Me please..."
    "..."
    nasim "No rush big boy."
    nasim "See you tomorrow!"
    hide nasim with dissolve
    $ desert_nasim.hidden = True
    "..."
    hide abd with dissolve
    jump desert

# Fights
default black_scorpion = unit(
    "Black scorpion",
    "char/foes/black_scorpion",
    lvl = 6,
    type = "Beast",
    items = [(scorpion_tail, 1)]
    )
default desert_black_scorpion = pnco(
    "Black scorpion",
    "bg/desert/black_scorpion.png",
    (182, 660),
    Jump('desert_black_scorpion'),
    )
label desert_black_scorpion:
    call screen btl_scr(team([abdul]), team([black_scorpion]))
    jump desert



default desert_map = pncs(
    "Main street",
    [
        desert_roc_pass,
        desert_agrabah,
        desert_heaven_oasis,
        desert_beduins_camp,
        desert_black_scorpion,
        desert_nasim,
    ], night = "bg/desert/night.webp"
    )
"""
Background design notes:
This background is the desert immediately outside of the city's gate, it can be few pathways towards different places. 3 should suffice.
"""
image bg desert = "bg/desert/bg.webp"
label desert:
    if not desert_map in all_places:
        $ all_places.append(desert_map)
    scene
    show bg desert onlayer bg
    show screen pnc(abdul, desert_map)
    pause
    jump desert




