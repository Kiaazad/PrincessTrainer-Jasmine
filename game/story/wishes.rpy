



screen wishes_search:
    hbox:
        text "I wish "
    


label wishes:
    jaf "Alright what's your wish?"



# to be
label wish_to_be_sultan:
    jaf "so be it"
    return

label wish_to_be_god:
    jaf "so you want to be something that doesn't exist?"
    me "huh?"
    jaf "as you wish then!"
    return

label wish_to_be_immortal:
    jaf "you'll never die then,no matter how old or sick you'll become."
    return

label wish_to_be_indestructible:
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
    jaf "the strongest man ever is long dead, that's what you wished for, and you'll be."
    return

label wish_to_be_rich:
    jaf "noney."
    return

label wish_to_be_healthy:
    jaf "noney."
    return

label wish_to_be_cleaver:
    jaf "noney."
    return

label wish_to_be_brave:
    jaf "noney."
    return

label wish_to_be_dancer:
    jaf "noney."
    return

label wish_to_be_the_best_chess_player:
    jaf "Now go find ."
    return

label wish_to_be_the_best_kisser:
    jaf "now go find somebody to kiss."
    return



# to have
label wish_to_have_my_fish_business_back:
    jaf "noney."
    return

label wish_to_have_a_lifetime_supply_of_baghlava:
    jaf "Here you go, you better get to eating, they spoil fast."
    return

label wish_to_have_a_camel_that_wont_ever_get_sick:
    jaf "A dead camel never gets sick, ever."
    return

label wish_to_have_a_neat_dress_thats_always_fashionable:
    jaf "shoes are always in fashion."
    return

label wish_to_have_a_well_that_never_runs_dry:
    jaf "I'll give you a well under the sea."
    return

label wish_to_have_a_sword_that_sharpens_itself:
    jaf "Hear that grinding sound, it's constantly sharpening itself."
    return

# my
label wish_to_bring_my_mother_mother_back_to_life:
    jaf "She's alive alright, though she can't do much more than suffering with her flesh rotted away."
    return

label wish_for_my_cat_to_have_a_longer_lifespan:
    jaf "Sure, your cat will keep getting sicker and sicker for a while more before dying."
    return


# I can
label wish_i_can_breath_under_water:
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
    jaf "."
    return


# for
label wish_for_a_golden_fish:
    jaf "."
    return

label wish_for_a_flying_carpet:
    jaf "."
    return

label wish_for_a_stallion:
    jaf "."
    return

label wish_for_a_slave:
    jaf "."
    return

label wish_for_everlasting_dinar:
    jaf "."
    return

label wish_for_everlasting_lavash:
    jaf "."
    return

label wish_for_a_jar_of_vine_that_never_get_empty:
    jaf "Here."
    jaf "It has a rock in it that won't come out... soooo..."
    return

label wish_for_a_jewelry_store:
    jaf "Here's one, hopefully you can afford something in it."
    return

label wish_for_a_moneychanger_store:
    jaf "Here's one, hopefully you can afford something in it."
    return

label wish_for_a_cup_of_water:
    jaf "Here's one, hopefully you can afford something in it."
    return


# to move
label wish_to_move_to_oasis:
    jaf "Here's one, hopefully you can afford something in it."
    return








