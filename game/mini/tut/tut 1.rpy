
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

screen tut(c):
    if len(c.tuts):
        timer 2.2 repeat True action Function(c.tut_show)
    else:
        timer .1 action Hide("tut")
screen tut_click(c):
    fixed:
        xysize 100,100 pos c[0],c[1] offset 20,20
        add "0GUI/pointer/01.png" at tut_clicked(1)
        add "0GUI/pointer/02.png" at tut_pointer(.3)
    timer 2 action Hide("tut_click")