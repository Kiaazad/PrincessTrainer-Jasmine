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
default bazaar_poor_loc = pnco(
    "Poor section",
    "bg/bazaar/poor.png",
    (407, 999),
    Jump('poor'),
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
        bazaar_poor_loc,
        bazaar_fatti,
    ], night = "bg/bazaar/night.jpg"
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
    call screen shop(s = simin_u)
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
        if hero.has(black_lamp) and not "shown lamp" in jeweler_u.flags:
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
        call screen shop(s = jeweler_u)
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
    call screen shop(s = akbar)
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
    show hakim normal at right
    if not "first" in hakim_u.flags:
        hak "Ah, Abdul, how are you today, are you feeling sick again?"
        $ hakim_u.add_flag("first")
    else:
        hak "Abdul, you're back."
    show abd normal at left
    menu:
        # planted_evidence
        "I just came to say hi." if qlog.has(planted_evidence) == "Active" and hero.has(the_free_lie_book):
            abd "No, I just came to say hi Hakim."
            hak "Ah, so nice of you. Let me put my grind away and come back to you."
            hide hakim with moveoutright
            abd "No no! I'm leaving, don't let me interrupt your work."
            menu:
                "Leave the book.":
                    $ hero.drop(the_free_lie_book, 1)
                    $ planted_evidence.complete()
            abd "Goodby hakim."
            jump bazaar
        "I have some bad news." if qlog.has(planted_evidence) == "Active" and len(planted_evidence.inf) == 1:
            abd "I have some bad news hakim."
            hak "What's the matter? Something happened to you? Are you in pain?"
            abd "It's Rasoul."
            hak "Oh man, is he up to no good again?"
            abd "Yes, and this time he's targeting you."
            hak "Me?"
            abd "He forcing me to plant this book in your shop."
            hak "This is bad"
            "..."
            hak "He wants me in jail.."
            abd "I can refuse and throw the book back to him."
            hak "There's no point."
            hak "He'll throw you in jail and comes for me some other way."
            abd "What should we do?"
            hak "I would run to Jafar, he was the wise man to know what to do, but he's g...{w=.2}{nw}"
            abd "Yes! I can ask him!"
            hak "He's no more Abdul."
            abd "Emmmm..."
            abd "I know somebody as wise as Jafar. I can ask him."
            hak "Who?"
            abd "I'll be right back."
            $ planted_evidence.extend(_("Talk to jafar and find a solution to Hakim's predicament."))
            jump bazaar
        "I have a solution." if qlog.has(planted_evidence) == "Active" and planted_evidence.inf[-1] in ["Plant a bottle of wine in Hakim's shop.", "Ask hakim for some money for the wine."] and "Talk to jafar and find a solution to Hakim's predicament." in planted_evidence.inf:
            abd "I have the solution Hakim."
            hak "Really? do tell."
            abd "I'll hide a bottle of wine in your shop, tell Rasoul that I've planted the book and the wine."
            abd "He can only find the wine and arrest you for it instead."
            hak "hmmm..."
            hak "If Rasoul doesn't bring another book to plant on me, That can actually work."
            hak "This friend of yours is a genius. Anyone I know?"
            abd "Maybe."
            hak "Interesting, can I meet him?"
            abd "Maybe later."
            hak "Right, let's deal with the situation at hand first."
            hak "Do you have the bottle of wine?"
            if hero.has(wine):
                abd "Yes."
                abd "Here."
                abd "Put it among your remedies."
                $ planted_evidence.complete()
            else:
                menu:
                    "I'll buy one...":
                        abd "No, but I'll buy one right away."
                    "I didn't have money.":
                        abd "No, They took my money, I didn't have any."
                        hak "I see, here..."
                        $ hero.gotcash(700)
                        hak "This should be enough."
                        abd "I'll be right back."
                $ planted_evidence.extend(_("Buy a bottle of wine for Hakim."))
            hak "Thank you, you're a savior Abdul."
            jump bazaar
        "I got the wine." if qlog.has(planted_evidence) == "Active" and planted_evidence.inf[-1] in ["Buy a bottle of wine for Hakim."] and hero.has(wine):
            abd "I got the wine Hakim."
            abd "Here..."
            hak "Thank you."
            abd "Put it among your remedies."
            hak "I will."
            $ planted_evidence.complete()
            "..."
            abd "I should go."
            hak "For sure, let's hope for the best."
            jump bazaar

        "I have bad news and good news..." if qlog.has(planted_evidence) == "Active" and planted_evidence.inf[-1] in ["Plant a bottle of wine in Hakim's shop.", "Ask hakim for some money for the wine."] and not "Talk to jafar and find a solution to Hakim's predicament." in planted_evidence.inf:
            abd "I have bad news and good news hakim."
            hak "oh? What about?"
            abd "THe bad news is... Rasoul is targeting you and tried to force me to plant one of Jafar's books in your shop or go to jail."
            hak "He didn't..."
            hak "That is indeed bad news. What's the good news?"
            abd "I already have a solution."
            hak "What's the solution?"
            abd "We'll plant a bottle of wine instead and you can make an excuse for it and both of us escape this predicament."
            "..."
            abd "What do you think?"
            hak "That certainty is a solution."
            hak "And he wouldn't back off until they get me behind the bars."
            abd "Who is him:"
            hak "The doctor of the palace."
            abd "Why he wants you locked up?"
            hak "He doesn't like cheap medicine available to the poor and accused me of stealing his patients."
            abd "I see."
            hak "In any case, let's proceed with your plan. I can't think of anything better."
            hak "Do you have the bottle of wine?"
            if hero.has(wine):
                abd "Yes."
                abd "Here."
                abd "Put it among your remedies."
                $ planted_evidence.complete()
            else:
                menu:
                    "I'll buy one...":
                        abd "No, but I'll buy one right away."
                    "I didn't have money.":
                        abd "No, They took my money, I didn't have any."
                        hak "I see, here..."
                        $ hero.gotcash(700)
                        hak "This should be enough."
                        abd "I'll be right back."
                $ planted_evidence.extend(_("Buy a bottle of wine for Hakim."))
            hak "Thank you, you're a savior Abdul."
            jump bazaar

        "Not today..." if not "not today" in hakim_u.flags:
            $ hakim_u.add_flag("not today")
            abd "Not today Hakim."
            hak "Have you come to buy a remedy?"
            abd "Let me see what you have."
        "Found anything to erect old men yet Hakim?" if not "erect old" in hakim_u.flags:
            $ hakim_u.add_flag("erect old")
            abd "Found anything to erect old men yet Hakim?"
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

    #just added a cue from the seller, otherwise Abdul continues to slap his lips.
    # since we might add lip flip to vendors, "{nw}" should do the job as well
    "{nw}"
    call screen shop(s = hakim_u)
    jump bazaar





# Tailor
define far = Character("Farrokh the tailor", color="#4ff", what_text_color="#dff")
image farrokh normal = "char/farrokh/normal.png"

default tailor_u = unit(
    "Farrokh the tailor",
    "char/farrokh",

    3410,
    [
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
    far "Do you need another stitching, Abdul?"
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
    call screen shop(s = tailor_u)
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
    if not "first" in petros_u.flags:
        show petros normal at right
        pet "Hey... Dabul... know any women to hook me up with?"
        show abd normal at left
        abd "It's Abdul, and no."
        pet "Came here to sin then? What's your choice?"
        $ petros_u.add_flag("first")
    else:
        show petros normal at right
        pet "Abully the sinner. What do you need this time?"
        show abd normal at left
    if qlog.has(beer_for_the_viking) and beer_for_the_viking.stat == "Active":
        abd "I need a keg of beer."
        pet "Ohohohoh, what for? having friends over?"
        pet "Any women? I'm coming too."
        abd "It's for somebody."
        pet "Ah, the guy at oasis?"
        abd "Yes."
        pet "I was wondering when he'll run out."
        pet "A keg costs 2400 Dinars."
        $ hero.paidcash(2400)
        $ petros_u.gotcash(2400)
        abd "Here."
        pet "Alright, wait here."
        hide petros with moveoutright
        pause 4
        show petros normal at right with moveinright
        pet "Here you go, a keg of the best beer in Agrabah."
        $ hero.got(beer_keg)
        $ beer_for_the_viking.complete()
        pet "Don't get caught."
        abd "Thanks"
        pet "And you don't know me if they catch you."
        "..."
        jump bazaar

    call screen shop(s = petros_u)
    jump bazaar

# fat
define fat = Character("Fatti", color="#4ff", what_text_color="#dff")
image fatti normal = "char/pedestrians/fatti.png"
label bazaar_fatti:
    scene
    show fatti normal at right
    fat "What are you shopping for Abdul?"
    show abd normal at left
    abd "Nothing for now."
    fat "You should buy something to eat Abdul, you're wasting away."
    jump bazaar


