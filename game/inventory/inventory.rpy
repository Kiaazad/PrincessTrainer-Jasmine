
screen inv(s = abdul):
    drag:
        frame:
            background "shop/shop.png" foreground "shop/shop1.png" xysize 480,740
            vbox:
                spacing 0
                viewport:
                    xysize 400,300 draggable True edgescroll (50,200) mousewheel True
                    frame:
                        padding 0,0 background None
                        hbox:
                            spacing 0 box_wrap True
                            for i in s.items:
                                button:
                                    xysize 100,100 padding 0,0
                                    background i.item.icon
                                    text "[i.qtt]" color "#fff" align(1.0, 1.0)
                                    tooltip i
                                    action Function(s.move, i.item, 1, s.items, s.finds)

                frame:
                    ysize 60 background None xpadding 30
                    hbox:
                        xfill True
                        text "[s.sum]" xalign 0.0
                        text "[s.cash]" xalign 1.0

                viewport:
                    xysize 400,300 draggable True edgescroll (50,200) mousewheel True
                    frame:
                        padding 0,0 background None
                        hbox:
                            spacing 0 box_wrap True
                            for i in s.finds:
                                button:
                                    xysize 100,100 padding 0,0
                                    background i.item.icon
                                    text "[i.qtt]" color "#fff" align(1.0, 1.0)
                                    tooltip i
                                    action Function(s.move, i.item, 1, s.finds, s.items)

