﻿default poor_bazaar = pnco(
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
            "So you can pick my pocket?" if qlog.has(learn_pick_pocket) == "Active":
                abd "So you can pick my pocket while I'm distracted?"
                ahm "I don't know what you're talking about."
                abd "Cut the crab Ahmad, I'm here to invoke your deal with jafar."
                ahm "What?"
                ahm "How do you know about it?"
                abd "He told me."
                ahm "But he's dead!"
                abd "Do you want to test your luck and disobey his order?"
                ahm "Alright, do you want your money back?"
                abd "No."
                ahm "What then?"
                abd "I want you to teach me how to pick pockets."
                ahm "No way!"
                abd "There's a reward in it for you."
                ahm "Why do you want to learn it?"
                abd "Jafar's order."
                ahm "But he's dead!"
                abd "Orders are orders."
                "..."
                ahm "Alright, meet me behind the town's wall tonight."
                ahm "And bring a meal."
                abd "Do you want to teach me how to eat with my left hand?"
                "..."
                ahm "Well..."
                abd "We all know that proverb. You can skip it and get to the point."
                abd "I'm not going to lose my hand."
                ahm "Alright, it's your hand."
                ahm "First you need a distraction..."
                ahm "Then with a little dexterity..."
                ahm "Strong fingers..."
                ahm "Anf finesse..."
                $ ahmad_u.pick_pocket(abdul)
                ahm "Viola..."
                "..."
                abd "Is that it?"
                ahm "In a nutshell."
                $ learn_pick_pocket.complete()
                ahm "Of course it needs years of practice and experience."
                abd "I don't have years."
                ahm "Then you won't have your hands for long."
                "..."
                ahm "Make a dummy and cover it with clothing to practice on."
                abd "Good idea."
                ahm "Just keep in mind: You don't know me and I don't know you."
                ahm "And never try to pick my pocket if you don't like having a blade inside your guts."
                abd "Not even for practice?"
                ahm "Never."
                ahm "Now go, I don't want to be seen talking to you for long."
                abd "Alright."

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
        $ beer_for_the_viking.extend(_("Deliver the keg to the Viking."))
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
    "new_spyglass",
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
                        "They sent me to bring it back.":
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
                    $ stolen_spyglass.extend(_("Deliver it to the Traveler."))
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
                    $ stolen_spyglass.extend(_("Deliver it to the Traveler."))
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
            abd "He said that you would take care of me."
            wid "Take care of you?"
            wid "{size=18}The nerve of that pig...{/size}"
            abd "Excuse me?!"
            wid "Oh... I said, I don't eat pigs; Pork, I mean I don't eat pork."
            abd "Well, yeah. Neither do I."
            "..."
            abd "So, may I come in? Or should I let Rasoul know that he was mistaken in sending me here?!"
            wid "Fine! Follow me, just don't touch anything!"
            # inside widow's house
            abd "Oh my, what a lovely home you have."
            wid "You can save the sarcasm."
            abd "What? No, I was being serious."
            abd "Compared to my place, this is a palace."
            wid "Sure, whatever. Can we just drop the small talk and get this over with?!"
            abd "Sorry?"
            wid "Look, I know you're only here because Rasoul sent you."

            wid "That bastard won't let me see my daughter unless I whore myself out to his disgusting friends."
            abd "Friends?"
            abd "Oh! {size=36}Yes{/size}, that's right! We're friends."
            abd "In fact, we're Such good friends that some people have even confused us as brothers, haha..."
            "..."
            wid "{size=18}More like lovers than brothers...{/size}"
            "..."
            wid "Anyway, lets get this over with before your stench permanently embeds itself in my home."
            abd "Wow, that was hurtful."
            wid "Remove your clothes!"
            abd "Yes, Ma'am!"
            # Show Abdul naked
            wid "{size=18}Oh, my...{/size}"
            "..."
            abd "And now?"
            wid "Oh... yes. Of course."
            wid "Now stand against the wall and close your eyes."
            abd "Close my eyes?"
            wid "Yes! This is degrading enough without having you ogle me like a hungry dog at a barbecue."
            abd "Okay fine, like this?"
            wid "Yes. Now stop talking!"
            # Show wid giving blowjob to abd
            abd "Oh, wow."
            wid "Mouth shut! Or I'll close mine!"
        "I have a few questions.":
            abd "I have a few questions."
            wid "I don't know anything, please leave."
            abd "Look, I know what Rasoul did to your husband."
            abd "I can only assume how difficult it has been for a woman as beautiful as yourself, living in this city without a husband's protection."
            "..."
            wid "You think I'm... {size=18}Beautiful{/size}?"
            abd "Well, yes. Of course I do."
            wid "But Rasoul..."
            abd "Let me worry about Rasoul!"
            wid "Let you worry?"
            wid "Aren't you his friend?"
            abd "Not exactly, I'm forced to work with him."
            wid "I see."
            abd "At some point I might dispatch him, hopefully that serves as revenge for you as well."
            wid "I don't think you understand what you're saying."
            wid "His power and influence reaches all the way to the palace. He can make people disappear if he wants to..."
            abd "Yes, I'm aware of that already."
            abd "What I need to know is how he did it."
            abd "Why did he go after your husband?"
            "..."
            wid "It's so stupid really..."
            wid "It was our daughter."
            abd "Your daughter?"
            wid "Yes. Ever since Jafar was killed, the city's been a terrible place for women."
            wid "Jafar would've never let it get this bad."
            abd "True."
            wid "Jafar had him on a short leash."
            abd "And rightfully so."
            abd "Is his intention to marry your daughter?"
            wid "We thought it was, but..."
            wid "Had we known what would happen what's to come."
            abd "I see."
            abd "Since Jafar, err... {size=18}died...{/size} that the laws aren't followed anymore."
            wid "Well, no. Most people in Agrabah still obey the law as tradition."
            wid "But the man appointed by the Sultan to uphold those laws, doesn't obey them himself..."
            abd "Jafar's man?"
            "..."
            wid "You must understand, my husband was a good man, and a better father. He was a hard worker who always provided for us."
            wid "So when Rasoul, {size=36}that animal who's not worthy of kissing my husbands shoes{/size}, came asking after our daughter."
            abd "Hang on! So, you're saying that Rasoul asked to marry your daughter?"
            wid "Yes."
            abd "And your husband was against the idea?!"
            wid "Well yes, of course, all of us where against it."
            wid "Ever since Jafar died, this city's repugnant underbelly has started spilling into the streets."
            wid "And my husband spared no effort to protect our daughter from all of it, especially Rasoul."
            abd "So after your husband turned him down, what happened?"
            wid "It was the next night. Loud noises outside awoke us from our bed."
            wid "My Husband got up to see what the cause was, and the next thing, palace guards were storming through our front door to arrest him."
            abd "Did they say why?"
            wid "Not at the time, no."
            wid "But later when I tried to visit him in jail, they turned me away."
            wid "As I was leaving, I heard one of the guards mutter something like, 'Families of spies should be put to death too.'"
            abd "Wow..."
            abd "I don't know what to say."
            abd "So what happened next?"
            wid "Well, the next time I tried to visit my husband..."
            # show wid crying
            wid "They told me he'd been... {size=18}executed!{/size}"
            "..."
            abd "So let me guess. It wasn't long before Rasoul came knocking on your door?!"
            wid "{size=36}The very next day!{/size} in fact."
            abd "Jesus Christ! I mean... Jesus, the prophet..."
            "..."
            wid "He told me if I raise a fuss, he'll throw me in the dungeon and sell her into slavery."
            abd "That's terrible..."
            abd "Look, I might know someone who can help."
            wid "If only that were true..."
            wid "I fear that the only person who could've done anything at this point, was Jafar."
            wid "His absence is sorely missed..."
            abd "Well anyway, thank you for the information."
            wid "Goodbye."
            # if quest to follow, this is where it would send abd to Jafar
        "I can help you.":
            abd "I can help you."
            wid "I don't need any help, please leave."
            abd "Look, I know what that piece of shit has done to your family."
            wid "You... What do you mean? He didn't do anything!"
            abd "Please, I'm not trying to trick you."
            abd "I can help save you and your daughter, if you'll let me."
            wid "Why... How do I know that this isn't just another one of that devil's schemes?"
            abd "Well, you don't."
            abd "But I know if you don't let me help you now, soon your daughter will be lost to Rasoul forever."
            "..."
            # show wid crying
            wid "Okay."
            abd "Okay?"
            wid "Yes, okay. Please help save my daughter."
    jump poor
