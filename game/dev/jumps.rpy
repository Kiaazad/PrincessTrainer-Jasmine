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
            $ qlog.got(sell_lamp)
            $ abdul.add_flag("Meet Jafar")
            $ persistent.theme_change = 1
            $ calendar.day = 1
            $ qlog.got(jafars_revenge)
            $ qlog.cancel(sell_lamp)
            $ street_home_loc.enabled = True
            $ des_0_col.add(des_0_return)
            $ qlog.got(visit_malik)
            $ qlog.got(visit_hosein)
            $ abdul.gotskill(kick)
            $ abdul.gotskill(punch)
            $ qlog.got(master_swordsman)
            $ agrabah_lamp.hidden = False
            $ agrabah_lamp.act = Jump('inside_lamp')
            $ qlog.got(cash_in_hand)

            $ renpy.take_screenshot()
            $ renpy.save("1-1", extra_info='')
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
