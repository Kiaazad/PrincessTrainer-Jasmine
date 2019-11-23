init python:
    class item:
        def __init__(self,
                name, inf = "", icon = "items/_frm.png", val = 0,
                type = None, use_event = None
            ):
            self.name = name
            self.inf = inf
            self.icon = icon
            self.val = val
            self.type = type
            self.use_event = use_event
