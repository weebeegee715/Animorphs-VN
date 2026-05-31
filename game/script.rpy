# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init python:
##  Basic Male Voice 1
    def guy_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guy.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
##  Basic Male Voice 2
    def guy2_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guy2.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
## Basic Male Voice Low
    def guylow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guylow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
## Basic Male Voice High
    def guyhigh_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("guyhigh.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
        
##  Basic Female Voice 1
    def girl_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girl.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
##  Basic Female Voice 2
    def girllow_beep(event, **kwargs):
        if event == "show":
            renpy.music.play("girllow.wav", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


define j = Character("Jake", callback=guy2_beep, color="#34aa2b")
define t = Character("Tobias", callback=guyhigh_beep, color="#59526f")
define r = Character("Rachel", callback=girllow_beep, color="#117e70ff")
define c = Character("Cassie", callback=girl_beep, color= "#a63eb4")
define m = Character("Marco", callback=guy_beep, color="#b60e0e")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    j "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    m "Just seeing how all the voices sound"

    r "I hope this turns out ok!"

    t "yeah woop woop woop woop "

    j "lalalalalalal"

    # This ends the game.

    return
