# Effects / buffs and de-buffs
# These are the effects that can be applied to someone, they remain on them until removed or their duration end.
default nose_bleed = spell(
    _("Nose bleed"),
    _("Nose bleed usually stops fast."),
    hp = -1,
    dur = 120,
    )

default bleed = spell(
    _("Bleed"),
    _("You're bleeding and that means you have a hole in your skin./nBleeding doesn't stop that easy, you better do something about it."),
    hp = -9,
    dur = 1200,
    )

default internal_bleed = spell(
    _("Internal bleeding"),
    _("Something inside of you raptured, it's serious, visit a Hakim."),
    hp = -12,
    dur = 700,
    )

default poisoned = spell(
    _("Poisoned"),
    _("Some poison is in your blood, you need an antidote."),
    hp = -8,
    dur = 600,
    )

# Food, potions and healing
default well_fed = spell(
    _("Well fed"),
    _("You are regenerating health faster now."),
    hp = 2,
    dur = 600,
    )

default hungry = spell(
    _("Hungry"),
    _("Your body needs food to generate health and stamina."),
    hp = -2,
    dur = 600,
    )

default very_hungry = spell(
    _("Very hungry"),
    _("Your body needs food to generate health and stamina."),
    dur = 600,
    hp = -4
    )

default thirsty = spell(
    _("Thirsty"),
    _("Your body needs water. A cold drink will help you restore your stamina."),
    mp = -3,
    dur = 600,
    )

default very_thirsty = spell(
    _("Very thirsty"),
    _("You've lost your stamina due to thirst and losing your health now."),
    hp = -6,
    dur = 600,
    )


