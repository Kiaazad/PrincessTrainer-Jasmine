default street_money_lender_loc = place("Money lender", (483, 576), Jump('money_lender'), "bg/street/Money lender.png")
default street_empty_shop_loc = place("Empty shop", (146, 486), Jump('empty_shop'), "bg/street/empty shop.png")
default street_karim_loc = place("Karim's shop", (94, 636), Jump('karim'), "bg/street/karim.png")
default street_palace_loc = place("Palace", (711, 357), Jump('palace'), "bg/street/palace.png")
default street_home_loc = place("Home", (1464, 200), Jump('agrabah'), "bg/street/home.png")
default street_blacksmith_loc = place("Blacksmith", (1536, 406), Jump('blacksmith'), "bg/street/blacksmith.png")


default street_desert_loc = place("Desert", (141, 742), Jump('desert'))
default street_bazaar_loc = place("Bazaar", (1046, 760), Jump('bazaar'))
default street_map = maps(
    "Main street",
    [
        street_money_lender_loc,
        street_empty_shop_loc,
        street_karim_loc,
        street_desert_loc,
        street_palace_loc,
        street_bazaar_loc,
        street_home_loc,
        street_blacksmith_loc,
    ]
    )

label street:
    scene image "bg/street.png"
    show screen map(street_map)
    pause

# Blacksmith
define rah = Character("Rahman", color="#4ff", what_text_color="#dff")
image rahman normal = "char/rahman/normal.png"

label blacksmith:
    show rahman normal at right
    rah "Abdul my friend, what you got for me today?"
    show abd normal at left
    abd "Maybe later Rahman."
    rah "Alright."
    jump street


# Money lender
define mst = Character("Mostafa the money lender", color="#4ff", what_text_color="#dff")
image mostafa normal = "char/money_lender/normal.png"

label money_lender:
    show mostafa normal at right
    mst "...?"
    show abd normal at left
    mst "No money unless you have something valuable?"
    mst "You don't look like having anything."
    mst "Get lost!"
    jump street

# Empty shop
label empty_shop:
    show mostafa normal at right
    mst "The rent is 4000 per month, do you want to rent?"
    show abd normal at left
    mst "I can't afford it."
    mst "Get lost then!"
    jump street

# Karim
define kar = Character("Karim", color="#4ff", what_text_color="#dff")
image karim normal = "char/karim/normal.png"
default karim_u = unit(
    "Karim",
    "char/karim",

    3410,
    [
        (rice, 24),
        (bread, 15),
        (salt, 12),
        (saffron, 2),
        (crackers, 16),
        (bread, 15),
        (hashish, 3),
        (opium, 2),
    ],
    1.3,

    8,
    "Peasant",
    )
label karim:
    show karim normal at right
    kar "No hand outs!"
    show abd normal at left
    abd "I didn't ask for any."
    kar "Just saying, what do you want?"
    show screen shop(s = karim_u, c = abdul)
    pause
    jump street

