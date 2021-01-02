init python:
    class btl_arc_class:
        def __init__(self):
            self.rem = 100
            self.ind = 0

            self.hp = 20
            self.mp = 20
            self.stm = 20
            self.pwr = 20
            self.agl = 20
        def adj(self):
            self.rem = self.hp + self.mp + self.stm + self.pwr + self.agl
            while self.hp + self.mp + self.stm + self.pwr + self.agl > 100:
                if self.ind == 0:
                    if self.hp > 1:
                        self.hp -= 1
                    self.ind += 1
                elif self.ind == 1:
                    if self.mp > 1:
                        self.mp -= 1
                    self.ind += 1
                elif self.ind == 2:
                    if self.stm > 1:
                        self.stm -= 1
                    self.ind += 1
                elif self.ind == 3:
                    if self.pwr > 1:
                        self.pwr -= 1
                    self.ind += 1
                else:
                    if self.agl > 1:
                        self.agl -= 1
                    self.ind = 0
                
default btl_arc_1 = btl_arc_class()
screen btl_arc(x = btl_arc_1):
    modal True
    default inp = ""
    timer .1 repeat True action Function(x.adj)
    vbox:
        text "%{}".format(x.rem)
        hbox:
            label "Health" xsize 120
            bar value FieldValue(x, "hp", 60) xysize 500,80 left_bar "#f00" right_bar "#fff9"
            label "%{}".format(x.hp) xsize 120
        hbox:
            label "Mana" xsize 120
            bar value FieldValue(x, "mp", 60) xysize 500,80 left_bar "#0ff" right_bar "#fff9"
            label "%{}".format(x.mp) xsize 120
        hbox:
            label "Stamina" xsize 120
            bar value FieldValue(x, "stm", 60) xysize 500,80 left_bar "#ff0" right_bar "#fff9"
            label "%{}".format(x.stm) xsize 120
        hbox:
            label "Power" xsize 120
            bar value FieldValue(x, "pwr", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
            label "%{}".format(x.pwr) xsize 120
        hbox:
            label "Agility" xsize 120
            bar value FieldValue(x, "agl", 60) xysize 500,80 left_bar "#444" right_bar "#fff9"
            label "%{}".format(x.agl) xsize 120
        hbox:
            frame:
                xsize 300
                input:
                    value ScreenVariableInputValue("inp")
            button:
                text "Copy"
                action Function(clip_put, "\"{}\": [{}, {}, {}, {}, {}]".format(inp, x.hp, x.hp + x.mp, x.hp + x.mp + x.stm, x.hp + x.mp + x.stm + x.pwr, x.hp + x.mp + x.stm + x.pwr + x.agl))

