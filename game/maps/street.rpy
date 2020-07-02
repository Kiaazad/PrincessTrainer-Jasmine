default street_money_lender_loc = place("Money lender", (483, 576), Jump('money_lender'), "bg/street/Money lender.png")
default street_empty_shop_loc = place("Empty shop", (146, 486), Jump('money_lender'), "bg/street/empty shop.png")
default street_left_shop_loc = place("Left shop", (94, 636), Jump('money_lender'), "bg/street/left shop.png")


default street_desert_loc = place("Desert", (141, 742), Jump('desert'))
default street_palace_loc = place("Palace", (711, 357), Jump('palace'), "bg/street/palace.png")
default street_bazaar_loc = place("Bazaar", (1046, 760), Jump('bazaar'))
default street_home_loc = place("Home", (1464, 200), Jump('agrabah'), "bg/street/home.png")
default street_map = maps(
    "Main street",
    [
        street_money_lender_loc,
        street_empty_shop_loc,
        street_left_shop_loc,
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

label money_lender:
    show mostafa normal at right
    mst "...?"
    show abd normal at left
    mst "No money unless you have something valuable?"
    mst "You don't look like having anything."
    mst "Get lost!"
    jump street