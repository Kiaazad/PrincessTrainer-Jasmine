image cg cg1 = "cg/found lamp/01.jpg"
image cg cg2 = "cg/found lamp/02.jpg"



image cg harem bath 01 = "cg/harem bath/01.jpg"
image cg harem bath 02 = "cg/harem bath/02.jpg"
image cg harem bath 03 = "cg/harem bath/03.jpg"
image cg harem bath 04 = "cg/harem bath/04.jpg"
image cg harem bath 05 = "cg/harem bath/05.jpg"


init python:
    class cg_obj:
        def __init__(self, name, img, model, target_pleasure = 0, player_pleasure = 0, tick_pleasure = None, type = "item"):
            self.name = name
            self.img = img
            self.model = model
            self.target_pleasure = target_pleasure
            self.player_pleasure = player_pleasure
            self.tick_pleasure = tick_pleasure
            self.x = 0
            self.y = 0
            self.type = type

    class l2dcg:
        def __init__(self, target, clicks = [], model = None):
            self.target = target
            self.clicks = clicks
            self.model = model

            self.hovering = []
            self.active = []
            self.reserved = []
            self.replace(clicks[0])
            self.tick_pleasure = 0
            self.show_bars = True
            self.show_options = False
            self.hover_game = True

        def settings(self, set):
            if set == "bars":
                self.show_bars = not self.show_bars
            if set == "gamify":
                self.hover_game = not self.hover_game
            if set == "side":
                self.show_options = not self.show_options

        def add_hover(self):
            r = renpy.random.choice(self.clicks)
            if not r in self.hovering:
                r.x = renpy.random.randint(-800, 800)
                r.y = renpy.random.randint(-400, 400)
                self.hovering.append(r)

        def clicked(self, click, from_reserved = False):
            self.target.pleasure += click.target_pleasure
            hero.pleasure += click.player_pleasure

            if click in self.active:
                self.active.remove(click)
            else:
                self.active.append(click)
            try:
                if from_reserved:
                    self.reserved.remove(click)
                else:
                    self.hovering.remove(click)
            except:
                pass
        def replace(self, click, from_reserved = False):
            for i in self.active:
                if i.type == click.type:
                    self.active.remove(i)
            self.active.append(click)
            if click.tick_pleasure is not None:
                self.tick_pleasure = click.tick_pleasure
            try:
                if from_reserved:
                    self.reserved.remove(click)
                else:
                    self.hovering.remove(click)
            except:
                pass
        def reserve(self, click):
            try:
                self.hovering.remove(click)
            except:
                pass
            self.reserved.append(click)
        def tick(self):
            self.target.pleasure += self.tick_pleasure
            hero.pleasure += self.tick_pleasure

        def img(self):
            m = None
            if self.model:
                m = self.model
                for i in self.active:
                    m += " "
                    m += i.model
                return m
            else:
                return False



screen cgscr(g):
    modal True
    tag cg
    if g.img():
        add g.img()
    if g.tick_pleasure:
        timer renpy.random.random()+.5 repeat True action Function(g.tick)
    timer renpy.random.randint(4, 10) repeat True action Function(g.add_hover)

    if g.show_bars:
        vbar value hero.pleasure range 1000 left_bar "0GUI/bar2.png" right_bar "0GUI/bar1.png" align(0.0,.5) xysize(63,688) left_gutter 44 right_gutter 44
        vbar value g.target.pleasure range 1000 left_bar "0GUI/bar4.png" right_bar "0GUI/bar3.png" align(1.0,.5) xysize(63,688) left_gutter 44 right_gutter 44
    
    if g.hover_game:
        for i in g.hovering:
            button:
                align .5,.5 xoffset i.x yoffset i.y xysize 150,150 background i.img
                text i.name
                at cg_hover
                if i.type == "item":
                    action Function(g.clicked, i)
                elif i.type == "expression":
                    action Function(g.replace, i)
                elif i.type == "motion":
                    action Function(g.replace, i)
                alternate Function(g.reserve, i)
        hbox:
            align .5,.99 box_wrap True spacing 10 box_wrap_spacing -310 order_reverse True
            for i in g.reserved:
                button:
                    xysize 150,150 background i.img
                    text i.name
                    if i.type == "item":
                        action Function(g.clicked, i, True)
                    elif i.type == "expression":
                        action Function(g.replace, i, True)
                    elif i.type == "motion":
                        action Function(g.replace, i, True)
    
    if g.show_options:
        drag:
            xalign 0.0
            frame:
                at zoom(.6)
                vbox:
                    box_wrap True spacing 10 box_wrap_spacing 10
                    for i in g.clicks:
                        button:
                            xysize 150,150 background i.img
                            text i.name
                            if i.type == "item":
                                action Function(g.clicked, i, True)
                            elif i.type == "expression":
                                action Function(g.replace, i, True)
                            elif i.type == "motion":
                                action Function(g.replace, i, True)

    drag:
        align .9,.1
        frame:
            
            vbox:
                text _("Settings")
                hbox:
                    button:
                        at btn
                        text _("Side bar")
                        action Function(g.settings, "side"), SelectedIf(g.show_options)
                    button:
                        at btn
                        text _("Gamify")
                        action Function(g.settings, "gamify"), SelectedIf(g.hover_game)
                    button:
                        at btn
                        text _("Bars")
                        action Function(g.settings, "bars"), SelectedIf(g.show_bars)


    button:
        align 1.0,1.0 offset -40,-40
        text _("Skip")
        action Hide("cgscr"), Return()

transform cg_hover:
    ease 2 xoffset renpy.random.randint(-40, 40) yoffset renpy.random.randint(-40, 40)
    ease 2 xoffset renpy.random.randint(-40, 40) yoffset renpy.random.randint(-40, 40)
    ease 2 xoffset renpy.random.randint(-40, 40) yoffset renpy.random.randint(-40, 40)
    ease 2 xoffset renpy.random.randint(-40, 40) yoffset renpy.random.randint(-40, 40)
    repeat

