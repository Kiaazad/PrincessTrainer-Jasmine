# Ways to push a notification into the stack

# 1- inside a python block
# msg.msg("Say something.")

# 2- inside script
# $ msg.msg("Say something.")

# 3- from screen action
# action Function(msg.msg, "say something")

########### WIP

init python:
    import time
    class msg2:
        def __init__(self, limit = 20, delay = 5):
            self.limit = limit
            self.list = []
            self.idx = 0
            self.delay = delay
        def msg(self, m):
            self.list.append([time.time(), m])
        def rem(self):
            for i in self.list:
                if i[0]+self.delay < time.time():
                    self.list.pop(0)
                else:
                    break


default msg = msg2(30)

init python:
    config.overlay_screens.append('notif')

transform notif_t(t):
    alpha 0
    ease .2 alpha 1
    # pause t-1
    # ease .2 alpha 0 yzoom 0

screen notif:
    zorder 2000
    if len(msg.list):
        timer .2 repeat True action Function(msg.rem)
    vbox:
        yalign 0.0 yoffset 40
        for i in msg.list:
            frame:
                at notif_t(msg.delay)
                text "{}".format(i[1])
    # test button, remove
    # button:
    #     text "ssd"
    #     action Function(msg.msg, "sdsdf")