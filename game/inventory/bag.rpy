

init python:
    def return_mouse_pos():
        return renpy.get_mouse_pos()
    def bag_to_bag(source, destination):
        for i in source.items:
            if i:
                destination.add(i.item, i.qtt)
                source.rem(i.item, i.qtt)
    def cash_to_cash(source, destination):
        destination.cash += source.cash
        source.cash = 0



screen show_bag(p = hero, xside = 0.5):
    default mode = "stack"
    default options = 1
    modal True
    drag:
        xalign xside
        dragged p.dragged
        hbox:
            if p.bag_x > 650:
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
                                action Function(p.change, i), SelectedIf(i==p.selected)
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
                        for ii,i in enumerate(p.selected.items):
                            if i == None:
                                button:
                                    xysize 128,128 padding 0,0
                                    action Function(p.selected.pick, ii, p)
                            else:
                                button:
                                    xysize 128,128 padding 0,0
                                    background i.item.icon
                                    if i.qtt > 1:
                                        text "[i.qtt]" color "#fff" align(.9,.9)
                                    tooltip i
                                    if mode == "stack":
                                        action Function(p.selected.pick, ii, p)
                                    elif mode == "single":
                                        action Function(p.selected.pickOne, ii, p)
                                    elif mode == "eat":
                                        action Function(p.eat, i.item)
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
                        action Function(p.selected.shuffle)
                    button:
                        text "Eat / drink"
                        at btn
                        action SetScreenVariable("mode", "eat"), SelectedIf(mode == "eat")
                    button:
                        text "Close"
                        at btn
                        action Hide("show_bag")

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



default test_chest = inventory(
    12,
    [
        [wood, 2],
        [string, 5],
        [book2, 1]
    ],
    1.0
)



screen show_loot(e = test_chest, p = hero, mandatory = None):
    default mode = "stack"
    modal True
    drag:
        vbox:
            hbox:
                frame: # Your bag
                    padding 0,0 xsize 660
                    vbox:
                        hbox:
                            # text "[p.name]"
                            for i in p.bags:
                                button:
                                    text i.name
                                    at btn
                                    action Function(p.change, i), SelectedIf(i==p.selected)
                            hbox:
                                text "[p.cash]"
                                add "inventory/coin.png"

                        hbox:
                            spacing 4 box_wrap True box_wrap_spacing 4
                            for ii,i in enumerate(p.selected.items):
                                if i == None:
                                    button:
                                        xysize 128,128 padding 0,0
                                        action Function(p.selected.pick, ii, p)
                                else:
                                    button:
                                        xysize 128,128 padding 0,0
                                        background i.item.icon
                                        if i.qtt > 1:
                                            text "[i.qtt]" color "#fff" align(.9,.9)
                                        tooltip i
                                        if mode == "stack":
                                            action Function(p.selected.pick, ii, p)
                                        elif mode == "single":
                                            action Function(p.selected.pickOne, ii, p)
                                        elif mode == "eat":
                                            action Function(p.eat, i.item)

                frame: # Enemies bag
                    padding 0,0 xsize 660
                    vbox:
                        hbox:
                            # text "[e.name]"
                            for i in e.bags:
                                button:
                                    text i.name
                                    at btn
                                    action Function(e.change, i), SelectedIf(i==e.selected)
                            hbox:
                                text "[e.cash]"
                                add "inventory/coin.png"

                        hbox:
                            spacing 4 box_wrap True box_wrap_spacing 4
                            for ii,i in enumerate(e.selected.items):
                                if i == None:
                                    button:
                                        xysize 128,128 padding 0,0
                                        action Function(e.selected.pick, ii, p)
                                else:
                                    button:
                                        xysize 128,128 padding 0,0
                                        background i.item.icon
                                        if i.qtt > 1:
                                            text "[i.qtt]" color "#fff" align(.9,.9)
                                        tooltip i
                                        if mode == "stack":
                                            action Function(e.selected.pick, ii, p)
                                        elif mode == "single":
                                            action Function(e.selected.pickOne, ii, p)
                                        elif mode == "eat":
                                            action Function(p.eat, i.item)

            hbox:
                button:
                    text "Take all"
                    at btn
                    action Function(bag_to_bag, e.selected, p.selected)
                button:
                    text "Deposit all"
                    at btn
                    action Function(bag_to_bag, p.selected, e.selected)

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
                    action Function(p.selected.shuffle)
                button:
                    text "Close"
                    at btn
                    action Hide("show_loot")

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

    if mandatory:
        button:
            background None
            action NullAction()

    if mandatory == "give":
        timer .8 action Function(bag_to_bag, p.selected, e.selected)
        timer 1.6 action Return()
    elif mandatory == "take":
        timer .8 action Function(bag_to_bag, e.selected, p.selected)
        timer 1.6 action Return()
    elif mandatory == "give_cash":
        timer .8 action Function(cash_to_cash, p, e)
        timer 1.6 action Return()
    elif mandatory == "take_cash":
        timer .8 action Function(cash_to_cash, e, p)
        timer 1.6 action Return()



