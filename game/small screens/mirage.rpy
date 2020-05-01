transform mirage_t(a):
    ease 1 alpha a
transform delayed(p):
    alpha 0
    pause p
    alpha 1
transform fade_to_screen:
    alpha .2 zoom .01
    ease 3 zoom 100 alpha 0
screen mirage_1:
    default alph = 0
    default intervals = 1
    if intervals < 20:
        timer 2 repeat True action SetScreenVariable("alph", .1), SetScreenVariable("intervals", intervals+1)
        timer intervals*.1 repeat True action SetScreenVariable("alph", 0)
    else:
        timer .01 action Return()
    if intervals == 5:
        text "Abdul" at fade_to_screen
    elif intervals == 10:
        text "Abdul" at fade_to_screen
    elif intervals == 15:
        text "Come to me" at fade_to_screen
    frame:
        background "#000"
        at mirage_t(float(intervals)/20)
    frame:
        background None yalign 1.0 padding 0,0
        at delayed(1)
        add "char/jasmine/seducing.png" at mirage_t(alph) 