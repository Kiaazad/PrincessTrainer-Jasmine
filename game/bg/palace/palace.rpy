default jasmines_quarter_loc = pnco(
    "Jasmine's quarter",
    "bg/palace/jasmine.png",
    (195, 558),
    Jump('jasmines_quarter'),
    hidden = False, hoffset = (0,-40),
    )
default throne_loc = pnco(
    "The Throne",
    "bg/palace/throne.png",
    (791, 651),
    Jump('the_throne'),
    hidden = False, hoffset = (174,-40),
    
    )
default sultans_quarter_loc = pnco(
    "Sultan's quarter",
    "bg/palace/sultan.png",
    (1530, 558),
    Jump('sultans_quarter'),
    hidden = False, hoffset = (209,-40),
    )
default palace_street_loc = pnco(
    "Go back",
    "bg/palace/city.png",
    (1025, 1019),
    Jump('street'),
    hidden = False, hoffset = (83,-40),
    )

default palace_bags = pnco(
    "bags",
    "bg/palace/bags.png",
    (748, 997),
    items = [1000, 700],
    regen = 10,
    )



default palace_map = pncs(
    "Palace",
    [
        jasmines_quarter_loc,
        throne_loc,
        sultans_quarter_loc,
        palace_street_loc,

        palace_bags,
    ]
    )

image bg palace = "bg/palace/bg.jpg"
label palace:
    scene
    show bg palace onlayer bg
    show screen pnc(abdul, palace_map)
    pause
    jump palace

define guard_1 = Character("Guard", color="#4ff", what_text_color="#dff")
image guard_1 normal = "char/guard/guy1 normal.png"


label jasmines_quarter:
    scene
    show guard_1 normal at left
    guard_1 "Where do you think you're going peasant? get lost."
    jump palace

label the_throne:
    scene
    show guard_1 normal at center
    guard_1 "You can't approach the throne peasant, get lost."
    jump palace

label sultans_quarter:
    scene
    show guard_1 normal at right
    guard_1 "You can't enter the building peasant, get lost."
    jump palace


label palace_yard:
    scene
    ras "Hey!"
    show ras normal at right
    ras "Where do you think you're going?"
    show abd alert at left
    abd "To the yard."
    ras "That's forbidden doe peasants, now get lost!"
    jump palace

label servants_quarter:
    scene
    "Servant" "Are you here to deliver something?."
    abd "No."
    "Servant" "Then you better leave before guards come and shake you down."
    abd "Alright."
    jump palace

label palace_treasury:
    scene
    "Guard" "You can't enter the building peasant, get lost."
    jump palace

