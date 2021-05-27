init python:
    config.underlay.append(
        renpy.Keymap(
            K_F7=lambda: renpy.jump("dev_jumps")
        )
    )
    config.underlay.append(
        renpy.Keymap(
            K_F10=lambda: ToggleScreen("btl_arc")()
        )
    )
    config.underlay.append(
        renpy.Keymap(
            K_F6=lambda: ToggleScreen("show_loot")()
        )
    )
label dev_jumps:
    menu:
        "jump to the city":
            $ calendar.day = 1
            $ street_home_loc.enabled = True
            $ des_0_col.add(des_0_return)
            jump agrabah
        "jump to the lamp":
            $ calendar.day = 1
            $ street_home_loc.enabled = True
            $ des_0_col.add(des_0_return)
            jump lamp_visit

        "desert_1_dream":
            jump desert_1_dream
        "main menu":
            jump main_menu_jump

label main_menu_jump:
    return
