default visit_malik = quest(
    _("Visit Malik"),
    _("Visit Malik and find something you can use against him."),
    )

default visit_hosein = quest(
    _("Visit Hosein"),
    _("Visit Hosein and find something you can use against him."),
    )

default master_swordsman = quest(
    _("Master Swordsman"),
    _("Become a master swordsman, the best in Agrabah."),
    )

label ch2:
    $ street_home_loc.enabled = True
    show black with Dissolve(2)
    show bg agrabah onlayer bg
    show screen pnc(abdul, agrabah_map)
    show abd normal at left
    show jaf normal at right
    hide black with Dissolve(2)
    show jaf smile at right
    jaf "Welcome to your new luxurious home, my friend."
    show abd confused at left
    "..."
    show jaf normal at right
    jaf "Alright, it's a dump. But look at that marvelous view!"
    show abd sad at left
    abd "There's a lot of cleaning up to do..."
    jaf "Don't bother, we won't spend too much time in here anyway."
    show abd alert at left
    jaf "Now tell me, who runs this city?"
    show abd alert at left
    abd "Malik and Hosein,{w=.2} Bin Salam's brothers."
    show jaf annoyed at right
    jaf "Those two cockroaches are back in the city?"
    abd "Yes. The Sultan invited them to his daughter's wedding, and they never left."
    show abd confused at left
    abd "Now they created two opposing sects in town, and both demand taxes from people."
    show abd normal at left
    show jaf angry at right
    jaf "Those sleazy bastards."
    jaf "For years, I've kept the sultan and the city shielded from their extreme ideology."
    show jaf normal at right
    jaf "We'll need to pay both a visit, eventually."
    $ qlog.got(visit_malik)
    $ qlog.got(visit_hosein)
    jaf "Abdul!"
    show abd alert at left
    $ abdul.gotskill(kick)
    $ abdul.gotskill(punch)
    menu:
        jaf "How are you with swords?"
        "Never used one.":
            abd "I never used one."
            show jaf disappointed at right
            jaf "Just my fucking luck. I'll have to come up with a way to teach you."
            jaf "You can kick and punch right?"
            show abd confused at left
            abd "Of course, why?"
            show jaf normal at right
            jaf "As a Genie, I can't directly kill anyone."
            jaf "So you're going to have to do that for me."
            show abd alert at left
            abd "But...{w=.2} I'm not a murderer, Jafar."
            show jaf annoyed at right
            jaf "Killing and murdering are different. Very different."
            jaf "Look! You have the opportunity to rescue your city! Man up and fight for it!"
            show jaf normal at right
            
            menu:
                jaf "Or... Maybe you'd rather sit here and do nothing?"
                "Well, I do have 3 wishes.":
                    show abd confused at left
                    abd "Well, I do have 3 wishes."
                    show jaf angry at right
                    
                    menu:
                        jaf "Are you going back on our deal, Abdul?"
                        "I mean, can't I just fix everything with my wishes now?":
                            abd "I mean, can't I just fix..."
                            show jaf angry at right
                            show abd alert at left
                            jaf "Is that so? You and your tiny brain of yours are going to fix everyone's problems. What can go wrong?"
                            jaf "Didn't I warn you what would happen?"
                            jaf "I can't afford to wait for the next person, Abdul. Don't ruin this for both of us."
                            jaf "Do you really want to go head to head with me?"
                            
                            menu:
                                jaf "Do you really want to try your luck?"
                                "No Jafar. Forgive my moment of stupidity.":
                                    show abd afraid at left
                                    abd "No Jafar. Forgive my moment of stupidity."
                                    $ qlog.got(master_swordsman)
                                    show jaf normal at right
                                    jaf "Good.{w=.5} You've escaped a sticky situation, Abdul."
                                    show abd normal at left
                                    jaf "Let's not waste any more time on this nonsense and let us start putting those wishes to good use."
                                    jump ch2_1
                                "Yes! I'm your master, Jafar!":
                                    "Yes! I'm your master, Jafar!{nw}"
                                    show jaf magic at right
                                    "So be it!"
                                    jump wishes
                        "No, no, no, I just forgot.":
                            show abd alert at left
                            abd "No, no, no, I just forgot."
                            $ qlog.got(master_swordsman)
                            show jaf disappointed at right
                            jaf "Get your head in the game, Abdul. I'm not going to hold your hand all the time."
                            show jaf normal at right
                            jaf "Let me take one of those wishes from your hands before you \"forget\" again."
                            jump ch2_1
                "Doing nothing sounds good.":
                    show abd smile at left
                    abd "Doing nothing sounds good."
                    show jaf thinking at right
                    jaf "I don't remember you being this lazy."
                    show abd sad at left
                    abd "I'm tired of trying Jafar. This city is beyond saving."
                    abd "All I want is a smooth ride to the end, where heaven awaits me."
                    jaf "Heaven you say? I'm not sure if that's what waiting for you."
                    jaf "But I'm certain that I can make this world your personal hell."
                    show abd alert at left
                    show jaf normal at right
                    jaf "Unless... you want to go to heaven now?"
                    show abd afraid at left
                    abd "No... I don't...{w=.5} I don't want to die."
                    jaf "Nobody does."
                    abd "Would you stop threatening my life please?"
                    jaf "Sure, just as soon as you pick up a sword and do as I say."
                    abd "Do I have any other choice?"
                    jaf "No."
                    show abd sad at left
                    abd "Fine!{w=.5} what now Jafar?"
                    $ qlog.got(master_swordsman)
                    show abd normal at left
                    jaf "It's your lucky day, we're going to use one of your wishes."
                    abd "You mean you're..."
                    jaf "Yes..."
                    jump ch2_1
                "No, you're right.":
                    abd "No, you're right."
                    show jaf normal at right
                    jaf "Yes, I am always right. Never forget that."
                    jaf "Now, let's find a sword and I'll teach you how to fight."
                    jaf "But first, I'm going to need one of your wishes."
                    $ qlog.got(master_swordsman)
                    jump ch2_1
        "I have one, this is Agrabah after all.":
            show abd smile at left
            abd "I have one, this is Agrabah after all."
            
            menu:
                jaf "Excellent! Can you fight or is it just for show?"
                "Just for show.":
                    show abd alert at left
                    abd "Just for show."
                    show jaf thinking at right
                    jaf "I'll have to come up with a way to train you, then."
                    $ qlog.got(master_swordsman)
                    jaf "Shouldn't be too hard."
                    show abd concerned at left
                    abd "Jafar, I'm not a young man anymore."
                    abd "I will get hurt, at this age, I'll never recover."
                    show jaf normal at right
                    jaf "Don't worry my friend, you'll be fine."
                    jaf "I'll be able to keep you relatively safe... at least when you practice."
                    show jaf thinking at right
                    jaf "Speaking of what I can do..."
                    show jaf normal at right
                    jaf "Let's see about those wishes."
                    jump ch2_1
                "I can defend myself if I have to.":
                    $ abdul.levelup(1)
                    $ abdul.gotskill(slash)
                    $ abdul.gotskill(pierce)
                    show abd smug at left
                    abd "I can defend myself if I have to."
                    show jaf thinking at right
                    jaf "Well, you'll have to. Probably sooner then you think."
                    show abd alert at left
                    show jaf normal at right
                    jaf "Hopefully you kept that sword sharp."
                    $ qlog.got(master_swordsman)
                    jaf "I will put your skills and sword to test today."
                    jaf "After some preparation of course."
                    jaf "But let's start with a wish."
                    jump ch2_1
        "Ohohoho... I've cut a hand or two.":
            $ abdul.levelup(3)
            $ abdul.gotskill(slash)
            $ abdul.gotskill(pierce)
            show abd smug at left
            abd "Ohohoho... I've cut a hand or two."
            show jaf disappointed at right
            jaf "You're a sick man, Abdul. Finding pleasure in such a barbaric act."
            abd "It is the law."
            show jaf normal at right
            jaf "I know, I know, I'm not against some bloodshed to get something important done. I just don't resort to violence unless I must."
            jaf "Cutting off hands is just stupid. Rehabilitation is pretty hard when you are missing a hand and can't work."
            show abd alert at left
            jaf "That being said, your enthusiasm for violence is exactly what I need right now."
            $ qlog.got(master_swordsman)
            jaf "But that attitude isn't enough on its own. We need your wishes, too. Let's use them so you can satisfy your bloodlust."
            show abd concerned at left
            abd "I'm not a bloodthirsty monster that you think I am."
            jaf "Yeah, keep telling that to yourself."
            show abd alert at left
            jaf "I can see it in your eyes."
            jump ch2_1

label ch2_1:
    show jaf thinking at right
    jaf "Okay, my last experience with wishes ended up in disaster."
    jaf "...and the first time, too."
    jaf "But we learn from our mistakes. Let's try this."
    show jaf normal at right

    menu:
        jaf "Repeat after me... {w=.4}I wish that Jafar can use the lamp as he wishes."
        "I wish that Jafar can use the lamp as he wishes.":
            show abd alert at left
            abd "I wish that Jafar can use the lamp as he wishes."
            show jaf looking at right
            "..."
            "..."
            show jaf normal at right
            show abd concerned at left
            abd "Did it work?"
            show jaf thinking at right
            jaf "I don't think so."
            jaf "That's like wishing for more wishes I suppose."
        "I wish that I can use the lamp as I wish.":
            show abd smug at left
            abd "I wish that I can use the lamp as I wish."
            show jaf angry at right
            jaf "ABDUL!?"
            show abd alert at left
            abd "What?"
            
            menu:
                jaf "ARE YOU TRYING TO FUCK WITH ME?"
                "It's my wish, isn't it?":
                    abd "It's my wish, isn't it?"
                    jaf "YOUR WISH AND YOUR LAST MISTAKE."
                    jaf "I'M NOT PUTTING UP WITH YOUR SHENANIGANS ANYMORE."
                    jaf "Let's see you benefit from your wishes without my help!"
                    jump wishes
                "Sorry Jafar, I didn't mean to.":
                    show abd alert at left
                    abd "Sorry Jafar,I didn't mean to."
                    jaf "SHUT UP YOU IDIOT. I KNOW WHAT YOU'RE UP TO."
                    jaf "You're lucky I need you at the moment."
                    show jaf disappointed at right
                    jaf "If I wasn't trapped in this fucking lamp, you would lose your head for even trying at that."
                    jaf "Keep in mind, this is the last time I'm accepting your apology."
    show jaf normal at right
    jaf "Now let's try it another way."
    show abd normal at left
    show jaf thinking at right
    jaf "Who can rob... {w=.4}No, {w=.4}who can enter... {w=.4}No, {w=.8}I need to choose my words carefully."
    "..."
    show jaf normal at right
    jaf "Aha, I know."
    jaf "Say: I wish that only Jafar can decide who can see this lamp."
    show abd concerned at left
    abd "Isn't that...?{nw}"
    
    menu:
        jaf "Just say it, We will find out."
        "I wish that only I can decide who can see this lamp.":
            show abd smug at left
            abd "I wish that only I can decide who can see this lamp.."
            show jaf genie at right
            jaf "What have you done, Abdul?!"
            jaf "You bastard, I should've known not to trust you!"
            jaf "I can't stop it now, Your...{w=.5} Your wish is granted...{w=.5} MASTER!"

            # add hard mode
            scene
            "The hard mode haven't been added yet, please start again and try to comply with Jafar this time."
            "I'll return you to an earlier point."
            jump ch2_1
            # jump hard_mode
        "I wish that only Jafar can decide who can see this lamp..":
            show abd alert at left
            abd "I wish that only Jafar can decide who can see this lamp.."
            show jaf magic at right
            jaf "Yessss...{w=.5} Yeeeeesss...{w=.5} Hahahahaha... It worked! I can feel it!"
            jaf "Haaaaa..."
            jaf "Your wish is granted, Master."
    show jaf thinking at right
    jaf "Do you know what this means?"
    show abd confused at left
    abd "Not really."
    jaf "Put the lamp in that corner."
    abd "Alright..."
    # ---------- lamp animation
    "{nw}"
    show abd normal at left:
        ease .6 xalign .2
        ease .4 xzoom -1
    pause 1
    show abd bent at left:
        xalign .2
    pause .2
    $ agrabah_lamp.hidden = False
    $ hero.drop(black_lamp, 1)
    show abd normal at left:
        ease .6 xalign .2
    jaf "Excellent."
    jaf "It means I can do this!"
    # ------ lamp hide
    $ agrabah_lamp.hidden = True
    
    show abd concerned at left with move
    show abd concerned at left:
        ease .2 xzoom 1
    abd "Hey! Where's the lamp?"
    jaf "Or this!"
    hide jaf
    abd "Hey...!"
    abd "Jafar?"
    "..."
    show abd sad at left
    abd "I knew it, he tricked me."
    jaf "You're thinking out loud again, my friend."
    show abd alert at left
    abd "Jafar?"
    jaf "I didn't go anywhere."
    show jaf normal at right
    abd "Ow,{w=.3} Jafar."
    show abd confused at left
    abd "I'm a bit confused. What happened here? Where did the lamp go?"
    jaf "The lamp is still there, I just hid it from everybody."
    jaf "We don't want it to be seen by somebody else, do we? That's caused a lot of problems in the past."
    show abd alert at left
    abd "No, I guess we don't."
    show abd concerned at left
    abd "Does this mean I still have two wishes?"
    jaf "More like one. Remember our deal? I get to use one other wish."
    show abd alert at left
    abd "Yes, of course."
    jaf "Believe me, one wish is more than enough."
    jaf "Now that the lamp is safe, go get something to eat and rest a little."
    jaf "I can hear your stomach rumbling."
    "..."
    jaf "Once you're ready, rub the lamp, we have more to do."
    abd "But you took it away."
    # show screen lamp_get
    show jaf magic at right
    $ agrabah_lamp.hidden = False
    jaf "Here"
    show jaf normal at right
    # ------------ lamp appear
    jaf "Now only you can see it."
    jaf "It should be safer than hanging from your waist."
    jaf "Now go, before the shops in the bazaar close."
    abd "Oh, right!"
    jump agrabah


transform lamp_get_trans:
    alpha 0 align (.5,.5) zoom 3 rotate 45
    ease .2 alpha 1
    ease .4 align (0.0,0.0) zoom .2 rotate 0

screen lamp_get:
    zorder 1100
    button:
        background None
        # at lamp_get_trans
        add "bg/agrabah/lamp.png"
        action Jump("lamp_visit")

