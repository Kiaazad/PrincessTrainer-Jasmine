default street_desert_loc = place("Desert", (141, 742), Jump('desert'))
default street_palace_loc = place("Palace", (711, 357), Jump('palace'), "bg/street/palace.png")
default street_bazaar_loc = place("Bazaar", (1333, 610), Jump('bazaar'))
default street_home_loc = place("Home", (1464, 200), Jump('agrabah'), "bg/street/home.png")
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
    scene image "bg/street.png"
    show screen map(street_map)
    pause