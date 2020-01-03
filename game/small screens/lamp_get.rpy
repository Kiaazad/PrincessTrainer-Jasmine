transform lamp_get_trans:
    alpha 0 align (.5,.5) zoom 3 rotate 45
    ease .2 alpha 1
    ease .4 align (0.0,0.0) zoom .2 rotate 0

screen lamp_get:
    zorder 1100
    button:
        background None
        at lamp_get_trans
        add "small screens/lamp.png"
        action Jump("lamp_visit")