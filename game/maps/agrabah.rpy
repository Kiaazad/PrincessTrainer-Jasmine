default palace_loc = place("Palace", (924, 77), Jump('palace'), "bg/agrabah/palace.png")
default barracks_loc = place("Barracks", (1583, 448), Jump('barracks'), "bg/agrabah/barracks.png")
default poor_loc = place("Poor section", (1654, 508), Jump('poor_town'), "bg/agrabah/poor.png")
default rich_loc = place("Rich section", (719, 512), Jump('rich_town'), "bg/agrabah/rich.png")
default school_loc = place("School", (936, 533), Jump('school'), "bg/agrabah/school.png")
default bazaar_loc = place("Bazaar", (1309, 496), Jump('bazaar'), "bg/agrabah/bazaar.png")
default street_loc = place("Main street", (832, 525), Jump('street'), "bg/agrabah/street.png")
default middle_loc = place("Mid town", (1191, 587), Jump('mid_town'), "bg/agrabah/middle.png")
default bed_loc = place("Bed", (1145, 729), Jump('sleeping'), "bg/agrabah/bed.png")

default agrabah_map = maps(
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
    ]
    )

label agrabah:
    scene image "bg/03.jpg"
    show screen map(agrabah_map)
    pause

label school:
    "You don't have anything to do in a school."
    jump agrabah

label mid_town:
    "Not ready yet."
    jump agrabah

label rich_town:
    "Not ready yet."
    jump agrabah

label poor_town:
    "Not ready yet."
    jump agrabah

label barracks:
    "Don't put your nose in guard's business."
    jump agrabah

label sleeping:
    "Resting for a while."
    jump agrabah