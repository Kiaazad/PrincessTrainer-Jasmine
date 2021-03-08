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
default viking_u = unit( # we use a unit class to manage every character that has important data to keep track of like items or money
    "The Viking",
    "char/viking",

    3410,
    [
        (beer, 1),
    ],
    1.2,

    28,
    "Warrior",
    interests = [],
    reject = ["lamp"]
    )


default beer_for_the_viking = quest( 
    _("Beer for the Viking"),
    _("The Viking in the oasis wants me to buy him some beer."),
    )


label the_viking:
    scene
    if not "talked about boat" in viking_u.flags: # checks if they have not talked about the boat incident
        show viking normal at right
        vik "Abdul the wood collector... so, have you come to take my boat apart?"
        show abd normal at left
        abd "Do you always have to mention that? I already told you, I thought it was abandoned."
        vik "Alright alright... Came to buy what I've fished out from my sunken cargo?"
        $ viking_u.add_flag("talked about boat") # adds a flag that they have talked about the boat
    else: # otherwise the usual greeting
        show viking normal at right
        vik "Abdul the shipwrecker! nice to see you again."
        show abd normal at left
        abd "Hey, hi."
    
    if not qlog.has(beer_for_the_viking): # check if the quest is not already in the quest log
        vik "I have a favor to ask Abdul my friend."
        abd "Out of food again?"
        vik "No, this time it's something more important."
        abd "More important than food?"
        vik "Of course, I ran out of beer."
        abd "I told you I can get in lots of trouble if the guards catch me with alcohol."
        vik "Come on, they won't suspect you."
        vik "I in other hand, can't take a step in that city without eyes following me."
        abd "I can't."
        vik "I'm dying of thirst Abdul."
        abd "There's water."
        vik "Vikings don't drink that junk. Help me here Abdul."
        abd "Alright!"
        vik "Thank you. You're a savior."
        $ qlog.got(beer_for_the_viking) # add the quest
        $ abdul.gotcash(1000) # Giving somebody some money
        vik "Here, take this money and buy as many as you can."
        abd "Sure, do you need any food?"
        vik "No I'm all set on that front."
        jump heaven_oasis
    elif qlog.has(beer_for_the_viking) == "Active" and abdul.has(beer): # If the quest is active
        vik "Got the beer?"
        abd "Yes, here!"
        $ beer_for_the_viking.complete()
        # I'll code this part properly
    
    vik "Come browse my stuff."
    # I'll add a shop here later



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



