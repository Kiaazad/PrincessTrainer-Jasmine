init python:
    class fight:
        def __init__(self, lvl, type):
            self.lvl = lvl
            self.type = type

            self.pts = 0
            self.used_pts = 0

            self.mhp = 0
            self.mmp = 0
            self.mstm = 0
            self.pwr = 0
            self.agl = 0

            self.pts_calc()
            self.arc(self.pts)

            self.hp = self.mhp
            self.mp = self.mmp
            self.stm = self.mstm

            self.xp = 0
            self.buffs = []
            self.alive = True

            self.ani = "idle"
            self.spells = [None, None, None, None, None, None]
            self.skills = []
            self.slc_skill = None
            self.slc_skill_up = None

        def arc(self, p): #archetype
            while p:
                c = renpy.random.randint(1,100)
                if c < arcDic[self.type][0]:
                    self.mhp += 1
                elif c < arcDic[self.type][1]:
                    self.mmp += 1
                elif c < arcDic[self.type][2]:
                    self.mstm += 1
                elif c < arcDic[self.type][3]:
                    self.pwr += 1
                elif c < arcDic[self.type][4]:
                    self.agl += 1
                p -= 1
                self.used_pts += 1

        def pts_calc(self):
            self.pts = int((float(self.lvl) / (float(self.lvl) + float(8)))*1000) + self.lvl

        def fr(self):
            if self.alive:
                self.hp += 10
        def en(self):
            if self.alive:
                self.hp -= 10
                if self.hp < 1:
                    self.hp = 0
                    self.alive = False
                self.ani = "hit"
                renpy.restart_interaction()
        
        def spell_calc(self, a, s): # attacker, spell
            chance = renpy.random.randint(1,100)
            if chance < self.agl:
                self.hp += s.hp*a.pwr
                self.mp += s.mp*a.pwr
                self.stm += s.stm*a.pwr
                self.pwr += s.pwr*a.pwr
                self.agl += s.agl*a.pwr
        def gotskill(self, x):
            if x not in self.skills:
                self.skills.append(x)
        def spellorder(self, x):
            if self.slc_skill is None:
                self.slc_skill = x
            else:
                self.spells[self.slc_skill], self.spells[x] = self.spells[x], self.spells[self.slc_skill]
                self.slc_skill = None
        def spellcancel(self):
            self.slc_skill = None
        def spellput(self, x):
            self.spells[self.slc_skill] = x
            self.slc_skill = None
        
        
        
        
        def gotxp(self):
            pass
        def buff(self):
            pass



    class team: # ----------------- Team class
        def __init__(self):
            self.army = []
            self.team = []
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

define arcDic = { # "Name": [health, mana, stamina, power, agility]
    "Peasant": [30, 35, 65, 80, 95],
    "Wizard": [14, 54, 62, 90, 100],
    "Dancer": [21, 28, 63, 73, 100],
    "Princess": [14, 21, 33, 49, 64],
    "Beast": [28, 29, 38, 67, 73],
}
