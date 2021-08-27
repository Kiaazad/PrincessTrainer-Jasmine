

transform btl_t_b:
    on hover:
        ease .2 yoffset -20
    on idle:
        ease .2 yoffset 0
    on selected:
        ease .2 yoffset -40

screen btl_team(t = me_team):
    modal True
    default add_2_team = 0
    default caster = None
    default spell = None
    add "#000c"
    hbox:
        for ii, i in enumerate(t.team):
            button:
                background Frame("items/_frm.png", 10,10)
                at btl_t_b

                action SetScreenVariable("caster", i), SelectedIf(i == caster)
                vbox:
                    add "{}/001.png".format(i.dir)
                    frame:
                        xsize 300
                        text i.name size 30 color "#ff0"
                    fixed:
                        fit_first True
                        bar value i.exp range 100 xysize 300, 30 left_bar "#0f08" right_bar "#0f04"
                        text "level {} {}".format(i.lvl, i.type)
                    fixed:
                        fit_first True
                        bar value i.hp range i.mhp xysize 300, 30 left_bar "#900" right_bar "#9008"
                        text "Health: {} / {}".format(i.hp, i.mhp) xalign 0.0 xoffset 10
                    fixed:
                        fit_first True
                        bar value i.mp range i.mmp xysize 300, 30 left_bar "#069" right_bar "#0698"
                        text "Mana: {} / {}".format(i.mp, i.mmp) xalign 0.0 xoffset 10
                    fixed:
                        fit_first True
                        bar value i.stm range i.mstm xysize 300, 30 left_bar "#b70" right_bar "#b708"
                        text "Stamina: {} / {}".format(i.stm, i.mstm) xalign 0.0 xoffset 10
                    text "Power: {}".format(i.pwr) xalign 0.0 xoffset 10
                    text "Agility: {}".format(i.agl) xalign 0.0 xoffset 10
        if len(t.team) < t.size:
            button:
                text "Add"
                action ToggleScreenVariable("add_2_team", 1, 0)
    if add_2_team:
        hbox:
            box_wrap True
            for i in t.army:
                if i not in t.team:
                    button:
                        background Frame("items/_frm.png", 10,10)
                        action Function(t.add, i), ToggleScreenVariable("add_2_team", 1, 0)
                        hbox:
                            
                            add "{}/001.png".format(i.dir)
                            vbox:
                                hbox:
                                    text i.name size 30 color "#ff0"
                                    text "level {} {}".format(i.lvl, i.type)
                                hbox:
                                    vbox:
                                        text "Health: {} / {}".format(i.hp, i.mhp) xalign 0.0 xoffset 10
                                        text "Mana: {} / {}".format(i.mp, i.mmp) xalign 0.0 xoffset 10
                                        text "Stamina: {} / {}".format(i.stm, i.mstm) xalign 0.0 xoffset 10
                                    vbox:
                                        text "Power: {}".format(i.pwr) xalign 0.0 xoffset 10
                                        text "Agility: {}".format(i.agl) xalign 0.0 xoffset 10

    if caster:
        add "battle/spells.png" yalign 1.0
        hbox:
            yalign 1.0 spacing 2
            for ii, i in enumerate(caster.spells):
                if i:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add i.icon
                        tooltip i
                        action SetScreenVariable("spell", ii), SelectedIf(ii == spell)
                else:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add "spells/empty.png"
                        tooltip i
                        action SetScreenVariable("spell", ii), SelectedIf(ii == spell)
    if caster is not None:
        if spell is not None:
            add "#000c"
            frame:
                background Frame("items/_frm.png", 10,10) yalign .8
                hbox:
                    button:
                        padding 0,0 background None
                        add "items/_frm.png"
                        # tooltip no_spell
                        action Function(caster.spellput, None, spell), SetScreenVariable("spell", None)
                        
                    for i in caster.skills:
                        button:
                            padding 0,0 background None
                            add i.icon
                            tooltip i
                            action Function(caster.spellput, i, spell), SetScreenVariable("spell", None)

    button:
        align 1.0,1.0 offset -40,-40
        text "Return"
        action ToggleScreen("btl_team")