init python:
    config.overlay_screens.append("item_inf")
screen item_inf:
    zorder 1000
    if GetTooltip():
        if type(GetTooltip()) is stack:
            hbox:
                align 0.0,1.0 offset 50,-44 spacing 0
                frame:
                    xsize 350 background Frame("_frm", 10,10)
                    vbox:
                        text GetTooltip().item.name color "#ff0"
                        text GetTooltip().item.inf
                        hbox:
                            text "{}".format(GetTooltip().item.val)
                            add "inventory/coin.png"
                add GetTooltip().item.icon yalign 0.0
        elif type(GetTooltip()) is item:
            hbox:
                align 0.0,1.0 offset 50,-44 spacing 0
                frame:
                    xsize 350 background Frame("_frm", 10,10)
                    vbox:
                        text GetTooltip().name color "#ff0"
                        text GetTooltip().inf
                        hbox:
                            text "{}".format(GetTooltip().val)
                            add "inventory/coin.png"
                add GetTooltip().icon yalign 0.0
        elif type(GetTooltip()) is spell:
            hbox:
                align 0.0,1.0 offset 50,-44 spacing 0
                frame:
                    xsize 350 background Frame("_frm", 10,10)
                    vbox:
                        text GetTooltip().name color "#ff0"
                        text GetTooltip().inf
                        if GetTooltip().hp:
                            text "Health {}".format(GetTooltip().hp)
                        if GetTooltip().mp:
                            text "Mana {}".format(GetTooltip().mp)
                        if GetTooltip().stm:
                            text "Stamina {}".format(GetTooltip().stm)
                        if GetTooltip().pwr:
                            text "Power {}".format(GetTooltip().pwr)
                        if GetTooltip().agl:
                            text "Agility {}".format(GetTooltip().agl)
                        if GetTooltip().effect:
                            for i in GetTooltip().effect:
                                text "Effects: {}".format(i[0].name)

                            
                add GetTooltip().icon yalign 0.0 