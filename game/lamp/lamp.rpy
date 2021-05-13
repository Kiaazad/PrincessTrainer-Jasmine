
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


default lamp_quest = pnco(
    "Jafar's den",
    "bg/lamp/quest.png",
    (1272, 828),
    Jump('lamp_quest'),
    hidden = False, hoffset = (114,80),
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

        lamp_quest,

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

label lamp_quest:
    call screen quests
    jump inside_lamp

label lamp_fight:
    scene
    "Under construction"
    jump inside_lamp

label lamp_harem:
    scene
    "Under construction"
    jump inside_lamp


default ring_recipe = item(
    _("Ring recipe"),
    _("A recipe for an odd looking copper ring. Jafar drawn and wrote it."),
    "items/wood.png",
    0,
    ["Finger", "jewelry"],
    )

default make_a_copper_ring = quest(
    _("Make a copper ring"),
    _("Jafar wants a copper ring made."),
    )


image bg jafars_lab = "bg/lamp/jafars_lab.png"
label lamp_jafar:
    scene
    "{nw}"
    show bg jafars_lab
    show abd normal at left
    show jaf normal at right
    menu:
        "Chit chat.":
            jaf "No time for chit chat."
        "I've got the money." if qlog.has(fast_cash) == "Active" and hero.cash > 2000:
            abd "I've got the money."
            jaf "Excellent!"
            $ abdul.got(ring_recipe, 1)
            jaf "take this to the jeweller in bazaar and tell him to make a copper ring as instructed."
            abd "Why not bronze?"
            jaf "Bronze is too shiny, nobody will steal a copper ring from you."
            abd "Ah, alright."
            $ qlog.complete(fast_cash)
            $ qlog.got(make_a_copper_ring)
            jaf "Is there anything else?"
            show abd alert at left
            abd "No!"
            jaf "get going then."
            show abd normal at left
            abd "Right!"
            jump agrabah
        "The ring is ready..." if qlog.has(make_a_copper_ring) == "Active" and False:
            pass

        "I have some books" if qlog.has(books_for_jafar) and False:
            jaf "Bating, go away."

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
        "I got the scroll." if qlog.has(my_to_do_list) == "Active" and hero.has(skin_scroll):
            abd "I got the scroll Jafar."
            jaf "Excellent!{W=.2} Hold it up."
            show jaf magic at right
            pause 1
            show jaf normal at right
            jaf "There."
            jaf "It keeps track of your tasks, now go do them."
            $ my_to_do_list.finish()
            abd "But...{w=.2}{NW}"
            jaf "Go figure it out.{w=.2} I can't explain everything to you."

    jump inside_lamp



