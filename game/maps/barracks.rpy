default barracks_agrabah = pnco(
    "Agrabah",
    None,
    (924, 77),
    Jump('agrabah'),
    )

default barracks_guard = pnco(
    "Guard",
    None,
    (400, 300),
    Jump('barracks_guard'),
    )




default barracks_map = pncs(
    "Barracks",
    [
        barracks_agrabah,
        barracks_guard,
    ]
    )

# image bg barracks = "bg/barracks/bg.jpg"
label barracks:
    scene
    show bg barracks onlayer bg
    show screen pnc(abdul, barracks_map)
    pause
    jump barracks


define guard_2 = Character("Guard", color="#4ff", what_text_color="#dff")
image guard_2 normal = "char/guard/guy2 normal.png"
label barracks_guard:
    scene
    show guard_2 normal at center
    guard_2 "If you came to turn yourself in, the jail is full, get lost!"
    guard_2 "We're not in the business of feeding lazy poor people."
    jump barracks
