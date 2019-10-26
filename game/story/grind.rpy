

label endless_grind:
    # $ quick_menu = True
    hide screen skips
    scene black
    show screen endless_grind_msg
    # show screen map(agrabah_st)
    # show screen clock
    pause
    hide screen endless_grind_msg
    jump ch0
screen endless_grind_msg:
    vbox:
        text "This branch of the game isn't ready yet."
        text "I'll return you to an earlier point. Rub the lamp this time."