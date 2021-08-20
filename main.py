import util
import helps



while True:
    flag = True
    print('\n' + '=' * 20 + 'NEW GAME' + '=' * 20 + '\n')
    exit_flag = False
    marks = []
    res = util.get_area()
    area = res[0]
    boom = res[1]
    while flag:
        i = 'str'
        util.print_area(area, marks=marks)
        while True:
            i = input('> ')
            if i == 'cheat':
                print('\n' + '=' * 20 + 'CHEAT' + '=' * 20 + '\n')
                util.print_area(area, True)
                print('\n' + '=' * 50 + '\n')
                continue
            if i == 'printarea':
                util.print_area(area, marks=marks)
                continue
            if i == 'exit':
                exit_flag = True
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
                if len(i) == 8 and util.is_mark_syntax(i) and not (int(i[5]), int(i[7])) in marks:
                    marks.append((int(i[5]), int(i[7])))
                    if util.all_clear(area, marks):
                        flag = False
                        print('YOU WIN')
                        break
                    continue
            except ValueError:
                pass
            if i == 'boom_remaining':
                print(boom - len(marks))
                continue
            if i == '':
                break
            print(util.say(i))
        if flag == False:
            break
        print('\n' + '=' * 50 + '\n')
        util.print_area(area, marks=marks)
        x = input('x ')
        y = input('y ')
        if x == 'exit' or y == 'exit':
            util.exit(x + ' ' +  y)
            exit_flag = True
            break
        x = int(x)
        y = int(y)
        if area[x][y] == '#':
            print('GAME OVER')
            util.print_area(area, True, x, y, marks)
            flag = False
        if area[x][y] == '-':
            area = util.dfs(area, x, y)
        if util.all_clear(area, marks):
            print('YOU WIN')
    if exit_flag:
        print('WELCOME YOUR NEXT COMING!!!!')
        print('GOOD-BYE:)')
        break
