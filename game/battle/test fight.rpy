
default test1_team = team([abdul])
default test2_team = team([warrior_man])
label test_fight_1:
    scene image "#333"
    show image "bg/fight.png"
    window hide
    show screen btl_scr(test1_team, test2_team)
    pause
    return
    