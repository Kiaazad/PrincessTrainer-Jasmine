
default vantage_point_rich = pnco(
    "Back to town",
    None,
    (1520, 947),
    Jump('rich'),
    hidden = False, hoffset = (100,-60),
    )
default vantage_point_cg = pnco(
    "Peep",
    None,
    (1393, 633),
    Jump('vantage_point_cg'),
    hidden = False, hoffset = (100,-60),
    )

default vantage_point_map = pncs(
    "Agrabah",
    [
        vantage_point_rich,
        vantage_point_cg,
    ], night = "bg/vantage_point/night.jpg"
    )

image bg vantage_point = "bg/vantage_point/bg.jpg"
label vantage_point:
    scene
    show bg vantage_point onlayer bg
    show screen pnc(abdul, vantage_point_map)
    pause
    jump vantage_point

label vantage_point_cg:
    "Under development."
    jump vantage_point
