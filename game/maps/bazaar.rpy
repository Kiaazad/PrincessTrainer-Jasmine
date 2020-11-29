default bazaar_street_loc = pnco(
    "Street",
    "bg/bazaar/street.png",
    (516, 343),
    Jump('street'),
    hidden = False, hoffset = (40,60),
    )
default akbar_loc = pnco(
    "Akbar's shack",
    "bg/bazaar/akbar.png",
    (0, 466),
    Jump('akbars_shack'),
    hidden = False, hoffset = (200,0),
    )
default fruits_loc = pnco(
    "Fruits shack",
    "bg/bazaar/fruits.png",
    (631, 581),
    Jump('fruit_shack'),
    hidden = False, hoffset = (83,-40),
    )
default jewelry_loc = pnco(
    "Jewelry",
    "bg/bazaar/jewelry.png",
    (798, 405),
    Jump('jewelry_shop'),
    hidden = False, hoffset = (146,-80),
    )
default rugs_loc = pnco(
    "Rugs and rags shack",
    "bg/bazaar/rugs.png",
    (868, 486),
    Jump('rugs_shop'),
    hidden = False, hoffset = (200,0),
    )
default tailor_loc = pnco(
    "Tailor",
    "bg/bazaar/tailor.png",
    (1195, 527),
    Jump('tailor'),
    hidden = False, hoffset = (154,-80),
    )
default hakim_loc = pnco(
    "Hakim",
    "bg/bazaar/hakim.png",
    (1476, 75),
    Jump('hakim'),
    hidden = False, hoffset = (100,100),
    )

default alley_loc = pnco(
    "Shady Figure",
    "bg/bazaar/shady figure.png",
    (332, 602),
    Jump('shady_alley'),
    hidden = False, hoffset = (20,-80),
    )
default bazaar_home_loc = pnco(
    "Home",
    "bg/bazaar/poor.png",
    (407, 999),
    Jump('agrabah'),
    hidden = False, hoffset = (0,0),
    )
default bazaar_fatti = pnco(
    "Fatti",
    "bg/bazaar/fatti.png",
    (532, 669),
    Jump('bazaar_fatti'),
    hidden = False, hoffset = (43,106),
    )
default bazaar_map = pncs(
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
        bazaar_fatti,
    ]
    )

image bg bazaar = "bg/bazaar/bg.jpg"
label bazaar:
    scene
    show bg bazaar onlayer bg
    show screen pnc(abdul, bazaar_map)
    pause
    jump bazaar

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
    interests = [],
    reject = ["Weapon", "armor", "lamp"]
    )
label fruit_shack:
    scene
    show simin normal at right
    sim "Dates?"
    show abd normal at left
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
        (silver_ring, 7),
        (gold_ring, 3),
    ],
    1.1,

    8,
    "Peasant",
    interests = ["jewelry"],
    reject = ["food", "fuel", "Weapon", "armor", "lamp"]
    )
label jewelry_shop:
    scene
    if not "first" in jeweler_u.flags:
        show jeweler normal at right
        jew "You don't look like you belong here! Did you find something valuable to sell?"
        show abd normal at left
        if abdul.has(black_lamp) and not "shown lamp" in jeweler_u.flags:
            $ jeweler_u.add_flag("shown lamp")
            abd "I've found this lamp in the desert."
            abd "Do you look like a junk trader?"
            jew "Take it elsewhere..."
        else:
            abd "No, I'm just browsing."
            jew "No browsing! Buys something or get out!"
        $ jeweler_u.add_flag("first")
    else:
        show jeweler normal at right
        jew "What do you want?"
        show abd normal at left
        show screen shop(s = jeweler_u, c = abdul)
        pause
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
        (prayer_beads, 12),

    ],
    1.1,

    8,
    "Peasant",
    interests = [],
    reject = []
    )

label akbars_shack:
    scene
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
        (book2, 1),
        (book4, 1),

    ],
    1.1,

    8,
    "Peasant",
    interests = ["remedy"],
    reject = ["Weapon", "armor"]
    )

label hakim:
    scene
    if not "erect old" in hakim_u.flags or not "shown lamp" in hakim_u.flags:
        show hakim normal at right
        hak "Ah, Abdul, how are you today, are you feeling sick again?"
        show abd normal at left
        menu:
            "Not today...":
                abd "Not today Hakim."
                hak "Have you came to buy a remedy?"
                abd "Let me see what you have."
            "Fond anything to erect old men yet Hakim?" if not "erect old" in hakim_u.flags:
                $ hakim_u.add_flag("erect old")
                abd "Fond anything to erect old men yet Hakim?"
                hak "Ah hahaha, This joke again? Let me know if there's anything I can do for you."
                abd "Sure. I'll take a look."
            "I've found this lamp..." if abdul.has(black_lamp) and not "shown lamp" in hakim_u.flags:
                $ hakim_u.add_flag("shown lamp")
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
    else:
        show hakim normal at right
        hak "Ah, Abdul, nice to see you again."
        show abd normal at left
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
        (simple_hat, 2),
        (simple_shirt, 3),
        (simple_pants, 2),

    ],
    1.1,

    8,
    "Peasant",
    interests = ["textile"],
    reject = ["Weapon", "armor", "lamp"]
    )

label tailor:
    scene
    show farrokh normal at right
    far "Do you need another stitching abdul?"
    show abd normal at left
    menu:
        "Not today...":
            abd "Not today Farrokh, I'm just browsing."
            far "Alright then, tell me if anything catches your eye."
        "I've found this lamp..." if abdul.has(black_lamp) and not "shown lamp" in tailor_u.flags:
            $ tailor_u.add_flag("shown lamp")
            abd "I've found this lamp in the desert."
            far "Hmmm... show it to Akbar. Or Hakim."
            far "I'll end up selling it to them if I buy it."
    show screen shop(s = tailor_u, c = abdul)
    pause
    jump bazaar

# Rugs shop
define nem = Character("Nemat", color="#4ff", what_text_color="#dff")
image nemat normal = "char/nemat/normal.png"
label rugs_shop:
    scene
    show nemat normal at right
    nem "Rugs?"
    show abd normal at left
    abd "Not today."
    jump bazaar

# Shady alley
define pet = Character("Petros", color="#4ff", what_text_color="#dff")
image petros normal = "char/petros/normal.png"

default petros_u = unit(
    "Petros",
    "char/petros",

    3410,
    [
        (beer, 1),
        (liquor, 1),
        (wine, 1),
    ],
    1.2,

    8,
    "Peasant",
    interests = [],
    reject = ["Weapon", "armor", "lamp"]
    )
label shady_alley:
    scene
    show petros normal at right
    pet "Hey... Dabul... know any women to hook me up with?"
    show abd normal at left
    abd "It's Abdul, and no."
    pet "Came here to sin then? What's your choice?"
    show screen shop(s = petros_u, c = abdul)
    pause
    jump bazaar

# fat
define fat = Character("Fatti", color="#4ff", what_text_color="#dff")
image fatti normal = "char/pedestrians/fatti.png"
label bazaar_fatti:
    scene
    show fatti normal at right
    fat "What are you shopping for Abdul."
    show abd normal at left
    abd "Nothing."
    fat "Buy something to eat Abdul, you've wasting away."
    jump bazaar


