# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

### Typography Pausemaker
init python:
    def typography(what):

        replacements = [
            ("? ", "? {w=.15}"),
            ("! ", "! {w=.15}"),
            (",", ", {w=.1}"),
            ( ". . .", ". . . {w=.15}"),
            (". ", ". {w=.15}"),
        ]

        for item in replacements:
            what = what.replace(item[0],item[1])
        
        return what
    
    config.say_menu_text_filter = typography

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

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    j "My name is Jake. {w=0.5} That's my first name, obviously."
    j "I can't tell you my last name. It would be too dangerous. The Controllers are everywhere. Everywhere."
    j "And if they knew my full name, they could find me and my friends, and then..."
    j "well, let's just say I don't want them to find me. What they do to people who resist them is too horrible to think about."
    j "I won't even tell you where I live. You'll just have to trust me that it is a real place, a real town. It may even be {i}your{/i} town."

    m "Nice going, Jake. We're out of quarters."

    

    # This ends the game.

    return
