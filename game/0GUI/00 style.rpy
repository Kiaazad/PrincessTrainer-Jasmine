init offset = -1

init python:
    class gui0:
        def __init__(self, texts, frames, boarders, t_alp, f_alp):
            self.texts = texts
            self.frames = frames
            self.boarders = boarders
            self.t_alp = t_alp
            self.f_alp = f_alp
            
            ### Text
            self.t_ins = texts + self.t_alp[0]
            self.t_idl = texts + self.t_alp[1]
            self.t_hov = texts + self.t_alp[2]
            
            self.t_slc_ins = texts + self.t_alp[0]
            self.t_slc_idl = texts + self.t_alp[1]
            self.t_slc_hov = texts + self.t_alp[2]
            
            ### Frames
            if frames[0] == "#":
                self.f_ins = self.frames + self.f_alp[0]
                self.f_idl = self.frames + self.f_alp[1]
                self.f_hov = self.frames + self.f_alp[2]
                
                self.f_slc_ins = self.frames + self.f_alp[0]
                self.f_slc_idl = self.frames + self.f_alp[1]
                self.f_slc_hov = self.frames + self.f_alp[2]
            else:
                self.f_ins = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.f_idl = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.f_hov = Frame(self.frames, self.boarders[0], self.boarders[1])
                
                self.f_slc_ins = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.f_slc_idl = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.f_slc_hov = Frame(self.frames, self.boarders[0], self.boarders[1])
            
            ### Bars
            if frames[0] == "#":
                self.l_bar = self.frames + self.f_alp[2]
                self.r_bar = self.frames + self.f_alp[0]
                self.l_bar_hov = self.frames + self.f_alp[1]
                self.r_bar_hov = self.frames + self.f_alp[0]
            else:
                self.l_bar = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.r_bar = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.l_bar_hov = Frame(self.frames, self.boarders[0], self.boarders[1])
                self.r_bar_hov = Frame(self.frames, self.boarders[0], self.boarders[1])


### Change these ###############################################################

define thm = gui0("#fff", "0GUI/frame/00.png", (8, 8),["2", "f", "f"],["2", "a", "f"]) # "0gui/frame/026.png"
define bgs = [
    "#444", # Main menu background
    "#000d", # Screens background
    "#000d", # Dimmed overlay
    ]

transform btn:
    parallel:
        zoom .6 alpha 0
       # pause renpy.random.random()/4
        alpha 1
        easein .2 zoom 1
    parallel:
        on idle:
            easein .2 additive 0
        on hover:
            easein .2 additive .3
        on selected_idle:
            easein .2 additive .2
        on selected_hover:
            easein .2 additive .3
        on insensitive:
            easein .2 additive 0

### Styles #####################################################################


style default:
    align(.5,.5)
    padding(20,20)
    spacing 10
    color thm.t_idl
    hover_color thm.t_hov
    font "0GUI/fonts/Acme-Regular.ttf"
    size 24

#    hover_sound "ui/sfx/hover.mp3"
#    activate_sound "ui/sfx/select.mp3"


    background thm.f_idl
    hover_background thm.f_hov
    selected_background thm.f_slc_idl
    selected_hover_background thm.f_slc_hov
    
    left_bar thm.l_bar
    right_bar thm.r_bar
    hover_left_bar thm.l_bar_hov
    hover_right_bar thm.r_bar_hov

init -10:
    $ left= Position(yalign=1.0,xalign=0.1)
    $ right= Position(yalign=1.0,xalign=0.9)
    $ midleft= Position(yalign=1.0,xalign=0.2)
    $ midright= Position(yalign=1.0,xalign=0.8)
    $ center= Position(yalign=1.0,xalign=0.5)
    $ leftend = Position(yalign=1.0,xalign=0.0)
    $ rightend = Position(yalign=1.0,xalign=1.0)
python:
    config.default_transform = center
