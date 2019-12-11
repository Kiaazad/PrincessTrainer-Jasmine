default des_1_1 = col_obj("mini/collecting/1/01.png",
    (1357, 596), 10,
    [[wood, 7]],
    tools = [axe, saw],
    )
default des_1_2 = col_obj("mini/collecting/1/02.png",
    (578, 725), 1,
    [[thorns, 1]],
    )
default des_1_3 = col_obj("mini/collecting/1/03.png",
    (1700, 900), 1,
    [[thorns, 1]]
    )
default des_1_4 = col_obj("mini/collecting/1/04.png",
    (961, 633), 1,
    [[thorns, 1]],
    )
default des_1_5 = col_obj("mini/collecting/1/05.png",
    (342, 867), 1,
    [[thorns, 1]],
    )

default des_1_col = col_game("Roc pass", "mini/collecting/1/bg.png",
    [des_1_1, des_1_2, des_1_3, des_1_4, des_1_5]
    )

label desert_1:
    scene black
    show screen collect(abdul, des_1_col)
    pause

    return