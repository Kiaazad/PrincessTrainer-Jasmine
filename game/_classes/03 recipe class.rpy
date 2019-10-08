init python:
    class recipe:
        def __init__(self,
                items, ing,
                tools =  None, req = None
            ):
            self.items = items
            self.ing = ing
            self.tools = tools
            self.req = req #requirements
