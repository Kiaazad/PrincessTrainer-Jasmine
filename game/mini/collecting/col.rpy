init python:
    class col_obj:
        def __init__(self, img, pos, hits = 1, items = [], act = None, tools = []):
            self.img = img
            self.pos = pos
            self.hits = hits
            self.items = items
            self.act = act
            self.tools = tools

    class col_game:
        def __init__(self, name, lst = [], bg = None):
            self.name = name
            self.lst = lst
            self.bg = bg
            self.act = None

        def clicked(self, o, p):
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
                            self.lst.remove(o)
            # if o.act:
            #     self.act = o.act
        def act_done(self):
            self.act = None


screen collect(p , g, c = False, e = True):
    modal True
    if g.act:
        timer .01 action g.act, Function(act_done)

    if g.bg:
        add g.bg
    for i in g.lst:
        button:
            background None anchor 0.0,0.0 padding 0,0
            pos i.pos
            add i.img
            action Function(g.clicked, i, p)
    if e:
        button:
            align 0.0,0.0 offset 50,44
            text "Go back"
            action Hide("collect"), Jump("desert")

    if not len(g.lst) and c:
        timer .1 action Hide("collect"), Return()