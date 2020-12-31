init python:
    class item:
        def __init__(self,
                name, inf = "", icon = "items/_frm.png", val = 0,
                tags = [], use_event = None, waste = []
            ):
            self.name = name
            self.inf = inf
            self.icon = icon
            self.val = val
            self.tags = tags
            self.use_event = use_event
            self.waste = waste