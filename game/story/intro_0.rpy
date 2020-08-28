image cg found_lamp = Movie(play="cg/found lamp/01.webm", size = (1920, 1080))



label intro_0:
    # default skip_next = "skip_to_ch1"
    show bg bg2  onlayer bg with Dissolve(2)
    jump desert_0
    # show screen skips
label intro_0_1:
    show abd tired at left with dissolve
    abd "Phew..."
    abd "There's nothing left here but sand."
    abd "Not even a single tumbleweed!"
    abd "I need to find another place to collect some firewood."
    show des_0_shine:
        align (.834,.73)
        anchor (.5,.5)
    show abd back at left with dissolve
    abd "{size=45}Huh!?"
    abd "That isn't...{w=.4} a mirage."
    abd "..."
    abd "There's something shiny in the sand."
    show abd confused at left with dissolve
    hide des_0_shine
    $ abdul.got(black_lamp,1,002)
    with dissolve
    abd "An oil lamp?"
    show abd smile at left with dissolve
    abd "Looks new."
    abd "Hah, this is my lucky day! I can sell this and finally eat a full meal tonight."
    $ qlog.got(sell_lamp)
    show abd alert at left
    with dissolve
    abd "Hmmm... They say Aladdin found his Genie in a lamp like this and the Genie made all his wishes come true."
    abd "I {b}wish{/b} these rumours were believable."
    $ _last_say_who = None
    menu:
        "Rub the lamp!":
            # hide abd
            show cg found_lamp with Dissolve(2)
            pause 6
            hide cg with Dissolve(2)
            
            show jaf genie at rightend with dissolve
            show abd scared at left
            jaf "{size=45}Muhahahaaaaaaaaaaaaaaaa{w=.5}{nw}"
            abd "{size=45}What the fuck?{w=1}{nw}"
            show jaf genie bent at rightend with dissolve
            jaf "{size=45}Don't you think there's benefit to naivete?{w=1}{nw}"
            $ msg.msg("You dropped the Black Lamp")
            abd "{size=45}Woah! {w=.6}whoa. {w=.4}wha {w=.2}wh...{nw}"
            hide abd with moveoutleft
            jaf "{size=45}Where are you running to?"
            jaf "{size=45}COME BACK HERE!{nw}" with hpunch
            show abd alert at left with moveinleft
            abd "{size=40}Please don't steal my soul!"
            jaf "{size=40}Calm down, I'm not interested in your soul."
            abd "{size=30}Are you a... {w=.5}a Genie?"
            jaf "Isn't it obvious?"
            jaf "Here, let me..."
            show jaf normal at right with dissolve
            jaf "Ah, much better."
            show abd afraid at left
            abd "Wait! {w=.3}Jafar?"
            jaf "In the flesh, {w=.5}or smoke. {w=.8}Fire to be precise."
            jaf "Yes,{w=.3} yes, {w=.3}Genies are made of fire."
            jaf "Pick up my lamp would you?"
            show abd alert at left
            abd "{size=25}Sorry."
            show abd bent at left
            $ msg.msg("You got the Black lamp.")
            show jaf thinking at right
            jaf "Abdul? {w=.8}Is that you?"
            show abd confused at left
            jaf "Where's your belly you fat fuck? {w=.5}I didn't even recognize you without it."
            jaf "What are you doing in the middle of desert at this time of day?"
            jaf "Shouldn't you be selling fish in the bazaar?"
            show jaf normal at right
            show abd sad at left
            abd "Well... {w=.6}I can't do that anymore."
            abd "Aladdin destroyed my fish stand in one of his fights."
            abd "Every other day, he would drag a fight into the bazaar and mess the place up."
            abd "Breaking my fish barrels every single time... {w=.5}Those cost lots of money."
            abd "They blamed it on you returning to Agrabah."
            jaf "Did they compensated you for the damages?"
            abd "No."
            abd "After your sudden death, nobody tends to peoples requests."
            jaf "I'm still alive, Abdul."
            show abd alert at left
            abd "I meant after you left."
            abd "I can't take my fish to the bazaar without any barrels."
            abd "No fish to sell means no money to buy barrels, {w=.4} which means no money to feed the fish, {w=.4}and now no money to buy bread."
            show jaf thinking at right
            jaf "That explains the missing belly."
            abd "And my fish pond is all dried up, Jafar. {w=.5}All of my fish died. {w=.8}I'm a wood collector now."
            show jaf normal at right
            jaf "Agrabah is an oasis, my friend. {w=.5}A drop of water in the middle of the scorching sand."
            show abd normal at left
            jaf "I warned the Sultan about wasting too much of our limited drinkable water for fountains and his garden."
            jaf "He never listened."
            jaf "Or maybe he never cared."
            jaf "Either way he's to blame. {w=.4}That motherfucking old piece of shit."
            abd "..."
            show jaf thinking at right
            jaf "Hey, {w=.4}hows your mother?"
            show abd sad at left
            abd "She died."
            jaf "Damn, {w=.8}how long was I gone for? {w=.5}That old hag still had a solid ten years or so."
            abd "Roughly a year."
            jaf "Is that so?"
            abd "Yes, my mother died few months ago, after I lost my business."
            if not persistent.theme_change:
                show jaf looking at right
                abd "She tried to help me by working..."
                jaf "Hmmm..."
                abd "Jafar?"
                show jaf normal at right
                jaf "Ah, {w=.5}sorry Abdul, {w=.5}I got distracted. Anyways."
            else:
                abd "She tried to help me by working..."
                jaf "Aha? {w=.8}Tell me about it later."
                show abd confused at left
            show jaf thinking at right
            jaf "But hey, you know what this means don't you?"
            show abd confused at left
            abd "What?"
            jaf "It means you're the hero of the story now!"
            abd "The hero?"
            show jaf normal at right
            jaf "Yes my friend, {w=.5}down on the luck, {w=.5}dead mother and facing an unbelievable opportunity."
            jaf "Those are the telltale signs of a story being written."
            jaf "This time, yours!"
            jaf "Abdul my friend... {w=.5}Your life is about to change. A new opportunity fell right into your lap!"
            if not persistent.theme_change:
                show jaf looking at right
                jaf "So..."
                show jaf normal at right
            abd "Opportunity?"
            show jaf disappointed at right
            jaf "Okay, okay. I'll spell it out for you."
            show jaf normal at right
            jaf "I'm a Genie. And you rubbed me out... {w=.4}hehe..."
            jaf "And now I shall grant you three wishes."
            abd "Really?"
            jaf "Yep! Those are the rules!"
            jaf "Aren't you glad you rubbed my lamp before selling it?"
            abd "How did you know that was my plan?"
            jaf "You have to stop talking to yourself out loud my friend."
            show abd alert at left
            jaf "You haven't gone crazy, have you?"
            abd "No!"
            show abd confused at left
            jaf "Good, {w=.5}nobody does that. {w=.5}Whenever you see someone talking to themselves, {w=.5}they're faking a friend, {w=.5}or they're just crazy."
            show abd embarrassed at left
            jaf "Now, as I was saying."
            jaf "Here's how it works. You wish for something and I'll try to twist your words against you."
            show abd alert at left
            abd "Against me? {w=.5}But why?"
            show jaf thinking at right
            jaf "Genies are known to use poorly phrased wishes in... interesting ways."
            jaf "I suppose it's something about teaching you a lesson."
            jaf "The value of Contentment or something stupid like that."
            show jaf normal at right
            jaf "HOWEVER!"
            jaf "I have a deal to propose."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "But first, {w=.5}let me do something about this ugliness."
                show jaf normal at right
                show abd confused at left
                abd "What ugliness?"
                jaf "Ah, {w=.5}Right! You can't see it."
                jaf "Let me show you."
                show jaf magic at right
                show abd alert at left
                abd "What the..."
                jaf "Let me just touch this up a little..."
                $ persistent.theme_change = 1
                show jaf thinking at right
                jaf "OK, still a work in progress... {w=.5}but better than that ugly wood."
                show jaf normal at right
                jaf "Much better, {w=.5}Don't you think, Abdul?"
                show abd smug at left
                abd "Is that gold?"
                jaf "Yes. {w=.5}Something wrong with it?"
                abd "Haven't you heard what Romans say about us?"
                jaf "That we love gold?"
                abd "Yes, they're mocking us for it."
                jaf "Don't you like gold?"
                show abd alert at left
                abd "I do, {w=.5}but..."
                jaf "So they are pointing out the truth, {w=.5}why should that bother me?"
                abd "But it's hateful talk."
                jaf "It's just a way for them to perceive us. {w=.5}We humans do that for everything."
                jaf "Even if it's hate, {w=.5}I choose spoken hate over hateful acts any day."
                show abd confused at left
                abd "You're right, Jafar. {w=.5}So, you mentioned a deal?"
                jaf "Ah, {w=.5}yes!"
            else:
                abd "A deal?"
                jaf "Yes."
            jaf "If you promise to help me get my revenge from those three idiots..."
            jaf "The bastards who trapped me in this thing...."
            jaf "I'll let you give me your first wish... {w=.5}and second wish..."
            jaf "Then I'll tell you how to avoid being screwed for your last wish."
            show abd confused at left
            abd "What do you mean by 'screwed?'"
            jaf "Well, under normal circumstances... {w=.5}I'd kill you with your own wish."
            show abd alert at left
            abd "Wait, I've heard that Genies can't kill..."
            jaf "Not directly we can't, {w=.5}but you'll be surprised to know..."
            abd "What you can live through?"
            jaf "You've just heard that one huh?"
            show abd confused at left
            jaf "No! That was the old me..."
            jaf "I was about to say: {w=.5}How easy is it to let people die on their own?"
            abd "What do you mean?"
            menu:
                jaf "No time to explain. {w=.5}What do you say? {w=.5}Do we have a deal?"
                "Sure..!?":
                    abd "Sure..!?"
                    jaf "Excellent! Now let us head back to Agrabah."
                    $ qlog.got(jafars_revenge)
                    $ qlog.cancel(sell_lamp)
                    jaf "Bring the thorns. {w=.5}We need all the money we can get."
                    $ msg.msg("You got CamelThorns")
                    jump ch1
                "No! I want my wishes":
                    show abd normal at left
                    abd "No! I just want my wishes Jafar!"
                    jaf "Are you sure? {w=.5}This will not end well for you my friend."
                    menu:
                        jaf "Last chance, Abdul! Don't throw away this opportunity."
                        "I really want my wishes Jafar.":
                            abd "I really want my wishes Jafar."
                            jaf "So be it."
                            jump wishes
                        "Okay, okay. I yield.":
                            abd "Okay, okay. I yield. Don't screw me up."
                            jaf "Good, let's make haste! {w=.5}Time's a-wastin'."
                            $ qlog.got(jafars_revenge)
                            $ qlog.cancel(sell_lamp)
                            show abd confused at left
                            abd "What?"
                            jaf "Something I heard- {w=.5}you know what, never mind."
                            jump ch1
        "Don't be naive, search for more firewood.":
            show abd alert at left
            abd "Back to work then."
            $ msg.msg("You hang the lap on your bundle.")
            show abd tired at left
            abd "It's unusually hot today."
            abd "..."
            call desert_1 from _call_desert_1
            

            jump endless_grind
        "<dev> jump to the city":
            jump agrabah