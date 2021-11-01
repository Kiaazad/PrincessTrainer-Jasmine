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
            $ sell_lamp.cancel()
            $ street_home_loc.enabled = True

            $ roc_pass_agrabahs_gate.hidden = False
            $ roc_pass_snakes_pass.hidden = False
            $ snake_pass_roc_pass.hidden = False
            $ roc_pass_marble_quarry.hidden = False

            $ qlog.got(visit_malik)
            $ qlog.got(visit_hosein)
            $ abdul.got_skill(kick)
            $ abdul.got_skill(punch)
            $ qlog.got(master_swordsman)
            $ agrabah_lamp.hidden = False
            $ agrabah_lamp.act = Jump('inside_lamp')
            $ qlog.got(cash_in_hand)
            $ qlog.got(my_to_do_list)

            $ renpy.take_screenshot()
            $ renpy.save("1-1", extra_info='')
            jump agrabah
        "jump to the lamp":
            $ calendar.day = 1
            $ street_home_loc.enabled = True

            $ roc_pass_agrabahs_gate.hidden = False
            $ roc_pass_snakes_pass.hidden = False
            $ snake_pass_roc_pass.hidden = False
            $ roc_pass_marble_quarry.hidden = False
            jump lamp_visit

        "desert_1_dream":
            jump desert_1_dream
        "visiting_widow":
            jump visiting_widow
        "main menu":
            jump main_menu_jump

label main_menu_jump:
    return
