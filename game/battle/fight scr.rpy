image abdul fight idle:
    "char/abdul/fight/idle.png"
    pause .1
    "char/abdul/fight/idle_2.png"
    pause .1
    "char/abdul/fight/idle_3.png"
    pause .1
    "char/abdul/fight/idle_2.png"
    pause .1
    repeat
image abdul fight attack:
    "char/abdul/fight/attack.png"
    pause .1
    xpos 100
    pause .1
    xoffset 0


image warrior_man fight idle:
    "char/warrior_man/fight/idle.png"
    pause .1
    "char/warrior_man/fight/idle_2.png"
    pause .1
    "char/warrior_man/fight/idle_3.png"
    pause .1
    "char/warrior_man/fight/idle_2.png"
    pause .1
    repeat
image warrior_man fight hit:
    "char/warrior_man/fight/hit.png"


init python:
    def spell_cast(caster, spell, enemy):
        # if spell.hpc:
        #     caster.hp += spell.hpc
        #     self.spell_calc(caster, spell)
        if spell.mpc:
            if caster.mp >= spell.mpc:
                caster.mp -= spell.mpc
                fight_cast(caster, spell, enemy)
            else:
                msg.msg("Not enough Mana.")
        if spell.stmc:
            if caster.stm >= spell.stmc:
                caster.stm -= spell.stmc
                fight_cast(caster, spell, enemy)
            else:
                msg.msg("Not enough Stamina.")

    def fight_cast(caster, spell, enemy):
        caster.ani = "attack"

        chance = renpy.random.randint(1,100)
        crit = renpy.random.randint(-30,10)
        pdbm = renpy.random.randint(0, 3)

        if chance > spell.pdbm[pdbm] + int((float(enemy.agl) / (float(enemy.agl) + float(100))) * 100)/2:
            enemy.ani = "hit"
            if spell.hp:
                damage = (spell.hp + (caster.pwr * spell.hp)/100) + crit
                enemy.hp += damage
                msg3(damage)
            if spell.mp:
                burn = (spell.mp + (caster.pwr * spell.mp)/100) + crit
                enemy.mp += burn
                msg3(burn)
            if spell.stm:
                breath = (spell.stm + (caster.pwr * spell.stm)/100) + crit
                enemy.stm += breath
                msg3(breath)
        else:
            msg3("{}".format(["Parry", "Dodge", "Block", "Miss"][pdbm]))
        if enemy.hp < 0:
            enemy.hp = 0
            enemy.ani = "dead"



screen btl_scr(f, e):
    modal True
    default caster = None
    default spell = None
    default fp = [(-200,-150), (-550,-140),
                    (-350,-40), (-700,-40)]
    default ep = [(200,-150), (550,-140),
                    (350,-40), (700,-40)]
    # ticker
    timer 1 repeat True action Function(f.tick), Function(e.tick)

    vbar value f.team[0].hp range f.team[0].mhp left_bar "0GUI/bar2.png" right_bar "0GUI/bar1.png" align(0.0,.5) xysize(63,688) left_gutter 44 right_gutter 44
    vbar value e.team[0].hp range e.team[0].mhp left_bar "0GUI/bar4.png" right_bar "0GUI/bar3.png" align(1.0,.5) xysize(63,688) left_gutter 44 right_gutter 44

    for ii, i in enumerate(f.team): # Friendly team
        vbox:
            yalign 1.0 offset fp[ii]
            bar value i.hp range i.mhp xysize(100,10) left_bar "#900" right_bar "#9005"
            bar value i.mp range i.mmp xysize(100,10) left_bar "#fff" right_bar "#fff5"
            button:
                background None focus_mask True
                add "abdul fight {}".format(i.ani) at flp
                action SetScreenVariable("caster", i)
    for ii, i in enumerate(e.team): # Enemy team
        vbox:
            yalign 1.0 offset ep[ii]
            bar value i.hp range i.mhp xysize(100,10) left_bar "#900" right_bar "#9005"
            bar value i.mp range i.mmp xysize(100,10) left_bar "#fff" right_bar "#fff5"
            button:
                background None focus_mask True
                add "warrior_man fight {}".format(i.ani)
                if caster is not None and spell is not None:
                    action Function(spell_cast, caster, spell, i)

    if caster: # Selected caster
        add "battle/spells.png" yalign 1.0
        hbox:
            yalign 1.0 spacing 2
            for i in caster.spells:
                if i:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add i.icon
                        tooltip i
                        action SetScreenVariable("spell", i)
                else:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add "spells/empty.png"
                        tooltip i
                        action SetScreenVariable("spell", i)

    hbox:
        align 0.0,0.0 offset 200,200
        button:
            text "Manage"
            action ToggleScreen("btl_team", t = f)

        button:
            text "Skip"
            action Hide("btl_scr"), Return()
    use stats(f, e)
    # if caster:
    #     use fine_tune(caster)

