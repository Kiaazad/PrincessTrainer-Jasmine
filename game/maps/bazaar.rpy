default bazaar_street_loc = place("Street", (516, 343), Jump('street'), "bg/bazaar/street.png")
default asghar_street_loc = place("Akbar's shack", (0, 466), Jump('akbars_shop'), "bg/bazaar/asghar.png")
default fruits_loc = place("Fruits shack", (631, 581), Jump('fruit_shack'), "bg/bazaar/fruits.png")
default jewelry_loc = place("Jewelry", (798, 405), Jump('jewelry_shop'), "bg/bazaar/jewelry.png")
default rugs_loc = place("Rugs and rags shack", (868, 486), Jump('rugs_shop'), "bg/bazaar/rugs.png")
default akbar_loc = place("Hakim", (1195, 527), Jump('hakim'), "bg/bazaar/akbar.png")
default front_loc = place("Akbar's shop", (1476, 75), Jump('front_shop'), "bg/bazaar/front.png")


default alley_loc = place("Shady Alley", (71, 379), Jump('shady_alley'))
default bazaar_home_loc = place("Home", (1172, 31), Jump('agrabah'))
default bazaar_map = maps(
    "Bazaar",
    [
        bazaar_street_loc,
        asghar_street_loc,
        fruits_loc,
        jewelry_loc,
        rugs_loc,
        akbar_loc,
        front_loc,
        alley_loc,
        bazaar_home_loc,
    ]
    )


label bazaar:
    scene image "bg/bazaar.jpg"
    show screen map(bazaar_map)
    pause

label fruit_shack:
    "Dates?"
    abd "Not today."
    "Alright."
    jump bazaar

label jewelry_shop:
    show jeweler normal at right
    jew "You don't look like you belong here! Did you find something valuable to sell?"
    show abd normal at left
    abd "No, I'm just browsing."
    jew "No browsing! Buys something or get out!"
    jump bazaar

label shady_alley:
    "There's some shady deals going on there."
    jump bazaar

label akbars_shop:
    show akbar normal at right
    akb "Ah, Abdul. what can I help you with?"
    show abd normal at left
    abd "Do you need firewood today?"
    akb "Yes. How much are you selling."
    show screen shop(s = akbar, c = abdul)
    pause

    jump bazaar

label hakim:
    show hakim normal at right
    hak "Ah, Abdul, how are you today, are you feeling sick again?"
    show abd normal at left
    abd "Not today Hakim."
    hak "Have you came to buy a remedy?"
    abd "No, just came to say hello."
    hak "Ah, how nice of you. Let me know if there's anything I can do for you."
    abd "Sure."
    jump bazaar

label rugs_shop:
    "Rugs?"
    abd "Not today."
    jump bazaar

label front_shop:
    "This shop is empty."
    jump bazaar





