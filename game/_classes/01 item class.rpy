init python:
    class item:
        def __init__(self,
                name, inf = "", icon = "_frm", val = 0,
                tags = [], use_event = None, waste = [],
                food = 0, water = 0,
            ):
            self.name = name
            self.inf = inf
            self.icon = icon
            self.val = val
            self.tags = tags
            self.use_event = use_event
            self.waste = waste

            self.food = food
            self.water = water