
default school_teacher_loc = pnco(
    "The teacher",
    "bg/school/teacher.png",
    (1405, 664),
    Jump('school_teacher'),
    )

default school_agrabah_loc = pnco(
    "Agrabah",
    "bg/school/city.png",
    (325, 1019),
    Jump('agrabah'),
    )
default school_map = pncs(
    "Agrabah",
    [
        school_teacher_loc,
        school_agrabah_loc,
    ]
    )



image bg school = "bg/school/bg.jpg"
label school:
    scene
    show bg school onlayer bg
    show screen pnc(abdul, school_map)
    pause
    jump school


default skin_scroll = item(
    _("Skin scroll"),
    _("A scroll made of goat skin."),
    "items/skin_scroll.png",
    1400,
    ["stationery"],
    )
default paper = item(
    _("Paper"),
    _("A blank sheet of paper."),
    "items/paper.png",
    100,
    ["stationery"],
    )
default black_ink = item(
    _("ink"),
    _("Black ink made of some black stuff."),
    "items/black_ink.png",
    800,
    ["stationery"],
    )


define tea = Character("Teacher", color="#4ff", what_text_color="#dff")
image teacher normal = "char/teacher/normal.png"
default teacher_u = unit(
    "Teacher",
    "char/teacher",

    2441,
    [
        (skin_scroll, 6),
        (paper, 22),
        (black_ink, 4),
    ],
    1.1,

    12,
    "Peasant",
    interests = ["book"],
    reject = ["drug", "Weapon", "armor"]
    )

default books_for_school = quest(
    _("Books for school"),
    _("The school teacher needs books, Jafar's books are preferred."),
    )


label school_teacher:
    scene
    if not "first" in teacher_u.flags:
        show teacher normal at right
        tea "State your business!"
        show abd normal at left
        menu:
            "I'm just looking around.":
                abd "Ermmm...{w=.5} I'm just looking around."
                tea "This is a place of learning. Please leave."
                $ teacher_u.affection -= 4
            "I need some books.":
                abd "I need some books."
                tea "Our library have suffered a great loss, I can't sell you any books right now."
                abd "What happened."
                tea "The guards have confiscated all books that Jafar have donated in the years he have been the royal Vizier."
                abd "I see..."
                tea "Only a man of culture seeks books, do you have any books to donate?"
                tea "Or I can buy them from you if the price is fair."
                abd "Not really."
                tea "Alright, let me know if you've came across any."
                $ qlog.got(books_for_school)
                $ teacher_u.affection += 20
                $ teacher_u.add_flag("first")

    else:
        show teacher normal at right
        tea "Got some books for me??"
        show abd normal at left
        menu:
            "Not yet.":
                abd "Not yet but I need something."
                tea "Alright."
                call screen shop(s = teacher_u)


    jump school