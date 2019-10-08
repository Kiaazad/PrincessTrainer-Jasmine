
transform tut_clicked(p):
    alpha 0 zoom .1
    pause p
    alpha 1
    ease 1 zoom 2 alpha 0

transform tut_pointer(p):
    xoffset renpy.random.randint(-200, 200)
    yoffset renpy.random.randint(-200, 200)
    alpha 0
    pause p
    ease .2 alpha 1
    parallel:
        ease_back .4 xoffset 0
    parallel:
        ease .3 yoffset 0
    ease 1 alpha 0

screen tut_timer(t, tut):
    timer t repeat True action Show(tut)

screen tut_1:
    if len(des_0_col.lst) == 3:
        timer 4 action Hide("tut_1")
        fixed:
            xysize 100,100 pos(1702, 920)
            add "0GUI/pointer/01.png" at tut_clicked(1)
            add "0GUI/pointer/02.png" at tut_pointer(.3)
        fixed:
            xysize 100,100 pos(962, 639)
            add "0GUI/pointer/01.png" at tut_clicked(2)
            add "0GUI/pointer/02.png" at tut_pointer(1.3)
        fixed:
            xysize 100,100 pos(576, 729)
            add "0GUI/pointer/01.png" at tut_clicked(3)
            add "0GUI/pointer/02.png" at tut_pointer(2.3)





    