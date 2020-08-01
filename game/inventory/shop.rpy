init python:
    # def itemswap(s,c):
    #     if s.sum > c.sum:
    #         diff = s.sum - c.sum
    #         if c.cash < diff:
    #             msg.msg("You don't have enough cash.")
    #         else:
    #             itemswap_f(s,c)
    #             c.cash -= diff
    #             s.cash += diff
    #     elif s.sum < c.sum:
    #         diff = c.sum - s.sum
    #         if s.cash < diff:
    #             msg.msg("The shop keeper is short on money.")
    #         else:
    #             itemswap_f(s,c)
    #             s.cash -= diff
    #             c.cash += diff
    #     else:
    #         itemswap_f(s,c)
    # def itemswap_f(s,c):
    #     s.togos, c.togos = c.togos, s.togos
    # def itemswap_exit(s, c):
    #     s.togos_collect()
    #     c.togos_collect()
    def buy_one(item, s, c):
        if c.cash < item.item.val*s.markup:
            msg.msg("You don't have enough cash.")
        else:
            c.cash -= int(item.item.val*s.markup)
            s.cash += int(item.item.val*s.markup)
            c.bags[0].add(item.item, 1)
            s.bags[0].rem(item.item, 1)
        

screen shop(s, c):
    modal True
    default mode = "single"
    default selling = True
    button:
        yalign 1.0
        text "Leave"
        action Hide("shop"), Return()
    frame:
        xsize 512+16 padding 0,0 background None
        vbox:
            frame:
                hbox:
                    if selling:
                        text "Buy from {}".format(s.name)
                        button:
                            text "Switch to Sell"
                            action SetScreenVariable("selling", False)
                    else:
                        text "Sell to {}".format(s.name)
                        button:
                            text "Switch to Buy"
                            action SetScreenVariable("selling", True)

            if selling:
                use shop_list_1(s = s, c = c)
            else:
                use shop_list_1(s = c, c = s)

screen shop_list_1(s, c):
    default mode = "single"
    hbox:
        spacing 4 box_wrap True box_wrap_spacing 4
        for ii,i in enumerate(s.bags[0].items):
            if i == None:
                button:
                    xysize 128,128 padding 0,0
            else:
                button:
                    xysize 128,128 padding 0,0
                    background i.item.icon
                    if i.qtt > 1:
                        text "[i.qtt]" color "#fff" align(.9,.9)
                    tooltip i
                    if mode == "stack":
                        action Function(buy_one, i, s, c)
                    elif mode == "single":
                        action Function(buy_one, i, s, c)
    frame:
        hbox:
            text "Cash: {}".format(c.cash)
            add "inventory/coin.png"
            button:
                text "Stacks"



# screen shop_old(s, c):
#     modal True
#     button:
#         yalign 1.0
#         text "Leave"
#         action Hide("shop"), Return()

#     vbox:
#         hbox:
#             text "Buying:  {}".format(s.sumit())
#             add "inventory/coin.png"
#         hbox:
#             text "selling:  {}".format(c.sumit())
#             add "inventory/coin.png"
#         if s.sum < c.sum:
#             hbox:
#                 text "Getting:  {}".format(c.sum-s.sum)
#                 add "inventory/coin.png"
#         else:
#             hbox:
#                 text "Paying:  {}".format(s.sum-c.sum)
#                 add "inventory/coin.png"
#         button:
#             text "Finish the deal"
#             action Function(itemswap, s, c)
#         button:
#             text "Collect"
#             action Function(itemswap_exit, s, c)
    
#     use shop_list(c, 0.0) 
#     use shop_list(s, 1.0)
        
# screen shop_list(u,xa):
#     default sb = u.bags[0]
#     default mode = "single"
#     frame:
#         xsize 500 background None
#         vbox:
#             spacing 4 box_wrap True box_wrap_spacing 4 xalign xa
#             for ii,i in enumerate(u.togos.items):
#                 if i == None:
#                     button:
#                         xysize 128,128 padding 0,0
#                         action Function(u.togos.pick, ii, u)
#                 else:
#                     button:
#                         xysize 128,128 padding 0,0
#                         background i.item.icon
#                         if i.qtt > 1:
#                             text "[i.qtt]" color "#fff" align(.9,.9)
#                         tooltip i
#                         if mode == "stack":
#                             action Function(u.togos.pick, ii, u)
#                         elif mode == "single":
#                             action Function(u.togos.pickOne, ii, u)

#     drag:
#         align xa,1.0
#         frame:
#             padding 0,0 xsize 660
#             vbox:
#                 hbox:
#                     text "[u.name]"
#                     for i in u.bags:
#                         button:
#                             text i.name
#                             action SetLocalVariable("sb", i)
#                     hbox:
#                         text "[u.cash]"
#                         add "inventory/coin.png"
                        
#                 if sb:

#                     hbox:
#                         spacing 4 box_wrap True box_wrap_spacing 4
#                         for ii,i in enumerate(sb.items):
#                             if i == None:
#                                 button:
#                                     xysize 128,128 padding 0,0
#                                     action Function(sb.pick, ii, u)
#                             else:
#                                 button:
#                                     xysize 128,128 padding 0,0
#                                     background i.item.icon
#                                     if i.qtt > 1:
#                                         text "[i.qtt]" color "#fff" align(.9,.9)
#                                     tooltip i
#                                     if mode == "stack":
#                                         action Function(sb.pick, ii, u)
#                                     elif mode == "single":
#                                         action Function(sb.pickOne, ii, u)

#     default mouse = (0,0)
#     if u.holding:
#         timer 0.02 repeat True action SetLocalVariable("mouse", renpy.get_mouse_pos())
#         fixed:
#             xysize 128,128
#             pos mouse
#             at holding_item_anim
#             add u.holding.item.icon
#             if u.holding.qtt > 1:
#                 text "[u.holding.qtt]" color "#fff" align(.9,.9)


