init python:
    class difficulty:
        def __init__(self, level):
            self.level = level
            self.ramp = 0
            self.amount = 0

        def calc(self, x):
            r = int((float(x) / (float(x) + float(self.ramp))) * self.amount)
