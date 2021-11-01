# Exits
default old_gate_beduins_camp = pnco(
    "Beduins camp",
    None,
    (124, 714),
    Jump('beduins_camp'),
    )
default old_gate_ruins = pnco(
    "Ruins",
    None,
    (1600, 576),
    Jump('ruins'),
    )
default old_gate_southern_trade_route = pnco(
    "Southern trade route",
    None,
    (955, 343),
    Jump('southern_trade_route'),
    )
label southern_trade_route:
    "not ready yet."
    jump old_gate

# Map
default old_gate_map = pncs(
    "Old gate",
    [
        old_gate_beduins_camp,
        old_gate_ruins,
        old_gate_southern_trade_route,
    ], night = "bg/old_gate/night.webp"
    )
"""
Background design notes:
The remains of an old gate in the middle of desert. It was the entrance of the old city that's under sand now.
"""
image bg old_gate = "bg/old_gate/bg.webp"
label old_gate:
    if not old_gate_map in all_places:
        $ all_places.append(old_gate_map)
    scene
    show bg old_gate onlayer bg
    show screen pnc(abdul, old_gate_map)
    pause
    jump old_gate




