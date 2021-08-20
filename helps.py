game_help = {
    'CONTENTS':'''

CONTENTS


keywords 1 ......... help 1
keywords 2 ......... help 2
history ............ help 3
auxiliary function . help 4
auther ............. help 0
''', 

    '1':'''
keywords 1

printarea ------ to print mine field
exit ----------- exit
cheat ---------- print booms
boom_remaining - view how much booms remaining

next page:help 2
don't know how to play:help 3
contents:help CONTENTS
''', 

    '2':'''
keywords 2

mark <x> <y> -- mark a position

next page:help 3
don't know how to play:help 3
contents:help CONTENTS
''', 

    '3':'''
Minesweeper is a single player computer game.
The goal of the game is to find all the squares without mines and complete the game.
If you step on the box with mines, the game fails.
The game is judged by the time it is completed.

next page:help 4
contents:help CONTENTS
''', 

    '4':'''
auxiliary functions:

idiot1
idiot2
smart1
mygod
boom

contents:help CONTENTS
''', 

    '0':'''
auther:
Ray Hu

personal web site:
r.pythoner.work

email:
r@pythoner.work
'''
}
def get_help(key):
    if key in game_help.keys():
        return game_help[key]
    return None
