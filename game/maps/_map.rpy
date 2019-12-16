init python:
    class place:
        def __init__(self, name, xy, act, icon = None):
            self.name = name
            self.xy = xy
            self.act = act
            self.icon = icon
    class maps:
        def __init__(self, name, p = []):
            self.name = name
            self.p = p # places
        def discover(self, x):
            self.p.append(x)
            msg.msg("Discovered {}".format(x.name))

screen map(m):
    modal True
    tag place
    frame:
        align 1.0,0.0 margin 100,100
        text m.name
    for i in m.p:
        button:
            pos i.xy
            text i.name
            action Hide("map"), i.act
