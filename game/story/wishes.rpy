 
    


label wishes:
    jaf "Alright what's your wish?"
    menu:
        "I wish to be...":
            menu:
                "I wish to be the Sultan.":
                    jump wish_to_be_sultan
                "I wish to be the God.":
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
                "I wish to have a neat dress thats always fashionable.":
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
                "I wish for everlasting lavash.":
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
                "I wish to move to oasis.":
                    jump wish_to_move_to_oasis







# to be
label wish_to_be_sultan:
    abd "I wish to be the Sultan."
    jaf "so be it"
    return

label wish_to_be_god:
    abd "I wish to be the God."
    jaf "so you want to be something that doesn't exist?"
    me "huh?"
    jaf "as you wish then!"
    return

label wish_to_be_immortal:
    abd "I wish to be immortal."
    jaf "you'll never die then,no matter how old or sick you'll become."
    return

label wish_to_be_indestructible:
    abd "I wish to be indestructible."
    menu:
        jaf "like a rok?"
        "yes":
            jaf "if that's your wish, you'll be like a rok. hard, heavy and lifeless!"
        "no":
            menu:
                jaf "like iron?"
                "yes":
                    jaf "if that's your wish, you'll be like iron. hard, heavy and lifeless!"
                "no":
                    menu:
                        jaf "like what then?"
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
    jaf "the strongest man ever is long dead, that's what you wished for, and you'll be."
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
    jaf "Now go find ."
    return

label wish_to_be_the_best_kisser:
    abd "I wish to be the best kisser."
    jaf "now go find somebody to kiss."
    return



# to have
label wish_to_have_my_fish_business_back:
    abd "I wish to have my fish business back."
    jaf "noney."
    return

label wish_to_have_a_lifetime_supply_of_baghlava:
    abd "I wish to have a lifetime supply of baghlava."
    jaf "Here you go, you better get to eating, they spoil fast."
    return

label wish_to_have_a_camel_that_wont_ever_get_sick:
    abd "I wish to have a camel that wont ever get sick."
    jaf "A dead camel never gets sick, ever."
    return

label wish_to_have_a_neat_dress_thats_always_fashionable:
    abd "I wish to have a neat dress thats always fashionable."
    jaf "shoes are always in fashion."
    return

label wish_to_have_a_well_that_never_runs_dry:
    abd "I wish to have a well that never runs dry."
    jaf "It wouldn't be hard to keep the bottom of a well moist. Here we...{nw}"
    abd "Wait! moist? but I want water."
    abd "A well that have no water to fill a bucket is called a dry well."
    abd "I want a well full of water."
    jaf "That was a close call wasn't it? be more specific next time."
    jaf "I'll give you a well under the sea."
    return

label wish_to_have_a_sword_that_sharpens_itself:
    abd "I wish to have a sword that sharpens itself."
    jaf "Hear that grinding sound, it's constantly sharpening itself."
    return

# my
label wish_my_mother_was_alive:
    abd "I wish my mother was alive."
    jaf "She's alive alright, though she can't do much more than suffering with her flesh rotted away."
    return

label wish_for_my_cat_to_have_a_longer_lifespan:
    abd "I wish for my cat to have a longer lifespan."
    jaf "Sure, your cat will keep getting sicker and sicker for a while more before dying."
    return


# I can
label wish_i_can_breath_under_water:
    abd "I wish I can breath under water."
    jaf "under water you say? you shall get your wish."
    jaf "abaladu'vali'na."
    jaf "there, do you need a body of water to breath under?"
    menu:
        "yes":
            jaf "let me send you under then."
        "I don't feel any different":
            jaf "because you've wished for something you already have."
            me "I did?"
            jaf "yes of course, you can breath anywhere."
            jaf "the reason people drown is the lack of breathable air under water not their inability to breath there."
            me "then I get my wish back?"
            jaf "no!"
            me "why not? you didn't give me anything!"
            jaf "you wished for something you already have. and I granted it. your mistake, not my problem."
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
    abd "I wish for everlasting dinar."
    jaf "."
    return

label wish_for_everlasting_lavash:
    abd "I wish for everlasting lavash."
    jaf "If that's what you want, sure."
    jaf "Ajji, majji, la, tarajji."
    jaf "Here you go."
    jaf "Try it!"
    abd "Alright."
    abd "..."
    jaf "Well?"
    abd "It's chewy..."
    jaf "It's a special kind of pure gluten made by my friend Adam."
    abd "Doesn't seem to break apart."
    jaf "It doesn't spouse to. Just swallow."
    abd "..."
    abd "Hey, it's smaller, it spoused to last forever."
    jaf "It will, provided you're willing to fish it out after it passed through you."
    abd "What?"
    jaf "Yep, it can't be digested. Last's forever."
    abd "You tricked me?"
    jaf "No that's exactly what you've wished for."
    return

label wish_for_a_jar_of_vine_that_never_gets_empty:
    abd "I wish for a jar of vine that never gets empty."
    jaf "Here."
    jaf "It has a rock in it that won't come out... soooo..."
    "..."
    jaf "Alright, you can such on the bottle all you want but you'll never be able to get all of the air out of it."
    return

label wish_for_a_jewelry_store:
    abd "I wish for a jewelry store."
    jaf "Here's one, hopefully you can afford something in it."
    return

label wish_for_a_moneychanger_store:
    abd "I wish for a moneychanger store."
    jaf "Here's one, hopefully you can afford something in it."
    return

label wish_for_a_cup_of_water:
    abd "I wish for a cup of water."
    jaf "Here's one, hopefully you can afford something in it."
    return


# to move
label wish_to_move_to_oasis:
    abd "I wish to move to oasis."
    jaf "Here's one, hopefully you can afford something in it."
    return








