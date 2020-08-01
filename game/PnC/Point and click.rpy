init python:
    class pnco:
        def __init__(self,
            name, img, pos,
            act = None, enabled = True, 
            hits = 1, items = [], tools = [],
            tut = False,
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
screen pnc(p , g):
    # modal True
    # layer "screens"
    zorder -100
    timer 1 repeat True action Function(g.idle_tick)

    for i in g.clicks:
        button:
            background None anchor 0.0,0.0 padding 0,0
            pos i.pos
            add i.img
            if i.enabled:
                if i.act:
                    action Function(g.clicked, i, p), i.act
                else:
                    action Function(g.clicked, i, p)

