 
    


label wishes:
    jaf "Alright what is your wish?"
    menu:
        "I wish to be...":
            menu:
                "I wish to be a Sultan.":
                    jump wish_to_be_sultan
                "I wish to be a God.":
                    jump wish_to_be_god
                "I wish to be immortal.":
                    jump wish_to_be_immortal
                "I wish to be indestructible.":
                    jump wish_to_be_indestructible
                "I wish to be the strongest man ever.":
                    jump wish_to_be_the_strongest_man_ever
                "I wish to be rich.":
                    jump wish_to_be_rich
                "I wish to be healthy.":
                    jump wish_to_be_healthy
                "I wish to be clever.":
                    jump wish_to_be_clever
                "I wish to be brave.":
                    jump wish_to_be_brave
                "I wish to be a dancer.":
                    jump wish_to_be_dancer
                "I wish to be the best chess player.":
                    jump wish_to_be_the_best_chess_player
                "I wish to be the best kisser.":
                    jump wish_to_be_the_best_kisser

        "I wish to have...":
            menu:
                "I wish to have my fish business back.":
                    jump wish_to_have_my_fish_business_back
                "I wish to have a lifetime supply of baghlava.":
                    jump wish_to_have_a_lifetime_supply_of_baghlava
                "I wish to have a camel that wont ever get sick.":
                    jump wish_to_have_a_camel_that_wont_ever_get_sick
                "I wish to have a neat dress that's always fashionable.":
                    jump wish_to_have_a_neat_dress_thats_always_fashionable
                "I wish to have a well that never runs dry.":
                    jump wish_to_have_a_well_that_never_runs_dry
                "I wish to have a sword that sharpens itself.":
                    jump wish_to_have_a_sword_that_sharpens_itself
        "I wish my...":
            menu:
                "I wish my mother was alive.":
                    jump wish_my_mother_was_alive
                "I wish for my cat to have a longer lifespan.":
                    jump wish_for_my_cat_to_have_a_longer_lifespan
        "I wish I can...":
            menu:
                "I wish I can breath under water.":
                    jump wish_i_can_breath_under_water
        "I wish to not...":
            menu:
                "I wish to not pay taxes.":
                    jump wish_to_not_pay_taxes
        "I wish for...":
            menu:
                "I wish for a golden fish.":
                    jump wish_for_a_golden_fish
                "I wish for a flying carpet.":
                    jump wish_for_a_flying_carpet
                "I wish for a stallion.":
                    jump wish_for_a_stallion
                "I wish for a slave.":
                    jump wish_for_a_slave
                "I wish for everlasting dinar.":
                    jump wish_for_everlasting_dinar
                "I wish for an everlasting lavash bread.":
                    jump wish_for_everlasting_lavash
                "I wish for a jar of vine that never gets empty.":
                    jump wish_for_a_jar_of_vine_that_never_gets_empty
                "I wish for a jewelry store.":
                    jump wish_for_a_jewelry_store
                "I wish for a moneychanger store.":
                    jump wish_for_a_moneychanger_store
                "I wish for a cup of water.":
                    jump wish_for_a_cup_of_water
        "I wish to move...":
            menu:
                "I wish to move to the oasis.":
                    jump wish_to_move_to_oasis



    $ abdul.wishes -= 1
    if abdul.wishes:
        jaf "Now you're down to [abdul.wishes] wishes."
    else:
        jaf "That was your last wish, and you've got what you deserved."
        jaf "That's very unfortunate for both of us."


# to be
label wish_to_be_sultan:
    abd "I wish to be a Sultan."
    jaf "Then so be it."
    return

label wish_to_be_god:
    abd "I wish to be a God."
    jaf "so you want to be something that doesn't exist?"
    abd "Huh?"
    jaf "As you wish then!"
    abd "But God does exist!"
    jaf "Yeah, yeah. There will be people believing you exist as well."
    abd "But...{nw}"
    jaf "Too late for buts Abdul. You are done for now, this was your last mistake!"
    # we should erase all save slots at this point to troll the player
    return

label wish_to_be_immortal:
    abd "I wish to be immortal."
    jaf "All right, you'll never die then, no matter how old or sick you'll become in the future."
    jaf "Who knows what will happen to you after you get married and grow old."
    jaf "Hope you make lots of friends."
    return

label wish_to_be_indestructible:
    abd "I wish to be indestructible."
    menu:
        jaf "As a rock?"
        "Yes":
            jaf "if that's your wish, you'll be like a rock. hard, heavy and lifeless!"
        "No":
            menu:
                jaf "As an iron?"
                "Yes":
                    jaf "if that's your wish, you'll be like an iron. hard, heavy and lifeless!"
                "no":
                    menu:
                        jaf "Then what?"
                        "a statue!":
                            jaf "Then a statue you will be!"
                        "a tree!":
                            jaf "Then a tree you will be!"
                        "the hercules!":
                            jaf "Then a myth you will be!"
                        "the God!!":
                            jaf "Then a lie you will be!"
    return

label wish_to_be_the_strongest_man_ever:
    abd "I wish to be the strongest man ever."
    jaf "The strongest man ever is long dead, if that's what you wished for, and you'll be stronger then anyone else."
    return

label wish_to_be_rich:
    abd "I wish to be rich."
    jaf "Here are you, now don't spend too much. It'll be gone before you know it."
    return

label wish_to_be_healthy:
    abd "I wish to be healthy."
    jaf "Okay, you'll only be healthy for a little while. You will get sick later on."
    abd "What?! But I wanted to be healthy forever!"
    jaf "Well, you should be more specific on your wish then."
    jaf "Good luck on living for the rest of your life. Hope you don't get sick after this."
    return

label wish_to_be_clever:
    abd "I wish to be clever."
    jaf "Okay, you are smart and all but it's not a guarantee that you'll become a successful business owner again."
    jaf "Also, your cleverness will get some haters because you'll make people feel even more dumb about themselves." 
    jaf "Good luck."
    return

label wish_to_be_brave:
    abd "I wish to be brave."
    jaf "Okay, good luck trying to be brave enough to fall over into the sea and survive."
    abd "Why would I want to do that?"
    jaf "It's for entertainment, you idiot. You make money out of it."
    jaf "You'll be brave enough to take risks, but what if that risk cost you to lose your life?"
    jaf "Well, good luck. You'll need it."
    return

label wish_to_be_dancer:
    abd "I wish to be a dancer."
    jaf "All right, good luck with the auditions though."
    jaf "I heard a lot of dancers failed because professionals say they weren't good enough'."
    jaf "You better start practicing now because you're about to get old soon."
    jaf "And you know what happens when you're old and out of shape?"
    jaf "Good luck. You'll need it."
    return

label wish_to_be_the_best_chess_player:
    abd "I wish to be the best chess player."
    jaf "There you go."
    jaf "Now go find an opponent to play with."
    return

label wish_to_be_the_best_kisser:
    abd "I wish to be the best kisser."
    jaf "Okay, now go find somebody to kiss."
    jaf "Hope you don't have to deal with love drama after this." 
    return

# to have
label wish_to_have_my_fish_business_back:
    abd "I wish to have my fish business back."
    jaf "Let's see how long it lasts again then."
    return

label wish_to_have_a_lifetime_supply_of_baghlava:
    abd "I wish to have a lifetime supply of baghlava."
    jaf "Here you go, but you better get to eating, they spoil fast."
    return

label wish_to_have_a_camel_that_wont_ever_get_sick:
    abd "I wish to have a camel that never gets sick."
    jaf "A dead camel never gets sick, ever."
    return

label wish_to_have_a_neat_dress_thats_always_fashionable:
    abd "I wish to have a neat dress that's always fashionable."
    jaf "Shoes always come in fashion."
    return

label wish_to_have_a_well_that_never_runs_dry:
    abd "I wish to have a well that never runs dry."
    jaf "It wouldn't be hard to keep the bottom of a well moist. Here we...{nw}"
    abd "Wait! Moist? but I want water."
    abd "A well that has no water to fill a bucket is called a dry well."
    abd "Then I want a well that is full of water."
    jaf "That was a close call wasn't it? Be more specific next time."
    jaf "I'll give you a well from under the sea."
    return

label wish_to_have_a_sword_that_sharpens_itself:
    abd "I wish to have a sword that sharpens itself."
    jaf "Hear that grinding sound? It'll constantly sharpening itself forever."
    return

# my
label wish_my_mother_was_alive:
    abd "I wish my mother was alive."
    jaf "She's alive alright, though she can't do much more than suffering with her flesh rotting away."
    return

label wish_for_my_cat_to_have_a_longer_lifespan:
    abd "I wish for my cat to have a longer lifespan."
    jaf "Sure, your cat will keep getting sicker and sicker for a while more before dying."
    return


# I can
label wish_i_can_breath_under_water:
    abd "I wish I can breath under water."
    jaf "Under water you say? Very well, you shall get your wish."
    jaf "abaladu'vali'na."
    jaf "There, now do you need a body of water to breath under?"
    menu:
        "Yes":
            jaf "Let me send you under then."
        "I don't feel any different":
            jaf "That's because you already wished for something you already have."
            abd "I did?"
            jaf "Yes of course, you can breathe anywhere."
            jaf "The reason people drown is the lack of breathable air under water, it's not their inability to breath there."
            abd "Then I get my wish back?"
            jaf "No!"
            abd "Why not? You didn't give me anything!"
            jaf "You wished for something you already have. and I granted it. Your mistake, not my problem."
    return

# to not
label wish_to_not_pay_taxes:
    abd "I wish to not pay taxes."
    jaf "All right, you'll be able to save some money, but it's not my fault if you go to jail soon."
    return


# for
label wish_for_a_golden_fish:
    abd "I wish for a golden fish."
    jaf "Here are you, now you better give it some water already. I think it's dying from the desert heat already."
    abd "What?! You could have given me a cup of water or something for my pet!"
    jaf "You could have wished for that in the first place."
    return

label wish_for_a_flying_carpet:
    abd "I wish for a flying carpet."
    jaf "."
    return

label wish_for_a_stallion:
    show abd smug at left  
    abd "I wish for a stallion."
    show jaf normal at right
    jaf "A stallion? Alright then..."
    hide jaf normal
    show jaf magic at right
    jaf "ajji, maji, ahhhhh..."
    hide jaf magic
    show jaf normal at right
    show abd excited at left
    abd "Whoa!"
    abd "A real live horse! I've always wanted to see the real one for years!"
    jaf "I even put the equipment on for it. Wanna ride it?"
    abd "Heck yeah I do!"
    jaf "It should the same as riding a camel, so it should be easy."
    hide abd excited
    show abd normal at left
    abd "Hmm... I never ride a camel before, but I'm sure I'll be fine."
    abd "Hut hut hut!"
    show abd confused at left
    "..."
    hide jaf normal 
    show jaf disappointed at right 
    jaf "That's for camels, you blubbering idiot. You have to either say "giddy up!" or "hi-yah!""
    hide abd confused
    show abd excited at left
    abd "Oh, got it! Giddy up!"
    "Neighhhhhh!!!"
    hide abd excited
    abd "Whoa! I'm falling!"
    hide jaf disappointed
    show jaf smile at right
    abd "Oof! What the-?! My foot is caught on something!"
    "Neigh!!!!!" 
    abd "Wait! Don't move! Ahhhhhhhh!!!!"
    abd "Ahhhhhh!!!!"
    abd "Jafar, help me!"
    show jaf looking2 at right
    jaf "Ouch , now that's gotta hurt. He's being dragged around by a really fast horse that can't seem to stop without a command."
    jaf "Must be painful for him." 
    jaf "Could have gotten some training in horseback riding earlier."
    return

label wish_for_a_slave:
    abd "I wish for a slave."
    jaf "Here you are, let's see how long he'll be able to serve you. He might escape by now."
    return

label wish_for_everlasting_dinar:
    abd "I wish for an everlasting dinner."
    show abd smug at left
    show jaf normal at right
    jaf "That's it? That's what you want?
    hide abd smug
    show abd tired at left
    hide jaf normal
    show jaf looking2
    abd "Yes, I haven't had a full meal in weeks! I'm always tired of eating nothing but plain bread and water!"
    abd "Sometimes I don't eat, so I'm always hungry all the time!" 
    hide abd tired
    show abd normal at left
    abd "Are you listening?"
    hide jaf looking2
    show jaf normal at left
    jaf "Huh? I thought I saw something, so I had to keep looking at it."
    jaf "Anyways, an everlasting dinner shall it be!"
    hide jaf normal
    show jaf magic at left
    jaf "Ajjji, majji, lajji..."
    jaf "Here you are!"
    hide jaf magic
    show jaf normal at right
    show abd excited at left
    abd "Whoa!" 
    abd "Finally! A full meal to myself!"
    abd "Look at all that meat! Chicken, beef, and there's a lamb kabob too!" 
    hide jaf normal
    show jaf smile at right
    jaf "Well, what are you waiting for? Dig in!"
    hide abd excited
    show abd alert at left
    abd "Oh right! I should eat them before it gets cold!"
    hide alert
    show abd excited at left
    abd "Now what should I start first?
    #fade in screen
    abd "Now that's delicious! Oh man! Eating it with that fresh pita bread makes it even more delicious too!"
    abd "Gom, nom, nom, gom!"
    jaf "Your belly is getting bigger now..." 
    abd "More! More! I need more! 
    jaf "There are plenty more..."
    #fade out screen
    show jaf smile at right
    jaf "Awwww... just look at him, sleeping like a baby. He ate so much his belly has gotten a LOT bigger than before."
    hide jaf smile
    show jaf looking2 at right
    jaf "Oh look, some vultures have arrived. They're waiting for him to just die already."
    jaf "Patiences is key, everyone! He won't be dead for a little while now."
    hide jaf looking2
    show jaf smile at right
    jaf "I put a sleeping spell on all of his food, so it'll make him sleep forever."
    jaf "Oh look, a snake is coming towards him. I wonder what will happen if I poke it a bunch of times?"
    return

label wish_for_everlasting_lavash:
    abd "I wish for an everlasting lavash bread."
    jaf "If that's what you want, sure."
    show jaf magic at right
    jaf "Ajji, majji, la, tarajji."
    hide jaf magic
    show jaf normal at right
    jaf "Here you go."
    jaf "Try it!"
    show abd excited at left
    abd "Alright."
    abd "..."
    jaf "Well?"
    hide abd excited
    show abd normal at left
    abd "It's chewy..."
    jaf "It's a special kind of pure gluten made by my friend, Adam."
    hide abd normal
    show abd confused at left
    abd "What's... a... gullytoon?"
    hide jaf normal
    show jaf disappointed at right
    jaf "It's not important."
    abd "Doesn't seem to break apart."
    hide jaf disappointed
    show jaf normal at right
    jaf "It's not suppose to. Just swallow."
    abd "..."
    hide abd confused
    show abd scared at left
    abd "Hey, it's smaller! It supposed to last forever."
    show jaf smile at right
    jaf "It will, are you willing to fish it out after it passed through you."
    hide abd scared
    show adb confused at left
    abd "What?"
    jaf "Yep, it can't be digested. It'll last in your stomach forever."
    abd "You tricked me?"
    jaf "No, that's exactly what you wished for."
    return

label wish_for_a_jar_of_vine_that_never_gets_empty:
    abd "I wish for a jar of wine that never gets empty."
    jaf "Here."
    jaf "It has a rock that won't come out... soooo..."
    "..."
    jaf "Alright, you can suck on the bottle all you want but you'll never be able to get all the air out of it."
    return

label wish_for_a_jewelry_store:
    abd "I wish for a jewelry store."
    jaf "As you wish..."
    show jaf magic at right
    jaf "Ajjj, ahhhh."
    hide jaf magic
    show jaf normal at right
    jaf "Here you are."
    show abd excited at left
    abd "Whoa! Look at all the jewelries I can sell for profit!" 
    abd "Imagine that! A warm bed to sleep on, eating delicous meals three times a day, and I can make my own private harem too!"
    hide jaf normal
    show jaf smile at right
    jaf "Yeah... good luck with that. You know that all of them are fake anyway."
    hide abd excited
    show abd confused at left
    abd "Wait, what?"
    hide jaf smile
    show jaf normal at right
    jaf "Well, yeah. If you choose to sell them, then you'll get some pocket money back."
    abd "You tricked me?"
    jaf "No, you asked for a jewelry store and you got it. You didn't ask me to give you a jewelry store that sells REAL JEWELS."
    jaf "You should be specific on your wishes, my good sir."
    return

label wish_for_a_moneychanger_store:
    abd "I wish for a moneychanger store."
    jaf "Here you are, hopefully you can afford something in there."
    return

label wish_for_a_cup_of_water:
    abd "I wish for a cup of water."
    show jaf disappointed at right
    jaf "Really? Just that?"
    show abd smug at left
    abd "Yes, that's exactly what I want. Now get to it!"
    hide jaf disappointed 
    show jaf normal at right
    jaf "As you wish."
    hide jaf normal
    show jaf magic at right
    jaf "Ajjjj, mjjj, ahhhh."
    hide jaf magic
    show jaf normal at right
    jaf "Here you are."
    hide abd smug
    show abd excited at left
    abd "Oh! Finally! Fresh water, here I come!"
    abd "Gulp, gulp, gulp..."
    show abd scared at left
    abd "Ahhhhhhh!!!!"
    abd "What the fuck?!" 
    abd "Since when did the cup get all black?!"
    abd "It wasn't like that before!"
    show jaf smile at right
    jaf "Oh, so the cup is completely black already?" 
    jaf "Well, you didn't wish for a FRESH cup of water. You asked for a CUP of water, ."
    hide abd scared
    show abd alert at left
    abd "If it's all black, then that means..."
    hide abd alert
    abd "*Cough!* *Hack!* *Wheeze!*"
    hide jaf smile
    show jaf probing at right
    jaf "Yep, black water is not safe to drink."
    return

 # to move
label wish_to_move_to_oasis:
    abd "I wish to move to the oasis."
    jaf "All right." 
    show jaf magic at right
    jaf "ajji, majji, aaaahhh."
    hide jaf magic
    show jaf normal at right
    jaf "Here we are."
    show abd back at left
    abd "Whoa! Now I can finally live near the waters!"
    hide abd back
    show abd excited at left
    abd "I wonder if I can swim in it?"
    jaf "Go ahead! You only have ONE life, so do it!"
    jaf "You're actually going to be the first person to try it out anyway!"
    abd "Really?!"
    jaf "Yeah."
    jaf "But I'm going to cover my eyes for a bit because I don't want to see that... body of yours."
    hide abd excited
    abd "Suit yourself!"
    hide jaf normal
    show jaf disappointed at right
    abd "Woohoo! Yeah! The water feels great!"
    abd "I can even drink out of it too!" 
    abd "Ahhh! So fresh!" 
    abd "Hey! Now here's an idea! I can make another business out of this!"
    jaf "Another business, huh?"
    abd "That's right! Abdul's Oasis! Sounds pretty catchy, right?"
    jaf "Right..."
    abd "Ahhhh!!! Something bit my ass!" 
    abd "What the fuck?!"
    abd "A desert crocodile! Ahhhhh!!!!"
    abd "Jafar! Help me!"
    show jaf smile at right
    jaf "Well it's about time, my hand was already cramping for shutting my eyes earlier."
    hide jaf smile
    show jaf thinking at right
    jaf "Ooooh... right in the leg and now it bites his ass again."
    hide jaf thinking 
    show jaf smile at right
    jaf "Yeah... I wouldn't go in there if I were you, Abdul!"
    jaf "Perhaps I probably should have said that earlier."
    jaf "Whoopies daisies."
    return








