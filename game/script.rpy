# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define mc = Character("[mcname]")
define a = Character("Avery")
define l = Character("Leviathan")
define s = Character("Sasha")
define j = Character("Jude")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    python:
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()

    mc "My name is [mcname]!"

label leviathanintro:

    play music "music/waltzprimordial.mp3"

    """
    You find them at the very back of the bar.

    Sitting at a table, far in the corner, hand wrapped around a completely full
    drink. Sharp black nails tapping against the glass. No one else looks at
    them or comes near: not even the light. They're lost deep in the shadows,
    and as you step closer, everything quiets.

    This is it, then. This is Leviathan.

    Time to introduce yourself.

    You slide into the seat across from them and rest your chin in your hands.
    There's pressure building against your chest, your ribcage.
    A thousand tons of water pressing down on you. You smile.
    """

    mc "Buy me a drink?"

    "Leviathan scoffs, and the pressure disappears. The shadows recede, just slightly, just enough to reveal the smirk on their lips. They slide their untouched glass towards you."

    mc "This isn't spiked with something, is it?"

    l "Just water."

    "You don't drink it."

    # This ends the game.

    return
