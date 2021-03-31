default des_1_1 = pnco(
    "Dried Tree",
    "bg/snakes_pass/01.png",
    (1357, 596),
    hits = 10,
    items = [[wood, 7]],
    tools = [axe, saw],
    )
default des_1_2 = pnco(
    "thorns",
    "bg/snakes_pass/02.png",
    (578, 725),
    items = [[thorns, 1]],
    )
default des_1_3 = pnco(
    "thorns",
    "bg/snakes_pass/03.png",
    (1700, 900),
    items = [[thorns, 1]]
    )
default des_1_4 = pnco(
    "thorns",
    "bg/snakes_pass/04.png",
    (961, 633),
    items = [[thorns, 1]],
    )
default des_1_5 = pnco(
    "thorns",
    "bg/snakes_pass/05.png",
    (342, 867),
    items = [[thorns, 1]],
    )

default des_1_col = pncs("Gate's view",
    [
        des_1_1,
        des_1_2,
        des_1_3,
        des_1_4,
        des_1_5
    ]
    )
image bg snakes_pass = "bg/snakes_pass/bg.png"
label desert_1:
    scene
    show bg snakes_pass onlayer bg
    show screen pnc(abdul, des_1_col)
    with dissolve

    show screen mirage_1
label desert_1_loop:
    pause
    jump desert_1_loop

transform mirage_t(a):
    ease 1 alpha a
transform delayed(p):
    alpha 0
    pause p
    alpha 1
transform fade_to_screen:
    alpha .2 zoom .01
    ease 3 zoom 100 alpha 0
screen mirage_1:
    default alph = 0
    default intervals = 1
    if intervals < 20:
        timer 2 repeat True action SetScreenVariable("alph", .1), SetScreenVariable("intervals", intervals+1)
        timer intervals*.1 repeat True action SetScreenVariable("alph", 0)
    else:
        timer .01 action Jump("desert_1_conv")
    if intervals == 5:
        text "Abdul" at fade_to_screen
    elif intervals == 10:
        text "Abdul" at fade_to_screen
    elif intervals == 15:
        text "Come to me" at fade_to_screen
    frame:
        background "#000"
        at mirage_t(float(intervals)/20)
    frame:
        background None yalign 1.0 padding 0,0
        at delayed(1)
        add "char/jasmine/seducing.png" at mirage_t(alph)


label desert_1_conv:
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


# ---------- CG

default jasmine_dream_veil = cg_obj(
    _("Veil"),
    "cg/jasmine dream/veil.png",
    "veil",
    5,10,
    type = "item"
    )
default jasmine_dream_leash = cg_obj(
    _("Leash"),
    "cg/jasmine dream/leash.png",
    "leash",
    10,5,
    type = "item"
    )

default jasmine_dream_shocked = cg_obj(
    _("Shocked"),
    "cg/jasmine dream/shocked.png",
    "shocked",
    type = "expression"
    )
default jasmine_dream_adore = cg_obj(
    _("Adore"),
    "cg/jasmine dream/adore.png",
    "adore",
    type = "expression"
    )
default jasmine_dream_angry = cg_obj(
    _("Angry"),
    "cg/jasmine dream/angry.png",
    "angry",
    type = "expression"
    )
default jasmine_dream_default = cg_obj(
    _("Default"),
    "cg/jasmine dream/neutral.png",
    "default",
    type = "expression"
    )


default jasmine_dream_scene1_fx = cg_obj(
    _("Scene1_fx"),
    "cg/jasmine dream/sex1.png",
    "scene1_fx",
    0,0,2,
    type = "motion"
    )
default jasmine_dream_scene2_fx = cg_obj(
    _("Scene2_fx"),
    "cg/jasmine dream/sex2.png",
    "scene2_fx",
    0,0,4,
    type = "motion"
    )
default jasmine_dream_scene3_fx = cg_obj(
    _("Scene3_fx"),
    "cg/jasmine dream/sex3.png",
    "scene3_fx",
    0,0,8,
    type = "motion"
    )

image jasmine_dream_l2d = Live2D("cg/jasmine dream/l2d/jassmine_ride_model.model3.json", loop=True,
    nonexclusive= ["veil","leash", "shocked", "adore", "angry", "default"],
    # update_function=i_love_you_parasite,
    )


default jasmine_dream_cg = l2dcg(
    jasmine,
    [
        jasmine_dream_scene1_fx,
        jasmine_dream_scene2_fx,
        jasmine_dream_scene3_fx,

        jasmine_dream_shocked,
        jasmine_dream_adore,
        jasmine_dream_angry,

        jasmine_dream_veil,
        jasmine_dream_leash,

    ], "jasmine_dream_l2d"
    )



label desert_1_dream:
    scene black with dissolve

    show screen cgscr(jasmine_dream_cg)
    pause

    show bg snakes_pass with dissolve
    show abd bent at left
    show abd tired at left with dissolve
    show abd alert at left
    abd "Woah..."
    abd "That was weird."
    abd "I need to got to the city before I die from heat."
    jump street
