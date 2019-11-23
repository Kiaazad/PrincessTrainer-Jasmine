init python:
    def msg3(m):
        t = "fight_notif{}".format(renpy.random.randint(1, 10000))
        renpy.show_screen("fight_notif", msg = m, tag = t, _tag = t)

transform fight_notif_trans:
    parallel:
        ease 1.2 yoffset -200
    parallel:
        pause .2
        ease 1 alpha 0

screen fight_notif(msg, tag):
    zorder 2000
    timer 1.3 action Hide(tag)
    default p = renpy.get_mouse_pos()
    text "{}".format(msg) at fight_notif_trans pos p size 40 color "#ff0" outlines [ (4, "#000", 0, 0) ]