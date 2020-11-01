
label splashscreen:
    scene black
    show screen danza_splash
    pause 3
    hide screen danza_splash
    show screen demo_warning
    pause
    hide screen demo_warning

screen demo_warning:
    modal True
    frame:
        xsize 1200
        vbox:
            text "Note" size 40
            text "Some of the art assets in this game are not finished yet and put in the game as placeholder, they will be replaced by beautifully drawn and animated assets over time." size 28 xalign 0.0 justify True layout "greedy"
            null height 30
            text "Check our {a=https://www.patreon.com/StudioDanza}{color=#f50}{u}patreon page{/u}{/color}{/a} for more information about our process. there is plenty of free posts and there are many way to support this game without spending any of your money." size 26 xalign 0.0 justify True layout "greedy"
            button:
                text "Alright!"
                action Return()
    
screen danza_splash:
    add "#999"
    add "splash/swoosh.png" at danza_splash_1(.3)
    add "splash/bam.png" at danza_splash_2(.4)
    add "splash/frame.png" at danza_splash_3(.6)
    add "splash/studio.png" at danza_splash_4(.8,188)
    add "splash/danza.png" at danza_splash_4(.8,-225)

transform danza_splash_1(d=0):
    crop_relative True
    crop(0.0,0.5,0.0,0.0)
    pause d
    ease .2 crop(0.0,0.0,1.0,1.0)

transform danza_splash_2(d=0):
    alpha 0 zoom .01
    pause d
    easein_bounce .2 alpha 1 zoom 1

transform danza_splash_3(d=0):
    alpha 0 xzoom .01
    pause d
    alpha 1
    ease .2 xzoom 1

transform danza_splash_4(d=0, o=0):
    alpha 0 xoffset o
    pause d
    ease .2 alpha 1
    pause .2
    easein_bounce .4 xoffset 0