default barracks_agrabah = pnco(
    "Poor section",
    None,
    (924, 929),
    Jump('poor'),
    )

default barracks_guard = pnco(
    "Guard",
    "bg/barracks/guard.png",
    (1300, 640),
    Jump('barracks_guard'),
    )


"""
Background design notes:
There are two entrances guarded by the same guard, one goes into the jail and one to the barracks.
preferably both entrances are in the palaces wall, but the barracks can be some shacks attached to the palace wall instead.
"""

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
    if qlog.has(planted_evidence) == "Finished":
        guard_2 "What do you want?"
        menu:
            "I need to talk to Rasoul.":
                abd "I need to talk to Rasoul."
                guard_2 "He's inside."
                jump inside_barracks
            "I need to talk to Qasim.":
                abd "I need to talk to Qasim."
                guard_2 "Alright, Go in."
                jump jail
    guard_2 "If you came to turn yourself in, the jail is full, get lost!"
    guard_2 "We're not in the business of feeding lazy poor people."
    jump barracks

label inside_barracks:
    scene
    show abd normal at left with dissolve
    show ras normal at midright with move
    ras "What do you want?"
    abd "I'm ready for more tasks."
    ras "Not now, I'm busy."
    jump barracks









