
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

image spyglass old = "cg/vantage_point/old_spyglass.png"
image cg jasmine_on_balcony = "cg/vantage_point/jasmine_on_balcony.png"

label vantage_point_cg:
    if hero.has(old_spyglass):
        scene
        show spyglass old with dissolve
        show cg jasmine_on_balcony behind spyglass with dissolve
        abd "Is that princess Jasmine?"
    elif hero.has(new_spyglass):
        scene
        # show spyglass old with dissolve
        show cg jasmine_on_balcony behind spyglass with dissolve
        abd "Princess Jasmine."
        abd "Naughty naughtily girl."
    else:
        abd "Can't see much"
    "Under development."
    jump vantage_point
