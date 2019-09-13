label ch0:
    # default skip_next = "skip_to_ch1"
    # call desert_0
    show bg bg1
    # show screen skips
    show me tired at left with dissolve
    me "Phew..."
    me "Not even a tumbleweed!"
    me "I need to find another area to collect thorns."
    me "There's nothing but sand left around here."
    show ev 01
    show me back at left with dissolve
    me "{size=45}Huh!?"
    me "That isn't... a mirage."
    me "..."
    me "There's something shiny in the sand."
    hide me
    hide ev 01
    show bg cg1
    # $ abdul.got(black_lamp,1,002)
    with dissolve
    me "An oil lamp?"
    me "Looks new."
    me "Hah, my lucky day! I can sell this and eat a full meal tonight."
    # $ qlog.got(sell_lamp)
    show bg bg1
    show me confused at left
    with dissolve
    me "They say Aladdin found his Genie in one of these, and he wished for all the things he desired."
    me "Hmph, I wish these rumours were believable."
    menu:
        "rub the lamp!":
            hide me
            show bg cg2 with Dissolve(2)
            me "{size=45}What the fuck?"
            show bg bg1
            show me alert at left
            with dissolve
            show jaf genie at right
            with dissolve
            jaf "{size=45}Aren't you glad to be naive?"
            show me afraid at left
            # $ msg.msg("You dropped CamelThorns and the lamp")
            me "{size=45}Woah! {w=.6}whoa. {w=.4}wha {w=.2}wh..."
            jaf "{size=45}Where are you running to?"
            me "{size=40}Please don't steal my soul."
            jaf "{size=40}Calm down, I'm not interested in your soul."
            me "{size=30}Are you? {w=.5}a... {w=.5}a Genie?"
            jaf "Is it that obvious? {w=.5}let me..."
            show jaf normal at right with dissolve
            jaf "Ah that's better."
            show me confused at left
            me "Wait! {w=.8}Jafar?"
            jaf "In the flesh, {w=.5}or smoke. {w=.8}Fire to be precise."
            jaf "Yes,{w=.3} yes, {w=.3}Genies are make of fire."
            jaf "Pick up my lamp would you?"
            show me alert at left
            me "{size=25}Sorry."
            show me bent at left
            # $ msg.msg("You got the Black lamp.")
            show jaf thinking at right
            jaf "Abdul? {w=.8}Is that you?"
            show me confused at left
            jaf "Where's your belly you fat fuck? {w=.5}I didn't recognize you without it."
            jaf "What are you doing in the middle of desert this time of day?"
            jaf "Shouldn't you be selling fish in the bazaar?"
            show jaf normal at right
            show me sad at left
            me "Well... {w=.6}I can't do that anymore."
            me "Aladdin destroyed my fish stand in one of his fights."
            me "They blamed it on you returning to Agrabah. {w=.6}but..."
            me "Every other day he would drag some problem into the bazaar and mess the place up."
            me "Breaking my fish barrels every single time... {w=.5}Those cost lots of money."
            me "I can't take my fish to the bazaar without barrels."
            me "No fish to sell, {w=.4}no money to buy barrels, {w=.4}no money to buy fish food, {w=.4}no money to buy bread."
            show jaf thinking at right
            jaf "Well... That explains the missing belly."
            me "And my fish pond dried up, Jafar. {w=.5}All of my fish died. {w=.8}I'm a thorn collector now."
            show jaf normal at right
            jaf "Agrabah is an oasis, my friend. {w=.5}A drop of water in the middle of the scorching sand."
            show me normal at left
            jaf "I warned the Sultan about wasting too much of drinkable water for fountains and his garden."
            jaf "He'd never listen."
            jaf "Or never cared."
            jaf "Either way he's to blame. {w=.4}That motherfucking old piece of shit."
            me "..."
            show jaf thinking at right
            jaf "Hey, {w=.4}hows your mother?"
            show me sad at left
            me "She died."
            jaf "Damn, {w=.8}how long I was gone for? {w=.5}That old hag still had a solid ten years or so."
            me "Roughly a year."
            jaf "Is that so?"
            me "Yes, {w=.8}My mother died few months ago, after I lost my business."
            if not persistent.theme_change:
                show jaf looking at right
                me "She tried to help me by working..."
                jaf "Hmmm..."
                me "Jafar?"
                show jaf normal at right
                jaf "Ah, {w=.5}sorry Abdul, {w=.5}I got distracted. Anyways."
            else:
                me "She tried to help me by working..."
                jaf "Aha? {w=.8}tell me about it later."
                show me confused at left
            show jaf thinking at right
            jaf "You know what this means don't you?"
            show me confused at left
            me "What?"
            jaf "It means you're the hero of the story now!"
            me "The hero?"
            show jaf normal at right
            jaf "Yes my friend, {w=.5}down on the luck, {w=.5}dead mother and facing an unbelievable opportunity."
            jaf "Those are the telltale of a story being written."
            jaf "This time, the story is yours!"
            jaf "Abdul my friend... {w=.5}Your life is about to change. A new opportunity fell right into your lap!"
            if not persistent.theme_change:
                show jaf looking at right
                jaf "So...?"
                show jaf normal at right
            me "Opportunity?"
            show jaf disappointed at right
            jaf "Haah... {w=.8}Alright, I'll spell it out for you."
            show jaf normal at right
            jaf "I'm a Genie. And you rubbed me out... {w=.4}hehe..."
            jaf "Now you have three wishes I shall grant."
            me "Really?"
            jaf "Yes, {w=.6}aren't you glad you rubbed my lamp before selling it?"
            me "How did you know that was my plan?"
            jaf "You have to stop talking aloud to yourself my friend."
            show me alert at left
            jaf "You haven't gone crazy, have you?"
            me "No!"
            show me confused at left
            jaf "Good, {w=.5}nobody does that. {w=.5}Anywhere you saw somebody talking to himself, {w=.5}it's totally fake."
            show me embarrassed at left
            jaf "As I was saying: {w=.5}You wish for something and I'll try to twist your words against you."
            show me alert at left
            me "Against me? {w=.5}But why?"
            show jaf thinking at right
            jaf "I spouse it's something about teaching you a lesson."
            jaf "The value of Contentment or something stupid like that."
            show jaf normal at right
            jaf "HOWEVER!"
            jaf "I have a deal to propose."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "But first, {w=.5}let me do something about this ugliness."
                show jaf normal at right
                show me confused at left
                me "What ugliness?"
                jaf "Ah, {w=.5}Right! You can't see it."
                jaf "Let me show you."
                show jaf magic at right
                show me alert at left
                me "What the..."
                jaf "With a little touch up."
                $ persistent.theme_change = 1
                show jaf thinking at right
                jaf "It's not finished yet, {w=.5}but better than that ugly wood thingy."
                show jaf normal at right
                jaf "Way better, {w=.5}Don't you think Abdul?"
                show me smug at left
                me "Gold?"
                jaf "Yes. {w=.5}Something wrong with it?"
                me "Haven't you heard what romans say about us?"
                jaf "That we love gold?"
                me "Yes, they're mocking us for it."
                jaf "Don't you like gold?"
                show me alert at left
                me "I do, {w=.5}but..."
                jaf "So they are pointing out the truth, {w=.5}why should that bother me?"
                me "But it's hateful talk."
                jaf "It's just a way for them to perceive us. {w=.5}We humans do that for everything."
                jaf "Even if it's hate, {w=.5}I choose spoken hate over hateful acts any day."
                show me confused at left
                me "You're right, Jafar. {w=.5}So, You mentioned a deal?"
                jaf "Ah, {w=.5}yes!"
            else:
                me "A deal?"
                jaf "Yes"
            jaf "If you promise to help me get my revenge from those three idiots..."
            jaf "The bastards who trapped me in this thing...."
            jaf "I'll let you have me decide what would be your first wish... {w=.5}and second wish..."
            jaf "And finally, I'll tell you how to avoid being screwed for your last wish."
            show me confused at left
            me "What do you mean by 'screwed?'"
            jaf "It means... {w=.5}I'll have to kill you with your own wish."
            show me alert at left
            me "Wait, I've heard that Genies can't kill..."
            jaf "Not directly we can't, {w=.5}but you'll be surprised to know..."
            me "What you can live through?"
            jaf "You've heard that one huh?"
            show me confused at left
            jaf "No! That was the old me..."
            jaf "I was about to say: {w=.5}How easy is it to let people die on their own."
            me "What do you mean?"
            menu:
                jaf "No time to explain. {w=.5}What do you say? {w=.5}Do we have a deal?"
                "Sure..!?":
                    jaf "Excellent! Now let us head back to Agrabah."
                    # $ qlog.got(jafars_revenge)
                    # $ qlog.cancel(sell_lamp)
                    jaf "Bring the thorns. {w=.5}We need any money we can get our hands on."
                    # $ msg.msg("You got CamelThorns")
                    jump ch1
                "No! I want my wishes":
                    show me normal at left
                    jaf "Are you sure? {w=.5}This doesn't end that well for you my friend."
                    menu:
                        jaf "Last chance, Abdul! Don't throw away this opportunity."
                        "I want my wishes Jafar.":
                            jaf "So be it."
                            jump wishes
                        "Alright, alright, I yield, don't screw me up.":
                            jaf "Good, let us haste! {w=.5}Time's a-wastin'."
                            # $ qlog.got(jafars_revenge)
                            # $ qlog.cancel(sell_lamp)
                            show me confused at left
                            me "What?"
                            jaf "Something I've heard- {w=.5}you know what, never mind."
                            jump ch1
        "Don't be naive, {w=.5}let's go back to the city.":
            jump endless_grind
