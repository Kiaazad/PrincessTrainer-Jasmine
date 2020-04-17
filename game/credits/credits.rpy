init python:
    class credits_class:
        def __init__(self, lst, animation_speed = 2):
            self.lst = lst
            self.animation_speeed = animation_speed
        def next(self, curr):
            renpy.show_screen("cred_ins", item = self.lst[curr], anispeed = self.animation_speeed, _tag = "cred_{}".format(curr))
 

default credits1 = credits_class(
    [
        [4, "Concept art  by", ["Pook", "ILW"]],
        [4, "Story  by", ["Gabe", "KiaAzad"]],
        [4, "Music by", ["Nobody Yet"]],
        [4, "Voice actors", ["Nobody Yet"]],
        [4, "Character art", ["Parasitius", "Pook"]],
        [4, "Background art", ["Raemn"]],
        [4, "Lead programmer", ["KiaAzad"]],
        [4, "GUI designer", ["KiaAzad"]],
        [4, "Sponsors", ["otakusexart.com", "hentaireviews.moe", "hentai-onahole.moe",]],
        [4, "Special thanks to our Patreon supporters", ["Ryan Miller", "Walter Jimenez", "Bobot","Christian Anthony Ramirez",  "Robert Perron", "And you?"]],
        [6, "text", "Thank you for playing."],
        [2, "action", Return()]
    ],
    animation_speed = 2 # [optional] default is 2sec
    )
transform cred_trans(speed, p, d=renpy.random.random()):
    subpixel True
    alpha 0 zoom 0
    pause d
    parallel:
        ease_bounce speed/2 zoom 1
        pause p+speed-d
        ease speed/2 zoom 0
    parallel:
        linear speed alpha 1
        pause p-d
        ease_quart speed alpha 0
screen credits(c=credits1):
    tag menu
    default curr = 0
    add "#000d"
    if curr == 0:
        timer 1 repeat True action Function(c.next, curr), SetScreenVariable("curr", curr+1)
    elif curr < len(c.lst):
        timer c.lst[curr][0]+(c.animation_speeed*2) repeat True action Function(c.next, curr), SetScreenVariable("curr", curr+1)

screen cred_ins(item, anispeed):
    timer item[0]+(anispeed*2) action Hide("cred_ins")
    frame:
        xfill True yfill True margin 100,100 background None
        if item[1] == "text":
            text item[2] at cred_trans(anispeed, item[0]) size 50
        elif item[1] == "action":
            timer item[0] action item[2]
        else:
            vbox:
                text item[1] at cred_trans(anispeed, item[0]) size 30 color "#4ff"
                vbox:
                    box_wrap True
                    for i in item[2]:
                        text i at cred_trans(anispeed, item[0]) size 50



        
