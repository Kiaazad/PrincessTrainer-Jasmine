init python:
    class recipe:
        def __init__(self, item, qtt, ing, tools =  None, req = None):
            self.item = item
            self.qtt = qtt
            self.ing = ing
            self.tools = tools
            self.req = req

default arrows_rcp = recipe( # the recipe name has _rcp at the end to avoid name collisions
    arrows, # the item to be crafted
    5, # The number of items for each crafting
    [stack(arrowhead, 5), stack(feather, 2), stack(stick, 5), stack(string, 1)], # The required ingredients
    # [hammer, knife], # the required tools
    # [workbench], # The required conditions
    )

default sand_bottle_rcp = recipe(
    sand_bottle,
    1,
    [stack(bottle, 1), stack(cork, 1), stack(rope, 1)],
)