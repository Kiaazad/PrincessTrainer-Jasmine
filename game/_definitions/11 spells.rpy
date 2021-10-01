# moves skills and spells
# here are the moves you can perform while fighting.
default kick = spell(
    _("Kick"),                                  # name
    _("A kick aimed for the ass area."),        # description
    "kick",                          # icon
    hp = -2,                                    # Health damage or heal
    stmc = 5,                                  # Stamina cost
    pdbm = [30, 40, 10, 30],                    # chance to [parry, dodge, block, miss]
    )

default punch = spell(
    _("Punch"),
    _("A punch to the face."),
    "punch",
    hp = -35,
    stmc = 10,
    hpc = 1,
    effect = [[nose_bleed, 5]],
    pdbm = [20, 50, 10, 20],
    )

default run_away = spell(
    _("Run away"),
    _("Run away like a coward."),
    "run_away",
    hp = 0,
    stmc = 10,
    pdbm = [20, 50, 10, 20],
    )
default surrender = spell(
    _("Surrender"),
    _("surrender."),
    "run_away",
    hp = 0,
    stmc = 10,
    pdbm = [20, 50, 10, 20],
    )
default mercy = spell(
    _("Mercy"),
    _("Mercy."),
    "run_away",
    hp = 0,
    stmc = 10,
    pdbm = [20, 50, 10, 20],
    )

default stand_still = spell(
    _("Stand still"),
    _("Such a dummy move."),
    "run_away",
    hp = 0,
    stmc = 0,
    pdbm = [20, 50, 10, 20],
    )

default slash = spell(
    _("Slash"),
    _("A slash that can cut through the skin. Causing the enemy to bleed."),
    "slash",
    hp = -21,
    stmc = 40,
    effect = [[bleed, 80]],
    pdbm = [40, 10, 40, 10],
    )

default pierce = spell(
    _("Pierce"),
    _("Can stab through the the enemy's skin. Causing them to bleed."),
    "pierce",
    hp = -40,
    stmc = 45,
    effect = [[bleed, 60]],
    pdbm = [10, 30, 30, 30],
    )

default slap = spell(
    _("Slap"),
    _("A good slap across the face. Such a princess move. Can cause to give your enemy a nose bleed."),
    "pierce",
    hp = -5,
    stmc = 15,
    effect = [[nose_bleed, 10]],
    pdbm = [10, 30, 30, 60],
    )

default bite = spell(
    _("Bite"),
    _("Nasty, isn't it?"),
    "pierce",
    hp = -5,
    stmc = 15,
    effect = [[bleed, 10]],
    pdbm = [10, 30, 30, 60],
    )

default maul = spell(
    _("Maul"),
    _("Can tear through the enemy's skin, causing them to bleed."),
    "pierce",
    hp = -5,
    stmc = 15,
    effect = [[bleed, 5]],
    pdbm = [10, 30, 30, 60],
    )

default stab = spell(
    _("Stab"),
    _("Preferably in the back, but the front is okay I guess. Can cause the enemy to bleed."),
    "pierce",
    hp = -5,
    stmc = 15,
    effect = [[bleed, 90]],
    pdbm = [10, 30, 30, 60],
    )

default eye_poke = spell(
    _("Eye poke"),
    _("Hard to pull but do it twice and your opponent will be blind, permanently."),
    "pierce",
    hp = -5,
    stmc = 15,
    effect = [[bleed, 90]],
    pdbm = [10, 30, 30, 80],
    )

default growl = spell(
    _("Growl"),
    _("Intimidating, isn't it? Can decrease... "),
    "pierce",
    mp = -10,
    stmc = 5,
    pdbm = [10, 30, 30, 50],
    )


default list_of_spells = [
    kick, punch, slash, pierce, slap,
]


