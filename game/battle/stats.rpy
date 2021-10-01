screen stats(f, e):
    style_prefix "stats"
    frame:
        align 0.0,0.0 margin 30,30 background None
        hbox:
            for i in f.team:
                hbox:
                    spacing -10
                    fixed:
                        fit_first True
                        add "{}/001.png".format(i.dir) at flp
                        text str(i.lvl)
                    vbox:
                        fixed:
                            fit_first True
                            bar value i.hp range i.mhp xysize(110,24) left_bar "#f00" right_bar "#f005"
                            text "{} / {}".format(i.hp, i.mhp)
                        fixed:
                            fit_first True
                            bar value i.mp range i.mmp xysize(110,24) left_bar "#0ff" right_bar "#0ff5"
                            text "{} / {}".format(i.mp, i.mmp)
                        fixed:
                            fit_first True
                            bar value i.stm range i.mstm xysize(110,24) left_bar "#ff0" right_bar "#ff05"
                            text "{} / {}".format(i.stm, i.mstm)
                    

    frame:
        align 1.0,0.0 margin 30,30 background None
        hbox:
            box_reverse True
            for i in e.team:
                hbox:
                    spacing -10 box_reverse True
                    fixed:
                        fit_first True
                        add "{}/001.png".format(i.dir)
                        text str(i.lvl)
                    vbox:
                        fixed:
                            fit_first True
                            bar value i.hp range i.mhp xysize(110,24) left_bar "#f00" right_bar "#f005" at flp
                            text "{} / {}".format(i.hp, i.mhp)
                        fixed:
                            fit_first True
                            bar value i.mp range i.mmp xysize(110,24) left_bar "#0ff" right_bar "#0ff5" at flp
                            text "{} / {}".format(i.mp, i.mmp)
                        fixed:
                            fit_first True
                            bar value i.stm range i.mstm xysize(110,24) left_bar "#ff0" right_bar "#ff05" at flp
                            text "{} / {}".format(i.stm, i.mstm)
                    
style stats_text:
    size 20
    outlines [(2, "#000", 0, 0)]