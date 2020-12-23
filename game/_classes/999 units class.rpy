init python:
    class unit(inventory, fight):
        def __init__(self, name, dir,
                    cash = 0, items = [], markup = 1,
                    lvl = 1, type = "Peasant",
                    interests = [], reject = [],
                    ):
            inventory.__init__(self, cash, items, markup)
            fight.__init__(self, lvl, type)
            self.name = name
            self.dir = dir
            
            self.wishes = 3
            self.sand = 0
            self.bottles = 0

            self.interests = interests
            self.reject = reject
            self.flags = []
            self.affection = 0


        def add_flag(self, flag):
            self.flags.append(flag)
        def add_interest(self, interest):
            self.interests.append(interest)
