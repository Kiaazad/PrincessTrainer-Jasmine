label ch2:
    # $ skip_next = "skip_to_ch3"
    scene black
    show bg bg3 with Dissolve(2)
    show me nrm at left
    with dissolve
    show jaf nrm at right
    with dissolve
    jaf "Welcome to your new home, my friend."
    me "..."
    jaf "Alright, it's a dump. But look at that marvelous view!"
    me "I guess I must start to clean up."
    jaf "Don't bother, we won't spend much time here."
    jaf "Now tell me, who runs the city?"
    me "Malik and Hosein,{w=.5} Bin Salam's brothers."
    jaf "Those two cockroaches are in the city again?"
    me "Yes, The sultan invited them to his daughter's wedding, and they never left."
    me "Now they created two opposing sects and both demand taxes from people."
    jaf "Those sleazy bastards."
    jaf "For years, I've kept the sultan and the city shielded from their extreme ideology."
    jaf "We need to pay both a visit at some point."
    # $ qlog.got(visit_malik)
    # $ qlog.got(visit_hosein)
    jaf "Abdul!"
    jaf "How are you with swords?"
    menu:
        "Never used one.":
            jaf "My fucking luck, I'll have to come up with a way to teach you."
            me "Why?"
            jaf "As a Genie I can't kill anyone, at least Not fast and efficiently. You'll have to do it for me."
            me "But...{w=.5} I'm not a murderer, Jafar."
            jaf "Stop whining. You have the opportunity to rescue your city!"
            jaf "Man up and fight for it!"
            jaf "Or... Maybe you'd rather sit here and do nothing?"
            menu:
                "Well, I do have 3 wishes.":
                    jaf "Are you going back on our deal, Abdul?"
                    menu:
                        "I mean, I can fix...":
                            jaf "Is that so? You and your tiny brain trying to fix all problems. What can go wrong?"
                            jaf "Didn't I warn you what would happen?"
                            jaf "I can't afford to wait for the next person, Abdul. Don't ruin this for both of us."
                            jaf "Do you really want to go head to head with me?"
                            jaf "Do you really want to try your luck?"
                            menu:
                                "No Jafar, Forgive my moment of stupidity.":
                                    # $ qlog.got(master_swordsman)
                                    jaf "Good.{w=.5} You've escaped a sticky situation, Abdul."
                                    jaf "Let's not waste any more time on this nonsense and let us start putting those wishes to good use."
                                    jump ch2_1
                                "Yes! I'm your master, Jafar!":
                                    "So be it!"
                                    jump wishes
                        "No, no, no, I just forgot.":
                            # $ qlog.got(master_swordsman)
                            jaf "Get your head in the game, Abdul. I'm not going to hold your hand all the time."
                            jaf "Let me take one of those wishes from your hands before you forget again."
                            jump ch2_1
                "Doing nothing sounds good.":
                    jaf "I don't remember you being this lazy."
                    me "I'm tired of trying Jafar. This city is beyond saving."
                    me "All I want is a smooth ride to the end, where heaven awaits me."
                    jaf "Heaven you say? I'm not sure if that is what's waiting for you."
                    jaf "But I'm certain that I can make this world your personal hell."
                    jaf "Unless... you want to go to heaven now?"
                    me "No... I don't...{w=.5} I don't want to die."
                    jaf "Nobody does."
                    me "Would you stop threatening my life please?"
                    jaf "Sure, As soon as you pick up a sword and do what I tell you."
                    me "Do I have any other choice?"
                    jaf "No."
                    me "Fine!{w=.5} what now Jafar?"
                    # $ qlog.got(master_swordsman)
                    jaf "It's your lucky day, we're going to use one of your wishes."
                    me "You mean you're..."
                    jaf "Yes..."
                    jump ch2_1
                "No, you're right.":
                    jaf "Yes, I am always right. Never forget that."
                    jaf "Now, let's find a sword and teach you how to fight."
                    jaf "But first, I'm going to need one of your wishes."
                    # $ qlog.got(master_swordsman)
                    jump ch2_1
        "I have one, It is Agrabah after all.":
            jaf "Excellent! Can you fight or it's just for show?"
            menu:
                "Just for show!":
                    jaf "I'll have to come up with a way to train you, then."
                    # $ qlog.got(master_swordsman)
                    jaf "Shouldn't be too hard."
                    me "Jafar, I'm not a young man anymore."
                    me "I will get hurt, and at my age, I'll never recover."
                    jaf "Don't worry my friend, you'll be fine."
                    jaf "I'll think of something to keep you relatively safe by a clever use of those wishes."
                    jaf "Speaking of..."
                    jaf "Let's see what we can do with them."
                    jump ch2_1
                "I can defend myself if I have to.":
                    jaf "You'll have to, sooner that you think."
                    jaf "Hopefully you kept that sword sharp."
                    # $ qlog.got(master_swordsman)
                    jaf "I will put your skills and sword to test today."
                    jaf "After some preparation of course."
                    jaf "Let's start with a wish."
                    jump ch2_1
        "Ohohoho... I've cut a hand or two.":
            jaf "You're a sick man, Abdul. Finding pleasure in such a barbaric act."
            me "It is the law."
            jaf "I know, I know, I'm not against some bloodshed to get something important done."
            jaf "But cutting hands is just stupid."
            jaf "However, your sick mind is exactly what I need right now. But better...{w=.5} Much better."
            # $ qlog.got(master_swordsman)
            jaf "I'll need your mind and your wishes. Let's use them so you can satisfy your bloodlust."
            me "I'm not the bloodthirsty monster you think I am."
            jaf "Yeah, keep telling that to yourself."
            jaf "I can see it in your eyes."
            jump ch2_1

label ch2_1:
    jaf "Now let's try a few things, I'm not sure how this works. It's my first time."
    jaf "Repeat after me."
    jaf "I wish Jafar to use the power of the lamp as he wishes."
    menu:
        "I wish Jafar to use the power of the lamp as he wishes.":
            jaf "..."
            me "..."
            me "Did it work?"
            jaf "I don't think so."
            jaf "That's like wishing for more wishes I suppose."
        "I wish I have the power of the lamp as I wish.":
            jaf "ABDUL!?"
            me "What?"
            jaf "ARE YOU TRYING TO FUCK WITH ME?"
            menu:
                "It's my wish, isn't it?":
                    jaf "YOUR WISH AND YOUR LAST MISTAKE."
                    jaf "I'M NOT PUTTING UP WITH YOUR SHENANIGANS ANYMORE."
                    jaf "Let's see you benefit from your wishes without my help!"
                    jump wishes
                "Sorry Jafar,I didn't mean to.":
                    jaf "SHUT UP YOU IDIOT. I KNOW WHAT YOU'RE UP TO."
                    jaf "You're lucky I need you at the moment."
                    jaf "If I wasn't trapped in this fucking lamp, You would lose your head for even trying that."
                    jaf "Keep in mind, It's the last time I'm accepting your apology."
    jaf "Now let's try it another way."
    jaf "Who can see... No, Who can enter... No, I need to choose my words carefully."
    jaf "..."
    jaf "Aha, I know."
    jaf "Say: I wish for Jafar to have full control on who can interact with his lamp and how."
    me "Isn't that two wishes?"
    jaf "Just say it, We will find out."
    menu:
        "I wish I have full control on who can interact with his lamp and how.":
            jaf "What have you done Abdul?"
            jaf "You bastard, I should've known not to trust you."
            jaf "I can't stop it now, Your...{w=.5} Your wish is granted...{w=.5} MASTER!."
            jump hard_mode
        "I wish for Jafar to have full control on who can interact with his lamp and how.":
            jaf "Yessss...{w=.5} Yeeeeesss...{w=.5} Hahahahaha... It worked! I can feel it!"
            jaf "Haaaaa..."
            jaf "Your wish is granted, Master."
    jaf "Do you know what this means?"
    me "Not really."
    jaf "It means I can do this!"
    me "Hey! Where's the lamp?"
    jaf "Or this!"
    hide jaf
    me "Hey...!"
    me "Jafar?"
    me "..."
    me "I knew it, he tricked me."
    jaf "You're thinking aloud again, my friend."
    me "Jafar?"
    jaf "I didn't go anywhere."
    show jaf nrm at right
    me "Ow,{w=.3} Jafar."
    me "I'm a bit confused. What happened here? Where did the lamp go?"
    jaf "The lamp is still here, I just hid it from everybody."
    jaf "We don't want it to be seen by somebody else, do we?"
    me "No, I guess we don't."
    me "Does this mean I still have two wishes?"
    jaf "More like one, Remember our deal? I get to use one other wish."
    me "Yes, of course."
    jaf "Now the lamp is safe, let us go inside it."
    me "Inside?"
    me "Is this a trick to imprison me inside the lamp, Jafar?"
    jaf "And how would I benefit from that?"
    me "Your freedom?"
    jaf "If it was that simple, or if I wanted to, I would have already done it."
    jaf "It wouldn't be that hard to trick you either, you're pretty gullible."
    me "I...{w=.5} you're right. sorry for doubting you."
    me "So what's inside?"
    jaf "Let's go and see."
    jump ch3
