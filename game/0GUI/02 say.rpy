init offset = -1

## Say screen ##################################################################

screen say(who, what):
    style_prefix "say"
    if not persistent.theme_change:
        window:
            id "window"
            yalign 1.0
            xysize (1154,202)
            background "0gui/abdul_say.png"

            if who is not None:
                window:
                    align(0.5,0.0) background None yoffset -20
                    id "namebox"
                    text who id "who" outlines [ (5, "#000d", 0, 0) ]
            label what id "what" xsize 1000 background None text_size 30
    else:
        window:
            id "window"
            yalign 0.0
            xsize 920
            yminimum 101
            padding 30,10
            background Frame("0gui/say.png", 0, 20, 0, 30)
            label what id "what" background None text_size 30 yoffset -10

        if who is not None:
            window:
                xsize 510 padding 0,0 id "namebox" background None align (1.0, 0.0)
                frame:
                    id "namebox1"
                    background Frame("0gui/namebox.png", 0, 25, 0, 70)
                    padding 30,5,50,5 xalign 0.0
                    ysize 87
                    text who id "who"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

init python:
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('namebox1')

## Choice screen ###############################################################
define menu_shuffle = 0
define menu_shuffle_keeper = 1
screen choice(items):
    style_prefix "cho"
    
    if menu_shuffle: # needs work
        on "hide" action SetVariable("menu_shuffle_keeper", 1) 
        if menu_shuffle_keeper:
            timer .001 action SetVariable("menu_shuffle_keeper", 0)
            $ renpy.random.shuffle(items)

    vbox:
        for i in items:
            textbutton i.caption action i.action xsize 1000 at btn

define config.narrator_menu = True

## Input screen ################################################################

screen input(prompt):
    style_prefix "inp"
    window:
        vbox:
            text prompt
            frame:
                xsize 400
                input id "input"

## Quick Menu screen ###########################################################

screen quick_menu():
    zorder 100
    if not persistent.theme_change:
        add "0gui/abdul_frm.png"
    else:
        add "0gui/frm.png" yalign 0.0
        if quick_menu:
            hbox:
                style_prefix "q"
                align 0.0,0.0
                button:
                    background None
                    add "0gui/q.png"
                    action ShowMenu('navigation')
    if not quick_menu:
        key "game_menu" action Function(msg.msg, renpy.random.choice(["Nope", "not yet", "Not available this early", "you don't have to save this early", "you'll get access to the settings before the sex sounds start", "if it's the full screen bothering you just press alt+enter or F11", "keep your pants on"]))
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style q_button_text:
    size 16
style q_button:
    padding(8,4)

## NVL screen ##################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing

        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0
                use nvl_dialogue(dialogue)

        else:
            use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None
                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

define config.nvl_list_length = gui.nvl_list_length