default jail_barracks = pnco(
    "Barracks",
    None,
    (924, 929),
    Jump('barracks'),
    )

default jail_books = pnco(
    "Books",
    None,
    (236, 839),
    Jump('jail_books'),
    )

default jail_qasim = pnco(
    "Qasim",
    None,
    (1431, 697),
    Jump('jail_qasim'),
    )

default jail_cells = pnco(
    "Cells",
    None,
    (689, 669),
    Jump('jail_cells'),
    )

default jail_map = pncs(
    "Jail",
    [
        jail_barracks,
        jail_books,
        jail_qasim,
        jail_cells,

    ]
    )

"""
Background design notes:
There are two doors, one goes to the jail cells and another to Qasim's room.
Qasim's room can't be entered and doesn't need a background 

Cells:
(I Imagined it as a round basement with a series of indentations in the wall that are separated from the middle with bars)
the middle hosts some torture devices and a set of stairs to the entrance.
"""
image bg jail = "bg/jail/bg.jpg"
label jail:
    scene
    show bg jail onlayer bg
    show screen pnc(abdul, jail_map)
    pause
    jump jail

label jail_books:
    scene
    show abd normal at left with dissolve
    show qasim normal at right with dissolve
    qasim "Don't touch those."
    jump jail

label jail_qasim:
    scene
    show abd normal at left with dissolve
    show qasim normal at right with dissolve
    qasim "Don't touch me."
    jump jail

label jail_cells:
    scene
    show abd normal at left with dissolve
    show qasim normal at right with dissolve
    qasim "Don't go there."
    jump jail


