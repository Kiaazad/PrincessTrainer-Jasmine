default heaven_oasis_viking = pnco(
    "The viking",
    "bg/heaven_oasis/viking.png",
    (518, 559),
    Jump('the_viking'),
    hidden = False, hoffset = (120,97),
    )
default heaven_oasis_1 = pnco(
    "thorns",
    "bg/rock_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    )
default heaven_oasis_fishing = pnco(
    "Start fishing",
    None,
    (824, 800),
    Jump('heaven_oasis_fishing'),
    )
default heaven_oasis_drink = pnco(
    "Drink",
    None,
    (924, 850),
    Jump('heaven_oasis_drink'),
    )
default heaven_oasis_back = pnco(
    "Back",
    None,
    (311, 629),
    Jump('desert'),
    hidden = False, hoffset = (83,-40),
    )

default heaven_oasis_loc = pncs(
    "Main street",
    [
        heaven_oasis_viking,
        heaven_oasis_back,
        heaven_oasis_fishing,
        heaven_oasis_drink,

    ]
    )

image bg heaven_oasis = "bg/heaven_oasis/bg.png"
label heaven_oasis:
    scene
    show bg heaven_oasis onlayer bg
    show screen pnc(abdul, heaven_oasis_loc)
    pause
    jump heaven_oasis

# The viking



define vik = Character("The Viking", color="#4ff", what_text_color="#dff")
image viking normal = "char/viking/normal.png"

label the_viking:
    scene
    #show bg water_front
    show viking normal at right
    vik "Abdul the wood collector... so, have you come to take my boat apart?"
    show abd normal at left
    abd "Do you always have to mention that? I already told you, I thought it was abandoned."
    vik "Alright alright... Came to buy what I've fished out from my sunken cargo?"
    abd "What do you have?"
    vik "Nothing yet, but soon."
    abd "Alright, I'll visit later."
    vik "Before you go, Abdul."
    vik "Do you think you could help me with a simple delivery job?"
    vik "Think of it as paying me back for almost wrecking my boat."
    abd "...you don’t have to put it like that."
    abd "But alright, I guess I can help. As long as it isn’t anything dangerous."
    abd "What do you need me to do?"
    vik "Do you know Petros? He sells me plenty of beer, and I still haven’t paid him off for the last few barrels I bought."
    vik "Here’s some money. Just pass it to him when you see him."
    vik "He should be somewhere in the baazar, hiding from the guards as usual."
    abd "Sounds easy enough."
    abd "So long as I don’t have to smuggle any alcohol."
    vik "Hah. Leave that to the experts. Wouldn't want Petros to get in trouble if you get caught."
    vik "Losing access to fresh beer would be troublesome."
    abd "Err, right."
    abd "Also, Agrabah isn’t that far. Why...I mean, you could have gone to find him yourself."
    vik "I’m not a wood collector. I don’t have a reason to be travelling in this blasted heat."
    abd "..."
    jump heaven_oasis


label heaven_oasis_fishing:
    scene
    show viking normal at right
    vik "Trying to fish with your hands?"
    show abd normal at left
    abd "Well..."
    vik "Don't bother, it's not ready yet."
    vik "Here, have this fish instead."
    $ abdul.got(fish,1)
    jump heaven_oasis

label heaven_oasis_drink:
    scene
    $ hero.drink(1, 4)
    jump heaven_oasis



