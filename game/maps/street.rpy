default street_desert_loc = place("Desert", (141, 742), Jump('desert'))
default street_palace_loc = place("Palace", (936, 674), Jump('palace'))
default street_bazaar_loc = place("Bazaar", (1172, 649), Jump('bazaar'))
default street_home_loc = place("Home", (1717, 706), Jump('agrabah'))
default street_map = maps(
    "Main street",
    [
        street_desert_loc,
        street_palace_loc,
        street_bazaar_loc,
        street_home_loc,
    ]
    )

label street:
    scene image "bg/street.jpg"
    show screen map(street_map)
    pause