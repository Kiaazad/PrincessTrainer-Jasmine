# default des_0_2 = col_obj("mini/collecting/1/02.png",
#     (578, 725), 1,
#     [[thorns, 1]],
#     )
# default des_0_3 = col_obj("mini/collecting/1/03.png",
#     (1700, 900), 1,
#     [[thorns, 1]]
#     )
# default des_0_4 = col_obj("mini/collecting/1/04.png",
#     (961, 633), 1,
#     [[thorns, 1]],
#     )

# default des_0_col = col_game("Roc pass", None,
#     [des_0_2, des_0_3, des_0_4]
#     )

# label desert_0:
#     scene black
#     show bg bg1
#     show screen collect(abdul, des_0_col, True, False)
#     with dissolve
#     show screen tut_timer(t=10, tut= "tut_1")
#     pause
#     hide tut_timer
#     return
# #----------------------

# #----------------------
# label desert:
#     scene black
#     show bg bg1 with dissolve
#     menu:
#         "Where to visit today?"
#         "Roc pass":
#             jump desert_1
#         "Salt bed":
#             jump desert_2
#         "Go to Agrabah":
#             return


# #----------------------
# default des_1_1 = col_obj("mini/collecting/1/01.png",
#     (1357, 596), 10,
#     [[wood, 7]],
#     tools = [axe, saw],
#     )
# default des_1_2 = col_obj("mini/collecting/1/02.png",
#     (578, 725), 1,
#     [[thorns, 1]],
#     )
# default des_1_3 = col_obj("mini/collecting/1/03.png",
#     (1700, 900), 1,
#     [[thorns, 1]]
#     )
# default des_1_4 = col_obj("mini/collecting/1/04.png",
#     (961, 633), 1,
#     [[thorns, 1]],
#     )
# default des_1_5 = col_obj("mini/collecting/1/05.png",
#     (342, 867), 1,
#     [[thorns, 1]],
#     )

# default des_1_col = col_game("Roc pass", "mini/collecting/1/bg.png",
#     [des_1_1, des_1_2, des_1_3, des_1_4, des_1_5]
#     )

# label desert_1:
#     scene black
#     show screen collect(abdul, des_1_col)
#     pause

#     return
# #----------------------
# default des_2_1 = col_obj("mini/collecting/2/01.png",
#     (1166, 782), 1,
#     [[wood, 1]],
#     )
# default des_2_2 = col_obj("mini/collecting/2/02.png",
#     (1659, 795), 1,
#     [[wood, 1]],
#     )
# default des_2_3 = col_obj("mini/collecting/2/03.png",
#     (1282, 795), 1,
#     [[wood, 1]],
#     )
# default des_2_4 = col_obj("mini/collecting/2/04.png",
#     (150, 788), 1,
#     [[wood, 2]],
#     )
# default des_2_5 = col_obj("mini/collecting/2/05.png",
#     (1038, 979), 1,
#     [[wood, 3]],
#     )
# default des_2_6 = col_obj("mini/collecting/2/06.png",
#     (1675, 839), 1,
#     [[wood, 1]],
#     )
# default des_2_7 = col_obj("mini/collecting/2/07.png",
#     (1541, 861), 1,
#     [[wood, 1]],
#     )
# # a
# default des_2_a1 = col_obj("mini/collecting/2/a1.png",
#     (1560, 562), 8,
#     [[wood, 4]],
#     tools = [axe, saw],
#     )
# default des_2_a2 = col_obj("mini/collecting/2/a2.png",
#     (1560, 562), 7,
#     [[wood, 5]],
#     tools = [axe, saw],
#     )
# default des_2_a3 = col_obj("mini/collecting/2/a3.png",
#     (1560, 562), 5,
#     [[wood, 3]],
#     tools = [axe, saw],
#     )
# default des_2_a4 = col_obj("mini/collecting/2/a4.png",
#     (1560, 562), 4,
#     [[wood, 2]],
#     tools = [axe, saw],
#     )

# default des_2_b1 = col_obj("mini/collecting/2/b1.png",
#     (1815, 671), 9,
#     [[wood, 7]],
#     tools = [axe, saw],
#     )
# default des_2_b2 = col_obj("mini/collecting/2/b2.png",
#     (1815, 671), 3,
#     [[wood, 4]],
#     tools = [axe, saw],
#     )

# default des_2_c1 = col_obj("mini/collecting/2/c1.png",
#     (480, 546), 12,
#     [[wood, 5]],
#     tools = [axe, saw],
#     )
# default des_2_c2 = col_obj("mini/collecting/2/c2.png",
#     (480, 546), 6,
#     [[wood, 5]],
#     tools = [axe, saw],
#     )
# default des_2_c3 = col_obj("mini/collecting/2/c3.png",
#     (480, 546), 2,
#     [[wood, 2]],
#     tools = [axe, saw],
#     )
# default des_2_c4 = col_obj("mini/collecting/2/c4.png",
#     (480, 546), 1,
#     [[wood, 3]],
#     )

# default des_2_d1 = col_obj("mini/collecting/2/d1.png",
#     (1055, 677), 8,
#     [[wood, 5]],
#     tools = [axe, saw],
#     )
# default des_2_d2 = col_obj("mini/collecting/2/d2.png",
#     (1055, 677), 3,
#     [[wood, 3]],
#     tools = [axe, saw],
#     )

# default des_2_e1 = col_obj("mini/collecting/2/e1.png",
#     (742, 681), 9,
#     [[wood, 6]],
#     tools = [axe, saw],
#     )
# default des_2_e2 = col_obj("mini/collecting/2/e2.png",
#     (742, 681), 2,
#     [[wood, 2]],
#     tools = [axe, saw],
#     )

# default des_2_f1 = col_obj("mini/collecting/2/f1.png",
#     (86, 674), 7,
#     [[wood, 7]],
#     tools = [axe, saw],
#     )
# default des_2_f2 = col_obj("mini/collecting/2/f2.png",
#     (86, 674), 3,
#     [[wood, 4]],
#     tools = [axe, saw],
#     )

# default des_2_axe = col_obj("mini/collecting/2/axe.png",
#     (126, 974), 1,
#     [[axe, 1]],
#     )


# default des_2_col = col_game("Salt bed", "mini/collecting/2/bg.png",
#     [
#     des_2_1, des_2_2, des_2_3, des_2_4, des_2_5, des_2_6, des_2_7,
#     des_2_a1, des_2_a2, des_2_a3, des_2_a4,
#     des_2_b1, des_2_b2,
#     des_2_c1, des_2_c2, des_2_c3, des_2_c4,
#     des_2_d1, des_2_d2,
#     des_2_e1, des_2_e2,
#     des_2_f1, des_2_f2,
#     des_2_axe,
#     ]
#     )

# label desert_2:
#     scene black
#     show screen collect(abdul, des_2_col)
#     pause

#     return