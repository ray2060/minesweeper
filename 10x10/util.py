from settings import *
import random as r
import re
from exceptions___ import Exit



def is_boom(area, x, y):
    return area[x][y] == '#'


def is_num(area, x, y):
    try:
        i = int(area[x][y])
    except ValueError:
        return False
    return True


def print_area(area, show_boom=False, x=INF, y=INF, marks=[]):
    print(' ', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    for i in range(len(area)):
        print('  ' + '-' * 20)
        print(i, end='')
        print('|', end='')
        for j in range(len(area[i])):
            if (i, j) in marks and show_boom:
                if area[i][j] != '#':
                    print('=', end='|')
                else:
                    print('+', end='|')
            elif (i, j) in marks:
                print('=', end='|')
            elif i == x and j == y:
                print('*', end='|')
            else:
                if not show_boom and area[i][j] == '#':
                    print(' ', end='|')
                else:
                    print(area[i][j], end='|')
        print()


def get_area(s):
    boom = 0
    area = []
    for i in range(10):
        try:
            p = 0.18
        except ZeroDivisionError:
            area.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
            continue
        res1 = []
        for j in range(10):
            r.seed(s)
            s = r.randint(0, s * 3)
            if r.random() <= p and boom < MAX_BOOM:
                res1.append('#')
                boom += 1
            else:
                res1.append(' ')
        area.append(res1)
    return area, boom


def say(s):
    if s == 'idiot1':
        return 'You feel like an idiot.'
    if s == 'idiot2':
        return 'You say, \"I\'m such an idiot.\"'
    if s == 'smart1':
        return 'You say, \"I\'m so smart.\"'
    if s == 'mygod':
        return 'You shout \"MY GOD\" and fall to the ground.'
    if s == 'boom':
        return 'You stepped on a fake bomb, yelled, and passed out.'
    return 'What???'

def is_mark_syntax(s, mode=1):
    if mode == 1:
        r = r'm [0-9] [0-9]'
    else:
        r = r'mark [0-9] [0-9]'
    if re.match(r, s):
        return True
    return False


def is_help_syntax(s):
    r = r'help'
    if re.match(r, s):
        return True
    return False


def is_press_syntax(s, mode=1):
    if mode == 1:
        r = r'p'
    else:
        r = r'press'
    if re.match(r, s):
        return True
    return False


def random_seed():
    return r.randrange(1, 20000000)


def all_clear(area, marks):
    cnt = 0
    for i in range(10):
        for j in range(10):
            if (i, j) in marks or is_num(area, i, j):
                cnt += 1
    return cnt == 100


def is_seed(i):
    try:
        a = int(i)
    except ValueError:
        return False
    return int(i) > 0

def dfs(area, x, y):
    if is_num(area, x, y):
        return area
    # print('dfs(%d, %d)' % (x, y))
    cnt = 0
    if x - 1 >= 0 and y - 1 >= 0 and is_boom(area, x - 1, y - 1):
        cnt += 1
    if y - 1 >= 0 and is_boom(area, x, y - 1):
        cnt += 1
    if y - 1 >= 0 and x + 1 < 10 and is_boom(area, x + 1, y - 1):
        cnt += 1
    if x - 1 >= 0 and is_boom(area, x - 1, y):
        cnt += 1
    if x + 1 < 10 and is_boom(area, x + 1, y):
        cnt += 1
    if y + 1 < 10 and x - 1 >= 0 and is_boom(area, x - 1, y + 1):
        cnt += 1
    if y + 1 < 10 and is_boom(area, x, y + 1):
        cnt += 1
    if y + 1 < 10 and x + 1 < 10 and is_boom(area, x + 1, y + 1):
        cnt += 1
    area[x][y] = str(cnt)
    if cnt:
        return area
    if y - 1 >= 0 and not is_boom(area, x, y - 1):
        area = dfs(area, x, y - 1)
    if x - 1 >= 0 and not is_boom(area, x - 1, y):
        area = dfs(area, x - 1, y)
    if x + 1 < 10 and not is_boom(area, x + 1, y):
        area = dfs(area, x + 1, y)
    if y + 1 < 10 and not is_boom(area, x, y + 1):
        area = dfs(area, x, y + 1)
    return area

def exit(exitcode):
    print(Exit(str(exitcode)))
