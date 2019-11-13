label ch3:
    # $ skip_next = "skip_to_ch4"
    scene black
    show bg black
    show abd concerned at left
    with dissolve
    show jaf normal at right
    with dissolve
    abd "Are we inside the lamp now?"
    jaf "Yes."
    abd "And I'm still alive?"
    jaf "Yes."
    show abd normal at left
    abd "..."
    show abd smug at left
    abd "It's a lot bigger on the inside."
    jaf "..."
    abd "You have quite a lot of leg room in here."
    jaf "..."
    abd "Doesn't smell like farts either."
    show jaf annoyed at right
    jaf "Stop with your wisecracks, we have work to do."
    show abd alert at left
    show jaf normal at right
    jaf "You need to learn how to navigate this place when I'm not around."
    show abd concerned at left
    abd "First question, how do I get inside on my own?"
    show jaf thinking at right
    jaf "Excellent question, I brought us in here just by thinking about it, but you're going to need a kind of spell."
    show abd normal at left
    jaf "I'll come up with something."
    show jaf normal at right
    jaf "But first, let me show you the different places in here."
    menu:
        "I can find my way around, let's get to something more exciting.":
            show abd smug at left
            abd "I can find my way around, let's get to something more exciting."
            show jaf thinking at right
            jaf "Eager to get going, aren't you?"
            show abd normal at left
            show jaf normal at right
            jaf "Have a look around then meet me in my library."
            jump ch3_1
        "Yes, please. This place looks like the desert night.":
            show abd concerned at left
            abd "Yes, please. This place looks like the desert night."
            jaf "Are you afraid of the dark?"
            abd "No. I'm afraid of what might be hiding in the darkness. How do I know I won't fall into a hole?"
            abd "What are we standing on, anyway?"
            show jaf thinking at right
            jaf "Quantum foam."
            abd "What?"
            jaf "Look, just, don't worry about it. You're safe in here."
            show abd alert at left
            show jaf normal at right
            jaf "Just don't wander too far away from the bright spots."
            jaf "It's not that easy to find your way back in the darkness."
            abd "Okay..."
            # save
            # show bg sav
            show abd normal at left
            abd "Wow... that's a lot of... empty jars?"
            show abd smug at left
            abd "Are they an obsession of yours?"
            show abd concerned at left
            abd "Where are they hanging from? I can't see the ceiling."
            jaf "Quantum foam."
            abd "..."
            show jaf normal at right
            show abd alert at left
            jaf "Here, take this."
            # $ msg.msg("Received a bag.")
            show abd normal at left
            abd "..."
            # $ msg.msg("...of sand?")
            show abd confused at left
            abd "A bag of sand?"
            jaf "These are the Sands of Time."
            jaf "Grab a handful, put in one of these jars and the 'you' from that moment will remain there."
            show abd alert at left
            # $ msg.msg("Right, Received sands of time, a dozen handfuls.")
            jaf "That 'you' can be recovered if something...{w=.5} unfortunate happens to you."
            abd "You can resurrect me?"
            show jaf thinking at right
            jaf "Not exactly."
            show abd concerned at left
            show jaf normal at right
            jaf "You would have to wish for resurrection, and it wouldn't be a pretty sight. Plus, it's difficult to wish when you're dead!"
            jaf "This is my way to manage around that problem."
            jaf "Just don't overdo it, you don't have much sand and it's not easy to obtain more of it."
            show abd alert at left
            abd "Alright."
            # set
            show bg sett
            show abd normal at left
            abd "What's this one?"
            show jaf thinking at right
            jaf "To be honest, I'm not entirely sure. These devices seem to have some minor effects on the outside world."
            show jaf normal at right
            jaf "Since I've been trapped in here, I haven't have any use for them."
            jaf "You'll have to try them by yourself, I'm afraid."
            # lib
            show bg lib
            # this part can use a revamp
            abd "You have a library in here?"
            jaf "Of course."
            show abd confused at left
            abd "Let's see..."
            abd "Jafar's Introductory Macroeconomics for Sultans."
            abd "Jafar's Guide to Appropriate and Proper Palace Etiquette."
            abd "Jafar's Illustrated Manual of...{w=.5} Tapdance?"
            show jaf disappointed at right
            jaf "Not one of my best, I have to admit."
            show jaf normal at right
            show abd smug at left
            abd "Are {b}all{/b} of these books written by you, Jafar?"
            show abd concerned at left
            jaf "Yes, I need to transfer my knowledge to the next generation somehow."
            show jaf thinking at right
            jaf "And it's not as though I've had a whole lot of other things on my plate."
            show abd alert at left
            jaf "You should borrow a few of them at some point."
            show jaf normal at right
            jaf "In fact...{w=.2} You'll need to read them all, they'll help you with your quest."
            show abd smug at left
            abd "Even...?"
            show jaf annoyed at right
            jaf "Yes, even \"Tapdance.\" Particularly that one."
            show abd normal at left
            show jaf normal at right
            jaf "Speaking of your quest..."
            jaf "I'll keep track of your progress...{nw}"
            # quest
            show bg quest
            jaf "Here."
            abd "A mirror?"
            jaf "Through this mirror I can watch you outside of the lamp. Guide you and give you information."
            show abd concerned at left
            abd "You can see me all the time?"
            show jaf probing at right
            jaf "What's the matter?"
            abd "What about my privacy?"
            show jaf normal at right
            jaf "Get over yourself, I don't have time to watch you all the time. I have books to write."
            jaf "And I don't have any interest in watching you jerk off."
            jaf "I have a harem for myself."
            show abd excited at left
            abd "A harem? Let's go see it!"
            # fight
            show bg fight
            abd "Not this."
            # gallery
            show bg gall
            abd "Nor this."
            # harem
            show bg harem
            abd "Woah, you have slave girls in here? Three of them?"
            jaf "No, they aren't slaves, they're free."
            show abd confused at left
            abd "Wifes?"
            jaf "No, they're just... here. For some reason."
            jaf "And they seem to be happy just keeping me company."
            show abd embarrassed at left
            abd "Ummm..."
            abd "Can I? Ummm... I mean... May I?"
            show jaf probing at right
            jaf "Fuck them?"
            show abd alert at left
            show jaf normal at right
            jaf "I'm not the one you should ask."
            show abd normal at left
            jaf "Ask them. They're adults, it's up to them to decide."
            show jaf thinking at right
            jaf "Communication might be a problem though. I'm not sure if they can speak."
            jaf "Never heard a word out of them myself."
            show jaf normal at right
            jaf "You might want to take advantage of the running water and take a shower first. We're trying to keep it clean in here."
            show abd alert at left
            abd "A shower...? Hey, are those?"
            show jaf disappointed at right
            jaf "Yes, those are statues of me peeing.{w=.5} It seemed like a good idea at the time."
            jaf "The girls seem to like them, and I wasn't expecting any guests."
            show jaf normal at right
            jaf "Now, let's go back and visit the places we skipped."
            menu:
                "Sure, I can come back later.":
                    show abd normal at left
                    abd "Sure, I can come back later."
                    # fight
                    show bg fight
                    jaf "This is my throne. You'll be fighting the creatures I conjure in here."
                    jaf "To increase your fighting skill, and maybe for my amusement."
                    jaf "You can come here and start fighting at any time."
                    jaf "Do you want to give it a try?"
                    menu:
                        "Yes.":
                            show abd alert at left
                            abd "Yes."
                            jaf "Alright, here we go."
                            # call ch3_fight(True)
                            show abd normal at left
                            with dissolve
                            show jaf normal at right
                            with dissolve
                            jaf "Not bad."
                            jaf "At least you didn't die."
                            jaf "Now."
                            jaf "I'll have to prepare something."
                            jaf "Meet me at my library when you're done."
                            hide jaf with dissolve
                            jump ch3_1
                        "Maybe later.":
                            show abd normal at left
                            show jaf normal at right
                            abd "Maybe later."
                            jaf "Alright. Next is the Hall of Memories."
                            # hall of memories
                            jaf "You can revisit your proudest moments in here."
                            jaf "And that's it. I have some thinking to do. Feel free to roam around while I'm busy."
                            jaf "Meet me at my library when you're done."
                            hide jaf with dissolve
                            jump ch3_1
                "I think I'm going to take that shower you've suggested now.":
                    show abd embarrassed at left
                    abd "I think I'm going to take that shower you've suggested now."
                    show jaf disappointed at right
                    jaf "Of course, there are women around, so you aren't capable of thinking straight."
                    jaf "Come to me when you've relieved yourself."
                    show jaf normal at right
                    jaf "I'll think of a plan in the mean time."
                    jaf "And we're going to have to work on your self-discipline."
                    hide jaf with dissolve
                    menu:
                        "Go talk to the girls.":
                            call harem_girls
                            jump ch3_1
                        "Jump right into the water.":
                            show bg cg_abdul_bathing
                            "the bathing scene is not ready"
                            menu:
                                "Go talk to the girls.":
                                    call harem_girls
                                    jump ch3_1
                                "Go back to Jafar.":
                                    jump ch4

label ch3_1:
    menu:
        "This part will be replaced by a proper screen, but for now have a menu."
        "Go to library.":
            jump ch4
        "Go to Harem.":
            jump ch3_harem
        "Go to hall of... Sands of Time.":
            jump ch3_sav
        "Go to Room of Settings.":
            jump ch3_set
        "Go Fight.":
            call ch3_fight
        "Go to the Mirror Room.":
            jump ch3_mirror
label ch3_harem:
    scene bg harem
    menu:
        "Go talk to the girls.":
            call harem_girls
            jump ch3_1
        "Jump right into the water.":
            show bg cg_abdul_bathing
            "the bathing scene is not ready"
            menu:
                "Go talk to the girls.":
                    call harem_girls
                    jump ch3_1
                "Go back to Jafar.":
                    jump ch4
    jump ch3_1
label ch3_sav:
    scene bg sav
    "Nothing to do here."
    jump ch3_1
label ch3_set:
    scene bg sett
    "Nothing to do here."
    jump ch3_1
label ch3_fight(j=False):
    window hide
    # call fights([player], [enemy1])
    if j:
        return
    else:
        jump ch3_1
label ch3_mirror:
    "the quest screen is not even designed, just a test to make sure it's functional."
    show screen quests
    pause
    jump ch3_1
