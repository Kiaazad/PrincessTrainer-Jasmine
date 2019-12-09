init python:
    class place:
        def __init__(self, name, xy, act):
            self.name = name
            self.xy = xy
            self.act = act
    class maps:
        def __init__(self, name,bg, p = []):
            self.name = name
            self.p = p # places
            self.bg = bg
        def discover(self, x):
            self.p.append(x)
            msg.msg("Discovered {}".format(x.name))

default palace_loc = place("Palace", (0.679, 0.349), Jump('palace'))
default bazaar_loc = place("Bazaar", (0.816, 0.467), Jump('bazaar'))
default street_loc = place("The street", (0.623, 0.574), Jump('street'))

default desert_loc = place("Desert", (0.190, 0.725), Jump('desert'))



default agrabah = maps("Agrabah", "bg/03.jpg", [palace_loc, bazaar_loc, street_loc])
default agrabah_st = maps("The street", "bg/02.jpg", [desert_loc, bazaar_loc, street_loc])

screen map(t = agrabah):
    modal True
    tag place
    add t.bg
    # frame:
    #     align 1.0,0.0 margin 100,100
    #     text t.name
    for i in t.p:
        button:
            align i.xy
            text i.name
            action Hide("map"), i.act

