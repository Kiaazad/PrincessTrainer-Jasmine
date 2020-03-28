default jasmines_quarter_loc = place("Jasmine's quarter", (195, 558), Jump('jasmines_quarter'), "bg/palace/jasmine.png")
default throne_loc = place("The Throne", (791, 651), Jump('the_throne'), "bg/palace/throne.png")
default sultans_quarter_loc = place("Sultan's quarter", (1530, 558), Jump('sultans_quarter'), "bg/palace/sultan.png")
default palace_street_loc = place("Go back", (530, 958), Jump('street'))

default palace_map = maps(
    "Palace",
    [
        jasmines_quarter_loc,
        throne_loc,
        sultans_quarter_loc,
        palace_street_loc,
    ]
    )

label palace:
    scene image "bg/palace.jpg"
    show screen map(palace_map)
    pause

label jasmines_quarter:
    "Guard" "Where do you think you're going peasant? get lost."
    jump palace

label the_throne:
    "Guard" "You can't approach the throne peasant, get lost."
    jump palace

label sultans_quarter:
    "Guard" "You can't enter the building peasant, get lost."
    jump palace


label palace_yard:
    ras "Hey!"
    show ras normal at right
    ras "Where do you think you're going?"
    show abd alert at left
    abd "To the yard."
    ras "That's forbidden doe peasants, now get lost!"
    jump palace

label servants_quarter:
    "Servant" "Are you here to deliver something?."
    abd "No."
    "Servant" "Then you better leave before guards come and shake you down."
    abd "Alright."
    jump palace

label palace_treasury:
    "Guard" "You can't enter the building peasant, get lost."
    jump palace

