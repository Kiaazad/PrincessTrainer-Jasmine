﻿
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

    def fight_cast(caster, spell, enemy, is_enemy = False):
        global combat_roll
        combat_roll += "\n {} - {}".format(caster.name, spell.name)
        caster.ani = "attack"
        caster.busy = 30
        caster.stm -= spell.stmc
        caster.mp -= spell.mpc

        chance = renpy.random.randint(1,500)
        crit = renpy.random.randint(-30,10)
        total = 0
        for i in ["Parry", "Dodge", "Block", "Miss"]:
            if not i in enemy.cant:
                total += renpy.random.randint(1,100)
                if chance < total:
                    if not is_enemy:
                        msg3(i)
                    else:
                        msg3(i, d = False)
                    break
        else:
            enemy.ani = "hit"
            enemy.busy = 30
            if spell.hp:
                damage = (spell.hp + (caster.pwr * spell.hp)/100) + crit
                enemy.hp += damage
                if not is_enemy:
                    msg3(damage)
                else:
                    msg3(damage, d = False)
            if spell.mp:
                burn = (spell.mp + (caster.pwr * spell.mp)/100) + crit
                enemy.mp += burn
                if enemy.mp < 1:
                    enemy.mp = 0
                    enemy.hp += burn/2
                if not is_enemy:
                    msg3(burn)
                else:
                    msg3(burn, d = False)
            if spell.stm:
                breath = (spell.stm + (caster.pwr * spell.stm)/100) + crit
                enemy.stm += breath
                if enemy.stm < 1:
                    enemy.stm = 0
                    enemy.hp += breath/2
                if not is_enemy:
                    msg3(breath)
                else:
                    msg3(breath, d = False)

        if enemy.hp < 1:
            enemy.hp = 0
            enemy.ani = "dead"
            if enemy.alive:
                enemy.alive = False
                global btl_e_levels
                btl_e_levels += enemy.lvl
                for i in enemy.bags[0].items:
                    if i:
                        btl_loot.append(i)

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
            fight_cast(caster, spell, target, True)


default btl_loot = []
default btl_e_levels = 0
screen btl_scr(f, e, escape_chance = .8):
    modal True

    default caster = f.team[0]
    default spell = None
    default fp = [(-200,-150), (-550,-140),
                    (-350,-40), (-700,-40)]
    default ep = [(200,-150), (550,-140),
                    (350,-40), (700,-40)]

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
        key "K_1" action SetScreenVariable("spell", caster.spells[0])
        key "K_2" action SetScreenVariable("spell", caster.spells[1])
        key "K_3" action SetScreenVariable("spell", caster.spells[2])
        key "K_4" action SetScreenVariable("spell", caster.spells[3])
        key "K_5" action SetScreenVariable("spell", caster.spells[4])
        key "K_6" action SetScreenVariable("spell", caster.spells[5])

        hbox:
            yalign 1.0 spacing 2
            for n, i in enumerate(caster.spells):
                if i:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add i.icon
                        tooltip i
                        action SetScreenVariable("spell", i), SelectedIf(spell== i)
                else:
                    button:
                        padding 0,0 background None
                        at btl_t_b
                        add "spells/empty.png"
                        tooltip i
                        action Show("fight_spell_select", caster = caster, spell = n), SelectedIf(spell== i)

    use stats(f, e)
    hbox:
        align 1.0,1.0 offset -40,-40
        button:
            text "Manage"
            action ToggleScreen("btl_team", t = f)

        # button:
        #     text "Skip"
        #     action Hide("btl_scr"), Return()

    default escape = 0
    default escape_window = 0
    if spell == run_away: # Run away
        timer .1 action SetScreenVariable("escape", renpy.random.randint(1, 10))
        button:
            background None
            action NullAction()
        frame:
            vbox:
                text "Looking for a chance!"
                if escape > 0:
                    timer 1 repeat True action SetScreenVariable("escape", escape - 1)
                    if escape < 2:
                        if escape_window < escape_chance:
                            timer .1 repeat True action SetScreenVariable("escape_window", escape_window + .1)
                            button:
                                text "NOW!"
                                action Return("Ran Away")
                        else:
                            timer.01 action SetScreenVariable("spell", None), SetScreenVariable("escape_window", 0), SetScreenVariable("escape", 0)


    if f.defeated(): # Defeated
        button:
            background None
            action NullAction()
        frame:
            vbox:
                text "You're dead!"
                button:
                    text "Resurrect"
                    action Show("load")
                button:
                    text "Let the darkness take ove."
                    action MainMenu()
    else:
        timer .016 repeat True action Function(f.tick), Function(e.tick)
    if e.defeated(): # Won
        button:
            background None
            action NullAction()
        if len(btl_loot) or btl_e_levels:
            frame:
                vbox:
                    text "You won this fight!"
                    text "Gained {} Exp.".format(calculate_exp(f))
                    if len(btl_loot):
                        text "And"
                        hbox:
                            for i in btl_loot:
                                button:
                                    xysize 128,128 padding 0,0
                                    background i.item.icon
                                    if i.qtt > 1:
                                        text "[i.qtt]" color "#fff" align(.9,.9)
                                    tooltip i
                                    action NullAction()
                    button:
                        text "Collect"
                        action Function(collect_loot, calculate_exp(f)), Return("won")
        else:
            button:
                background None
                action NullAction()
            frame:
                vbox:
                    text "It's already dead!"
                    button:
                        text "Close"
                        action Return("won")
    else:
        timer renpy.random.random()*4 repeat True action Function(fight_ai, f, e)




init python:
    def collect_loot(exp):
        global btl_loot, btl_e_levels
        for i in btl_loot:
            hero.got(i.item, i.qtt)
        btl_loot = []
        btl_e_levels = 0
        hero.got_exp(exp)

    def calculate_exp(f):
        global btl_e_levels
        if btl_e_levels:
            f_levels = 0
            for i in f.team:
                f_levels += i.lvl
            exp = 5 - (f_levels - btl_e_levels)
            if exp < 1:
                exp = 1
            return exp
        else:
            return 0
