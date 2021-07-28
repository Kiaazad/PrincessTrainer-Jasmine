
# Exists
default beduins_camp_back = pnco(
    "Back",
    None,
    (911, 729),
    Jump('desert'),
    hidden = False, hoffset = (83,-40),
    )
default beduins_camp_ruins = pnco(
    "The ruins",
    None,
    (560, 467),
    Jump('ruins'),
    )

# Fights
default sand_warrior = unit(
    "Sand warrior",
    "char/sand_warrior",
    lvl = 5,
    type = "Warrior",
    )
default beduins_camp_sand_warrior = pnco(
    "Sand warrior",
    "bg/beduins_camp/sand_warrior.png",
    (1240, 660),
    Jump('beduins_camp_sand_warrior'),
    )
label beduins_camp_sand_warrior:
    call screen btl_scr(team([abdul]), team([sand_warrior]))
    jump beduins_camp

default beduins_camp_loc = pncs(
    "Main street",
    [
        beduins_camp_back,
        beduins_camp_ruins,
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

