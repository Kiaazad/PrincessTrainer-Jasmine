default poor_bazaar = pnco(
    "Bazaar",
    None,
    (780, 980),
    Jump('bazaar'),
    )
default poor_thief = pnco(
    "Ahmad",
    "bg/poor/thief.png",
    (1294, 601),
    Jump('poor_thief'),
    shifts = [[100,180], [190, 250]]
    )
default poor_ali = pnco(
    "Ali",
    "bg/poor/ali.png",
    (1051, 640),
    Jump('poor_ali'),
    )
default poor_barracks = pnco(
    "Barracks",
    None,
    (800, 600),
    Jump('barracks'),
    )
default petros_shop = pnco(
    "Shady Figure",
    "bg/poor/petros.png",
    (136, 330),
    Jump('petros_shop'),
    hidden = False, hoffset = (20,-80),
    )


default poor_map = pncs(
    "Poor section",
    [
        poor_bazaar,
        poor_ali,
        poor_thief,
        poor_barracks,
        petros_shop,
    ], night = "bg/poor/night.webp"
    )

image bg poor = "bg/poor/bg.webp"
label poor:
    scene
    show bg poor onlayer bg
    show screen pnc(abdul, poor_map)
    pause
    jump poor

# Ahmed
default ahmad_u = unit(
    "Sleazy Ahmad",
    "char/ahmad",

    490,
    [

    ],
    1.1,

    8,
    "Peasant",
    interests = ["jewelry"],
    reject = ["fuel"]
    )

define ahm = Character("Sleazy Ahmad", color="#4ff", what_text_color="#dff")
image ahmed normal = "char/ahmad/normal.png"
label poor_thief:
    scene
    if not "first" in ahmad_u.flags:
        $ ahmad_u.pick_pocket_skill = 80
        show ahmed normal at right
        ahm "Hey baddy!"
        ahm "Do you want to play coins?"
        show abd normal at left
        abd "You seem the wrong type to gamble with."
        ahm "Come on buddy... What's the harm?"
        abd "I don't know..."
        $ ahmad_u.pick_pocket(abdul)
        ahm "Alright buddy... I'm here if you want to have some fun."
        $ ahmad_u.add_flag("first")
    else:
        show ahmed normal at right
        ahm "Came to play buddy?"
        show abd normal at left
        menu:
            "sure!":
                abd "Sure..."
                ahm "..."
                ahm "Oh that's odd, I can't find my lucky coin. let's do it later."
                $ ahmad_u.pick_pocket(abdul)
                ahm "let's do it later."
            "No!":
                ahm "Come on buddy..."
                ahm "Don't be like that."
                abd "NO!"
                ahm "..."
                $ ahmad_u.pick_pocket(abdul)
                ahm "Alright, you'll be back."
    jump poor


# Petros
define pet = Character("Petros", color="#4ff", what_text_color="#dff")
image petros normal = "char/petros/normal.png"

default petros_u = unit(
    "Petros",
    "char/petros",

    3410,
    [
        (beer, 1),
        (liquor, 1),
        (wine, 1),
    ],
    1.2,

    8,
    "Peasant",
    interests = [],
    reject = ["Weapon", "armor", "lamp"]
    )
label petros_shop:
    scene
    if not "first" in petros_u.flags:
        show petros normal at right
        pet "Hey... Dabul... know any women to hook me up with?"
        show abd normal at left
        abd "It's Abdul, and no."
        pet "Came here to sin then? What's your choice?"
        $ petros_u.add_flag("first")
    else:
        show petros normal at right
        pet "Abully the sinner. What do you need this time?"
        show abd normal at left
    if qlog.has(beer_for_the_viking) and beer_for_the_viking.stat == "Active":
        abd "I need a keg of beer."
        pet "Ohohohoh, what for? having friends over?"
        pet "Any women? I'm coming too."
        abd "It's for somebody."
        pet "Ah, the guy at oasis?"
        abd "Yes."
        pet "I was wondering when he'll run out."
        pet "A keg costs 2400 Dinars."
        $ hero.paidcash(2400)
        $ petros_u.gotcash(2400)
        abd "Here."
        pet "Alright, wait here."
        hide petros with moveoutright
        pause 4
        show petros normal at right with moveinright
        pet "Here you go, a keg of the best beer in Agrabah."
        $ hero.got(beer_keg)
        $ beer_for_the_viking.complete()
        pet "Don't get caught."
        abd "Thanks"
        pet "And you don't know me if they catch you."
        "..."
        jump bazaar

    call screen shop(s = petros_u)
    jump poor

default new_spyglass = item(
    _("Brand new spyglass"),
    _("It looks pristine."),
    "items/new_spyglass.png",
    9000,
    [],
    )


define ali = Character("Ali", color="#4ff", what_text_color="#dff")
image ali normal = "char/ali/normal.png"

default ali_u = unit(
    "Ali",
    "char/ali",

    210,
    [
        [new_spyglass, 1]
    ],
    1.2,

    3,
    "Peasant",
    interests = ["Weapon", "armor"],
    reject = ["lamp"]
    )
label poor_ali:
    scene
    if ali_u.has(new_spyglass) and qlog.has(stolen_spyglass):
        if not "agreed" in ali_u.flags:
            show abd normal at left
            abd "Ali, come over here."
            show ali normal at right
            ali "Yes?"
            abd "Have you bee stealing again?"
            ali "No!"
            abd "Don't lie to me Ali..."
            abd "Where did you got the apple?"
            ali "My home."
            "..."
            abd "Should I ask your mother?"
            ali "I found it."
            abd "Are you trying to kill your mother?"
            abd "What if you get caught?"
            ali "It's just one apple, chill man."
            abd "I'm not talking about the apple anymore."
            abd "Hve you been to the caravansarai again?"
            ali "Maybe."
            menu:
                "You stole something, give it to me.":
                    abd "You stole something, give it to me."
                    ali "Like what?"
                    abd "A spyglass."
                    abd "Why should I give it to you?"
                    menu:
                        "Because if you don't I'll tell your mother.":
                            abd "Because if you don't I'll tell your mother."
                            ali "You think I'm afraid of her?"
                            abd "When she finds out you've been stealing again, she'll keep you in the basement till your hair turn white."
                            ali "No prison can contain Ali, I'll escape."
                            abd "Alright, what do you want for it?"
                            ali "Got a monkey?"
                            abd "No."
                            "..."
                            ali "8000 Dinars."
                            abd "Are you crazy?"
                            ali "I've asked around, it's what it worth."
                            abd "Maybe brand new. And not stolen."
                            abd "I'll give you 2000 for it."
                            ali "6000"
                            abd "3000"
                            ali "5000"
                            abd "4000"
                            ali "I guess I'll keep it."
                            abd "Alright 5000"
                            $ ali_u.pay = 5000
                        "I'll buy it from you.":
                            abd "I'll buy it from you."
                            ali "9000"
                            abd "For a stolen item? Not a chance."
                            ali "5000?"
                            abd "No."
                            ali "4000 is the last price."
                            "..."
                            abd "Alright."
                            $ ali_u.pay = 4000

                "They're looking for you.":
                    abd "They're looking for you."
                    ali "Who?"
                    abd "Some armed bodyguard in the caravansarai."
                    "..."
                    abd "Did you do something?"
                    ali "Nooo...!?"
                    abd "Stole something again?"
                    ali "Maybe?"
                    abd "What?"
                    ali "A spyglass."
                    menu:
                        "THey sent me to bring it back.":
                            abd "THey sent me to bring it back."
                            ali "Why should I give it to you?"
                            abd "Do you want them to come after you?"
                            "..."
                            ali "They're paying you right?"
                            abd "Maybe."
                            ali "I want some of the money."
                            abd "I'll give you 1000 dinars."
                            ali "More."
                            abd "2000?"
                            ali "Make it 3000 and we have a deal."
                            abd "Alright."
                            $ ali_u.pay = 3000
                        "You should give it back.":
                            abd "You should give it back before they send the guards for you."
                            "..."
                            ali "Go there and get caught?"
                            ali "Fuck that, they have no proof."
                            abd "Do you think the guards care about proof?"
                            "..."
                            abd "give it to me and I'll deliver it."
                            "..."
                            ali "You had me for a second there."
                            ali "What's in it for you?"
                            abd "I'm saving your skin kid."
                            "..."
                            abd "Alright there a reward for it."
                            ali "Aha! I knew it."
                            ali "How much do I get?"
                            abd "I don't know, I'll split the money with you later."
                            ali "No."
                            ali "Money first."
                            abd "1000 dinars?"
                            ali "Double it!"
                            abd "Alright."
                            $ ali_u.pay = 2000
            $ ali_u.add_flag("agreed")
            ali "Fork over the money then."
            if hero.cash >= ali_u.pay:
                $ hero.paidcash(ali_u.pay)
                abd "Here."
                abd "Now give me the spyglass."
                ali "Wait here. I'll go get it."
                abd "Alright, leave the money here though."
                "..."
                ali "Alright."
                hide ali with moveoutright
                pause 3
                show ali normal at right with moveinright
                ali "Here..."
                $ ali_u.drop(new_spyglass, 1)
                $ hero.got(new_spyglass, 1)
                if qlog.has(stolen_spyglass) == "Active":
                    $ stolen_spyglass.complete()
                "..."
                abd "Now go home and stop stealing."
                abd "You're going to end up in palace's jail with a hand cut off."
                ali "Or in the palace, as a king with a pretty princess as my wife."
                "..."
                abd "You need a better role model."
                abd "And think of your poor mother, she'll cry herself to death if something happens to you."
                ali "Better than the king?"
                abd "I don't know what to tell you anymore."
                "..."
            else:
                abd "I don't have enough right now."
                ali "Alright, I'll wait."
        else:
            show ali normal at right
            show abd normal at left
            ali "Got my money?."
            if hero.cash >= ali_u.pay:
                $ hero.paidcash(ali_u.pay)
                abd "Here."
                abd "Now give me the spyglass."
                ali "Wait here. I'll go get it."
                abd "Alright, leave the money here though."
                "..."
                ali "Alright."
                hide ali with moveoutright
                pause 3
                show ali normal at right with moveinright
                ali "Here..."
                $ ali_u.drop(new_spyglass, 1)
                $ hero.got(new_spyglass, 1)
                if qlog.has(stolen_spyglass) == "Active":
                    $ stolen_spyglass.complete()
                "..."
                abd "Now go home and stop stealing."
                abd "You're going to end up in palace's jail with a hand cut off."
                ali "Or in the palace, as a king with a pretty princess as my wife."
                "..."
                abd "You need a better role model."
                abd "And think of your poor mother, she'll cry herself to death if something happens to you."
                ali "Better than the king?"
                abd "I don't know what to tell you anymore."
                "..."
            else:
                abd "Not yet."
                ali "Alright, I'll wait."
    else:
        show ali normal at right
        show abd normal at left
        "..."
    jump poor

label widows_house:
    scene
    show bg widows house onlayer bg
    hide screen pnc
    show abd normal at left with dissolve
    show wid normal at right with dissolve
    "..."
    menu:
        "Rasoul sent me.":
            abd "Rasoul sent me."
            wid "For what purpose?"
            abd "He said you'll take care of me."
        "I have some questions.":
            abd "I have some questions."
            wid "I can't answer, please leave."
        "I came to assist you.":
            abd "I've came to assist you."
            wid "I don't need any assistance. please leave."
    
    jump poor


