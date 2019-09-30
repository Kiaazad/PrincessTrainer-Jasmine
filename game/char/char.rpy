define abd = Character("Abdul", color="#44f", namebox_align=(.1, .95))
define jas = Character("Jasmine", color="#4ff", what_text_color="#dff", namebox_align=(.9, .95))
define jaf = Character("Jafar", color="#f44", what_text_color="#fdd", namebox_align=(.9, .95))

define lag = Character("Lago")



# Abdul images
image abd normal = ConditionSwitch(
    "_last_say_who == 'abd'", "char/abdul/normal.png",
    "not _last_say_who == 'abd'", "char/abdul/normal.png")

image abd back = "char/abdul/back.png"
image abd smile = "char/abdul/smile.png"
image abd tired = "char/abdul/tired.png"
image abd sad = "char/abdul/sad.png"
image abd afraid = "char/abdul/afraid.png"
image abd confused = "char/abdul/confused.png"
# image abd bent = "char/abdul/bent.png"
image abd alert = "char/abdul/alert.png"
image abd embarrassed = "char/abdul/embarrassed.png"
image abd smug = "char/abdul/smug.png"
image abd scared = "char/abdul/scared.png"
# image abd concerned = "char/abdul/concerned.png"



# Jafar
image jaf normal = ConditionSwitch(
    "_last_say_who == 'jaf'", "char/jafar/normal.png",
    "not _last_say_who == 'jaf'", im.Grayscale("char/jafar/normal.png"))

# image jaf genie = "char/jafar/genie.png"
image jaf thinking = "char/jafar/thinking.png"
image jaf disappointed = "char/jafar/disappointed.png"
image jaf magic = "char/jafar/magic.png"
image jaf angry = "char/jafar/angry.png"
# image jaf smile = "char/jafar/smile.png"
# image jaf annoyed = "char/jafar/annoyed.png"
# image jaf probing = "char/jafar/probing.png"
image jaf looking:
    "char/jafar/looking1.png"
    pause 2
    "char/jafar/looking2.png"
    pause 2
    repeat