init python:
    def archetype_calc(unit): #archetype calculator
        for i in range(unit.lvl):
            s = renpy.random.choice(arcDic[unit.type][1])
            if s not in unit.spells:
                unit.skills.append(s)