init python:
    def itemswap(s,c):
        if s.sum > c.sum:
            diff = s.sum - c.sum
            if c.cash < diff:
                msg.msg("You don't have enough cash.")
            else:
                itemswap_f(s,c)
                c.cash -= diff
                s.cash += diff
        elif s.sum < c.sum:
            diff = c.sum - s.sum
            if s.cash < diff:
                msg.msg("The shop keeper is shop on money.")
            else:
                itemswap_f(s,c)
                s.cash -= diff
                c.cash += diff
        else:
            itemswap_f(s,c)
    def itemswap_f(s,c):
        s.items += c.togos
        c.items += s.togos
        del s.togos[:]
        del c.togos[:]
        s.sumit()
        c.sumit()


screen shop(s, c):
    modal True

    button:
        text "Return"
        action Hide("shop"), Return()
    use shop_list(c, 0.0) 
    use shop_list(s, 1.0)
        
screen shop_list(u,xa):
    default sb = u.bags[0]

    hbox:
        spacing 50 align xa,0.2
        text "[u.name]"
        for i in u.bags:
            button:
                text i.name
                action SetScreenVariable("sb", i)
        hbox:
            add "items/_coin.png"
            text "[u.cash]"
    if sb:
        frame:
            ysize 740 align xa,1.0
            vbox:
                spacing 10 box_wrap True box_wrap_spacing 10
                for ii,i in enumerate(sb.items):
                    if i == None:
                        button:
                            xysize 128,128 padding 0,0
                            # action Function(s.pick, ii, abdul)
                    else:
                        button:
                            xysize 128,128 padding 0,0
                            background i.item.icon
                            text "[i.qtt]" color "#fff" align(.9,.9)
                            tooltip i
                            # if mode == "stack":
                            #     action Function(c.pick, ii, s)
                            # elif mode == "single":
                            #     action Function(c.pickOne, ii, s)




