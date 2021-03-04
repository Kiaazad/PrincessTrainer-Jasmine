
init offset = -1

## Navigation screen ###########################################################
transform lampoff(x,y):
    parallel:
        alpha 0 offset (0,0)
        ease .2 offset (x,y) alpha 1
    parallel:
        on idle:
            easein .2 alpha .6
        on hover:
            easein .2 alpha 1.0
        # on selected_idle:
        #     easein .2 additive .2
        # on selected_hover:
        #     easein .2 additive .3
        on insensitive:
            easein .2 alpha .2
screen navigation(ii=0):
    style_prefix "nav"
    tag menu
    add "#000"
    button: 
        add "bg/lamp/back.png"
        action Return()
    button:
        at lampoff(-350, 150)
        add "bg/lamp/fight.png"
        action Return()
    button:
        at lampoff(350, 150)
        add "bg/lamp/harem.png"
        action Return()
    button:
        at lampoff(0, 260)
        add "bg/lamp/library.png"
        action Call("lamp_jafar")
    button:
        at lampoff(350, -150)
        add "bg/lamp/quest.png"
        action Return()
    button:
        at lampoff(-350, -150)
        add "bg/lamp/replay.png"
        action Return()
    button:
        at lampoff(0, -260)
        add "bg/lamp/save.png"
        action ShowMenu("save")
    button:
        at lampoff(-600, 0)
        add "bg/lamp/settings.png"
        action ShowMenu("preferences")
    button:
        at lampoff(600, 0)
        add "bg/lamp/mm.png"
        action MainMenu()

init python:
     config.game_menu_action = [None]
style nav_button:
    background None


default learn_pick_pocket = quest(
    _("Learn pick pocket"),
    _("Jafar wants you to learn pick pocket from Ahmad.")
)




default lamp_jafar = pnco(
    "Jafar's den",
    "bg/lamp/library.png",
    (412, 225),
    Jump('lamp_jafar'),
    hidden = False, hoffset = (114,80),
    )

default lamp_harem = pnco(
    "Jafar's harem",
    "bg/lamp/harem.png",
    (724, 47),
    Jump('lamp_harem'),
    hidden = False, hoffset = (114,80),
    )

default lamp_agrabah = pnco(
    "Back to Agrabah",
    "bg/lamp/back.png",
    (103, 604),
    Jump('agrabah'),
    hidden = False, hoffset = (114,80),
    )

default lamp_fight = pnco(
    "Fighting ground",
    "bg/lamp/fight.png",
    (916, 476),
    Jump('lamp_fight'),
    hidden = False, hoffset = (114,80),
    )

default lamp_save = pnco(
    "Jar room",
    "bg/lamp/save.png",
    (1024, 234),
    ShowMenu("save"),
    hidden = False, hoffset = (114,80),
    )

default lamp_settings = pnco(
    "The odd room",
    "bg/lamp/settings.png",
    (600, 758),
    ShowMenu("preferences"),
    hidden = False, hoffset = (114,80),
    )

default lamp_gate = pnco(
    "The gate",
    "bg/lamp/mm.png",
    (1423, 533),
    MainMenu(),
    hidden = False, hoffset = (114,80),
    )

default lamp_map = pncs(
    "Jafar's lamp",
    [
        lamp_jafar,
        lamp_harem,
        lamp_fight,

        lamp_save,
        lamp_settings,
        lamp_gate,
        lamp_agrabah,
    ]
    )

image bg lamp = "#000"
label inside_lamp:
    scene
    show bg lamp onlayer bg
    show screen pnc(abdul, lamp_map)
    pause
    jump inside_lamp

label lamp_fight:
    scene
    "Under construction"
    jump inside_lamp

label lamp_harem:
    scene
    "Under construction"
    jump inside_lamp

label lamp_jafar:
    scene
    menu:
        "Chit chat.":
            jaf "No time for chit chat."
        "I've got the money." if abdul.has(fast_cash) == "Active" and abdul.cash > 2000:
            abd "I've got the money."
            jaf "Excellent, take this to the jeweller in bazaar and tell him to make a cooper ring as instructed."
            abd "Why not bronze?"
            jaf "Bronze is too shiny, nobody will steal a cooper ring from you."
            abd "Ah, alright."
            jaf "Is there anything else?"
            abd "No!"
            jaf "get going then."
            abd "Right!"
            jump agrabah
        "I think I've got rubbed." if "something is missing" in abdul.flags:
            abd "I think I've got rubbed Jafar."
            jaf "Let me guess, Ahmad?"
            abd "I think so, how do you know?"
            jaf "Caught him for picking pockets long ago."
            abd "But he still have both hands!"
            jaf "Yes, I don't like cutting parts of people."
            jaf "And his skilled hands where more useful to me attached to his arms."
            jaf "I've let him keep them in exchange for him acquiring some items for me."
            jaf "And his promise to find an honorable line of work of course."
            jaf "You should go back and talk to him soon."
            abd "Why? I'm sure he'll deny everything."
            jaf "You should learn what he does."
            jaf "It can be a pretty handy skill to have."
            jaf "Tell him you know about his deal with me, and you'll reward him handsomely for few lessons."
            abd "But rewarding needs money."
            jaf "Go get some, you're good at it."
            $ qlog.got(learn_pick_pocket)
            "..."
            jaf "Don't stand around, go!"
            abd "Alright."
            jump agrabah
    jump inside_lamp
