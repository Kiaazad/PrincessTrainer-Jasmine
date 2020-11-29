﻿init python:
    class pnco:
        def __init__(self,
            name, img, pos,
            act = None, enabled = True, 
            hits = 1, items = [], tools = [],
            tut = False, hidden = True, hoffset = (0,0)
        ):
            self.name = name
            self.img = img
            self.pos = pos
            self.act = act
            self.enabled = enabled
            self.hits = hits
            self.items = items
            self.tools = tools
            self.tut = tut
            self.hov = 0
            self.hidden = hidden
            self.hoffset = hoffset
        def hovered(self, h):
            if not self.hidden:
                self.hov = h

    class pncs:
        def __init__(self, name, clicks = [],
            cond = []):
            self.name = name
            self.clicks = clicks
            self.cond = cond
            self.tuts = []
            self.idle = 0
        def clicked(self, o, p):
            self.idle = 0
            if o.items:
                if o.tools and not p.has(o.tools):
                    msg.msg("You don't have the right tools ({}) for this.".format(' or '.join(i.name for i in o.tools)))
                else:
                    if o.hits > 1:
                        o.hits -= 1
                        msg3("{}".format(o.hits))
                    else:
                        if o.items:
                            for i in o.items:
                                if isinstance(i, (int, long)):
                                    p.gotcash(i)
                                else:
                                    p.got(i[0], i[1])
                            self.clicks.remove(o)
            self.cond_check()
        def cond_check(self):
            for i in self.cond:
                for ii in i[0]:
                    if ii in self.clicks:
                        break
                else:
                    renpy.show_screen("do_it", i[1])
                    self.cond.remove(i)
        def add(self, click, cond = None):
            self.clicks.append(click)
            if cond:
                self.cond.append(cond)
        def act_done(self):
            self.act = None
        def idle_tick(self):
            self.idle += 1
            if self.idle > 10:
                for i in self.clicks:
                    if i.tut:
                        self.tuts.append(i.pos)
                renpy.show_screen("tut", self)
                self.idle = 0
        def tut_show(self):
            p = self.tuts.pop()
            renpy.show_screen("tut_click", p)
        def on_show(self):
            for i in self.clicks:
                i.hov = 0

screen pnc(p , g):
    default hov = None
    tag place
    layer "map"
    timer 1 repeat True action Function(g.idle_tick)

    for i in g.clicks:
        if isinstance(i, basestring):
            add i
        else:
            button:
                anchor 0.0,0.0 
                pos i.pos
                if i.img:
                    background None padding 0,0
                    add i.img
                else:
                    text i.name
                if i.enabled:
                    if i.act:
                        focus_mask True
                        at map_transform
                        action Function(g.clicked, i, p), Function(g.on_show), i.act
                        hovered Function(i.hovered, 1)
                        unhovered Function(i.hovered, 0)
                    else:
                        action Function(g.clicked, i, p)
        if not i.hidden:
            frame:
                at pnc_hover(i.hov)
                anchor .5,0.0 pos i.pos offset i.hoffset
                background Frame("0GUI/scroll.png", 20, 0)
                text i.name color "#000"
    vbox:
        align 1.0,0.0 offset -100,100
        frame:
            text g.name
        if hov:
            text hov

transform pnc_hover(a):
    ease .2 alpha a yoffset (a-1)*20
