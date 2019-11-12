label ch0:
    # default skip_next = "skip_to_ch1"
    call desert_0
    show bg bg1
    # show screen skips
    show abd tired at left with dissolve
    abd "Phew..."
    abd "There's nothing here but sand."
    abd "Not even a single tumbleweed!"
    abd "I need to find another area to collect firewood."
    show ev 01
    show abd back at left with dissolve
    abd "{size=45}Huh!?"
    abd "That isn't a mirage."
    abd "..."
    abd "There's something shining in the sand over there!"
    hide abd
    hide ev 01
    show cg cg1
    $ abdul.got(black_lamp,1,002)
    with dissolve
    abd "An oil lamp?"
    abd "It's in good shape for being buried out here..."
    abd "Hah, this is my lucky day! I can sell this and eat a full meal tonight."
    $ qlog.got(sell_lamp)
    hide cg
    show abd confused at left
    with dissolve
    abd "Hmmm. They say Aladdin found his Genie in a lamp like this and the Genie made all his wishes come true."
    abd "What a bunch of crap."
    abd "I {b}wish{/b} these rumours were believable."
    abd "Still, it might be worth a shot to rub it... even if it would be a a naive thing to do."
    menu:
        "Who cares if it's naive? Rub the lamp!":
            hide abd
            show cg cg2 with Dissolve(2)
            abd "{size=45}What the fuck?"
            hide cg
            show abd alert at left
            with dissolve
            show jaf genie at right
            with dissolve
            jaf "{size=45}Sometimes it's good to be a little naive, don't you think?"
            show abd scared at left
            $ msg.msg("You dropped the Black Lamp")
            abd "{size=45}Woah! {w=.6}Whoa. {w=.4}wha... {w=.2}wh..."
            jaf "{size=45}Where are you running to?"
            abd "{size=40}Please don't steal my soul."
            jaf "{size=40}Calm down, I'm not interested in your soul."
            abd "{size=30}Are you a... {w=.5}a Genie?"
            jaf "Isn't it obvious?"
            jaf "Here, let me..."
            show jaf normal at right with dissolve
            jaf "Ah that's better."
            show abd afraid at left
            abd "Wait! {w=.8}Jafar?"
            jaf "In the flesh, {w=.5}or smoke. {w=.8}Fire to be precise."
            jaf "Yes,{w=.3} yes, {w=.3}Genies are made of fire."
            jaf "Pick up my lamp would you?"
            show abd alert at left
            abd "{size=25}Sorry."
            show abd bent at left
            $ msg.msg("You got the Black Lamp.")
            show jaf thinking at right
            jaf "Abdul? {w=.3}Abdul the fishmonger? {w=.8}Is that you?"
            jaf "I used to buy fish from you..."
            show abd confused at left
            jaf "Where's your belly? {w=.5}It's hard to recognize you without it."
            jaf "What are you doing in the middle of desert this time of day?"
            jaf "Shouldn't you be selling fish in the bazaar?"
            show jaf normal at right
            show abd sad at left
            abd "I don't do that any more."
            abd "Aladdin destroyed my fish stand in one of his fights."
            abd "Every other day he would drag some problem into the bazaar and mess the place up."
            abd "Breaking my fish barrels every single time... {w=.5}Those cost lots of money."
            abd "I went to the palace to ask for compensation, but they said Aladdin had to do it for national security reasons and was \"indemnified.\""
            abd "They blamed it on you returning to Agrabah."
            abd "I can't take my fish to the bazaar without barrels."
            abd "No fish to sell means no money to buy barrels, {w=.4} which means no money to buy fish food, {w=.4}and now no money to buy bread."
            show jaf thinking at right
            jaf "That explains the missing belly."
            abd "And my fish pond dried up, Jafar. {w=.5}All of my fish died. {w=.8}I'm a wood collector now."
            show jaf normal at right
            jaf "Agrabah is an oasis, my friend. {w=.5}A drop of water in the middle of the scorching sand."
            show abd normal at left
            jaf "I warned the Sultan about wasting too much of our limited drinkable water for fountains and his garden."
            jaf "He never listened."
            jaf "Or maybe he just never cared."
            jaf "Either way he's to blame. {w=.4}That old cracker-eating piece of shit."
            abd "..."
            show jaf thinking at right
            jaf "Hey, {w=.4}hows your mother?"
            show abd sad at left
            abd "She died."
            jaf "Damn, how long have I been away? {w=.5}I thought she still had a solid ten years or so."
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
                jaf "Oh? {w=.8}You'll have to tell me about it later."
                show abd confused at left
            show jaf thinking at right
            jaf "But hey, you know what this means don't you?"
            show abd confused at left
            abd "What?"
            jaf "It means you're the hero of the story now!"
            abd "What story? And why am I the hero?"
            show jaf normal at right
            jaf "Look at the facts, my friend. {w=.5}You're down on your luck. {w=.5}Your mother recently died. {w=.5}But you've just received a new opportunity!"
            jaf "Those are the telltale signs of a story being written."
            jaf "This time, you're the main character!"
            jaf "Abdul, my friend... {w=.5}Your life is about to change."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "So...?"
                show jaf normal at right
            abd "Opportunity?"
            show jaf disappointed at right
            jaf "Okay, okay. I'll spell it out for you."
            show jaf normal at right
            jaf "I'm a Genie. And you rubbed my lamp... {w=.4}hehe..."
            jaf "And now I shall grant you three wishes."
            abd "Really?"
            jaf "Yep! Those are the Rules!"
            jaf "Aren't you glad you rubbed my lamp before selling it?"
            abd "How did you know that was my plan?"
            jaf "You have to stop talking to yourself out loud my friend."
            show abd alert at left
            jaf "You haven't gone crazy, have you?"
            abd "No!"
            show abd confused at left
            jaf "Good, {w=.5}nobody does that. {w=.5}Whenever you see someone talking to themselves, {w=.5}they're faking, {w=.5}or crazy."
            show abd embarrassed at left
            jaf "Now, as I was saying."
            jaf "Here's how it works. You wish for something and I'll try to twist your words against you."
            show abd alert at left
            abd "Against me? {w=.5}But why?"
            show jaf thinking at right
            jaf "It's in the Rules."
            show abd confused at left
            abd "Rules? What rules?"
            show jaf normal at right
            jaf "The Genie Rules. Turns out there are quite a few of them. Bureaucratic bastard universe mongers..."
            show abd alert at left
            jaf "Ahem. Excuse me."
            jaf "The point is, I have to try to twist your words. I suppose it's something about teaching you a lesson."
            jaf "The {b}value of contentment{/b} or something stupid like that."
            show jaf normal at right
            jaf "HOWEVER!"
            jaf "I have a deal to propose."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "But first, {w=.5}let me do something about this ugliness."
                show jaf normal at right
                show abd confused at left
                abd "What ugliness?"
                jaf "Oh yeah. You can't see it."
                jaf "Let me show you."
                show jaf magic at right
                show abd alert at left
                abd "What the..."
                jaf "Let me just touch this up a little..."
                $ persistent.theme_change = 1
                show jaf thinking at right
                jaf "OK, still a work in progress... {w=.5}but better than that ugly wood."
                show jaf normal at right
                jaf "Way better, {w=.5}Don't you think Abdul?"
                show abd smug at left
                abd "Gold?"
                jaf "Yes. {w=.5}Something wrong with it?"
                abd "Haven't you heard what Romans say about us?"
                jaf "That we love gold?"
                abd "Yes, they're mocking us for it."
                jaf "Don't you like gold?"
                show abd alert at left
                abd "I do, {w=.5}but..."
                jaf "So they are pointing out the truth, {w=.5}why should that bother me?"
                abd "But it's hateful talk."
                jaf "It's just a way for them to perceive us. {w=.5}Humans do that for everything."
                jaf "Even if it's hate, {w=.5}I choose spoken hate over hateful acts any day."
                show abd confused at left
                abd "You're right, Jafar. {w=.5}So, You mentioned a deal?"
                jaf "Ah, yes!"
            else:
                abd "A deal?"
                jaf "Yes."
            jaf "Rules, even Genie Rules, can always be... {w=.5}managed."
            jaf "If you promise to help me get my revenge on the three idiots who trapped me in this lamp..."
            jaf "I'll help you make your wishes."
            jaf "And most importantly, I'll tell you how to avoid being screwed with your last wish."
            show abd confused at left
            abd "What do you mean by 'screwed?'"
            jaf "Well, under normal circumstances... {w=.5}I'd have to kill you with your own wish."
            show abd alert at left
            abd "Wait, I've heard that Genies can't kill..."
            jaf "Not directly we can't, {w=.5}but we can certainly place you in a deadly situation."
            jaf "And it's remarkably easy to let people die on their own."
            menu:
                jaf "So, what do you say? {w=.5}Do we have a deal?"
                "Sure.":
                    abd "Sure."
                    jaf "Excellent! Now let us head back to Agrabah."
                    $ qlog.got(jafars_revenge)
                    $ qlog.cancel(sell_lamp)
                    jaf "Bring whatever you've collected so far. {w=.5}We need any money we can get our hands on."
                    $ msg.msg("You got CamelThorns")
                    jump ch1
                "No! I want control over my wishes!":
                    show abd normal at left
                    abd "No! I want control over my wishes!"
                    jaf "Are you sure? {w=.5}This doesn't end well for you my friend."
                    menu:
                        jaf "Last chance, Abdul! Don't throw away this opportunity."
                        "I want my wishes Jafar.":
                            abd "I want my wishes Jafar."
                            jaf "So be it."
                            jump wishes
                        "Okay, okay. I yield.":
                            abd "Okay, okay. I yield. Don't screw me up."
                            abd "I'm still better off than I was this morning."
                            jaf "Good, let us haste! {w=.5}Time's a-wastin'."
                            $ qlog.got(jafars_revenge)
                            $ qlog.cancel(sell_lamp)
                            show abd confused at left
                            abd "What?"
                            jaf "Something I've heard- {w=.5}you know what, never mind."
                            jump ch1
        "Don't be naive, go back to the city.":
            jump endless_grind
