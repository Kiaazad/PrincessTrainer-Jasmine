


init python:
    def spell_cast(caster, spell, enemy):
        if caster.alive:
            if spell.mpc:
                if caster.mp >= spell.mpc:
                    pass
                else:
                    msg.msg("Not enough Mana.")
                    return
            if spell.stmc:
                if caster.stm >= spell.stmc:
                    pass
                else:
                    msg.msg("Not enough Stamina.")
                    return
            fight_cast(caster, spell, enemy)
        else:
            msg.msg("You're dead.")

    def fight_cast(caster, spell, enemy):
        caster.ani = "attack"
        caster.busy = 30
        caster.stm -= spell.stmc
        caster.mp -= spell.mpc

        chance = renpy.random.randint(1,100)
        crit = renpy.random.randint(-30,10)
        pdbm = renpy.random.randint(0, 3)

        if chance > spell.pdbm[pdbm] + int((float(enemy.agl) / (float(enemy.agl) + float(100))) * 100)/2:
            enemy.ani = "hit"
            enemy.busy = 30
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
            enemy.alive = False
            enemy.hp = 0
            enemy.ani = "dead"

    def fight_ai(f, e):
        caster = None
        spell = None
        target = None
        for i in f.team:
            if i.alive:
                target = i
                break
        else:
            return
        for i in e.team:
            if i.alive:
                caster = i
                break
        else:
            return
        for i in caster.spells:
            if i:
                if caster.mp >= i.mpc and caster.stm >= i.stmc:
                    spell = i
                    break
        else:
            return

        
        if caster and spell and target:

            fight_cast(caster, spell, target)


screen btl_scr(f, e):
    modal True
    default caster = None
    default spell = None
    default fp = [(-200,-150), (-550,-140),
                    (-350,-40), (-700,-40)]
    default ep = [(200,-150), (550,-140),
                    (350,-40), (700,-40)]
    # ticker
    if f.defeated():
        timer 1 action Show("fight_result", r="lose")
    else:
        timer .016 repeat True action Function(f.tick), Function(e.tick)
    if e.defeated():
        timer 1 action Show("fight_result", r="win")
    else:
        timer renpy.random.random()*4 repeat True action Function(fight_ai, f, e)

    vbar value f.team[0].hp range f.team[0].mhp left_bar "0GUI/bar2.png" right_bar "0GUI/bar1.png" align(0.0,.5) xysize(63,688) left_gutter 44 right_gutter 44
    vbar value e.team[0].hp range e.team[0].mhp left_bar "0GUI/bar4.png" right_bar "0GUI/bar3.png" align(1.0,.5) xysize(63,688) left_gutter 44 right_gutter 44

    for ii, i in enumerate(f.team): # Friendly team
        vbox:
            yalign 1.0 offset fp[ii]
            bar value i.hp range i.mhp xysize(100,10) left_bar "#900" right_bar "#9005"
            # bar value i.mp range i.mmp xysize(100,10) left_bar "#fff" right_bar "#fff5"
            button:
                background None focus_mask True
                add "{} fight {}".format(i.name, i.ani) at flp
                action SetScreenVariable("caster", i)
    for ii, i in enumerate(e.team): # Enemy team
        vbox:
            yalign 1.0 offset ep[ii]
            bar value i.hp range i.mhp xysize(100,10) left_bar "#900" right_bar "#9005"
            # bar value i.mp range i.mmp xysize(100,10) left_bar "#fff" right_bar "#fff5"
            button:
                background None focus_mask True
                add "{} fight {}".format(i.name, i.ani)
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

screen fight_result(r):
    modal True
    if r == "win":
        frame:
            vbox:
                text "You won this fight!"
                button:
                    text "Done"
                    action Hide("btl_scr"), Hide("fight_result"), Return()
    if r == "lose":
        frame:
            vbox:
                text "You're dead!"
                button:
                    text "Resurrect"
                    action Show("load")


