init python:
    class calendar_class:
        def __init__(self):
            self.minute = 0
            self.day = 14127
            self.night = 1.0
            self.eve = 0.0
            self.evening = 0.0
            self.speed = 2
        def tick(self, n = 1):
            for i in range(n):
                self.minute += 1

                if hero.stat in ["Resting", "Chatting"]:
                    hero.food -= 1
                    hero.water -= 1
                else:
                    hero.food -= 2
                    hero.water -= 2
                if hero.food in [10, 20, 30, 40]:
                    msg.msg("You feel hungry.")
                elif hero.food in [-100, -200, -300, -400]:
                    msg.msg("You're starving.")
                elif hero.food < -1000:
                    msg.msg("You've died of starvation.")

                if hero.water in [10, 20, 30, 40]:
                    msg.msg("You feel thirsty.")
                elif hero.water in [-100, -200, -300, -400]:
                    msg.msg("You're very thirsty.")
                elif hero.water < -1000:
                    msg.msg("You've died of thirst.")

                if hero.location:
                    hero.location.tick()

                if self.minute > 360:
                    self.day += 1
                    self.minute = 0
                    overnight_regen(all_places)

                if 70 < self.minute < 100:
                    self.night -= .05
                    if self.night < 0:
                        self.night = 0
                if 250 < self.minute < 280:
                    self.night += .05
                    if self.night > 1:
                        self.night = 1


        def hour_of_day(self):
            return self.minute % 15
        def day_of_week(self):
            return self.day % 7
        def speed_change(self, d = "reset"):
            if d == "up" and self.speed > 0.1:
                self.speed -= 0.1
            elif d == "down" and self.speed < 3.0:
                self.speed += 0.1
            elif d == "reset":
                self.speed = 2.0

default all_places = []

transform clock_rot(r):
    subpixel True
    rotate r

default week_days = [_("Saturday"), _("Sunday"), _("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"), _("Friday")]

default calendar = calendar_class()
screen clock:
    default t = 0
    if len(renpy.get_return_stack()):
        text "{}".format(renpy.get_return_stack()[0])
    drag:
        align(0.07, 0.134)
        fixed:
            fit_first True
            add "clock/c1.png" at clock_rot(calendar.minute)
            add "clock/c2.png"
            text "Day: [calendar.day]" color "#fff" yoffset 30
            hbox:
                button:
                    xysize 20,20
                    action Function(calendar.speed_change, "down")
                text str(calendar.speed)
                button:
                    xysize 20,20
                    action Function(calendar.speed_change, "up")

    timer calendar.speed repeat True action Function(calendar.tick)



screen time_pass(minutes):
    modal True
    default m = minutes*15
    text str(m/15)
    if m > 0:
        timer .1 repeat True action Function(calendar.tick, 5), SetScreenVariable("m", m-5)
    else:
        timer .1 action Hide("time_pass")