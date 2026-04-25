label splashscreen:
scene black
with Pause (1)

show image "images/splash.png" with d
with Pause(2)
hide image "images/splash.png" with d
show black
pause 2
return 


label start:
    scene black
    stop music
     
    "It was any other unremarkable Tuesday," 
    "Business{w=.25} - while not failing,{w=.25} - was as quiet and slow like any other day."
    " Couples,{w=.25} Normies,{w=.25} the occasional tourist or two would come,{w=.25} order,{w=.25} read and leave."
    "The quiet atmosphere was something Adeline knew too well."
    $ renpy.movie_cutscene("images/intro_cutscene.ogv")

    jump prep

    # This ends the game.

