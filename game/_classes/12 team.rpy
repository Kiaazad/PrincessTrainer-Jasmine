init python:
    class team: # ----------------- Team class
        def __init__(self, team = []):
            self.army = []
            self.team = team
            self.caster = None
            self.size = 4

        def join(self, x):
            if x not in self.army:
                self.army.append(x)
                msg.msg("{} joined your army.".format(x.name))
        def leave(self, x):
            if x in self.army:
                self.army.remove(x)
                msg.msg("{} left your army.".format(x.name))
        
        def add(self, x):
            if x in self.team:
                msg.msg("{} is already in your team.".format(x.name))
            else:
                if len(self.team) < self.size:
                    self.team.append(x)
                else:
                    msg.msg("Your team is full.")
        def rem(self, x):
            self.team.remove(x)


        def order(self, x):
            if self.caster is None:
                self.caster = x
            else:
                self.team[self.caster], self.team[x] = self.team[x], self.team[self.caster]
                self.caster = None
        def cancel(self):
            self.caster = None

        def tick(self):
            for i in self.team:
                if i.alive:
                    i.tick()
        def defeated(self):
            for i in self.team:
                if i.alive:
                    return False
            else:
                return True