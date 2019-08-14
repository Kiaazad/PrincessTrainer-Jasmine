# The spell class ------------------------------
init python:
    class spell:
        def __init__(self, name, inf, icon = "spells/empty.png",
                        hp = 0, mp = 0, stm = 0,
                        mpc = 0, stmc = 0,
                        effect = None, pdbm = [0,0,0,0],
                        pwr = 0, agl = 0, dur = 0
                        ):
            self.name = name
            self.inf = inf
            self.icon = icon

            self.dur = dur

            self.hp = hp
            self.mp = mp
            self.stm = stm

            self.pwr = pwr
            self.agl = agl

            self.mpc = mpc # Mana cost
            self.stmc = stmc # stamina cost

            self.effect = effect
            self.pdbm = pdbm # [parry, dodge, block, miss]

# ----------------------------------------------
default no_spell = spell(
    _("Empty"),
    _("Click to add spell"),
    )
# ----------------------------------------------

# Effects / buffs and de-buffs
# These are the effects that can be applied to someone, they remain on them until removed or their duration end.
default nose_bleed = spell(
    "Nose bleed",
    "Nose bleed usually stops fast.",
    hp = -1,
    dur = 120,
    )

default bleed = spell(
    "Bleed",
    "You're bleeding and that means you have a hole in your skin./nBleeding doesn't stop that easy, you better do something about it.",
    hp = -9,
    dur = 1200,
    )

default internal_bleed = spell(
    "Internal bleeding",
    "Something inside of you raptured, it's serious, visit a Hakim.",
    hp = -12,
    dur = 700,
    )

default poisoned = spell(
    "Poisoned",
    "Some poison is in your blood, you need an antidote.",
    hp = -8,
    dur = 600,
    )

# Food, potions and healing
default well_fed = spell(
    "Well fed",
    "You are regenerating health faster now.",
    hp = 2,
    dur = 600,
    )

default hungry = spell(
    "Hungry",
    "Your body needs food to generate health and stamina.",
    hp = -2,
    dur = 600,
    )

default very_hungry = spell(
    "Very hungry",
    "Your body needs food to generate health and stamina.",
    dur = 600,
    hp = -4
    )

default thirsty = spell(
    "Thirsty",
    "Your body needs water. A cold drink will help you restore your stamina.",
    mp = -3,
    dur = 600,
    )

default very_thirsty = spell(
    "Very thirsty",
    "You've lost your stamina due to thirst and losing your health now.",
    hp = -6,
    dur = 600,
    )


# moves skills and spells
# here are the moves you can perform while fighting.
default kick = spell(
    _("Kick"),
    _("A kick aimed for the ass area."),
    "spells/kick.png",
    hp = -2,
    stmc = 20,
    pdbm = [30, 40, 10, 30],
    )

default punch = spell(
    "Punch",
    "A punch to the face.",
    "spells/punch.png",
    hp = -15,
    stmc = 10,
    effect = [[nose_bleed, 5]],
    pdbm = [20, 50, 10, 20],
    )

default slash = spell(
    "Slash",
    "The slash of blade to cut the skin.",
    "spells/slash.png",
    hp = -21,
    stmc = 20,
    effect = [[bleed, 80]],
    pdbm = [40, 10, 40, 10],
    )

default pierce = spell(
    "Pierce",
    "The slash of blade to cut the skin.",
    "spells/pierce.png",
    hp = -40,
    stmc = 15,
    effect = [[bleed, 60]],
    pdbm = [10, 30, 30, 30],
    )




