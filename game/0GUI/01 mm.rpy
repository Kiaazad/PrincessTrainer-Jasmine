init -100:
    ## Hide on MM, Hide on Nav, Hide on mobile, Show while replay Text, Action
    define menuz = [
        [1,0,0,1,_("Return"),Return()],
        [0,1,0,1,_("Start"),Start()],
        [1,0,0,0,_("Save"),ShowMenu("save")],
        [0,0,0,1,_("Load"),ShowMenu("load")],
        [0,0,0,1,_("Settings"),ShowMenu("preferences")],
        [0,0,0,1,_("Credits"),ShowMenu("credits")],
        [1,0,0,1,_("Main Menu"),MainMenu()],
        [0,0,1,1,_("Quit"),Quit(confirm=not main_menu)],
        ]

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
        action Return()
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
     config.game_menu_action = [  ShowMenu("navigation")]
style nav_button:
    background None

## Main Menu screen ############################################################

screen main_menu(ii=0):
    style_prefix "mm"
    tag menu

    if not persistent.theme_change:
        add "bg/01.png"
        add "0gui/abdul_frm.png"
        vbox:
            yoffset 100 spacing 10
            add "0gui/abdul.png"
            null height 100
            button:
                background None
                add "0gui/abdul_pl.png"
                action Start()
            button:
                background None
                add "0gui/abdul_ex.png"
                action Quit(confirm=not main_menu)
    else:
        add "0GUI/mm/bg.jpg"
        hbox:
            align(0.72, 0.21)
            button:
                text "Start"
                action Start()
                at btn
            button:
                text "Load"
                action ShowMenu("load")
                at btn
            button:
                text "Settings"
                action ShowMenu("preferences")
                at btn
            button:
                text "Quit"
                action Quit(confirm=not main_menu)
                at btn
        # fixed:
        #     fit_first True
        #     align (0.9, 0.0)
        #     button:
        #         add "0GUI/mm/start.png"
        #         action Start()
        #         at btn
        #     button:
        #         add "0GUI/mm/load.png"
        #         action ShowMenu("load")
        #         at btn
        #     button:
        #         add "0GUI/mm/settings.png"
        #         action ShowMenu("preferences")
        #         at btn
        #     button:
        #         add "0GUI/mm/quit.png"
        #         action Quit(confirm=not main_menu)
        #         at btn
        #     add "0GUI/mm/logo.png"

style mm_button:
    # background None
    # padding (0,0)
    focus_mask True
## Game Menu screen ############################################################

screen game_menu(title):
    style_prefix "gm"
    add bgs[1]
    transclude
    vbox:
        align(1.0,0.0)
        label title at btn
        button:
            at btn
            text "Return"
            action ShowMenu("navigation")

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style gm_viewport:
    xfill True xalign .5