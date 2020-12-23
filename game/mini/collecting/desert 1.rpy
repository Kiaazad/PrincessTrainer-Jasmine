default des_1_1 = col_obj("mini/collecting/1/01.png",
    (1357, 596), 10,
    [[wood, 7]],
    tools = [axe, saw],
    )
default des_1_2 = col_obj("mini/collecting/1/02.png",
    (578, 725), 1,
    [[thorns, 1]],
    )
default des_1_3 = col_obj("mini/collecting/1/03.png",
    (1700, 900), 1,
    [[thorns, 1]]
    )
default des_1_4 = col_obj("mini/collecting/1/04.png",
    (961, 633), 1,
    [[thorns, 1]],
    )
default des_1_5 = col_obj("mini/collecting/1/05.png",
    (342, 867), 1,
    [[thorns, 1]],
    )

default des_1_col = col_game("Roc pass",
    [des_1_1, des_1_2, des_1_3, des_1_4, des_1_5]
    )

label desert_1:
    scene black
    show bg rock_pass
    show screen collect(abdul, des_1_col, e = False)
    show screen mirage_1
    pause
    scene black with dissolve
    hide screen collect
    hide screen mirage_1
    show jas seducing at center with Dissolve(3)
    jas "Abdul..."
    abd "Yes?"
    jas "Come to me, Abdul."
    abd "Yes, your highness."
    jas "Abdul, I need your help."
    abd "What can I do for you, my princess?"
    jas "Agrabah is in trouble."
    abd "I will give my life for my city. What do you need from me?"
    jas "I need your seed, Abdul."
    abd "My seed?"
    jas "I need you to honor me with an heir."
    abd "With...?"
    jas "I need you to impregnate me, Abdul. Right here, Right now."
    abd "Are you..."
    abd "If you insist, your highness."

image cg dream jasmine 01 = Movie(play="cg/jasmine dream/01.webm", size = (1920, 1080))
image cg dream jasmine 02 = Movie(play="cg/jasmine dream/02.webm", size = (1920, 1080))
label desert_1_dream:
    scene black with dissolve
    show cg dream jasmine 01 with dissolve
    pause 8
    show cg dream jasmine 02 with dissolve:
    pause 8
    pause 1
    hide cg with dissolve
    show bg rock_pass with dissolve
    abd "Woah..."
    abd "That was weird."
    abd "I need to got to the city before I die from heat."
    jump street
