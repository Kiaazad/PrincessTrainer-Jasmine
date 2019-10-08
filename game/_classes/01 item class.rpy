init python:
    class item:
        def __init__(self,
                name, val, icon,
                inf = "", type = None, use_event = None
            ):
            self.name = name
            self.val = val
            self.inf = inf
            self.icon = icon
            self.type = type
            self.use_event = use_event
