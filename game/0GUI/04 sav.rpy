init python:
    class sav_btl_lst:
        def __init__(self):
            self.lst = persistent.sav_ins
            self.imgs = [0,1,2,3,4,5,]
        def add(self):
            img = renpy.random.choice(self.imgs)
            y = renpy.random.randint(-400, -100)
            zm = renpy.random.randint(6,10)
            flp = renpy.random.choice([True, False])
            self.lst.append([img, 960, y, zm*.1, flp])
        def drag(self, drags, drop, ii=0):
            pass
            self.lst[drags[0].drag_name][1] = (drags[0].x)+50
            self.lst[drags[0].drag_name][2] = self.lst[drags[0].drag_name][2]
            renpy.restart_interaction()
        def delete(self, x):
            self.lst.pop(x)
define persistent.sav_ins = []

init offset = -1
define config.thumbnail_width = 384
define config.thumbnail_height = 216
## Load and Save screens #######################################################
transform sav_btl(t):
    transform_anchor True
    rotate_pad False
    subpixel True
    ease t rotate 2
    ease t rotate -2
    repeat
transform sav_thmb:
    zoom 5 alpha 0
    ease .4 alpha .5

screen save():
    modal True
    tag menu
    use file_slots(_("Save"))

screen load():
    modal True
    tag menu
    use file_slots(_("Load"))

default save_list = sav_btl_lst()
screen file_slots(title, s = save_list):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    style_prefix "sav"
    use game_menu(title):
        default simg = None
        vbox:
            button:
                text "test"
                action Function(s.add)

        if simg:
            add FileScreenshot(simg) at sav_thmb
            key "save_delete" action FileDelete(simg)
            key "y" action Function(s.delete, simg-1)
        add "0GUI/sav/fg.webp"
        if s.lst:
            for ii, i in enumerate(s.lst):
                drag:
                    yalign 0.0 xpos i[1] ypos i[2] yanchor 0.0
                    drag_name ii
                    dragged s.drag
                    at sav_btl(renpy.random.random()+1)
                    fixed:
                        fit_first True
                        if i[4]:
                            at flp
                        add "0GUI/sav/{}{}.png".format(i[0],"b" if FileTime(ii+1) else "a") zoom i[3]
                        # text "{} - {}".format(i[1],i[2])
                        button:
                            ysize 220 yalign 1.0
                            background None
                            action FileAction(ii+1)
                            hovered SetLocalVariable("simg", ii+1)
                            unhovered SetLocalVariable("simg", None)


                # has vbox
                # 
                # text FileTime(slot, format=_("{#file_time}%a, %H:%M - %b %d  %Y, "), empty=_("empty slot")) text_align .5
                # if FileSaveName(slot):
                #     text FileSaveName(slot)
                

            # hbox:
            #     textbutton _("<") action FilePagePrevious() at btn
            #     button:
            #         at btn
            #         key_events True
            #         action page_name_value.Toggle()
            #         input:
            #             value page_name_value
            #     textbutton _(">") action FilePageNext() at btn
