
# Exists
default beduins_camp_agrabahs_gate = pnco(
    "Agrabah's gate",
    None,
    (980, 1009),
    Jump('agrabahs_gate'),
    hidden = False, hoffset = (83,-40),
    )
default beduins_old_gate = pnco(
    "Old gate",
    None,
    (1734, 704),
    Jump('old_gate'),
    )
default beduins_heaven_or_hell_fork = pnco(
    "Heaven or hell fork",
    None,
    (91, 714),
    Jump('heaven_or_hell_fork'),
    )
# Fights
default sand_warrior = unit(
    "Sand warrior",
    "char/foes/sand_warrior",
    lvl = 5,
    type = "Warrior",
    items = [(quartz_bit, 1)]
    )
default beduins_camp_sand_warrior = pnco(
    "Sand warrior",
    "bg/beduins_camp/sand_warrior.png",
    (1240, 660),
    Jump('beduins_camp_sand_warrior'),
    aggressive = True,
    )
default a_diamond_to_sell = quest(
    _("A diamond to sell"),
    [_("This might be a diamond, I must show it to the jeweler, or better Jafar.")],
    )
label beduins_camp_sand_warrior:
    call screen btl_scr(team([abdul]), team([sand_warrior]))
    if hero.has(quartz_bit):
        show abd normal at left
        abd "A gem stone?"
        $ qlog.got(a_diamond_to_sell)
    jump beduins_camp

default beduins_camp_loc = pncs(
    "Beduins camp",
    [
        beduins_camp_agrabahs_gate,
        beduins_old_gate,
        beduins_heaven_or_hell_fork,
        beduins_camp_sand_warrior,
    ], night = "bg/beduins_camp/night.webp"
    )

image bg beduins_camp = "bg/beduins_camp/bg.webp"
label beduins_camp:
    if not beduins_camp_loc in all_places:
        $ all_places.append(beduins_camp_loc)
    scene
    show bg beduins_camp onlayer bg
    show screen pnc(abdul, beduins_camp_loc)

    pause
    jump beduins_camp

