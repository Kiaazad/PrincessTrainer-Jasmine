 
    


label wishes:
    jaf "Alright what's your wish?"
    menu:
        "I wish to be...":
            menu:
                "I wish to be the Sultan.":
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
    abd "I wish to be the Sultan."
    jaf "Then so be it"
    return

label wish_to_be_god:
    abd "I wish to be a God."
    jaf "so you want to be something that doesn't exist?"
    me "Huh?"
    jaf "As you wish then!"
    me "But God does exist!"
    jaf "Yeah, yeah. There will be people believing you exist as well."
    me "But...{nw}"
    jaf "Too late for buts Abdul. You are done for now, this was your last mistake!"
    # we should erase all save slots at this point to troll the player
    return

label wish_to_be_immortal:
    abd "I wish to be immortal."
    jaf "All right, you'll never die then, no matter how old or sick you'll become in the future."
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
                            jaf "a statue you will be then!"
                        "a tree!":
                            jaf "a tree you will be then!"
                        "the hercules!":
                            jaf "a myth you will be then!"
                        "the God!!":
                            jaf "a lie you will be then!"
    return

label wish_to_be_the_strongest_man_ever:
    abd "I wish to be the strongest man ever."
    jaf "the strongest man ever is long dead, if that's what you wished for, and you'll be stronger then anyone else."
    return

label wish_to_be_rich:
    abd "I wish to be rich."
    jaf "noney."
    return

label wish_to_be_healthy:
    abd "I wish to be healthy."
    jaf "noney."
    return

label wish_to_be_clever:
    abd "I wish to be clever."
    jaf "noney."
    return

label wish_to_be_brave:
    abd "I wish to be brave."
    jaf "noney."
    return

label wish_to_be_dancer:
    abd "I wish to be a dancer."
    jaf "noney."
    return

label wish_to_be_the_best_chess_player:
    abd "I wish to be the best chess player."
    jaf "Now go find an opponent to play with."
    return

label wish_to_be_the_best_kisser:
    abd "I wish to be the best kisser."
    jaf "Now go find somebody to kiss."
    return



# to have
label wish_to_have_my_fish_business_back:
    abd "I wish to have my fish business back."
    jaf "noney."
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
            me "I did?"
            jaf "Yes of course, you can breathe anywhere."
            jaf "The reason people drown is the lack of breathable air under water, it's not their inability to breath there."
            me "Then I get my wish back?"
            jaf "No!"
            me "Why not? You didn't give me anything!"
            jaf "You wished for something you already have. and I granted it. Your mistake, not my problem."
    return

# to not
label wish_to_not_pay_taxes:
    abd "I wish to not pay taxes."
    jaf "."
    return


# for
label wish_for_a_golden_fish:
    abd "I wish for a golden fish."
    jaf "."
    return

label wish_for_a_flying_carpet:
    abd "I wish for a flying carpet."
    jaf "."
    return

label wish_for_a_stallion:
    abd "I wish for a stallion."
    jaf "."
    return

label wish_for_a_slave:
    abd "I wish for a slave."
    jaf "."
    return

label wish_for_everlasting_dinar:
    abd "I wish for everlasting dinner."
    jaf "."
    return

label wish_for_everlasting_lavash:
    abd "I wish for an everlasting lavash bread."
    jaf "If that's what you want, sure."
    jaf "Ajji, majji, la, tarajji."
    jaf "Here you go."
    jaf "Try it!"
    abd "Alright."
    abd "..."
    jaf "Well?"
    abd "It's chewy..."
    jaf "It's a special kind of pure gluten made by my friend, Adam."
    abd "What's... a... gullytoon?"
    jaf "It's not important."
    abd "Doesn't seem to break apart."
    jaf "It doesn't spouse to. Just swallow."
    abd "..."
    abd "Hey, it's smaller, it spoused to last forever."
    jaf "It will, provided you're willing to fish it out after it passed through you."
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
    jaf "Here you are, hopefully you can afford something in there."
    return

label wish_for_a_moneychanger_store:
    abd "I wish for a moneychanger store."
    jaf "Here you are, hopefully you can afford something in there."
    return

label wish_for_a_cup_of_water:
    abd "I wish for a cup of water."
    jaf "Here you are, hopefully you can afford another one."
    return


# to move
label wish_to_move_to_oasis:
    abd "I wish to move to the oasis."
    jaf "Here you are, hopefully you can afford something in there."
    return








