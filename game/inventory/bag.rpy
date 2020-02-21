
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

screen show_bag(p = abdul, xside = 0.0):
    default mode = "stack"
    default options = 0
    default selected_bag = p.bags[0]
    drag:
        xalign xside
        dragged selected_bag.drop
        hbox:
            
            if selected_bag.dropped_x > 650:
                box_reverse True
            frame:
                padding 0,0 xsize 660
                vbox:
                    hbox:
                        text "[p.name]"
                        for i in p.bags:
                            button:
                                text i.name
                                at btn
                                action SetScreenVariable("selected_bag", i), SelectedIf(i==selected_bag)
                        hbox:
                            text "[p.cash]"
                            add "inventory/coin.png"
                            
                        hbox:
                            button:
                                text "Options"
                                at btn
                                action ToggleScreenVariable("options", 1, 0)

                    hbox:
                        spacing 4 box_wrap True box_wrap_spacing 4
                        for ii,i in enumerate(selected_bag.items):
                            if i == None:
                                button:
                                    xysize 128,128 padding 0,0
                                    action Function(selected_bag.pick, ii, abdul)
                            else:
                                button:
                                    xysize 128,128 padding 0,0
                                    background i.item.icon
                                    if i.qtt > 1:
                                        text "[i.qtt]" color "#fff" align(.9,.9)
                                    tooltip i
                                    if mode == "stack":
                                        action Function(selected_bag.pick, ii, p)
                                    elif mode == "single":
                                        action Function(selected_bag.pickOne, ii, p)
            if options:
                vbox:
                    button:
                        text "Take Stacks"
                        at btn
                        action SetScreenVariable("mode", "stack"), SelectedIf(mode == "stack")
                    button:
                        text "Take One"
                        at btn
                        action SetScreenVariable("mode", "single"), SelectedIf(mode == "single")
                    button:
                        text "Discard"
                        at btn
                        action Function(p.discard)
                    button:
                        text "Shuffle"
                        at btn
                        action Function(selected_bag.shuffle)
    default mouse = (0,0)
    if p.holding:
        timer 0.02 repeat True action SetScreenVariable("mouse", renpy.get_mouse_pos())
        fixed:
            xysize 128,128
            pos mouse
            at holding_item_anim
            add p.holding.item.icon
            if p.holding.qtt > 1:
                text "[p.holding.qtt]" color "#fff" align(.9,.9)


transform holding_item_anim:
    alpha 0
    pause .05
    ease .1 alpha 1