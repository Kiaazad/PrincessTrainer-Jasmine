default akbar_loc = place("Akbar's shop", (1731, 750), Jump('bazaar'))
# default fruits_loc = place("Fruits shack", (0.816, 0.467), Jump('bazaar'))
# default jewelry_loc = place("Jewelry", (0.816, 0.467), Jump('bazaar'))
# default alley_loc = place("Alley", (0.816, 0.467), Jump('bazaar'))
default bazaar_street_loc = place("The main street", (1260, 737), Jump('street'))
default bazaar_home_loc = place("Home", (69, 620), Jump('agrabah'))
default bazaar_map = maps(
    "Bazaar",
    [
        akbar_loc,
        bazaar_street_loc,
    ]
    )


label bazaar:
    scene image "bg/bazaar.jpg"
    show screen map(bazaar_map)
    pause