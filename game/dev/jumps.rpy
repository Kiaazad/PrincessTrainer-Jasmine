init python:
    config.underlay.append(
        renpy.Keymap(
            K_F7=lambda: renpy.jump("dev_jumps")
        )
    )
    config.underlay.append(
        renpy.Keymap(
            K_F10=lambda: renpy.show_screen("btl_arc")
        )
    )
label dev_jumps:
    menu:
        "city":
            jump street