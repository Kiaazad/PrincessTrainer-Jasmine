default barracks_agrabah = pnco(
    "Poor section",
    None,
    (924, 929),
    Jump('poor'),
    )

default barracks_guard = pnco(
    "Guard",
    "bg/barracks/guard.png",
    (1100, 640),
    Jump('barracks_guard'),
    )




default barracks_map = pncs(
    "Barracks",
    [
        barracks_agrabah,
        barracks_guard,
    ]
    )

image bg barracks = "bg/barracks/bg.jpg"
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
    if qlog.has(planted_evidence) == "Completed":
        guard_2 "You're back?"
        guard_2 "We're full, go away?"
        abd "I must talk to Rasoul."
        guard_2 "Oh it's like that? You can go in."
        "..."
        jump rasoul_arc_end
                
                 
    guard_2 "If you came to turn yourself in, the jail is full, get lost!"
    guard_2 "We're not in the business of feeding lazy poor people."
    jump barracks
