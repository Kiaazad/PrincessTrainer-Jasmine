label ch2:
    # $ skip_next = "skip_to_ch3"
    scene black
    show bg bg3 with Dissolve(2)
    show me normal at left
    with dissolve
    show jaf normal at right
    with dissolve
    show jaf smile at right
    jaf "Welcome to your new home, my friend."
    show me confused at left
    me "..."
    show jaf normal at right
    jaf "Alright, it's a dump. But look at that marvelous view!"
    show me sad at left
    me "I guess I must start to clean up."
    jaf "Don't bother, we won't spend much time here."
    show me alert at left
    jaf "Now tell me, who runs the city?"
    show me alert at left
    me "Malik and Hosein,{w=.5} Bin Salam's brothers."
    show jaf annoyed at right
    jaf "Those two cockroaches are in the city again?"
    me "Yes, The sultan invited them to his daughter's wedding, and they never left."
    show me confused at left
    me "Now they created two opposing sects and both demand taxes from people."
    show me normal at left
    show jaf angry at right
    jaf "Those sleazy bastards."
    jaf "For years, I've kept the sultan and the city shielded from their extreme ideology."
    show jaf normal at right
    jaf "We need to pay both a visit at some point."
    # $ qlog.got(visit_malik)
    # $ qlog.got(visit_hosein)
    jaf "Abdul!"
    show me alert at left
    jaf "How are you with swords?"
    menu:
        "Never used one.":
            me "I never used one."
            show jaf disappointed at right
            jaf "My fucking luck, I'll have to come up with a way to teach you."
            show me confused at left
            me "Why?"
            show jaf normal at right
            jaf "As a Genie I can't kill anyone, at least Not fast and efficient. You'll have to do it for me."
            show me alert at left
            me "But...{w=.5} I'm not a murderer, Jafar."
            show jaf annoyed at right
            jaf "Stop whining. You have the opportunity to rescue your city!"
            jaf "Man up and fight for it!"
            show jaf normal at right
            jaf "Or... Maybe you'd rather sit here and do nothing?"
            menu:
                "Well, I do have 3 wishes.":
                    show me confused at left
                    me "Well, I do have 3 wishes."
                    show jaf angry at right
                    jaf "Are you going back on our deal, Abdul?"
                    menu:
                        "I mean, I can fix everything with my wishes now.":
                            me "I mean, I can fix..."
                            show jaf angry at right
                            show me alert at left
                            jaf "Is that so? You and your tiny brain trying to fix all problems. What can go wrong?"
                            jaf "Didn't I warn you what would happen?"
                            jaf "I can't afford to wait for the next person, Abdul. Don't ruin this for both of us."
                            jaf "Do you really want to go head to head with me?"
                            jaf "Do you really want to try your luck?"
                            menu:
                                "No Jafar, Forgive my moment of stupidity.":
                                    show me afraid at left
                                    me "No Jafar, Forgive my moment of stupidity."
                                    # $ qlog.got(master_swordsman)
                                    show jaf normal at right
                                    jaf "Good.{w=.5} You've escaped a sticky situation, Abdul."
                                    show me normal at left
                                    jaf "Let's not waste any more time on this nonsense and let us start putting those wishes to good use."
                                    jump ch2_1
                                "Yes! I'm your master, Jafar!":
                                    "Yes! I'm your master, Jafar!{nw}"
                                    show jaf magic at right
                                    "So be it!"
                                    jump wishes
                        "No, no, no, I just forgot.":
                            show me alert at left
                            me "No, no, no, I just forgot."
                            # $ qlog.got(master_swordsman)
                            show jaf disappointed at right
                            jaf "Get your head in the game, Abdul. I'm not going to hold your hand all the time."
                            show jaf normal at right
                            jaf "Let me take one of those wishes from your hands before you \"forget\" again."
                            jump ch2_1
                "Doing nothing sounds good.":
                    show me smile at left
                    me "Doing nothing sounds good."
                    show jaf thinking at right
                    jaf "I don't remember you being this lazy."
                    show me sad at left
                    me "I'm tired of trying Jafar. This city is beyond saving."
                    me "All I want is a smooth ride to the end, where heaven awaits me."
                    jaf "Heaven you say? I'm not sure if that is what's waiting for you."
                    jaf "But I'm certain that I can make this world your personal hell."
                    show me alert at left
                    show jaf normal at right
                    jaf "Unless... you want to go to heaven now?"
                    show me afraid at lef
                    me "No... I don't...{w=.5} I don't want to die."
                    jaf "Nobody does."
                    me "Would you stop threatening my life please?"
                    jaf "Sure, As soon as you pick up a sword and do what I tell you."
                    me "Do I have any other choice?"
                    jaf "No."
                    show me sad at left
                    me "Fine!{w=.5} what now Jafar?"
                    # $ qlog.got(master_swordsman)
                    show me normal at left
                    jaf "It's your lucky day, we're going to use one of your wishes."
                    me "You mean you're..."
                    jaf "Yes..."
                    jump ch2_1
                "No, you're right.":
                    me "No, you're right."
                    show jaf normal at right
                    jaf "Yes, I am always right. Never forget that."
                    jaf "Now, let's find a sword and teach you how to fight."
                    jaf "But first, I'm going to need one of your wishes."
                    # $ qlog.got(master_swordsman)
                    jump ch2_1
        "I have one, It is Agrabah after all.":
            show me smile at left
            me "I have one, It is Agrabah after all."
            jaf "Excellent! Can you fight or it's just for show?"
            menu:
                "Just for show!":
                    show me alert at left
                    me "Just for show!"
                    show jaf thinking at right
                    jaf "I'll have to come up with a way to train you, then."
                    # $ qlog.got(master_swordsman)
                    jaf "Shouldn't be too hard."
                    show me concerned at left
                    me "Jafar, I'm not a young man anymore."
                    me "I will get hurt, and at my age, I'll never recover."
                    show jaf normal at right
                    jaf "Don't worry my friend, you'll be fine."
                    jaf "I'll think of something to keep you relatively safe by a clever use of those wishes."
                    show jaf thinking at right
                    jaf "Speaking of..."
                    show jaf normal at right
                    jaf "Let's see what we can do with them."
                    jump ch2_1
                "I can defend myself if I have to.":
                    show me smug at left
                    me "I can defend myself if I have to."
                    show jaf thinking at right
                    jaf "You'll have to, sooner that you think."
                    show me alert at left
                    show jaf normal at right
                    jaf "Hopefully you kept that sword sharp."
                    # $ qlog.got(master_swordsman)
                    jaf "I will put your skills and sword to test today."
                    jaf "After some preparation of course."
                    jaf "Let's start with a wish."
                    jump ch2_1
        "Ohohoho... I've cut a hand or two.":
            show me smug at left
            me "Ohohoho... I've cut a hand or two."
            show jaf disappointed at right
            jaf "You're a sick man, Abdul. Finding pleasure in such a barbaric act."
            me "It is the law."
            show jaf normal at right
            jaf "I know, I know, I'm not against some bloodshed to get something important done."
            jaf "But cutting hands is just stupid."
            show me alert at left
            jaf "However, your sick mind is exactly what I need right now. But better...{w=.5} Much better."
            # $ qlog.got(master_swordsman)
            jaf "I'll need your mind and your wishes. Let's use them so you can satisfy your bloodlust."
            show me concerned at left
            me "I'm not the bloodthirsty monster you think I am."
            jaf "Yeah, keep telling that to yourself."
            show me alert at left
            jaf "I can see it in your eyes."
            jump ch2_1

label ch2_1:
    show jaf thinking at right
    jaf "Now let's try a few things, I'm not sure how this works."
    jaf "Last time ended up in a disaster."
    show jaf normal at right
    jaf "Repeat after me."
    jaf "I wish Jafar to use the power of the lamp as he wishes."
    menu:
        "I wish Jafar to use the power of the lamp as he wishes.":
            show me alert at left
            me "I wish Jafar to use the power of the lamp as he wishes."
            show jaf looking at right
            jaf "..."
            me "..."
            show jaf normal at right
            show me concerned at left
            me "Did it work?"
            show jaf thinking at right
            jaf "I don't think so."
            jaf "That's like wishing for more wishes I suppose."
        "I wish I have the power of the lamp as I wish.":
            show me smug at left
            me "I wish I have the power of the lamp as I wish."
            show jaf angry at right
            jaf "ABDUL!?"
            show me alert at left
            me "What?"
            jaf "ARE YOU TRYING TO FUCK WITH ME?"
            menu:
                "It's my wish, isn't it?":
                    me "It's my wish, isn't it?"
                    jaf "YOUR WISH AND YOUR LAST MISTAKE."
                    jaf "I'M NOT PUTTING UP WITH YOUR SHENANIGANS ANYMORE."
                    jaf "Let's see you benefit from your wishes without my help!"
                    jump wishes
                "Sorry Jafar,I didn't mean to.":
                    show me alert at left
                    me "Sorry Jafar,I didn't mean to."
                    jaf "SHUT UP YOU IDIOT. I KNOW WHAT YOU'RE UP TO."
                    jaf "You're lucky I need you at the moment."
                    show jaf disappointed at right
                    jaf "If I wasn't trapped in this fucking lamp, You would lose your head for even trying that."
                    jaf "Keep in mind, It's the last time I'm accepting your apology."
    show jaf normal at right
    jaf "Now let's try it another way."
    show me normal at left
    show jaf thinking at right
    jaf "Who can see... No, Who can enter... No, I need to choose my words carefully."
    jaf "..."
    show jaf normal at right
    jaf "Aha, I know."
    jaf "Say: I wish for Jafar to have full control on who can interact with his lamp and how."
    show me concerned at left
    me "Isn't that two wishes?"
    jaf "Just say it, We will find out."
    menu:
        "I wish I have full control on who can interact with his lamp and how.":
            show me smug at left
            me "I wish I have full control on who can interact with his lamp and how."
            show jaf genie at right
            jaf "What have you done Abdul?"
            jaf "You bastard, I should've known not to trust you."
            jaf "I can't stop it now, Your...{w=.5} Your wish is granted...{w=.5} MASTER!."
            jump hard_mode
        "I wish for Jafar to have full control on who can interact with his lamp and how.":
            show me alert at left
            me "I wish for Jafar to have full control on who can interact with his lamp and how."
            show jaf magic at right
            jaf "Yessss...{w=.5} Yeeeeesss...{w=.5} Hahahahaha... It worked! I can feel it!"
            jaf "Haaaaa..."
            jaf "Your wish is granted, Master."
    show jaf thinking at right
    jaf "Do you know what this means?"
    show me confused at left
    me "Not really."
    jaf "It means I can do this!"
    show me concerned at left
    me "Hey! Where's the lamp?"
    jaf "Or this!"
    hide jaf
    me "Hey...!"
    me "Jafar?"
    me "..."
    show me sad at left
    me "I knew it, he tricked me."
    jaf "You're thinking aloud again, my friend."
    show me alert at left
    me "Jafar?"
    jaf "I didn't go anywhere."
    show jaf normal at right
    me "Ow,{w=.3} Jafar."
    show me confused at left
    me "I'm a bit confused. What happened here? Where did the lamp go?"
    jaf "The lamp is still here, I just hid it from everybody."
    jaf "We don't want it to be seen by somebody else, do we?"
    show me alert at left
    me "No, I guess we don't."
    show me concerned at left
    me "Does this mean I still have two wishes?"
    jaf "More like one, Remember our deal? I get to use one other wish."
    show me alert at left
    me "Yes, of course."
    jaf "Believe me, one wish is more than enough."
    jaf "Now the lamp is safe, let us go inside it."
    show me concerned at left
    me "Inside?"
    me "Is this a trick to imprison me inside the lamp, Jafar?"
    show jaf probing at right
    jaf "And how would I benefit from that?"
    show me alert at left
    me "Your freedom?"
    show jaf normal at right
    jaf "If it was that simple, or if I wanted to, I would have already done it."
    jaf "It wouldn't be that hard to trick you either, you're pretty gullible."
    show me embarrassed at left
    me "I...{w=.5} you're right. sorry for doubting you."
    show me concerned at left
    me "So what's inside?"
    jaf "Let's go and see."
    jump ch3
