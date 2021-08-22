import util
import helps



print('Welcome!')
print('type \'help\' to get help')
flag2 = True
while True:
    flag = True
    print('\n' + '=' * 20 + 'NEW GAME' + '=' * 20 + '\n')
    if flag2:
        print('input minefield\'s seed first')
        print('if you want get a random seed')
        print('type \'newline\'')
        flag2 = False
    seed = input('seed:')
    if seed == '':
        seed = util.random_seed()
    while not util.is_seed(seed):
        print('That\'s not a seed!!!')
        seed = input('try again:')
        if seed == '':
            seed = util.random_seed()
    seed = int(seed)
    exit_flag = False
    marks = []
    res = util.get_area(seed)
    area = res[0]
    boom = res[1]
    while flag:
        i = ''
        util.print_area(area, marks=marks)
        while True:
            i = input('> ')
            if i == 'm':
                while True:
                    j = input('mark mode> ')
                    flag = False
                    try:
                        if j == 'exit':
                            break
                        if len(j) == 3:
                            if not (int(j[0]), int(j[2])) in marks and \
                                       (area[int(j[0])][int(j[2])] == ' ' or area[int(j[0])][int(j[2])] == '#'):
                                marks.append((int(j[0]), int(j[2])))
                                util.print_area(area, marks=marks)
                                flag = True
                    except SyntaxError:
                        print('What???')
                        flag = True
                    if not flag:
                        print('What???')
                continue
            if i == 'cheat':
                print('\n' + '=' * 20 + 'CHEAT' + '=' * 20 + '\n')
                util.print_area(area, True, marks=marks)
                print('\n' + '=' * 50 + '\n')
                continue
            if i == 'printarea':
                util.print_area(area, marks=marks)
                continue
            if i == 'exit':
                exit_flag = True
                flag = False
                break
            if i == 'seed':
                print(seed)
                continue
            if i == 'new':
                flag = False
                break
            if len(i) > 5 and util.is_help_syntax(i):
                res = helps.get_help(i[5:])
                if res:
                    print(res)
                    continue
            if i == 'help':
                print(helps.get_help('CONTENTS'))
                continue
            try:
                if len(i) == 8 and util.is_mark_syntax(i, 2) and \
                           not (int(i[5]), int(i[7])) in marks and \
                           (area[int(i[5])][int(i[7])] == ' ' or area[int(i[5])][int(i[7])] == '#'):
                    marks.append((int(i[5]), int(i[7])))
                    util.print_area(area, marks=marks)
                    if util.all_clear(area, marks):
                        flag = False
                        print('YOU WIN')
                        break
                    continue
            except ValueError:
                pass
            try:
                if len(i) == 5 and util.is_mark_syntax(i) and\
                           not (int(i[2]), int(i[4])) in marks and \
                           (area[int(i[2])][int(i[4])] == ' ' or area[int(i[2])][int(i[4])] == '#'):
                    marks.append((int(i[2]), int(i[4])))
                    util.print_area(area, marks=marks)
                    if util.all_clear(area, marks):
                        flag = False
                        print('YOU WIN')
                        break
                    continue
            except ValueError:
                pass
            try:
                if len(i) == 9 and util.is_press_syntax(i, 2) and (int(i[6]), int(i[8])):
                    x = int(i[6])
                    y = int(i[8])
                    if area[x][y] == '#':
                        print('GAME OVER')
                        util.print_area(area, True, x, y, marks)
                        flag = False
                    if area[x][y] == ' ':
                        area = util.dfs(area, x, y)
                    util.print_area(area, marks=marks)
                    if util.all_clear(area, marks):
                        print('YOU WIN')
                    continue
            except ValueError:
                pass
            try:
                if len(i) == 5 and util.is_press_syntax(i) and (int(i[2]), int(i[4])):
                    x = int(i[2])
                    y = int(i[4])
                    if area[x][y] == '#':
                        print('GAME OVER')
                        util.print_area(area, True, x, y, marks)
                        flag = False
                    if area[x][y] == ' ':
                        area = util.dfs(area, x, y)
                    util.print_area(area, marks=marks)
                    if util.all_clear(area, marks):
                        print('YOU WIN')
                    continue
            except ValueError:
                pass
            if i == 're_mines':
                print(boom - len(marks))
                continue
            if i == '':
                continue
            print(util.say(i))
        if flag == False:
            break
    if exit_flag:
        print('WELCOME YOUR NEXT COMING!!!!')
        print('GOOD-BYE:)')
        break
