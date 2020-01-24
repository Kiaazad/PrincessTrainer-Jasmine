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
            pos i.xy anchor 0.0,0.0
            if i.icon:
                padding 0,0 background None
                add i.icon 
            else:
                text i.name
            action Hide("map"), i.act
            at map_transform
            focus_mask True

transform map_transform:
    on idle:
        ease .2 additive 0.0
    on hover:
        ease .2 additive 0.5