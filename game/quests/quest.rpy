
screen quests(q = qlog):
    default filters = ["All", "Active", "Completed", "Finished", "Canceled", "Failed"]
    default colors = {
        "Completed": "#fd0",
        "Finished": "#6f0",
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
                        text "Filter: {}".format(filters[q.filt])
                        action Function(q.filter)
                    for i in q.log:
                        if i.stat == filters[q.filt] or filters[q.filt] == "All":
                            button:
                                background None selected_foreground Frame("quests/arrow.png", 10,0,32,0) xalign 0.0 padding 10,10,40,10 
                                text i.name:
                                    if i.stat == "Completed":
                                        color colors["Completed"]
                                    elif i.stat == "Finished":
                                        color colors["Finished"]
                                    elif i.stat == "Canceled":
                                        color colors["Canceled"]
                                    elif i.stat == "Failed":
                                        color colors["Failed"]
                                action Function(q.chose, i), SelectedIf(i == q.slc)
                
                frame:
                    yfill True xsize 400
                    if q.slc:
                        text q.slc.inf yalign 0.0
                        hbox:
                            yalign 1.0
                            text "Status:"
                            text q.slc.stat:
                                if q.slc.stat == "Completed":
                                    color colors["Completed"]
                                elif q.slc.stat == "Finished":
                                    color colors["Finished"]
                                elif q.slc.stat == "Canceled":
                                    color colors["Canceled"]
                                elif q.slc.stat == "Failed":
                                    color colors["Failed"]

    button:
        align 0.0,0.0 margin 100,100
        text "Return"
        action Hide("quests"), Return()


    # drag:
    #     align(0.848, 0.522)
    #     frame:
    #         vbox:
    #             text "Tests"
    #             button:
    #                 text "Add"
    #                 action Function(q.got, sell_lamp), Function(q.got, jafars_revenge), Function(q.got, visit_malik), Function(q.got, visit_hosein), Function(q.got, master_swordsman)
    #             button:
    #                 text "Complete"
    #                 action Function(q.complete, sell_lamp), Function(q.complete, jafars_revenge), Function(q.complete, visit_malik), Function(q.complete, visit_hosein)
    #             button:
    #                 text "Finish"
    #                 action Function(q.finish, sell_lamp), Function(q.finish, jafars_revenge), Function(q.finish, visit_malik)
    #             button:
    #                 text "Cancel"
    #                 action Function(q.cancel, sell_lamp), Function(q.cancel, jafars_revenge)
    #             button:
    #                 text "Fail"
    #                 action Function(q.fail, sell_lamp)