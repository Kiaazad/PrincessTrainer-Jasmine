default palace_loc = pnco(
    "Palace",
    "bg/agrabah/palace.png",
    (924, 77),
    Jump('palace'),
    hidden = False, hoffset = (114,80),
    )
default barracks_loc = pnco(
    "Barracks",
    "bg/agrabah/barracks.png",
    (1583, 448),
    Jump('barracks'),
    hidden = False, hoffset = (12,-66),
    )
default poor_loc = pnco(
    "Poor section",
    "bg/agrabah/poor.png",
    (1654, 508),
    Jump('poor'),
    hidden = False, hoffset = (80,-80),
    )
default rich_loc = pnco(
    "Rich section",
    "bg/agrabah/rich.png",
    (719, 512),
    Jump('rich'),
    hidden = False, hoffset = (100,-60),
    )
default school_loc = pnco(
    "School",
    "bg/agrabah/school.png",
    (936, 533),
    Jump('school'),
    hidden = False, hoffset = (50,-80),
    )
default bazaar_loc = pnco(
    "Bazaar",
    "bg/agrabah/bazaar.png",
    (1309, 496),
    Jump('bazaar'),
    hidden = False, hoffset = (120,-80),
    )
default street_loc = pnco(
    "Main street",
    "bg/agrabah/street.png",
    (832, 525),
    Jump('street'),
    hidden = False, hoffset = (300,-40),
    )
default caravanserai_loc = pnco(
    "Caravanserai",
    "bg/agrabah/middle.png",
    (1191, 587),
    Jump('caravanserai'),
    hidden = False, hoffset = (300,-80),
    )
default bed_loc = pnco(
    "Bed",
    "bg/agrabah/bed.png",
    (1145, 729),
    Jump('sleeping'),
    hidden = False, hoffset = (340,100),
    )

default agrabah_coins = pnco(
    "Coins",
    "bg/agrabah/coins.png",
    (192, 874),
    items = [30]
    )

default agrabah_lamp = pnco(
    "Lamp",
    "bg/agrabah/lamp.png",
    (10, 854),
    Jump('lamp_visit'),
    hoffset = (340,100),
    hidden = True
    )
default vantage_point = pnco(
    "The vantage point",
    None,
    (521, 328),
    Jump('vantage_point'),
    hoffset = (340,100),
    hidden = True,
    )

default agrabah_map = pncs(
    "Agrabah",
    [
        palace_loc,
        barracks_loc,
        poor_loc,
        rich_loc,
        school_loc,
        bazaar_loc,
        street_loc,
        caravanserai_loc,
        bed_loc,
        agrabah_lamp,
        agrabah_coins,
        vantage_point,
    ], night = "bg/agrabah/night.jpg"
    )

image bg agrabah = "bg/agrabah/bg.jpg"
label agrabah:
    scene
    show bg agrabah onlayer bg
    show screen pnc(abdul, agrabah_map)
    pause
    jump agrabah


label sleeping:
    show screen time_pass(renpy.random.randint(3,10))
    "Resting for a while."
    jump agrabah