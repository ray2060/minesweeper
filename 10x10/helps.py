game_help = {
    'CONTENTS':'''

CONTENTS


keywords 1 ......... help 1
keywords 2 ......... help 2
history ............ help 3
auxiliary function . help 4
mark mode .......... help 5
symbols ............ help 6
author ............. help 0
''', 

    '1':'''
keywords 1

meaning ----------- func
press ------------- press <x> <y>
         for short: p <x> <y>
mark -------------- mark <x> <y>
         for short: m <x> <y>
mark mode --------- m
         about mark mode: help 5
exit -------------- exit
get seed ---------- seed
new minefield ----- new
get minefield ----- printarea


next page:help 2
contents:help CONTENTS
''', 

    '2':'''
keywords 2

get remaining mines - re_mines
cheat --------------- cheat

next page:help 3
contents:help CONTENTS
''', 

    '3':'''
history


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

    '5':'''
mark mode

type 'm' to set mark mode
when you are marking
input like this:
> m
mark mode> 0 0
  0 1 2 3 4 5 6 7 8 9
  --------------------
0|=|1| | | | | | | | |
  --------------------
1|1|1| | | | | | | | |
  --------------------
2|0|0|1| | | | | | | |
  --------------------
3|1|1| | | | | | | | |
  --------------------
4| | | | | | | | | | |
  --------------------
5| | | | | | | | | | |
  --------------------
6| | | | | | | | | | |
  --------------------
7| | | | | | | | | | |
  --------------------
8| | | | | | | | | | |
  --------------------
9| | | | | | | | | | |
mark mode> exit
>

next page: help 6
''',

    '6':'''
symbols


+ true mark
= mark
' ' non-pressed
0 1 2 3 4 5 6 7 8 pressed
# boom
* blown boom
''', 

    '0':'''
author:
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
