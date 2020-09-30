
default school_teacher_loc = pnco(
    "The teacher",
    None,
    (400, 400),
    Jump('school_teacher'),
    )

default school_agrabah_loc = pnco(
    "Agrabah",
    None,
    (600, 500),
    Jump('agrabah'),
    )
default school_map = pncs(
    "Agrabah",
    [
        school_teacher_loc,
        school_agrabah_loc,
    ]
    )



label school:
    scene
    show bg school onlayer bg
    show screen pnc(abdul, school_map)
    pause
    jump school

define tea = Character("Teacher", color="#4ff", what_text_color="#dff")
image teacher normal = "char/teacher/normal.png"
label school_teacher:
    scene
    show teacher normal at right
    tea "State your business!"
    show abd normal at left
    menu:
        "I'm just looking around.":
            abd "Ermmm...{w=.5} I'm just looking around."
            tea "This is a place of learning. Please leave."
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
    jump school