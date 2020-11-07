init python:
    config.underlay.append(
        renpy.Keymap(
            K_F7=lambda: renpy.jump("dev_jumps")
        )
    )

label dev_jumps:
    menu:
        "city":
            jump street