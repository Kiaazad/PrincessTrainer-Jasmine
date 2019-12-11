
screen tool_bar:
    hbox:
        yalign 1.0 spacing 2
        for i in caster.spells:
            if i:
                button:
                    padding 0,0 background None
                    at btl_t_b
                    add i.icon
                    tooltip i
                    action SetScreenVariable("spell", i)
            else:
                button:
                    padding 0,0 background None
                    at btl_t_b
                    add "spells/empty.png"
                    tooltip i
                    action SetScreenVariable("spell", i)