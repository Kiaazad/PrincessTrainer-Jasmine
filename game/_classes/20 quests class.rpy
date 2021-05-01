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
        def finish(self):
            self.stat = "Finished"


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
        def cancel(self, q):
            q.stat = "Canceled"
            msg.msg("Quest canceled: {}".format(q.name))
        def complete(self, q):
            q.stat = "Completed"
            msg.msg("Quest completed: {}".format(q.name))
        def finish(self, q):
            q.stat = "Finished"
            msg.msg("Quest finished: {}".format(q.name))
        def fail(self, q):
            q.stat = "Failed"
            msg.msg("Quest failed: {}".format(q.name))
        def has(self, quest):
            if quest in self.log:
                return quest.stat
            else:
                return False
