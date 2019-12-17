default akbar_loc = place("Akbar's shop", (1768, 561), Jump('akbars_shop'))
default fruits_loc = place("Fruits shack", (936, 517), Jump('fruit_shack'))
default jewelry_loc = place("Jewelry", (1583, 599), Jump('jewelry_shop'))
default alley_loc = place("Shady Alley", (71, 379), Jump('shady_alley'))
default bazaar_street_loc = place("The main street", (1339, 599), Jump('street'))
default bazaar_home_loc = place("Home", (1172, 31), Jump('agrabah'))
default bazaar_map = maps(
    "Bazaar",
    [
        akbar_loc,
        fruits_loc,
        jewelry_loc,
        alley_loc,
        bazaar_home_loc,
        bazaar_street_loc,
    ]
    )


label bazaar:
    scene image "bg/bazaar.jpg"
    show screen map(bazaar_map)
    pause

label akbars_shop:
    "Ah, Abdul. what can I help you with?"
    abd "Do you need firewood today?"
    "Maybe tomorrow."
    abd "Alright."
    jump bazaar

label fruit_shack:
    "Dates?"
    abd "Not today."
    "Alright."
    jump bazaar

label jewelry_shop:
    "You don't look like you belong here! Did you find something valuable to sell?"
    abd "No, I'm just browsing."
    "No browsing! Buys something or get out!"
    jump bazaar

label shady_alley:
    "There's some shady deals going on there."
    jump bazaar







