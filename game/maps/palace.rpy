default jasmines_room_loc = place("Jasmine's room", (562, 759), Jump('palace'), "bg/palace/jasmines_room.png")
default throne_room_loc = place("Throne room", (916, 645), Jump('palace'), "bg/palace/throne_room.png")
# default sultans_room_loc = place("Sultan's room", (0.679, 0.349), Jump('palace'), "bg/palace/sultans_room.png")
# default palace_yard_loc = place("The yard", (0.679, 0.349), Jump('palace'), "bg/palace/palace_yard.png")
# default servants_quarter_loc = place("Servant's quarter", (0.679, 0.349), Jump('palace'), "bg/palace/servants_quarter.png")
# default treasury_loc = place("Treasury", (0.679, 0.349), Jump('palace'), "bg/palace/treasury.png")
default palace_street_loc = place("Back to the main street", (0.679, 0.349), Jump('street'), "bg/palace/palace_back.png")
default palace_map = maps(
    "Palace",
    [
        jasmines_room_loc,
        throne_room_loc,
        # sultans_room_loc,
        # palace_yard_loc,
        # servants_quarter_loc,
        # Treasury_loc,
        palace_street_loc,
    ]
    )

label palace:
    scene image "bg/palace.jpg"
    show screen map(palace_map)
    pause