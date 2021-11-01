screen quests(q = qlog):
    default filters = ["All", "Active", "Completed", "Canceled", "Failed"]
    default colors = {
        "All": "#fff",
        "Active": "#ffc",
        "Completed": "#6f0",
        "Canceled": "#005",
        "Failed": "#444",
    }
    modal True
    drag:
        frame:
            ysize 650
            hbox:
                vbox:
                    align 0.0,0.0
                    button:
                        xsize 300
                        at btn
                        text "Filter: {}".format(filters[q.filt]) color colors[filters[q.filt]]
                        action Function(q.filter)
                    viewport:
                        xsize 300 draggable True mousewheel True edgescroll 200,200
                        frame:
                            xsize 300
                            vbox:
                                for i in q.log:
                                    if i.stat == filters[q.filt] or filters[q.filt] == "All":
                                        button:
                                            at btn
                                            background None selected_foreground Frame("quests/arrow.png", 10,0,32,0) xalign 0.0 padding 10,10,40,10 
                                            text i.name:
                                                color colors[i.stat]
                                            action Function(q.chose, i), SelectedIf(i == q.slc)
                
                frame:
                    yfill True xsize 400
                    if q.slc:
                        viewport:
                            draggable True
                            vbox:
                                yalign 0.0
                                for i in q.slc.info:
                                    text i 
                        hbox:
                            yalign 1.0
                            text "Status:"
                            text q.slc.stat:
                                color colors[q.slc.stat]

    button:
        align 0.0,0.0 margin 100,100
        text "Return"
        action Hide("quests"), Return()

