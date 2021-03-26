define config.gl2 = True
init python:
    class pncc:
        def __init__(self,
            name, img, pos,
            jump = None,
            model = None,
            enabled = True,
            items = [],
            regen = 0,
            tools = [],
            hits = 1
        ):
            self.name = name
            self.img = img
            self.pos = pos
            self.jump = jump
            self.model = model

            self.items = items
            self.regen = regen
            self.enabled = enabled
            self.tools = tools
            self.hits = hits

    class pnch():
        def __init__(self, name, clicks = [], model = None):
            self.name = name
            self.clicks = clicks
            self.model = model

            self.idle = 0
        def clicked(self, click):
            if click.jump:
                renpy.jump(click.jump)
            else:
                if click.tools and not hero.has(click.tools):
                    msg.msg("You don't have the right tools ({}) for this.".format(' or '.join(i.name for i in click.tools)))
                else:
                    if click.hits > 1:
                        click.hits -= 1
                        msg3("{}".format(click.hits))
                    else:
                        if click.items:
                            for i in click.items:
                                if isinstance(i, (int, long)):
                                    hero.gotcash(i)
                                else:
                                    hero.got(i[0], i[1])
                        click.enabled = False

        def add(self, click, cond = None):
            self.clicks.append(click)
            if cond:
                self.cond.append(cond)
        def img(self):
            m = None
            if self.model:
                m = self.model + " idle"
                for i in self.clicks:
                    if i.enabled and i.model:
                        m += " "
                        m += i.model
                return m
            else:
                return False

init python:
    def i_love_you_parasite(model, st):
        day_time = calendar.minute*0.71111+200
        if day_time >= 256:
            day_time -= 256
        model.blend_parameter("day_time", "Add", day_time)
        return 0
    

screen pnc2(g):
    layer "map"
    tag place
    if g.img():
        add g.img()
    for i in g.clicks:
        if i.enabled:
            button:
                at pnc_t
                anchor 0.0,0.0 
                pos i.pos
                background None padding 0,0
                add i.img
                focus_mask True
                action Function(g.clicked, i)

    use clock

transform pnc_t():
    on idle:
        ease .2 alpha 0
    on hover:
        ease .2 alpha 1
transform alpha(a):
    alpha a
transform rotate(r):
    rotate r
transform zoom(z):
    zoom z
