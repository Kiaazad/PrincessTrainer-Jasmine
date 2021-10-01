init python:
    def pts_calc(self):
        self.pts = int((float(self.lvl) / (float(self.lvl) + float(20)))*1000) + self.lvl

    def arc_calc(self):
        while self.pts:
            c = renpy.random.randint(1,100)
            if c < arcDic[self.type][0][0]:
                self.mhp += 10
            elif c < arcDic[self.type][0][1]:
                self.mmp += 4
            elif c < arcDic[self.type][0][2]:
                self.mstm += 4
            elif c < arcDic[self.type][0][3]:
                self.pwr += 1
            elif c < arcDic[self.type][0][4]:
                self.agl += 1
            self.pts -= 1
            self.used_pts += 1
        for i in range(self.lvl):
            s = renpy.random.choice(arcDic[self.type][1])
            if s not in self.skills:
                self.skills.append(s)
        for ii, i in enumerate(self.skills):
            if self.spells[ii] is None:
                self.spells[ii] = i

    class fight:
        def __init__(self, lvl, type, cant):
            self.lvl = lvl
            self.type = type
            self.cant = cant

            self.pts = 0
            self.used_pts = 0

            self.mhp = 10
            self.mmp = 10
            self.mstm = 10
            self.pwr = 1
            self.agl = 1

            self.spells = [None, None, None, None, None, None]
            self.skills = []

            pts_calc(self)
            arc_calc(self)

            self.hp = self.mhp
            self.mp = self.mmp
            self.stm = self.mstm

            self.exp = 0
            self.buffs = []
            self.alive = True

            self.ani = "idle"
            self.busy = 0
            self.elapsed = 0
        def reset(self):
            self.hp = self.mhp
            self.mp = self.mmp
            self.stm = self.mstm
            self.ani = "idle"
            self.busy = 0
            self.elapsed = 0
            self.buffs = []
            self.alive = True

        def tick(self):
            self.elapsed += 1
            if self.elapsed == 60:
                self.regen()
                self.elapsed = 0
            if self.busy > 1:
                self.busy -= 1
            else:
                self.ani = "idle"

        def regen(self, rest = False):
            if self.mp < self.mmp:
                self.mp += int(self.mmp/50)+1
                if self.mp > self.mmp:
                    self.mp = self.mmp
            if self.stm < self.mstm:
                self.stm += int(self.mstm/50)+1
                if self.stm > self.mstm:
                    self.stm = self.mstm
            if self.hp < self.mhp and rest:
                self.hp += int(self.mhp/300)+1
                if self.hp > self.mhp:
                    self.hp = self.mhp
        def got_skill(self, x):
            if x not in self.skills:
                self.skills.append(x)
        def spellorder(self, x):
            if self.slc_skill is None:
                self.slc_skill = x
            else:
                self.spells[self.slc_skill], self.spells[x] = self.spells[x], self.spells[self.slc_skill]
                self.slc_skill = None

        def spellput(self, x, p):
            self.spells[p] = x


        def levelup(self, amount):
            self.lvl += amount
            msg.msg("{} gained a level.".format(self.name))
            pts_calc(self)

        
        def got_exp(self, amount):
            self.exp += amount
            if self.exp > 100:
                self.exp -= 100
                self.levelup(1)
                
        def buff(self):
            pass


