define me = Character("Abdul", color="#44f", namebox_align=(.1, .95))
define jas = Character("Jasmine", color="#4ff", what_text_color="#dff", namebox_align=(.9, .95))
define jaf = Character("Jafar", color="#f44", what_text_color="#fdd", namebox_align=(.9, .95))

define lag = Character("Lago")



# Abdul images
image me normal = ConditionSwitch(
    "_last_say_who == 'me'", "char/abdul/normal.png",
    "not _last_say_who == 'me'", im.Grayscale("char/abdul/normal.png"))

image me back = "char/abdul/back.png"

image me tired = "char/abdul/tired.png"
image me sad = "char/abdul/sad.png"
image me afraid = "char/abdul/afraid.png"
image me confused = "char/abdul/confused.png"
# image me bent = "char/abdul/bent.png"
image me alert = "char/abdul/alert.png"
image me embarrassed = "char/abdul/embarrassed.png"
image me smug = "char/abdul/smug.png"
image me hesitant = "char/abdul/hesitant.png"

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

image jaf looking:
    "char/jafar/looking1.png"
    pause 2
    "char/jafar/looking2.png"
    pause 2
    repeat