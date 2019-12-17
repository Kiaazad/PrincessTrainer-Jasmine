default jasmines_room_loc = place("Jasmine's room", (339, 573), Jump('jasmines_room'), "bg/palace/jasmines_room.png")
default throne_room_loc = place("Throne room", (890, 700), Jump('throne_room'), "bg/palace/throne_room.png")
default sultans_room_loc = place("Sultan's room", (1307, 509), Jump('sultans_room'), "bg/palace/sultans_room.png")
default palace_yard_loc = place("The yard", (91, 847), Jump('palace_yard'), "bg/palace/palace_yard.png")
default servants_quarter_loc = place("Servant's quarter", (1816, 727), Jump('servants_quarter'), "bg/palace/servants_quarter.png")
default treasury_loc = place("Treasury", (908, 249), Jump('palace_treasury'), "bg/palace/treasury.png")
default palace_street_loc = place("Back to the main street", (1157, 37), Jump('street'), "bg/palace/palace_back.png")
default palace_map = maps(
    "Palace",
    [
        jasmines_room_loc,
        throne_room_loc,
        sultans_room_loc,
        palace_yard_loc,
        servants_quarter_loc,
        treasury_loc,
        palace_street_loc,
    ]
    )

label palace:
    scene image "bg/palace.jpg"
    show screen map(palace_map)
    pause

label palace_yard:
    ras "Hey!"
    show ras normal at right
    ras "Where do you think you're going?"
    show abd alert at left
    abd "To the yard."
    ras "That's forbidden doe peasants, now get lost!"
    jump palace

label jasmines_room:
    "Guard" "You can't enter the building peasant, get lost."
    jump palace

label throne_room:
    "Guard" "You can't enter the building peasant, get lost."
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

label sultans_room:
    "Guard" "You can't enter the building peasant, get lost."
    jump palace