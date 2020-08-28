default bazaar_street_loc = place("Street", (516, 343), Jump('street'), "bg/bazaar/street.png")
default akbar_loc = place("Akbar's shack", (0, 466), Jump('akbars_shack'), "bg/bazaar/akbar.png")
default fruits_loc = place("Fruits shack", (631, 581), Jump('fruit_shack'), "bg/bazaar/fruits.png")
default jewelry_loc = place("Jewelry", (798, 405), Jump('jewelry_shop'), "bg/bazaar/jewelry.png")
default rugs_loc = place("Rugs and rags shack", (868, 486), Jump('rugs_shop'), "bg/bazaar/rugs.png")
default tailor_loc = place("Tailor", (1195, 527), Jump('tailor'), "bg/bazaar/tailor.png")
default hakim_loc = place("Hakim", (1476, 75), Jump('hakim'), "bg/bazaar/hakim.png")

default alley_loc = place("Shady Alley", (71, 379), Jump('shady_alley'))
default bazaar_home_loc = place("Home", (1172, 31), Jump('agrabah'))

default bazaar_map = maps(
    "Bazaar",
    [
        bazaar_street_loc,
        akbar_loc,
        fruits_loc,
        jewelry_loc,
        rugs_loc,
        tailor_loc,
        hakim_loc,
        alley_loc,
        bazaar_home_loc,
    ]
    )


label bazaar:
    scene image "bg/bazaar.jpg"
    show screen map(bazaar_map)
    pause

# Fruit vendor
define sim = Character("Simin", color="#4ff", what_text_color="#dff")
image simin normal = "char/fruit_trader/normal.png"
default simin_u = unit(
    "Fruit trader",
    "char/fruit_trader",

    1641,
    [
        (dates, 42),
        (cantaloupe, 6),
        (pomegranate, 12),
        (watermelon, 3),
        (apple, 23),
    ],
    1.1,

    8,
    "Peasant",
    )
label fruit_shack:
    show simin normal at right
    sim "Dates?"
    show screen shop(s = simin_u, c = abdul)
    pause
    jump bazaar

# Jeweler
define jew = Character("Jeweler", color="#4ff", what_text_color="#dff")
image jeweler normal = "char/jeweler/normal.png"

default jeweler_u = unit(
    "Jeweler",
    "char/jeweler",

    9610,
    [
        (book3, 1),
        (arrows, 6),
    ],
    1.1,

    8,
    "Peasant",
    )
default jewelry_shop = True
label jewelry_shop:
    show jeweler normal at right
    jew "You don't look like you belong here! Did you find something valuable to sell?"
    show abd normal at left
    if abdul.has(black_lamp) and jewelry_shop:
        $ jewelry_shop = False
        abd "I've found this lamp in the desert."
        abd "Do you look like a junk trader?"
        jew "Take it elsewhere..."
    else:
        abd "No, I'm just browsing."
        jew "No browsing! Buys something or get out!"
    jump bazaar



# Akbar
define akb = Character("Akbar", color="#4ff", what_text_color="#dff")
image akbar normal = "char/akbar/normal.png"

default akbar = unit(
    "Akbar",
    "char/akbar",

    2210,
    [
        (wood, 20),
        (small_sword, 1),
        (bow, 1),
        (book1, 1),
        (book4, 1),
        (book2, 1),
        (arrows, 6),
        (water, 7),
    ],
    1.1,

    8,
    "Peasant",
    )

label akbars_shack:
    show akbar normal at right
    akb "Ah, Abdul. what can I help you with?"
    show abd normal at left
    abd "Do you need firewood today?"
    akb "Yes. How much are you selling."
    show screen shop(s = akbar, c = abdul)
    pause

    jump bazaar

# hakim
define hak = Character("Hakim", color="#4ff", what_text_color="#dff")
image hakim normal = "char/hakim/normal.png"

default hakim_u = unit(
    "Hakim",
    "char/hakim",

    1710,
    [
        (snake_bite_remedy, 2),
        (scorpion_bite_remedy, 5),
        (salt, 12),
        (saffron, 2),
        
    ],
    1.1,

    8,
    "Peasant",
    )

label hakim:
    show hakim normal at right
    hak "Ah, Abdul, how are you today, are you feeling sick again?"
    show abd normal at left
    menu:
        "Not today...":
            abd "Not today Hakim."
            hak "Have you came to buy a remedy?"
            abd "Let me see what you have."
        "Fond anything to erect old men yet Hakim?":
            abd "Fond anything to erect old men yet Hakim?"
            hak "Ah hahaha, This joke again? Let me know if there's anything I can do for you."
            abd "Sure. I'll take a look."
        "I've found this lamp..." if abdul.has(black_lamp):
            abd "I've found this lamp hakim."
            abd "Do you want to buy it?"
            hak "Hmmm... I do need a good old lamp for my nightly reading sessions."
            hak "Looks fine... How much are you selling it?"
            abd "For you hakim, 2000!"
            hak "You know I can't afford that abdul."
            hak "1500?"
            menu:
                "Sure":
                    abd "Sure"
                    hak "Thank you abdul. I'll make it up to you"
                    $ abdul.sell(black_lamp, 1, hakim_u, 1500)
                    hak "Do you want to buy something as well?"
                    abd "Sure."
                "Too low!":
                    abd "That's too low hakim."
                    hak "Alright, buy something and I might be able to buy it from you."
                    abd "Sure."
    hak "Choose wisely."
    #just added a cue from the seller, otherwise Abdul continues to slap his lips.
    # since we might add lip flip to vendors, "{nw}" should do the job as well
    show screen shop(s = hakim_u, c = abdul)
    pause
    jump bazaar

# Tailor
define far = Character("Farrokh the tailor", color="#4ff", what_text_color="#dff")
image farrokh normal = "char/farrokh/normal.png"

default tailor_u = unit(
    "Farrokh the tailor",
    "char/farrokh",

    3410,
    [
        (book1, 1),
        (book4, 1),
        (book2, 1),
    ],
    1.1,

    8,
    "Peasant",
    )

label tailor:
    show farrokh normal at right
    far "Do you need another stitching abdul?"
    show abd normal at left
    menu:
        "Not today...":
            abd "Not today Farrokh, I'm just browsing."
            far "Alright then, tell me if anything catches your eye."
        "I've found this lamp..." if abdul.has(black_lamp):
            abd "I've found this lamp in the desert."
            far "Hmmm... show it to Akbar. Or Hakim."
            far "I'll end up selling it to them if I buy it."
    show screen shop(s = tailor_u, c = abdul)
    pause
    jump bazaar


label rugs_shop:
    "Rugs?"
    abd "Not today."
    jump bazaar

label shady_alley:
    "There's some shady deals going on there."
    jump bazaar
