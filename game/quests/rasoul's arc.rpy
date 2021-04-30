# Rasoul the head of guards
# Normal
image ras_normal_blink:
    "char/rasoul/normal_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image ras_normal_mouth_moving:
    "char/rasoul/normal_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image ras_normal_mouth = ConditionSwitch(
    "_last_say_who == 'ras'", "ras_normal_mouth_moving",
    "not _last_say_who == 'ras'", "char/rasoul/normal.png")

image ras normal = Composite((800, 962),
    (0,0), "char/rasoul/normal.png",
    (0,0), "ras_normal_mouth",
    (0,0), "ras_normal_blink",
)
# Angry
image ras_angry_blink:
    "char/rasoul/angry_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image ras_angry_mouth_moving:
    "char/rasoul/angry_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image ras_angry_mouth = ConditionSwitch(
    "_last_say_who == 'ras'", "ras_angry_mouth_moving",
    "not _last_say_who == 'ras'", "char/rasoul/angry.png")

image ras angry = Composite((800, 962),
    (0,0), "char/rasoul/angry.png",
    (0,0), "ras_angry_mouth",
    (0,0), "ras_angry_blink",
)

define ras = Character("Rasoul", color="#f44", what_text_color="#fdd", namebox_align=(1.0, 0.0))

label rasoul_arc_1:
    scene
    show bg street onlayer bg
    show screen pnc(abdul, street_map)
    show abd normal at midleft with dissolve
    show ras normal at midright with dissolve
    menu:
        "I didn't do anything wrong...":
            abd "I didn't do anything wrong Rasoul."
            ras "Shut up!" with hpunch

        "Head of the palace guards, taking orders from Kamal...":
            abd "I never imagined to see head of palace guards taking orders from Kamal."
            "..."
            abd "Does he have some dirt on you?"
            ras "I'm just doing my job and keeping the scum like you off the street."
            abd "What did I do?"
            ras "Violation of people's property."
            ras "Don't tell me it wasn't you talking to female slaves in the rich section."
            abd "Well I did talk, but...{w=.2}{nw}"
            ras "So you've confessed.{w=.2}{nw}"
            ras "MOVE IT!" with hpunch
    scene
    show bg bazaar onlayer bg
    show screen pnc(abdul, bazaar_map)
    show ras normal at midright with dissolve
    ras "Walk faster!"
    "{nw}"
    show abd normal at midleft with dissolve
    scene
    show bg poor onlayer bg
    show screen pnc(abdul, poor_map)
    "{w=1}{nw}"
    show bg barracks onlayer bg
    show screen pnc(abdul, barracks_map)
    show abd normal at midleft with dissolve
    show ras normal at midright with dissolve
    ras "Guard!"
    show abd normal at left
    show ras normal at center
    with move
    show guard_2 normal at right with dissolve
    guard_2 "Yes sir?"
    ras "Take him to jail."
    guard_2 "Yes sir!"
    hide ras with moveoutright
    show guard_2 at center with move
    "{w=.2}{nw}"
    hide screen pnc

image bg jail = "bg/jail/bg.jpg"
image bg jail cell = "bg/jail/cell.jpg"
label rasoul_arc_2:
    scene
    show bg jail onlayer bg
    # show screen pnc(abdul, barracks_map)
    show abd normal at midleft with dissolve
    show guard_2 normal at midright with dissolve
    guard_2 "You're pretty lucky to get in.{w=.2} We're fully booked."
    guard_2 "Now give me your belongings.{w=.2} I'll keep them safe."
    "{w=2}{nw}"
    # stripped of items and money
    abd "A pile of books?"
    guard_2 "They're illegal books we confiscated, not for the prisoners."
    show bg jail cell onlayer bg
    show abd normal at midleft with dissolve
    show guard_2 normal at midright with dissolve
    guard_2 "Here's your room..."
    guard_2 "No bed but the shackles are pretty comfy.{w=.2} Just yell if you want me to put them on you."
    "..."
    guard_2 "Enjoy your stay in the palace."
    show abd normal at left with dissolve
    hide guard_2 with dissolve

default planted_evidence = quest(
    _("Planted evidence"),
    _("Rasoul wants you to plant one of Jafar's books in Hakim's shop."),
    )


label rasoul_arc_3:
    menu:
        "Sleep":
            show screen time_pass(renpy.random.randint(3,10))
            "Resting for a while."
            jump rasoul_arc_3
        "Ask for food.":
            abd "Guard...{w=.2} guard!"
            "..."
            abd "Guard!"
            show guard_2 normal at right with dissolve
            guard_2 "What is it?"
            abd "I'm hungry."
            guard_2 "Where do you think you are?{w=.2} A tavern?"
            if (calendar.day % 2):
                guard_2 "You'll get your piece of bread every other day.{w=.2} Today isn't the other day."
            else:
                guard_2 "You'll get your piece of bread every other day.{w=.2} Lucky for you, today is an other day."
            guard_2 "Now shut up!"
            hide guard_2 with dissolve
            menu:
                "I can't stay here...":
                    abd "Guard!"
                    "..."
                    show guard_2 normal at right with dissolve
                    guard_2 "Will you shut up?"
                    abd "Guard...{w=.2} please...{w=.2} I can't stay here..."
                    guard_2 "Why didn't you say so?{w=.2} Let me release you."
                    "..."
                    abd "Really?"
                    guard_2 "Of course not.{w=.2} You idiot."
                    abd "Come on,{w=.2} there must be a way,{w=.2} I didn't do anything wrong."
                    guard_2 "Why didn't yo...{w=.2}{nw}"
                    ras "There is a way."
                    show ras normal at center with moveinright
                    ras "You can pay the fine."
                    abd "But you took all of my money."
                    guard_2 "You have some money stashed somewhere don't you?"
                    ras "Do you?"
                    abd "I'm a wood collector sleeping on the streets Rasoul."
                    ras "Then this is an improvement for you, isn't it?"
                    abd "Please Rasoul, you know I'm innocent."
                    ras "Hmmm...{w=.2} Maybe you can do something for me."
                    abd "Anything Rasoul."
                    ras "Bring me the book!"
                    guard_2 "Yes sir."
                    hide guard_2 with moveoutright
                    "..."
                    show guard_2 normal at right with moveinright
                    guard_2 "Sir."
                    ras "Take this!"
                    # Receive jafar's book
                    ras "Plant this book on Hakim's shelf and I'll forgive you."
                    abd "Alright...{w=.2} But why."
                    $ qlog.got(planted_evidence)
                    ras "Because I said so."
                    abd "Hakim is my friend Rasoul.{w=.2} What are you planning to do to him."
                    ras "Do you want to get out of here or not?"
                    abd "Yes."
                    ras "Then do as I say."
                    abd "well...{w=.2} If I have to."
                    ras "Good.{w=.2} Release him!"
                    hide ras with moveoutright
                    guard_2 "Yes sir!"
                    "..."
                    scene
                    show bg jail onlayer bg
                    # show screen pnc(abdul, barracks_map)
                    show abd normal at midleft with dissolve
                    show guard_2 normal at midright with dissolve
                    abd "Can I have my belongings back?"
                    guard_2 "What belongings?"
                    abd "The ones you took from me."
                    guard_2 "Alright, here are your junk."
                    abd "And my money?"
                    guard_2 "You didn't have any."
                    abd "But...{w=.2}{nw}"
                    guard_2 "Do you want to go back to your cell?"
                    abd "No."
                    guard_2 "Then get out!"
                    "..."
                    guard_2 "Go!"
                    jump barracks