init python:
    class quest:
        def __init__(self, name, info, items = [], objc = [], rewards = [], img = []):
            self.name = name
            self.info = info
            self.objc = objc
            self.rewards = rewards
            self.img = img
            self.stat = "Active"
        def complete(self):
            self.stat = "Completed"
            Show("quest_notif", s = "qst_completed")()
        def cancel(self):
            self.stat = "Canceled"
            Show("quest_notif", s = "qst_canceled")()
        def fail(self):
            Show("quest_notif", s = "qst_failed")()
        def extend(self, text):
            self.info.append(text)
            msg.msg("Changed quest: {}\n{}".format(self.name, text))
        
    class quest_log:
        def __init__(self):
            self.log = []
            self.slc = None
            self.filt = 0

        def chose(self, n):
            self.slc = n
        def filter(self):
            if self.filt < 4:
                self.filt += 1
            else:
                self.filt = 0


        def got(self, q):
            if q not in self.log:
                self.log.append(q)
                msg.msg("New quest: {}".format(q.name))
                Show("quest_notif", s = "qst_accepted")()
        def has(self, quest):
            if quest in self.log:
                return quest.stat
            else:
                return False

image quest_notification = Live2D("quests/quest_menu_l2d/quest_menu.model3.json", loop=False, zoom=0.5
    )

screen quest_notif(s):
    add "quest_notification [s]":
        yalign 0.9
    timer 5 action Hide("quest_notif")