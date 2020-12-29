init python:
    class pnco:
        def __init__(self,
            name, img, pos,
            act = [], enabled = True, 
            hits = 1, items = [], tools = [],
            tut = False, hidden = True, hoffset = (0,0), highlight = False
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
            self.highlight = highlight
        def hovered(self, h):
            if not self.hidden:
                self.hov = h

    class pncs:
        def __init__(self, name, clicks = [],
            cond = []):
            self.name = name
            self.clicks = clicks
            self.cond = cond
            self.command = None
            self.tuts = []
            self.idle = 0
        def clicked(self, click, p):
            self.idle = 0
            if click.items:
                if click.tools and not p.has(click.tools):
                    msg.msg("You don't have the right tools ({}) for this.".format(' or '.join(i.name for i in click.tools)))
                else:
                    if click.hits > 1:
                        click.hits -= 1
                        msg3("{}".format(click.hits))
                    else:
                        if click.items:
                            for i in click.items:
                                if isinstance(i, (int, long)):
                                    p.gotcash(i)
                                else:
                                    p.got(i[0], i[1])
                            self.clicks.remove(click)
                            self.cond_check(click)
        def cond_check(self, click):
            for i in self.cond:
                if click in i[0]:
                    i[0].remove(click)
                    if len(i[0]) == 1 :
                        self.command = i
                        self.cond.remove(i)

        def add(self, click, cond = None):
            self.clicks.append(click)
            if cond:
                self.cond.append(cond)

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

    # text str(g.command) size 50 yoffset 50
    # if len(g.cond):
    #     text str(len(g.cond[0][0])) size 50 xoffset 150

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
                        if g.command and g.command[0][0] == i:
                            action Function(g.clicked, i, p), g.command[1]
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
