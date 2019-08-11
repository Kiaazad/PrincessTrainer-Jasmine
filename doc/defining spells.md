Defining a new spell only needs a name and description. Everything else is optional.

```python
default stink_eye = spell(
    "Stink eye",
    "Show them that you're not okay with what they are doing",
    )
```
Of course what is a spell without it's icon? and while we're at it let's add everything else to it:

```python
default skill_example = spell( # The instance name: "skill_example" must be a unique name in all of the game.
    "Devastation",
    "With all of the numbers we added to this spell it does a number on you or your enemy.",
    icon = "spells/skill_example.png",

    hp = -10,
    mp = -5,
    stm = -10,

    mpc = 10,
    stmc = 10,
    
    pwr = 20,
    agl = 40,
    dur = 5,

    effect = [[stink_eye, 20]],
    pdbm = [30, 40, 10, 30],
)
```
A spell can add to a stat or reduce it by having a positive or negative value.
Here's all of the stats and their effects:

## name = "Stink eye"
The name that is shown in the interface and tooltip, must be a string.

## inf = "Show them that you're not okay with what they are doing"
A short description of what the spell does, or a long one, must be a string, can be multiple lines using \n

## icon = "spells/skill_example.png"
Optional, must be a string
It's better to keep the icon name the same as the skill name but not necessary.

## hp = -10
Optional, number
A negative value will damage the receiver and a positive value will heal the receiver.

## mp = -5
Optional, number
A negative value will burn the receivers mana and a positive value will give the receiver mana.

## stm = -10
Optional, number
A negative value will charge the receivers stamina and a positive value will give the receiver stamina.

## mpc = 10
Optional, number
Mana cost to cast a spell.

## stmc = 10
Optional, number
Stamina cost for a move.

## pwr = 20
Optional, number, Only for effects
A negative value will lower the power and a positive value will buff the power.

## agl = 40
Optional, number, Only for effects
A negative value will lower the agility and a positive value will buff the agility.

## dur = 5
Optional, number, Only for effects
The duration of effect in seconds.

## effect = [[stink_eye, 20]]
Optional, list
A list of effects applied by this skill plus the chance of each effect being applied.

## pdbm = [30, 40, 10, 30]
Optional, list
The base chance of [parry, dodge, block, miss] for the spell or skill.



And finally, To make them available for translation put the name and description inside a _() like the example below

```python
default no_spell = spell(
    _("Empty"),
    _("Click to add spell"),
    )
```