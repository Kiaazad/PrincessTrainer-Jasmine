
define abd = Character("Abdul", color="#226", namebox_align=(0.0, 0.0), namebox1_xalign = 1.0, namebox1_background = Frame("0gui/namebox1.png", 0, 70, 0, 25), namebox1_padding = (50,5,30,5))
define jas = Character("Jasmine", color="#4ff", what_text_color="#dff")
define jaf = Character("Jafar", color="#622", what_text_color="#fdd")
define ras = Character("Rasoul", color="#f44", what_text_color="#fdd", namebox_align=(1.0, 0.0))

define lag = Character("Lago")

define hal = Character("Halia", color="#4ff", what_text_color="#dff")
define hur = Character("Huria", color="#4ff", what_text_color="#dff")
define hul = Character("Hulu", color="#4ff", what_text_color="#dff")


# Halia images
image hal normal = "char/halia/normal.png"
image hal scream = "char/halia/scream.png"

# Hulu images
image hul normal = "char/hulu/normal.png"
image hul seducing = "char/hulu/seducing.png"

# Huria images
image hur normal = "char/huria/normal.png"
image hur shocked = "char/huria/shocked.png"


# Abdul images
# Normal
image abd_normal_blink:
    "char/abdul/normal_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_normal_mouth_moving:
    "char/abdul/normal_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_normal_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_normal_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/normal.png")

image abd normal = Composite((425, 833),
    (0,0), "char/abdul/normal.png",
    (0,0), "abd_normal_mouth",
    (0,0), "abd_normal_blink",
)

# smile
image abd_smile_blink:
    "char/abdul/smile_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_smile_mouth_moving:
    "char/abdul/smile_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_smile_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_smile_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/smile.png")

image abd smile = Composite((418, 833),
    (0,0), "char/abdul/smile.png",
    (0,0), "abd_smile_mouth",
    (0,0), "abd_smile_blink",
)

# alert
image abd_alert_blink:
    "char/abdul/alert_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_alert_mouth_moving:
    "char/abdul/alert_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_alert_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_alert_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/alert.png")

image abd alert = Composite((424, 835),
    (0,0), "char/abdul/alert.png",
    (0,0), "abd_alert_mouth",
    (0,0), "abd_alert_blink",
)

# embarrassed
image abd_embarrassed_blink:
    "char/abdul/embarrassed_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_embarrassed_mouth_moving:
    "char/abdul/embarrassed_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_embarrassed_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_embarrassed_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/embarrassed.png")

image abd embarrassed = Composite((424, 774),
    (0,0), "char/abdul/embarrassed.png",
    (0,0), "abd_embarrassed_mouth",
    (0,0), "abd_embarrassed_blink",
)

# smug
image abd_smug_blink:
    "char/abdul/smug_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_smug_mouth_moving:
    "char/abdul/smug_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_smug_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_smug_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/smug.png")

image abd smug = Composite((429, 895),
    (0,0), "char/abdul/smug.png",
    (0,0), "abd_smug_mouth",
    (0,0), "abd_smug_blink",
)

# concerned
image abd_concerned_blink:
    "char/abdul/concerned_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_concerned_mouth_moving:
    "char/abdul/concerned_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_concerned_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_concerned_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/concerned.png")

image abd concerned = Composite((437, 819),
    (0,0), "char/abdul/concerned.png",
    (0,0), "abd_concerned_mouth",
    (0,0), "abd_concerned_blink",
)

# excited
image abd_excited_blink:
    "char/abdul/excited_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image abd_excited_mouth_moving:
    "char/abdul/excited_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image abd_excited_mouth = ConditionSwitch(
    "_last_say_who == 'abd'", "abd_excited_mouth_moving",
    "not _last_say_who == 'abd'", "char/abdul/excited.png")

image abd excited = Composite((553, 830),
    (0,0), "char/abdul/excited.png",
    (0,0), "abd_excited_mouth",
    (0,0), "abd_excited_blink",
)


image abd back = "char/abdul/back.png"
image abd tired = "char/abdul/tired.png"
image abd sad = "char/abdul/sad.png"
image abd afraid = "char/abdul/afraid.png"
image abd confused = "char/abdul/confused.png"
image abd bent = "char/abdul/bent.png"
image abd scared = "char/abdul/scared.png"


# Jafar images
# excited
image jaf_normal_blink:
    "char/jafar/normal_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image jaf_normal_mouth_moving:
    "char/jafar/normal_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image jaf_normal_mouth = ConditionSwitch(
    "_last_say_who == 'jaf'", "jaf_normal_mouth_moving",
    "not _last_say_who == 'jaf'", "char/jafar/normal.png")

image jaf normal = Composite((783, 1063),
    (0,0), "char/jafar/normal.png",
    (0,0), "jaf_normal_mouth",
    (0,0), "jaf_normal_blink",
)

# thinking
image jaf_thinking_blink:
    "char/jafar/thinking_blink.png"
    alpha 0
    choice:
        2
    choice:
        3

    alpha 1
    .1
    repeat
image jaf_thinking_mouth_moving:
    "char/jafar/thinking_bla.png"
    .1
    alpha 0
    .2
    alpha 1
    repeat

image jaf_thinking_mouth = ConditionSwitch(
    "_last_say_who == 'jaf'", "jaf_thinking_mouth_moving",
    "not _last_say_who == 'jaf'", "char/jafar/thinking.png")

image jaf thinking = Composite((783, 1097),
    (0,0), "char/jafar/thinking.png",
    (0,0), "jaf_thinking_mouth",
    (0,0), "jaf_thinking_blink",
)


image jaf genie = "char/jafar/genie.png"
image jaf genie bent = "char/jafar/genie_bent.png"
image jaf disappointed = "char/jafar/disappointed.png"
image jaf magic = "char/jafar/magic.png"
image jaf angry = "char/jafar/angry.png"
image jaf smile = "char/jafar/smile.png"
image jaf annoyed = "char/jafar/annoyed.png"
image jaf probing = "char/jafar/probing.png"
image jaf looking:
    "char/jafar/looking1.png"
    pause 2
    "char/jafar/looking2.png"
    pause 2
    repeat


# Jasmine
image jas normal = "char/jasmine/normal.png"
image jas seducing = "char/jasmine/seducing.png"

# Rasoul the head of guards
image ras normal = "char/rasoul/normal.png"


#------------------------------------ Shops

# Money lender
define mst = Character("Mostafa the money lender", color="#4ff", what_text_color="#dff")
image mostafa normal = "char/money_lender/normal.png"












