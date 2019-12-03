default des_0_2 = col_obj("mini/collecting/1/02.png",
    (578, 725), 1,
    [[thorns, 1]],
    )
default des_0_3 = col_obj("mini/collecting/1/03.png",
    (1700, 900), 1,
    [[thorns, 1]]
    )
default des_0_4 = col_obj("mini/collecting/1/04.png",
    (961, 633), 1,
    [[thorns, 1]],
    )

default des_0_col = col_game("Roc pass", None,
    [des_0_2, des_0_3, des_0_4]
    )

label desert_0:
    scene black
    show bg bg1
    show screen collect(abdul, des_0_col, True, False)
    with dissolve
    show screen tut_timer(t=10, tut= "tut_1")
    pause
    hide tut_timer
    return
#----------------------
