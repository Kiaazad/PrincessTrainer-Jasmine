init python:
    class eat:
        def __init__(self):
            self.max_water = 1000
            self.max_food = 1000
            self.water = 670
            self.food = 789

        def drink(self, salt, filth):
            if self.water < -500:
                self.water = -500
            if salt == 1:
                msg.msg("A bit salty.")
                self.water += 600
            elif salt == 2:
                msg.msg("salty!")
                self.water += 500
            elif salt == 3:
                msg.msg("very salty!!")
                self.water += 300
            elif salt == 4:
                msg.msg("It's practically brine!!!")
                self.water += 200
            elif salt > 4:
                msg.msg("Enough salt to kill.")
                self.water += 200
            
            r = renpy.random.randint(0, 100)
            if r < filth:
                msg.msg("You'll get sick.")
            if self.water > 1000:
                self.water = 1000
        def eat(self, item):
            if self.water < -500:
                self.water = -500
            if self.food < -500:
                self.food = -500
            if "food" in item.tags:
                self.water += item.water
                if self.water > 1000:
                    self.water = 1000

                self.food += item.food
                if self.food > 1080:
                    self.food = 1080
                
                self.drop(item, 1, False)
            else:
                msg.msg("Can't eat that!")


    class unit(inventory, fight):
        def __init__(self, name, dir,
                    cash = 0, items = [], markup = 1,
                    lvl = 1, type = "Peasant",
                    interests = [], reject = [], cant = []
                    ):
            inventory.__init__(self, cash, items, markup)
            fight.__init__(self, lvl, type, cant)
            self.name = name
            self.dir = dir
            
            self.wishes = 3
            self.sand = 0
            self.bottles = 0
            self.fishing_skill = 0.3

            self.interests = interests
            self.reject = reject
            self.reject.append("unsellable")
            self.flags = []
            self.affection = 0

            self.water = 670
            self.food = 789
            self.pleasure = 0

            self.pay = 0
            self.stat = "Normal"
            self.location = None
        def drink(self, salt, filth):
            if self.water < -500:
                self.water = -500
            if salt == 1:
                msg.msg("A bit salty.")
                self.water += 600
            elif salt == 2:
                msg.msg("salty!")
                self.water += 500
            elif salt == 3:
                msg.msg("very salty!!")
                self.water += 300
            elif salt == 4:
                msg.msg("It's practically brine!!!")
                self.water += 200
            elif salt > 4:
                msg.msg("Enough salt to kill.")
                self.water += 200
            
            r = renpy.random.randint(0, 100)
            if r < filth:
                msg.msg("You'll get sick.")
            if self.water > 1000:
                self.water = 1000


        def eat(self, item):
            if self.water < -500:
                self.water = -500
            if self.food < -500:
                self.food = -500
            if "food" in item.tags:
                self.water += item.water
                if self.water > 1000:
                    self.water = 1000

                self.food += item.food
                if self.food > 1080:
                    self.food = 1080
                
                self.drop(item, 1, False)
            else:
                msg.msg("Can't eat that!")

        def add_flag(self, flag):
            self.flags.append(flag)




