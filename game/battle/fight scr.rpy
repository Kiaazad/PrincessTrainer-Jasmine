        

label fight_test:
    scene image "#333"
    show image "bg/fight.png"
    window hide
    show screen btl_scr(me_team, en_team)
    pause
    return

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
                add "{}/fight/{}.png".format(i.dir, i.ani) at flp
                action SetScreenVariable("caster", i)
    for ii, i in enumerate(e.team): # Enemy team
        vbox:
            yalign 1.0 offset ep[ii]
            bar value i.hp range i.mhp xysize(100,10) left_bar "#900" right_bar "#9005"
            bar value i.mp range i.mmp xysize(100,10) left_bar "#fff" right_bar "#fff5"
            button:
                background None focus_mask True
                add "{}/fight/{}.png".format(i.dir, i.ani)
                if caster is not None and spell is not None:
                    action Function(i.spell_check, caster, spell)

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


    button:
        align 0.0,0.0 margin 200,200
        text "Manage"
        action ToggleScreen("btl_team", t = f)

    use stats(f, e)
    # if caster:
    #     use fine_tune(caster)

