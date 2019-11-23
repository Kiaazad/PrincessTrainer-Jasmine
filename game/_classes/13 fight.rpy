init python:
    class fight:
        def __init__(self, lvl, type):
            self.lvl = lvl
            self.type = type

            self.pts = 0
            self.used_pts = 0

            self.mhp = 10
            self.mmp = 10
            self.mstm = 10
            self.pwr = 1
            self.agl = 1

            self.spells = [None, None, None, None, None, None]
            self.skills = []

            self.pts_calc()
            self.arc_calc()

            self.hp = self.mhp
            self.mp = self.mmp
            self.stm = self.mstm

            self.xp = 0
            self.buffs = []
            self.alive = True

            self.ani = "idle"


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


        def spell_cast(self, spell):
            # if spell.hpc:
            #     caster.hp += spell.hpc
            #     self.spell_calc(caster, spell)
            if spell.mpc:
                if self.mp >= spell.mpc:
                    self.mp -= spell.mpc
                    self.spell_calc(caster, spell)
                else:
                    msg.msg("Not enough Mana.")
            if spell.stmc:
                if self.stm >= spell.stmc:
                    self.stm -= spell.stmc
                    self.spell_calc(caster, spell)
                else:
                    msg.msg("Not enough Stamina.")

        def pts_calc(self):
            self.pts = int((float(self.lvl) / (float(self.lvl) + float(20)))*1000) + self.lvl

        def spell_check(self, caster, spell):
            # if spell.hpc:
            #     caster.hp += spell.hpc
            #     self.spell_calc(caster, spell)
            if spell.mpc:
                if caster.mp >= spell.mpc:
                    caster.mp -= spell.mpc
                    self.spell_calc(caster, spell)
                else:
                    msg.msg("Not enough Mana.")
            if spell.stmc:
                if caster.stm >= spell.stmc:
                    caster.stm -= spell.stmc
                    self.spell_calc(caster, spell)
                else:
                    msg.msg("Not enough Stamina.")

        def spell_calc(self, caster, spell): # attacker, spell
            chance = renpy.random.randint(1,100)
            crit = renpy.random.randint(-30,10)
            pdbm = renpy.random.randint(0, 3)

            if chance > spell.pdbm[pdbm] + int((float(self.agl) / (float(self.agl) + float(100))) * 100)/2:
                if spell.hp:
                    damage = (spell.hp + (caster.pwr * spell.hp)/100) + crit
                    self.hp += damage
                    msg3(damage)
                if spell.mp:
                    burn = (spell.mp + (caster.pwr * spell.mp)/100) + crit
                    self.mp += burn
                    msg3(burn)
                if spell.stm:
                    breath = (spell.stm + (caster.pwr * spell.stm)/100) + crit
                    self.stm += breath
                    msg3(breath)
            else:
                msg3("{}".format(["Parry", "Dodge", "Block", "Miss"][pdbm]))
            if self.hp < 0:
                self.hp = 0
                self.ani = "dead"
        def regen(self):
            if self.mp < self.mmp:
                self.mp += int(self.mmp/100)
                if self.mp > self.mmp:
                    self.mp = self.mmp
            if self.stm < self.mstm:
                self.stm += int(self.mstm/100)
                if self.stm > self.mstm:
                    self.stm = self.mstm


        def gotskill(self, x):
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


        
        
        def gotxp(self):
            pass
        def buff(self):
            pass


