init python:
    class quest:
        def __init__(self, name, inf, items = [], objc = [], rewards = [], img = []):
            self.name = name
            self.inf = inf
            self.objc = objc
            self.rewards = rewards
            self.img = img
            self.stat = "Active"
        def complete(self):
            self.stat = "Completed"
            Show("quest_notif", s = "qst_completed")()
        def finish(self):
            self.stat = "Finished"
        def cancel(self):
            self.stat = "Canceled"
            Show("quest_notif", s = "qst_canceled")()
        def fail(self):
            Show("quest_notif", s = "qst_failed")()

    class quest_log:
        def __init__(self):
            self.log = []
            self.slc = None
            self.filt = 0

        def chose(self, n):
            self.slc = n
        def filter(self):
            if self.filt < 5:
                self.filt += 1
            else:
                self.filt = 0


        def got(self, q):
            if q not in self.log:
                self.log.append(q)
                msg.msg("New quest: {}".format(q.name))
                Show("quest_notif", s = "qst_accepted")()
        def cancel(self, q):
            q.stat = "Canceled"
            msg.msg("Quest canceled: {}".format(q.name))
            Show("quest_notif", s = "qst_canceled")()
        def complete(self, q):
            q.stat = "Completed"
            msg.msg("Quest completed: {}".format(q.name))
            Show("quest_notif", s = "qst_completed")()
        def finish(self, q):
            q.stat = "Finished"
            msg.msg("Quest finished: {}".format(q.name))
        def fail(self, q):
            q.stat = "Failed"
            msg.msg("Quest failed: {}".format(q.name))
            Show("quest_notif", s = "qst_failed")()
        def has(self, quest):
            if quest in self.log:
                return quest.stat
            else:
                return False

image quest_notification = Live2D("quests/quest_menu_l2d/quest_menu.model3.json", loop=False
    )

screen quest_notif(s):
    modal True
    add "quest_notification [s]"
    timer 5 action Hide("quest_notif")