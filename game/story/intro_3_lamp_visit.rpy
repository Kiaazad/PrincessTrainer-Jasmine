label lamp_visit:
    scene black
    hide screen pnc
    hide screen lamp_get
    show bg black
    show abd concerned at left
    with dissolve
    $ agrabah_lamp.act = Jump('inside_lamp')
    abd "Woaaaaah. What?"
    jaf "Welcome to my humble lamp, Abdul."
    show jaf normal at right
    with dissolve
    abd "Jafar? Did you bring me inside your lamp?"
    jaf "Yes."
    abd "I knew it!"
    jaf "You knew what?"
    abd "Did you bring me here to trap me inside your lamp?"
    show jaf probing at right
    jaf "Now why would I want to do that?"
    show abd alert at left
    abd "To gain your freedom?"
    show jaf normal at right
    jaf "If it was that simple, or even if I wanted to, I would have done it already."
    jaf "It wouldn't be that hard to trick you either, you're pretty gullible."
    show abd embarrassed at left
    abd "I...{w=.5} you're right. Sorry for doubting you."
    show abd concerned at left
    abd "So why did you bring me here?"
    jaf "Abdul my friend, we are going to work together."
    jaf "I want to show you my home."
    abd "This darkness is your home?"
    show abd normal at left
    "..."
    show abd smug at left
    abd "It's a lot bigger on the inside."
    "..."
    abd "You have quite the leg room in here too."
    "..."
    abd "Doesn't smell like farts either."
    show jaf annoyed at right
    jaf "Stop with your wisecracks, we have work to do."
    show abd alert at left
    show jaf normal at right
    jaf "You need to learn how to navigate this place when I'm not around."
    show abd concerned at left
    abd "First question, how do I get in and out on my own?"
    show jaf thinking at right
    jaf "Excellent question, to get in just rub the lamp."
    show abd normal at left
    abd "And rub it again to go out?"
    jaf "Nope, you can't bring the lamp inside itself."
    abd "Hey, it's gone..."
    jaf "Didn't you hear what I said?"
    abd "Oh!"
    jaf "I'll come up with something. We can worry about that later."
    show jaf normal at right

    menu:
        jaf "But first, let me show you around."
        "I can find my way around, let's get to something more exciting.":
            show abd smug at left
            abd "I can find my way around, let's get to something more exciting."
            show jaf thinking at right
            jaf "Eager to draw your sword, aren't you?"
            show abd normal at left
            show jaf normal at right
            jaf "All right, have a look around by yourself then meet me in my library."
            hide jaf with dissolve
            jump ch3_1
        "Yes, please. This place looks like the desert at night.":
            show abd concerned at left
            abd "Yes, please. This place looks like the desert at night."
            jaf "Are you afraid of the dark?"
            abd "No. I'm afraid of what might be hiding in the darkness. How do I know I won't fall in a hole?"
            show jaf thinking at right
            show abd alert at left
            show jaf normal at right
            jaf "Just don't wander far away from the bright spots."
            jaf "It's not that easy to find your way back in the darkness."
            abd "Okay..."

label lamp_visit_save:
    # save
    # show bg sav
    show screen save(_layer = "bg")
    scene
    show jaf normal at right
    show abd normal at left
    abd "Empty jars?"
    show abd smug at left
    abd "Are they an obsession of yours?"
    show abd concerned at left
    abd "Where are they hanging from? I can't see the ceiling."
    jaf "There's no ceiling here, no walls and that thing you're walking on is not a floor."
    show abd scared at left
    abd "Wait, what!?"
    show jaf angry at right
    jaf "Focus, Abdul!"
    show jaf normal at right
    show abd alert at left
    jaf "Here, take this."
    $ msg.msg("Received a bag?")
    show abd normal at left
    "..."
    $ msg.msg("...of sand?")
    show abd confused at left
    abd "A bag of sand?"
    jaf "These are the Sands of Time."
    jaf "Extremely valuable!"
    jaf "Grab a handful, put it in one of these jars and the 'you' from that moment will remain in it."
    show abd alert at left
    $ msg.msg("Right, Received sands of time, a dozen handfuls.")
    jaf "That 'you' can be recovered if something...{w=.5} unfortunate happens to you."
    jaf "Well, {w=.2}You need to bring in your own jars."
    jaf "The things I conjure in here will disappear a while after I take my mind of them.."
    # Remove jars
    abd "You can resurrect me?"
    show jaf thinking at right
    jaf "Not exactly."
    show abd concerned at left
    show jaf normal at right
    jaf "You would have to wish for resurrection, and it wouldn't be a pretty sight. Plus, it's difficult to wish When you're dead."
    jaf "This is my way to manage around that problem."
    jaf "Just don't overdo it, you don't have much sand and it's not easy to obtain more of it."
    # add a jar
    jaf "In fact... {w=.4}Let's preserve you in this moment."
    show abd alert at left
    abd "Are you sure it's... {w=.2}{nw}"
    show jaf magic at right
    $ save_list.add()
    "...{nw}"
    $ renpy.take_screenshot()
    $ renpy.save("1-1", extra_info='')
    abd "... safe?"
    show jaf normal at right
    jaf "I'm sure we'll find out soon."
    abd "Does that mean I'm going to die soon?"
    jaf "Let's move on."
    $ renpy.hide_screen("save", layer = "bg")

label lamp_visit_settings:
    # set
    show bg sett behind jaf
    show abd normal at left
    abd "What's this one?"
    show jaf thinking at right
    jaf "To be honest, I'm not entirely sure. These devices seem to have some minor effects on the outside world."
    show jaf normal at right
    jaf "I don't have any use for them."
    jaf "You'll have to try them by yourself, I'm afraid."

default books_for_jafar = quest(
    _("Books for jafar"),
    [_("Jafar wants books, lots of them.")],
    )

label lamp_visit_library:
    # lib
    show bg lib
    # this part can use a revamp
    abd "You have a library here?"
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
    abd "Are {b}all{/b} of these books are written by you, Jafar?"
    show abd concerned at left
    jaf "Of course, I can't collect any other books, being stuck in this lamp."
    jaf "And I need to transfer my knowledge to the next generation somehow."
    show jaf thinking at right
    jaf "Speaking of, You should collect and bring me as many books as you can."
    abd "Books are expensive Jafar."
    jaf "They're worth it. Buy when you can afford them."
    abd "But..."
    jaf "Do as I say."
    abd "Alright."
    $ qlog.got(books_for_jafar)

    show abd alert at left
    jaf "You should borrow a few of them at some point."
    show jaf normal at right
    jaf "In fact...{w=.2} You'll need to read them all, these will help you with your quest."
    show abd smug at left
    abd "Even...{w=.4}tap{w=.4}dan...{w=.2}{nw}?"
    show jaf annoyed at right
    "...{nw}"
    show jaf magic at right
    show abd afraid at left
    abd "Whah..."
    jaf "There... It never existed."
    show jaf annoyed at right
    jaf "Happy now?"
    abd "Sorry, sorry, it was just a joke."
    abd "Did you have to burn it right in my hand?"
    jaf "Now you know better to not annoy a powerful Genie."
    show jaf normal at right
    jaf "Now where were we? Ah yes, speaking of quests."
    show abd normal at left
    jaf "I'll keep track of your progress...{nw}"

default my_to_do_list = quest(
    _("A to-do list"),
    [_("Jafar wants to write you a to-do list and he needs a blank skin scroll.")],
    )

label lamp_visit_quests:
    # quest
    show bg quest
    jaf "Here."
    abd "A mirror?"
    jaf "Through this mirror, I can watch you outside of the lamp. I can also guide you and give you information."
    show abd concerned at left
    abd "All the time?"
    show jaf thinking at right
    jaf "You're right, I have much better things to do than sitting here controlling your every move."
    "..."
    show jaf normal at right
    jaf "Get me a skin scroll, I'll make a to do list for you.{w=.4} Make it your first priority."
    $ qlog.got(my_to_do_list)
    abd "Um...{w=.2} my concern was something else."
    show jaf probing at right
    jaf "What's the matter?"
    abd "What about my privacy?"
    show jaf normal at right
    jaf "Get over yourself, I don't have time to watch you all the time. I have books to write."
    jaf "And I don't have any interest in watching you jerk off."
    jaf "I have a harem for myself anyway."
    show abd excited at left
    abd "A harem? Let me see it!"

label lamp_visit_harem:
    # fight
    show bg fight
    abd "Not this."
    # gallery
    show bg gall
    abd "Nor this."
    # harem
    show bg harem
    abd "Woah, you have slave girls in here? You also have three of them too?"
    jaf "No, they aren't slaves, they're free people."
    show abd confused at left
    abd "Wives?"
    jaf "No, they're just... here. For some reason."
    jaf "And they seem to be happy just keeping me company."
    show abd embarrassed at left
    abd "Ummm..."
    abd "Can I? Ummm... I mean... May I?"
    show jaf probing at right
    jaf "Fuck them?"
    show abd alert at left
    abd "No no, speak to them."
    show jaf normal at right
    jaf "I'm not the one you should ask."
    show abd normal at left
    jaf "Who am I to say what they can and can't do?"
    jaf "You might want to take advantage of the running water and at least take a shower first."
    jaf "We're trying to keep it clean in here."
    show abd alert at left
    abd "A shower...? Hey, are those?"
    show jaf disappointed at right
    jaf "Yes, those statues look a lot like me peeing.{w=.5} It seemed like a good idea at that time."
    jaf "The girls seem to like them, and I wasn't expecting any guests in here anytime soon either."
    show jaf normal at right
    
    menu:
        jaf "Now, let's go back and visit the places we skipped."
        "Sure, I can come back later.":
            show abd normal at left
            abd "Sure, I can come back later."
            jump lamp_visit_fight

        "I think I'm going to take that shower you just suggested to me.":
            show abd embarrassed at left
            abd "I think I'm going to take that shower you just suggested to me."
            show jaf disappointed at right
            jaf "Of course, there are women around, so you aren't capable of thinking straight."
            jaf "Come to me when you've relieved yourself."
            show jaf normal at right
            jaf "I'll think of a plan in the mean time."
            jaf "And we're going to have to work on your self-discipline."
            hide jaf with dissolve
            jump harem

label lamp_visit_fight:
    # fight
    scene black
    show bg fight
    show jaf normal at right
    show abd normal at left
    jaf "This is my throne. You'll be fighting the creatures I conjure in here."
    jaf "To increase your fighting skill, and maybe for my amusement."
    jaf "You can come here and start fighting any time."
    
    menu:
        jaf "But... do you want to give it a try right now?"
        "Yes.":
            show abd alert at left
            abd "Yes."
            jaf "Alright, here we go."

            hide abd
            hide jaf
            window hide
            call screen btl_scr(team([abdul]), team([training_dummy]))

            show abd normal at left
            with dissolve
            show jaf normal at right
            with dissolve
            jaf "Not bad."
            jaf "At least you didn't die."
            jaf "Or, if you did, the sands of time have worked."
            jaf "It would be hard to decern."
            jaf "Anyways..."
            jaf "I'll have to prepare something."
            jaf "Explore the lamp as you wish, meet me at my library when you're done."
            hide jaf with dissolve
            jump ch3_1
        "Maybe later.":
            show abd normal at left
            show jaf normal at right
            abd "Maybe later."
            jaf "Alright. Next is the Hall of Memories."
            # hall of memories
            jaf "You can revisit your most proudest moments in here."
            jaf "And that's it. I have some thinking to do. Feel free to roam around while I'm busy."
            jaf "Meet me at my library when you're done."
            hide jaf with dissolve
            jump ch3_1

label ch3_1:
    scene black
    show screen lamp_visit_menu
    pause
    jump ch3_1

screen lamp_visit_menu:
    style_prefix "nav"
    modal True
    button:
        at lampoff(-350, 150)
        add "bg/lamp/fight.png"
        action Hide("lamp_visit_menu"), Jump("ch3_fight")
    button:
        at lampoff(350, 150)
        add "bg/lamp/harem.png"
        action Hide("lamp_visit_menu"), Jump("harem")
    button:
        at lampoff(0, 260)
        add "bg/lamp/library.png"
        action Hide("lamp_visit_menu"), Jump("lamp_visit_back_to_jafar")
    button:
        at lampoff(350, -150)
        add "bg/lamp/quest.png"
        action Hide("lamp_visit_menu"), Jump("ch3_mirror")
    button:
        at lampoff(-350, -150)
        add "bg/lamp/replay.png"
        action Hide("lamp_visit_menu"), Jump("ch3_replay")
    button:
        at lampoff(0, -260)
        add "bg/lamp/save.png"
        action Hide("lamp_visit_menu"), Jump("ch3_sav")
    button:
        at lampoff(-600, 0)
        add "bg/lamp/settings.png"
        action Hide("lamp_visit_menu"), Jump("ch3_set")
    button:
        at lampoff(600, 0)
        add "bg/lamp/mm.png"
        action Hide("lamp_visit_menu"), Jump("ch3_mm")

label ch3_mm:
    # scene bg sav
    "Nothing to do here."
    jump ch3_1
label ch3_sav:
    # scene bg sav
    "Nothing to do here."
    jump ch3_1
label ch3_set:
    scene bg sett
    "Nothing to do here."
    jump ch3_1
label ch3_replay:
    scene bg sett
    "Nothing to do here."
    jump ch3_1
label ch3_mirror:
    show screen quests
    pause
    jump ch3_1


label ch3_fight(j=False):
    window hide
    call screen btl_scr(team([abdul]), team([unit("Training dummy", "char/training_dummy", lvl = 1, type = "Dummy")]))

    if j:
        return
    else:
        jump ch3_1
