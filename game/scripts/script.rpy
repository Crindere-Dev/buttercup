label splashscreen:
scene black
with Pause (1)

show image "images/splash.png" with d
with Pause(2)
hide image "images/splash.png" with d
show black
pause 2
return 
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    scene black
     
    "placeholder"
    show text "mar"
    pause 0.5
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    jump prep

    # This ends the game.

