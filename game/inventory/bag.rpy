
default test_bag = bag(
    "test bag",
    20,
    [
        (wood, 20),
        (snake_bite_remedy, 2),
        (scorpion_bite_remedy, 5),
        (small_sword, 1),
        (bow, 1),
        (book1, 1),
        (book4, 1),
        (book2, 1),
        (book3, 1),
        (arrows, 6),
    ],
)

init python:
    def return_mouse_pos():
        return renpy.get_mouse_pos()

screen show_bag(s = test_bag, p = abdul):
    default mode = "stack"

    drag:
        frame:
            padding 0,0 background None xsize 656
            hbox:
                spacing 4 box_wrap True box_wrap_spacing 4
                for ii,i in enumerate(s.items):
                    if i == None:
                        button:
                            xysize 128,128 padding 0,0
                            action Function(s.pick, ii, abdul)
                    else:
                        button:
                            xysize 128,128 padding 0,0
                            background i.item.icon
                            text "[i.qtt]" color "#fff" align(.9,.9)
                            tooltip i
                            if mode == "stack":
                                action Function(s.pick, ii, p)
                            elif mode == "single":
                                action Function(s.pickOne, ii, p)
                hbox:
                    button:
                        text "Take stack"
                        action SetScreenVariable("mode", "stack")
                    button:
                        text "Take one"
                        action SetScreenVariable("mode", "single")
                    button:
                        text "Discard"
                        action Function(p.discard)
                    button:
                        text "Shuffle"
                        action Function(s.shuffle)
    default mouse = (0,0)
    if p.holding:
        timer 0.02 repeat True action SetScreenVariable("mouse", renpy.get_mouse_pos())
        fixed:
            xysize 128,128
            pos mouse
            at holding_item_anim
            add p.holding.item.icon
            text "[p.holding.qtt]" color "#fff" align(.9,.9)


transform holding_item_anim:
    alpha 0
    pause .05
    ease .1 alpha 1