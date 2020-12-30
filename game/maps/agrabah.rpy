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
default middle_loc = pnco(
    "Mid town",
    "bg/agrabah/middle.png",
    (1191, 587),
    Jump('mid_town'),
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
        middle_loc,
        bed_loc,
        
        agrabah_coins,
    ]
    )

image bg agrabah = "bg/agrabah/bg.jpg"
label agrabah:
    scene
    show bg agrabah onlayer bg
    show screen pnc(abdul, agrabah_map)
    pause
    jump agrabah




label mid_town:
    "Not ready yet."
    jump agrabah




label sleeping:
    "Resting for a while."
    jump agrabah