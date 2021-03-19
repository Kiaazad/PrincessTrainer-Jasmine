image cg cg1 = "cg/found lamp/01.jpg"
image cg cg2 = "cg/found lamp/02.jpg"



image cg harem bath 01 = "cg/harem bath/01.jpg"
image cg harem bath 02 = "cg/harem bath/02.jpg"
image cg harem bath 03 = "cg/harem bath/03.jpg"
image cg harem bath 04 = "cg/harem bath/04.jpg"
image cg harem bath 05 = "cg/harem bath/05.jpg"


init python:
    class lcg:
        def __init__(self, clicks = [], model = None):
            self.clicks = clicks
            self.model = model

        def clicked(self, click):
            pass
        def img(self):
            m = None
            if self.model:
                m = self.model + " idle"
                for i in self.clicks:
                    if i.enabled:
                        m += " "
                        m += i.model
                return m
            else:
                return False

screen cgscr(g):
    tag cg
    if g.img():
        add g.img()
    drag:
        align .0,.5
        frame:
            for i in g.clicks:
                if i.enabled:
                    button:
                        text i.name
                        action Function(g.clicked, i)

