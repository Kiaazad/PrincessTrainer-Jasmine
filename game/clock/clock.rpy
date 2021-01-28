init python:
    class calendar_class:
        def __init__(self):
            self.minute = 0
            self.day = 14127
        def tick(self, n = 1):
            for i in range(n):
                self.minute += 1
                abdul.hunger += 1
                abdul.thirst += 1
                if self.minute > 360:
                    self.day += 1
                    self.minute = 0
                    overnight_regen(all_places)
        def hour_of_day(self):
            return self.minute % 15
        def day_of_week(self):
            return self.day % 7
default all_places = []

transform clock_rot(r):
    subpixel True
    rotate r

default week_days = [_("Saturday"), _("Sunday"), _("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"), _("Friday")]

default calendar = calendar_class()
screen clock:
    default t = 0
    drag:
        align(0.07, 0.134)
        fixed:
            fit_first True
            add "clock/c1.png" at clock_rot(calendar.minute)
            add "clock/c2.png"
            text "Day: [calendar.day]" color "#fff" yoffset 30

    timer 2 repeat True action Function(calendar.tick)



screen time_pass(minutes):
    modal True
    default m = minutes*15
    text str(m/15)
    if m > 0:
        timer .1 repeat True action Function(calendar.tick, 5), SetScreenVariable("m", m-5)
    else:
        timer .1 action Hide("time_pass")