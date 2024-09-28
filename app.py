"""Следующие 3 строки - переменные для строк поля(с 1 по 3 строку)"""
line1 = [[' '], [' '], [' ']]
line2 = [[' '], [' '], [' ']]
line3 = [[' '], [' '], [' ']]
line_list = [line1, line2, line3] #список для удобной нумерации линий
"""Следующие 3 строки - вывод поля для игры"""
print(line1)
print(line2)
print(line3)


def win_first(line1, line2, line3):
    flag = 0
    if (line1 == [['×'], ['×'], ['×']] or line2 == [['×'], ['×'], ['×']] or
        line3 == [['×'], ['×'], ['×']] or
        (line1[0] == line2[0] == line3[0] == ['×']) or
        (line1[1] == line2[1] == line3[1] == ['×']) or
        (line1[2] == line2[2] == line3[2] == ['×']) or
        (line1[0] == line2[1] == line3[2] == ['×']) or
        (line1[2] == line2[1] == line3[0] == ['×'])):
        flag = 1
    return flag


def win_second(line1, line2, line3):
    flag = 0
    if (line1 == [['0'], ['0'],['0']] or line2 == [['0'], ['0'], ['0']] or
            line3 == [['0'], ['0'], ['0']] or
        (line1[0] == line2[0] == line3[0] == ['0']) or
            (line1[1] == line2[1] == line3[1] == ['0']) or
        (line1[2] == line2[2] == line3[2] == ['0']) or
        (line1[0] == line2[1] == line3[2] == ['0']) or
            (line1[2] == line2[1] == line3[0] == ['0'])) ==1:
        flag = 1
    return flag


def end(line1, line2, line3):
    flag = 0
    if (line1[0] == line2[0] == line3[0] != [' '] or 
        line1[1] == line2[1] == line3[1] != [' '] or 
        line1[2] == line2[2] == line3[2] != [' '] or 
        line1[0] == line1[1] == line1[2] != [' '] or 
        line2[0] == line2[1] == line2[2] != [' '] or 
        line3[0] == line3[1] == line3[2] != [' '] or 
        line1[0] == line2[1] == line3[2] != [' '] or 
        line1[2] == line2[1] == line3[0] != [' '] or
        line1.count([' ']) + line2.count([' ']) + line3.count([' ']) == 0):
        flag = 1
    return flag       
count = 0 #счетчик четности хода(четное-первый игрок, нечетное - второй)


while end(line1, line2, line3) != 1:
    if count%2 == 0:
        player = 'Первый игрок'
    else:
        player = 'Второй игрок'
    argument = 0 #переменная для проверки того, сделан ли ход игроком
    '''Цикл while работает до тех пор пока игрок не сделает ход'''
    while argument != 1:
        '''arg_move - переменная для проверки корректности данных,
    введенных первым игроком'''
        arg_move = 0 
        '''Цикл while работает до тех пор пока игрок не введет подходящие
        значения(целое число от 1 до 3 вкл), это нужно для того чтобы потом
        программа не прекращалась из-за ошибки'''
        while arg_move != 1:
            move_line = input(f"{player}, введите номер строки, на" + '\n' +
                              'которой хотите поставить знак '
                               '(целое число от 1 до 3): \n')
            move_column = input(f"{player}, введите номер строки, на" + '\n' +
                              'которой хотите поставить знак '
                               '(целое число от 1 до 3): \n')
            if (move_line in ['1', '2', '3'] and move_column in
                ['1', '2', '3']):
                arg_move = 1 #данные удовл. условиям, присваиваем 1
                move_line = int(move_line) #перевод в int для индексации
                move_column = int(move_column) #перевод в int для индексации
            else:
                print('Ошибка, введите целое число от 1 до 3 вкл \n')
        '''Если клетка, запрошенная игроком пуста, присвоим
        ей нужное значение'''
        if count%2==0:
            if line_list[move_line-1][move_column-1] == [' ']:
                line_list[move_line-1][move_column-1] = ['×']
                argument = 1 #ход сделан успешно, присваиваем единицу
                count += 1 #ход сделан успешно, присваиваем единицу
            else:
                print('На этой клетке уже стоит знак, поставьте знак '
                      'на пустую клетку \n')
        else:
            if line_list[move_line-1][move_column-1] == [' ']:
                line_list[move_line-1][move_column-1] = ['0']
                argument = 1#ход сделан успешно, присваиваем единицу
                count += 1 #ход сделан успешно, присваиваем единицу
            else:
                print('На этой клетке уже стоит знак, поставьте знак '
                      'на пустую клетку \n')
    '''Вывод игрового поля'''
    print(line1)
    print(line2)
    print(line3)
if win_first(line1, line2, line3):
    print('Победил первый игрок')
elif win_second(line1, line2, line3):
    print('Победил второй игрок')
else:
    print('Ничья')


input("Нажмите Enter для выхода!")






    
    
    


