default street_loc = place("The street", (0.623, 0.574), Jump('street'))
default palace_loc = place("Palace", (0.679, 0.349), Jump('palace'))
default bazaar_loc = place("Bazaar", (0.816, 0.467), Jump('bazaar'))
default agrabah_map = maps(
    "Agrabah",
    [
        palace_loc,
        bazaar_loc,
        street_loc,
    ]
    )

label agrabah:
    scene image "bg/03.jpg"
    show screen map(agrabah_map)
    pause
