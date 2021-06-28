default caravanserai_street = pnco(
    "Street",
    "bg/caravanserai/street.png",
    (445, 221),
    Jump('street'),
    hidden = False, hoffset = (114,80),
    )
default caravanserai_desert = pnco(
    "Desert",
    "bg/caravanserai/desert.png",
    (1534, 300),
    Jump('desert'),
    hidden = False, hoffset = (114,80),
    )
default traveler_1 = pnco(
    "Traveler",
    "bg/caravanserai/traveler.png",
    (1235, 550),
    Jump('traveler_1'),
    hidden = False, hoffset = (114,80),
    )

default caravanserai_map = pncs(
    "Caravanserai",
    [
        caravanserai_street,
        caravanserai_desert,
        traveler_1,

    ], night = "bg/caravanserai/night.webp"
    )

image bg caravanserai = "bg/caravanserai/bg.webp"
label caravanserai:
    scene
    show bg caravanserai onlayer bg
    show screen pnc(abdul, caravanserai_map)
    pause
    jump caravanserai



default stolen_spyglass = quest(
    _("Stolen spyglass"),
    [_("The virgin hunting traveler needs his stolen spyglass returned to him.")],
    )

define vir = Character("Traveler", color="#4ff", what_text_color="#dff")
image vir normal = "char/pedestrians/virgin hunter.png"
default virgin_hunter = unit(
    "Virgin hunter",
    "char/virgin_hunter",

    2210,
    [

    ],
    1.1,

    28,
    "Peasant",
    interests = [],
    reject = []
    )
label traveler_1:
    scene
    show abd normal at left with dissolve
    show vir normal at right with dissolve
    if not qlog.has(stolen_spyglass):
        "..."
        vir "Yes?"
        abd "Sorry, I didn't mean to stare."
        vir "Still you did."
        abd "Well, that's an odd broach you're wearing."
        vir "Quite a conversation started isn't it?"
        abd "What does it mean?"
        vir "Can't say."
        "..."
        abd "You seem irritated."
        vir "Because I am."
        abd "Why?"
        vir "I've been robbed."
        vir "By a little brat."
        abd "Have you reported him to the guards?"
        vir "I Can't."
        "..."
        abd "Money?"
        vir "No, something much more important."
        abd "Jewelry?"
        vir "No."
        abd "Care to tell me what it was?"
        vir "Why?"
        abd "I might be able to help you in some way."
        vir "You can tell me where I can find a lense grinder in this city so I can buy another one."
        abd "I don't think we have one of those. What does a lense grinder does?"
        vir "Shapes glass into lenses."
        abd "We have a jeweler."
        vir "Does he sell spyglass?"
        abd "So that's what they took from you?"
        abd "Wise of you to not report it. The head of guards doesn't like spyglass in people's hands."
        vir "I know."
        abd "So why do you need one?"
        "..."
        vir "Fuck it, now that pussycat is out of the bag, let me tell you what I do."
        vir "I'm a virgin hunter. On a special mission to find wives for the prince of my land."
        $ vir.name = "The virgin hunter"
        vir "I've heard that the princess of Agrabah is an unmatched beauty that recently came of age."
        abd "She's not a virgin anymore."
        vir "I know! The news travels slow and I've heard of her marriage when I got here."
        abd "So what do you need spyglass for?"
        vir "My job is to verify if the princess is beautiful and pure for the prince."
        vir "And meeting a princess isn't always that straight forward."
        abd "The princess often comes to her balcony to watch the city, you can wait outside of the palace to see her."
        abd "And you don't need spyglass for that."
        vir "Well. Usually from that angle, only her face is visible."
        vir "I need to see emmm... more..."
        vir "You know..."
        "..."
        vir "I think I've talked too much."
        vir "In revealing more I might incriminate myself."
        vir "I don't want any trouble with the guards."
        abd "Do I look like a guard? I won't tell anyone."
        "..."
        abd "Come on, I'm trying to help you."
        vir "Alright, alight. I do need my spyglass before I leave for the next target."
        vir "If there's any chance I get them back, I'll have to trust you."
        vir "You look trustworthy."
        abd "I am."
        vir "I've spotted a vantage point on the mountains to the left of the city."
        vir "From there, I would've be able to verify if the princess has a beautiful body as well."
        vir "For research purposes of course."
        vir "But she's no longer single and virgin. So, I just need to find my spyglass, buy a new one or send for one before moving on."
        $ vantage_point.hidden = False
        $ qlog.got(stolen_spyglass)
        abd "I'll see what I can do for you."
        abd "Can't promise anything though. Thieves of Agrabah hide their loot and it's almost impossible to get it back."
        vir "Do this and I'll reward you handsomely."
        abd "I'll try harder then."
    elif qlog.has(stolen_spyglass) in ["Active", "Completed"]:
        vir "What do you have for me?"
        menu:
            "I've got an old one." if hero.has(old_spyglass):
                abd "I've got this old one."
                vir "Hmmmm...."
                vir "The front glass is broken."
                vir "The body is dinged up."
                vir "Its joins are lose."
                vir "It's garbage!"
                vir "But it will do for now."
                $ hero.drop(old_spyglass, 1)
                $ stolen_spyglass.finish()
                "..."
                vir "Ah yes, your reward."
                $ hero.gotcash(5000)
                vir "Here's 5000 dinars."
                menu:
                    "That's what I've for it.":
                        abd "That's what I've for it."
                        vir "A haggler huh?"
                        abd "No really, it was almost 5000 dinars."
                        $ hero.gotcash(1000)
                        vir "Alright, here's something extra."
                        abd "Thank you."
                    "I've paid more than that for it.":
                        abd "I've paid more than that for it."
                        vir "For this pice of junk?"
                        abd "Yes."
                        vir "You've got ripped off."
                        $ hero.gotcash(500)
                        vir "Here..."
                        vir "More than that and you can have it back."
                        abd "Alright."
                    "..."
                vir "You may go now."
                abd "Right!"

            "I've got it." if hero.has(new_spyglass):
                abd "I've got it."
                $ hero.drop(new_spyglass, 1)
                abd "Here..."
                vir "Great, Let me see."
                vir "The glasses are still there... It opens and closes... Perfect."
                "..."
                vir "Right, your reward. is 5000 dinars enough?"
                menu:
                    "I actually paid a hefty handsome to get it.":
                        abd "I actually paid a hefty handsome to get it."
                        vir "Hopefully not more than its worth."
                        menu:
                            "6000":
                                abd "6000"
                                vir "I see..."
                                $ hero.gotcash(6000)
                                vir "here you go."
                                $ hero.gotcash(3000)
                                vir "With something extra for your troubles."
                            "7000":
                                abd "7000"
                                vir "That is hefty."
                                $ hero.gotcash(7000)
                                vir "Here's your money."
                                $ hero.gotcash(2000)
                                vir "And your reward."
                            "8000":
                                abd "8000"
                                $ hero.gotcash(8000)
                                vir "Seems excessive you should learn how to negotiate."
                                vir "I can only return to you the money you've paid."
                            "9000":
                                abd "9000"
                                vir "That's a lie, nobody in their right mind would pay that much for it."
                                $ hero.gotcash(6000)
                                vir "Take this 6000 and never try that with me again."
                    "Sure.":
                        abd "Sure."
                        $ hero.gotcash(5000)
                        vir "Here you go."
                $ stolen_spyglass.finish()
    "..."
    pause
    jump caravanserai