label harem:
    scene bg harem
    show abd normal at left
    menu:
        "Go talk to the girls.":
            menu:
                "Go to the sweet one.":
                    abd "Hello."
                    show hur normal at right with dissolve
                    $ renpy.pause(.1)
                    show hur shocked at right
                    hur "Eeeep? You can talk?"
                    abd "Don't panic please, I'm a friend of Jafar."
                    hur "You're not one of Jafar's conjured creatures?"
                    show hal scream at midright
                    hal "Back off! Back off from her!"
                    show hur worry at right
                    hur "Halia wait! He's not a creature."
                    show hal confused at midright
                    hal "He's not?"
                    abd "It's true. I'm a real human."
                    hal "A real human? how did you get inside the lamp?"
                    abd "I've found the lamp. And Jafar brought me in here."
                    menu:
                        "I've made a deal with Jafar to help him.":
                            abd "I've made a deal with Jafar to help him."
                            hal "..."
                            hal "Then go back to Jafar. I'll have to think."
                            abd "errm..{nw}"
                            hal "What are you waiting for?"
                            abd "Sure, see you later then."
                            jump lamp_visit_back_to_jafar

                        "I'm the lamp's owner and your master now.":
                            show abd smug at left
                            abd "I'm the lamp's owner and your master now."
                            show hal normal at midright
                            hal "No you're not!"
                            abd "I'm pretty sur...{nw}"
                            show hal scream at midright
                            hal "No! You're wrong! Now get lost before I cut you!"
                            menu:
                                "Alright alright, I'm going.":
                                    show abd scared at left
                                    abd "Alright alright, I'm going."
                                    jump lamp_visit_back_to_jafar
                                "No way.":
                                    abd "No way! you need to respect me."
                                    hal "Respect huh?"
                                    hide hur
                                    hal "Alright, here's my respect."
                                    hal "For the dead!"
                                    hide abd
                                    hide hal
                                    window hide
                                    call screen btl_scr(team([abdul]), team([halia]))
                                    pause

                                    jump lamp_visit_back_to_jafar
                "Go to the angry one.":
                    show hal normal at midright
                    abd "hi."
                    hide abd
                    show black # Halia knocks abdul out
                    $ renpy.pause(3)
                    show hur normal at right behind black
                    hide black with dissolve
                    abd "What happened?"
                    hal "See he's alive."
                    hal "Next time don't jump me like that."
                    abd "I didn't..."
                    hal "Now get up!"
                    show abd bent at left
                    $ renpy.pause(.1)
                    show abd normal at left
                    hal "Can you walk?"
                    abd "Yes."
                    hal "Great, get lost then!"
                    abd "But..."
                    hal "Now!"
                    abd "Alright... I'm going..."
                    jump lamp_visit_back_to_jafar
                "Go to the conceded one.":
                    show hul normal at right
                    abd "hi."
                    hul "No you didn't..."
                    abd "I didn't what?"
                    hul "Tell me you didn't come to me expecting something all dirty like that."
                    abd "No no! I just wanted to say hi to such a beaut...{nw}"
                    hul "Hold it right there! I knew it. You did come here to get under my skirt."
                    abd "No I didn't."
                    hul "do you want to?"
                    abd "I mean...{nw}"
                    hul "I knew it!"
                    abd "..."
                    hul "Not like this though, Go sit in that tub and start washing yourself."
                    hul "I'll join you soon."
                    jump harem_bath
                "Hey ladies...!":
                    abd "Hey ladies."
                    hal "Step back! don't come any closer!"
                    abd "I...{nw}"
                    hal "Turn around and walk out of here while you can."
                    abd "But I'm...{nw}"
                    hal "Now!"
                    abd "Alright... Alright..."
                    abd "Well that was counter productive."
                    hal "Stop mumbling and walk faster!"
                    jump lamp_visit_back_to_jafar
        "Jump right into the water.":
            # show bg cg_abdul_bathing
            show hul normal at right with dissolve
            hul "We have a tub you know!"
            abd "Oh, Hi! I didn't want to disturb you ladies."
            hul "That's alright, the water will clear up soon."
            hul "You should have removed your cloths first."
            abd "But...{nw}"
            hul "Come on! Don't be shy."
            hul "Get naked and get in that tub over there."
            hul "I'll join you shortly."
            jump harem_bath



label harem_bath:
    scene black
    show cg harem bath 01 with dissolve
    hul "{size=10} ... once ... me ... Huria can...."
    hal "{size=10} ... crazy? ... filthy son ... no way ... day...."
    hul "{size=10} ... is it ... time ... us ... time ..."
    hal "{size=10} ... if I ... but ... once ..."
    hal "{size=10} ... alright but ..."
    hal "{size=10} ... yay ... love ..."
    $ renpy.pause(1)
    show cg harem bath 02 with dissolve
    $ renpy.pause(1)
    show cg harem bath 03 with dissolve
    $ renpy.pause(1)
    show cg harem bath 04 with dissolve
    $ renpy.pause(1)
    show cg harem bath 05 with dissolve
    $ renpy.pause(1)
    hide cg with dissolve
    scene bg harem with dissolve
    show abd normal at left with dissolve
    show hur normal at right with dissolve
    show hul normal at midright with dissolve
    show hal normal at center with dissolve
    hal "Alright, you had your fun, now beat it!"
    hal "Hulu has lots of cleaning to do."
    hul "You're cruel Halia."
    hal "Your idea, your mess, your job to clean!"
    hul "Alright, what's your name stud?"
    abd "Abdul."
    hul "Don't be a stranger, pay us a visit soon."
    hul "Come again, and again, and again..."
    hal "Stop it..."
    abd "Um... sure?"
    hal "What are you standing here for?"
    abd "Oh right, see you later then."
    jump lamp_visit_back_to_jafar