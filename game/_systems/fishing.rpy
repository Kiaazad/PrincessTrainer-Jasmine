

init python:
    class fishing_class:
        def __init__(self, capacity, population, variety):
            self.capacity = capacity
            self.population = population
            self.variety = variety
            self.y = 0
            self.time = 0
            self.is_fishing = 0
        def y_reset(self):
            self.y = 0
        def regen(self):
            if self.population < self.capacity:
                r = renpy.random.randint(0, 100)
                if r < (float(self.population)/self.capacity)*100:
                    self.population += self.population/10
        def fish(self):
            if self.time:
                if self.time < .5:
                    fish = renpy.random.choice(self.variety)
                    hero.got(fish, 1)
                    self.population -= 1
                    self.time = 0
                    self.is_fishing = 0

                    f = renpy.random.randint(0,100)
                    if f < 10 and hero.fishing_skill < 1.0:
                        hero.fishing_skill += 0.01
                        msg.msg("You've got a little more skilled in fishing.")
                else:
                    self.is_fishing = 0
                    msg.msg("No fish on the hook!")
                    self.time = 0
        def cast(self):
            r = (1 + renpy.random.random()) - (float(self.population)/self.capacity)
            self.time = round(r * 4, 2)
            self.is_fishing = 1
            renpy.play("_systems/fishing/drop.ogg", "sound")
        def tick(self):
            self.time -= 0.01
            if self.time < hero.fishing_skill and not self.y:
                renpy.play("_systems/fishing/splash.ogg", "sound")
                self.y = 40
            if self.time < 0:
                self.time = 0
                self.is_fishing = 0
                msg.msg("The fish got away!")



screen fishing(p):
    modal True
    # vbox:
    #     align .2,.2
    #     text str(p.time)
    #     text str(hero.fishing_skill)
    #     text str(p.population)
    vbox:
        spacing -180
        button:
            background None
            add "_systems/fishing/bob.png" at fishing_caught(p.y)
            action Function(p.fish)
            at fishing_bob(p.is_fishing)
        add "_systems/fishing/water.png"
    if not p.is_fishing:
        button:
            text _("Cast")
            action Function(p.cast)
    if p.time > 0:
        timer .01 repeat True action Function(p.tick)
    if p.y:
        timer hero.fishing_skill+.5 repeat True action Function(p.y_reset)
    button:
        align 1.0,1.0 offset -20,-20
        text _("Done")
        action Return()
transform fishing_bob(a):
    parallel:
        ease .4 alpha a
    parallel:
        ease .5 yoffset 20
        ease .5 yoffset 0
        repeat
transform fishing_caught(y):
    ease .2 yoffset y