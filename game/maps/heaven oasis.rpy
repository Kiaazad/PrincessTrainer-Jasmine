default heaven_oasis_viking = pnco(
    "The viking",
    "bg/heaven_oasis/viking.png",
    (518, 559),
    Jump('the_viking'),
    )
default heaven_oasis_1 = pnco(
    "thorns",
    "bg/rock_pass/02.png",
    (1713, 559),
    items = [[thorns, 1]],
    )

default heaven_oasis_back = pnco(
    "Back",
    None,
    (611, 729),
    Jump('desert'),
    )

default heaven_oasis_loc = pncs(
    "Main street",
    [
        heaven_oasis_viking,
        heaven_oasis_back,

    ]
    )

image bg heaven_oasis = "bg/heaven_oasis/bg.png"
label heaven_oasis:
    scene
    show bg heaven_oasis onlayer bg
    show screen pnc(abdul, heaven_oasis_loc)
    pause
    jump desert

# The viking



define vik = Character("The Viking", color="#4ff", what_text_color="#dff")
image viking normal = "char/viking/normal.png"

label the_viking:
    scene
    #show bg water_front
    show viking normal at right
    vik "Abdul the wood collector... have you came here to take my boat apart?"
    show abd normal at left
    abd "Do you have to mention that every time? I thought it was abandoned."
    vik "Alright alright... Came to buy what I've fished out from my sunken cargo?"
    abd "What do you have."
    vik "Nothing yer, but soon."
    abd "Alright I'll visit later."
    jump desert




