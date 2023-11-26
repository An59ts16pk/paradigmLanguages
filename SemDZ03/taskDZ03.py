# Использованы парадигмы ООП и процедурная
# В классах ООП задаём игровое поле и игроков,
# что позволяет не допускать измениния их полей из вне и делает ограниченный доступ
# к их значениям, а процедурной реализована логика игры без использования GOTO
import random

class Board():
    def __init__(self, brd_list):
        self.brd_list = brd_list

    # Метод выводит в консоль игровое поле   
    def board_prn(self):
        brd = list(range(1, 10))
        print("+{}+{}+{}+".format('-' * 9, '-' * 9, '-' * 9))
        for i in range(3):
            print("|{: ^9}|{: ^9}|{: ^9}|".format(self.brd_list[brd[0+i*3]], self.brd_list[brd[1+i*3]],
                self.brd_list[brd[2+i*3]]))
            print("+{}+{}+{}+".format('-' * 9, '-' * 9, '-' * 9))

    # Метод определяет - клетка занята или свободна
    def check_cell(self, num_cell):
        if self.brd_list[num_cell] == '0' or self.brd_list[num_cell] == 'X':
            print('Клетка номер: ', num_cell, '- занята. Введите другой номер от 1 до 9!')
            return False
        return True

    # Метод определяет победные комбинации клеток    
    def check_win(self):
        win_comb = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9))
        for i_cell in win_comb:
            if self.brd_list[i_cell[0]] == self.brd_list[i_cell[1]] == self.brd_list[i_cell[2]]:
                return self.brd_list[i_cell[0]]
        return False

class Player():
    def __init__(self, name):
        self.name = name
        self.playerlist = ['0']
        self.playerlist.append(name)

    def set_sign(self, sign):
        self.playerlist[0] = sign

    def get_sign(self):
        return self.playerlist[0]
    
    def get_name(self):
        return self.playerlist[1]
    
def gamerInit(): # функция инициализации игры и игроков
    gamerList = []

    print('\nИгра "Крестики - Нолики" на два игрока.\n')
    numName = random.randint(1, 2) # кто ходит первым
    numSign = random.randint(1, 2) # знак игрока

    name_1 = input('Первый игрок - Введите Ваше имя: ')
    name_2 = input('Второй игрок - Введите Ваше имя: ')
    player_1 = Player(name_1) 
    player_2 = Player(name_2)

    if numSign == 1:
        player_2.set_sign('X')
    else:
        player_1.set_sign('X')
    
    print('\nВыбираем случайно - за кем будет первый ход и знак для хода')
    if numName == 1:
        print('Первым ходит игрок: {} и ваш знак для хода: {}'.format(player_1.get_name(), player_1.get_sign()))
        print('Вторым ходит игрок: {} и ваш знак для хода: {}'.format(player_2.get_name(), player_2.get_sign()))
        gamerList.append(player_1)
        gamerList.append(player_2)
    else:
        print('Первым ходит игрок: {} и ваш знак для хода: {}'.format(player_2.get_name(), player_2.get_sign()))
        print('Вторым ходит игрок: {} и ваш знак для хода: {}'.format(player_1.get_name(), player_1.get_sign()))
        gamerList.append(player_2)
        gamerList.append(player_1)
    
    return gamerList

def gameRun(): # запуск и логика игры
    board_list = {1: '1 cell', 2: '2 cell', 3: '3 cell', 4: '4 cell', 5: '5 cell', 6: '6 cell', 7: '7 cell',
                  8: '8 cell', 9: '9 cell'} # перврначальное заполнение клеток board
    boardGame = Board(board_list)

    listGamer = gamerInit()
    gamer_1 = listGamer[0]
    gamer_2 = listGamer[1]

    print('Исходная доска игры:')
    boardGame.board_prn()

    print('\nИгрок вводит число от 1 до 9 - номер клетки, куда ставится Ваш знак.')
    print('Для выхода введите: q\n')

    flag1 = True
    count = 0
    out = ''
    while flag1:
        for i_gamer in range(1, 3):
            if out == 'q':
                break
            if count == 9:
                print('Ничья. Общее кол-во ходов - 9.')
                flag1 = False
                break
            
            count += 1
            if i_gamer == 1:
                gamer = gamer_1
            else:
                gamer = gamer_2
            print('{} ваш ход (ваш знак {}):'.format(gamer.get_name(), gamer.get_sign()))

            flag2 = True
            while flag2:
                print('    Если хотите выйти из игры - введите: q')
                player_answer = input('    Введите число от 1 до 9: ')

                if '1' <= player_answer <= '9' and player_answer != 'q':
                    pl_answer = int(player_answer)
                    if boardGame.check_cell(pl_answer):
                        board_list[pl_answer] = gamer.get_sign()
                        print('    {} Вы успешно сделали ход в клетку номер: {}'.format(gamer.get_name(), pl_answer))
                        break
                    else:
                        print('    {} Сделайте ход в другую клетку.'.format(gamer.get_name()))

                elif player_answer == 'q':
                    out = 'q'
                    flag1 = False
                    flag2 = False
                    print('Игрок {} сдался и вышел из игры'.format(gamer.get_name()))
                    gmr = ''
                    if gamer.get_name() != gamer_1.get_name():
                        gmr = gamer_1.get_name()
                    else:
                        gmr = gamer_2.get_name()
                    print('Победил игрок - {}'.format(gmr))
                
                else:
                    print('Вы ввели неизвестный знак. Введите число от 1 до 9 - номер клетки.')

            symbol = boardGame.check_win()
            boardGame.board_prn()
            if flag2 and symbol == gamer.get_sign():
                print('      Ура. Победил {} на {} ходе'.format(gamer.get_name(), count))
                print('      Конец игры.')
                flag1 = False
                break

gameRun()