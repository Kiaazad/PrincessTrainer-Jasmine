# Exits
default agrabahs_gate_roc_pass = pnco(
    "Roc pass",
    "bg/agrabahs_gate/roc pass.png",
    (1600, 576),
    Jump('roc_pass'),
    )
default agrabahs_gate_agrabah = pnco(
    "Agrabah",
    "bg/agrabahs_gate/agrabah.png",
    (720, 880),
    Jump('street'),
    )
default agrabahs_gate_beduins_camp = pnco(
    "Beduins camp",
    None,
    (932, 501),
    Jump('beduins_camp'),
    )
default agrabahs_gate_farms = pnco(
    "Farms",
    None,
    (111, 796),
    Jump('farms'),
    )

label farms:
    "not ready yet"
    jump agrabahs_gate


# Random
default agrabahs_gate_nasim = pnco(
    "Trap",
    "bg/agrabahs_gate/nasim.png",
    (1057, 628),
    Jump('agrabahs_gate_nasim'),
    )
define nasim = Character("Nasim", color="#4ff", what_text_color="#dff")
image nasim normal dark = "char/nasim/normal dark.png"

label agrabahs_gate_nasim:
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
    $ agrabahs_gate_nasim.hidden = True
    "..."
    hide abd with dissolve
    jump agrabahs_gate

# Fights
default black_scorpion = unit(
    "Black scorpion",
    "char/foes/black_scorpion",
    lvl = 6,
    type = "Beast",
    items = [(scorpion_tail, 1)]
    )
default agrabahs_gate_black_scorpion = pnco(
    "Black scorpion",
    "bg/agrabahs_gate/black_scorpion.png",
    (182, 660),
    Jump('agrabahs_gate_black_scorpion'),
    )
label agrabahs_gate_black_scorpion:
    call screen btl_scr(team([abdul]), team([black_scorpion]))
    jump agrabahs_gate



default agrabahs_gate_map = pncs(
    "Agrabah's gate",
    [
        agrabahs_gate_agrabah,
        agrabahs_gate_roc_pass,
        agrabahs_gate_farms,
        agrabahs_gate_beduins_camp,
        agrabahs_gate_black_scorpion,
        agrabahs_gate_nasim,
    ], night = "bg/agrabahs_gate/night.webp"
    )
"""
Background design notes:
This background is the desert immediately outside of the city's gate, it can be few pathways towards different places. 3 should suffice.
"""
image bg desert = "bg/agrabahs_gate/bg.webp"
label agrabahs_gate:
    if not agrabahs_gate_map in all_places:
        $ all_places.append(agrabahs_gate_map)
    scene
    show bg desert onlayer bg
    show screen pnc(abdul, agrabahs_gate_map)
    pause
    jump agrabahs_gate




