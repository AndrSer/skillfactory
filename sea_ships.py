import random
import re


class ShipLengthLess(Exception):
    value_length: int

    def __init__(self, value):
        self.value_length = value

    def __str__(self):
        return f'Значение длинны корабля length: {self.value_length} < 0'


class ShipDirectionLess(Exception):
    value_direction: int

    def __init__(self, value):
        self.value_direction = value

    def __str__(self):
        return f'Значение направления коробля: {self.value_direction} не равно 0 либо 1'


class ShipHealthLess(Exception):
    value_health: int

    def __init__(self, value):
        self.value_health = value

    def __str__(self):
        return f'Значение здоровья коробля: {self.value_health} не в диапазоне от 1 до 4ех'


class PropertyHidLess(Exception):
    def __init__(self, hid):
        self.hid = hid

    def __str__(self):
        return f'Значение флага hid: {self.hid} не является булевым значением'


class CountAliveLess(Exception):
    count_alive: int

    def __init__(self, value):
        self.count_alive = value

    def __str__(self):
        return f'Количество живых кораблей: {self.count_alive} не может быть меньше 0'


class SymbolLess(Exception):
    symbol: str

    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return f'Символ: {self.symbol} не является символом X, M или O'


class OutOfBoardException(Exception):
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Координаты: {self.x}, {self.y} находится за пределами игрового поля'


class AddShipException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Установить корабль в такой конфигурации нельзя'


class DotTypeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Координата точки: {self.value} не является целым числом'


class AlreadyMarkDot(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Вы уже стреляли в эту точку'


class Dot:
    cord_x: int
    cord_y: int
    symbol: str

    def __init__(self, **kwargs):
        if not kwargs:
            self.cord_x = 0
            self.cord_y = 0
            self.symbol = 'O'
        else:
            self.property_cord_x = kwargs.get('x')
            self.property_cord_y = kwargs.get('y')
            self.property_symbol = kwargs.get('symbol')

    @property
    def property_cord_x(self):
        return self.cord_x

    @property
    def property_cord_y(self):
        return self.cord_y

    @property
    def property_symbol(self):
        return self.symbol

    @property_cord_x.setter
    def property_cord_x(self, value_x):
        if type(value_x) is int:
            self.cord_x = value_x
        else:
            raise DotTypeException(value_x)

    @property_cord_y.setter
    def property_cord_y(self, value_y):
        if type(value_y) is int:
            self.cord_y = value_y
        else:
            raise DotTypeException(value_y)

    @property_symbol.setter
    def property_symbol(self, symbol):
        if symbol.upper() in ['X', 'O', 'M']:
            self.symbol = symbol.upper()
        else:
            raise SymbolLess(symbol)

    def __eq__(self, other):
        return True if other.cord_x == self.property_cord_x and \
                       other.cord_y == self.property_cord_y and \
                       other.symbol == self.property_symbol else False


class Ship:
    ship_length: int
    dot_nose_ship: Dot
    ship_direction: int
    health: int
    all_dots: list

    def __init__(self):
        self.ship_length = 1
        self.ship_direction = 0
        self.health = self.property_ship_length
        self.all_dots = []

    @property
    def property_ship_length(self):
        return self.ship_length

    @property
    def property_dot_nose_ship(self):
        return self.dot_nose_ship

    @property
    def property_ship_direction(self):
        return self.ship_direction

    @property
    def property_ship_health(self):
        return self.health

    @property
    def property_all_dots(self):
        return self.all_dots

    @property_all_dots.setter
    def property_all_dots(self, input_dot: Dot):
        self.all_dots.append(input_dot)

    @property_ship_length.setter
    def property_ship_length(self, value_length):
        if value_length > 0:
            self.ship_length = value_length
        else:
            raise ShipLengthLess(value_length)

    @property_ship_direction.setter
    def property_ship_direction(self, value_direction):
        if value_direction in [0, 1]:
            self.ship_direction = value_direction
        else:
            raise ShipDirectionLess(value_direction)

    @property_ship_health.setter
    def property_ship_health(self, value_health):
        if value_health in range(0, 4):
            self.health = value_health
        else:
            raise ShipHealthLess(value_health)

    @property_dot_nose_ship.setter
    def property_dot_nose_ship(self, dot_nose_p: Dot):
        self.dot_nose_ship = dot_nose_p


class Board:
    list_cells: list
    list_cells_hide: list
    list_ships: list
    list_contour_ships: list
    hid: bool
    count_alive_ships: int

    def __init__(self):
        self.list_cells = [['b', 'A', 'B', 'C', 'D', 'E', 'F'],
                           ['1', '-', '-', '-', '-', '-', '-'],
                           ['2', '-', '-', '-', '-', '-', '-'],
                           ['3', '-', '-', '-', '-', '-', '-'],
                           ['4', '-', '-', '-', '-', '-', '-'],
                           ['5', '-', '-', '-', '-', '-', '-'],
                           ['6', '-', '-', '-', '-', '-', '-']]
        self.list_cells_hide = [['b', 'A', 'B', 'C', 'D', 'E', 'F'],
                                ['1', '-', '-', '-', '-', '-', '-'],
                                ['2', '-', '-', '-', '-', '-', '-'],
                                ['3', '-', '-', '-', '-', '-', '-'],
                                ['4', '-', '-', '-', '-', '-', '-'],
                                ['5', '-', '-', '-', '-', '-', '-'],
                                ['6', '-', '-', '-', '-', '-', '-']]
        self.list_ships = []
        self.list_contour_ships = []
        self.hid = False
        self.count_alive_ships = 0

    @property
    def property_list_cells(self):
        return self.list_cells

    @property
    def property_list_cells_hide(self):
        return self.list_cells_hide

    @property
    def property_list_ships(self):
        return self.list_ships

    @property
    def property_list_contour_ships(self):
        return self.list_contour_ships

    @property
    def property_hid(self):
        return self.hid

    @property
    def property_count_alive_ships(self):
        return self.count_alive_ships

    @property_list_contour_ships.setter
    def property_list_contour_ships(self, dot):
        self.property_list_contour_ships.append(dot)

    @property_list_cells.setter
    def property_list_cells(self, dot: Dot):
        self.list_cells[dot.property_cord_x + 1][dot.property_cord_y + 1] = dot.property_symbol

    @property_list_cells_hide.setter
    def property_list_cells_hide(self, dot: Dot):
        self.list_cells_hide[dot.property_cord_x + 1][dot.property_cord_y + 1] = dot.property_symbol

    @property_list_ships.setter
    def property_list_ships(self, ship):
        self.list_ships.append(ship)

    @property_hid.setter
    def property_hid(self, hid):
        if type(hid) == bool:
            self.hid = hid
        else:
            raise PropertyHidLess(hid)

    @property_count_alive_ships.setter
    def property_count_alive_ships(self, count_alive):
        if count_alive >= 0:
            self.count_alive_ships = count_alive
        else:
            raise CountAliveLess(count_alive)

    def add_ship(self, ship: Ship):
        if ship.property_ship_length > 1:
            if ship.property_ship_direction == 0:
                start = ship.property_dot_nose_ship
                for dot in ship.property_all_dots:
                    if dot.property_cord_x != start.property_cord_x + 1 or \
                            dot.property_cord_y != start.property_cord_y:
                        raise AddShipException
                    else:
                        start = dot
            elif ship.property_ship_direction == 1:
                start = ship.property_dot_nose_ship
                for dot in ship.property_all_dots:
                    if dot.property_cord_x != start.property_cord_x or \
                            dot.property_cord_y != start.property_cord_y + 1:
                        raise AddShipException
                    else:
                        start = dot
            self.property_list_cells = ship.property_dot_nose_ship
            for dot in ship.property_all_dots:
                self.property_list_cells = dot
            self.property_list_ships = ship
        else:
            self.property_list_cells = ship.property_dot_nose_ship
            self.property_list_ships = ship

    def contour(self, ship: Ship):
        first_dot: Dot = ship.property_dot_nose_ship
        last_dot: Dot
        list_dots_start = None
        list_dots_end = None

        if ship.property_ship_direction == 0:
            list_dots_start = [Dot(x=first_dot.property_cord_x,
                                   y=first_dot.property_cord_y - 1,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x,
                                   y=first_dot.property_cord_y + 1,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x - 1,
                                   y=first_dot.property_cord_y,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x - 1,
                                   y=first_dot.property_cord_y + 1,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x - 1,
                                   y=first_dot.property_cord_y - 1,
                                   symbol='O')]
        elif ship.property_ship_direction == 1:
            list_dots_start = [Dot(x=first_dot.property_cord_x + 1,
                                   y=first_dot.property_cord_y,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x - 1,
                                   y=first_dot.property_cord_y,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x,
                                   y=first_dot.property_cord_y - 1,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x + 1,
                                   y=first_dot.property_cord_y - 1,
                                   symbol='O'),
                               Dot(x=first_dot.property_cord_x - 1,
                                   y=first_dot.property_cord_y - 1,
                                   symbol='O')]

        if ship.property_ship_length == 1:
            list_dots_start.append(Dot(x=first_dot.property_cord_x + 1,
                                       y=first_dot.property_cord_y,
                                       symbol='O'))
            list_dots_start.append(Dot(x=first_dot.property_cord_x + 1,
                                       y=first_dot.property_cord_y + 1,
                                       symbol='O'))
            list_dots_start.append(Dot(x=first_dot.property_cord_x + 1,
                                       y=first_dot.property_cord_y - 1,
                                       symbol='O'))
            for i in list_dots_start:
                if i not in self.property_list_contour_ships:
                    self.property_list_contour_ships = i
        elif ship.property_ship_length == 2:
            last_dot = ship.property_all_dots[0]

            if ship.property_ship_direction == 0:
                list_dots_end = [Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y - 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y - 1,
                                     symbol='O')]
            elif ship.property_ship_direction == 1:
                list_dots_end = [Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x - 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x - 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O')]
            for i in list_dots_start + list_dots_end:
                if i not in self.property_list_contour_ships:
                    self.property_list_contour_ships = i
        elif ship.property_ship_length > 2:
            last_dot: Dot = ship.property_all_dots[-1]
            list_dots_end = []

            if ship.property_ship_direction == 0:
                list_dots_end = [Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y - 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y - 1,
                                     symbol='O')]
            elif ship.property_ship_direction == 1:
                list_dots_end = [Dot(x=last_dot.property_cord_x,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x - 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x - 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O'),
                                 Dot(x=last_dot.property_cord_x + 1,
                                     y=last_dot.property_cord_y + 1,
                                     symbol='O')]
            list_dots = []
            for dot in ship.property_all_dots[0:-1]:
                if ship.property_ship_direction == 0:
                    list_dots.append(Dot(x=dot.property_cord_x,
                                         y=dot.property_cord_y + 1,
                                         symbol='O'))
                    list_dots.append(Dot(x=dot.property_cord_x,
                                         y=dot.property_cord_y - 1,
                                         symbol='O'))
                else:
                    list_dots.append(Dot(x=dot.property_cord_x + 1,
                                         y=dot.property_cord_y,
                                         symbol='O'))
                    list_dots.append(Dot(x=dot.property_cord_x - 1,
                                         y=dot.property_cord_y,
                                         symbol='O'))
            for i in list_dots_start + list_dots + list_dots_end:
                if i not in self.property_list_contour_ships:
                    self.property_list_contour_ships = i

    def board_hid(self):
        if not self.hid:
            for row in self.property_list_cells:
                for x in row:
                    print("{:4s}".format(x), end="")
                print()
        else:
            for row in self.property_list_cells_hide:
                for x in row:
                    print("{:4s}".format(x), end="")
                print()
        print()

    def out(self, dot: Dot) -> bool:
        if 0 <= dot.property_cord_x < len(self.list_cells) - 1 and \
                0 <= dot.property_cord_y < len(self.list_cells) - 1:
            return False
        else:
            return True

    def shot(self, new_dot: Dot) -> bool:
        if self.out(new_dot):
            raise OutOfBoardException(new_dot.property_cord_x, new_dot.property_cord_y)
        else:
            for ship in self.property_list_ships:
                if new_dot.__eq__(ship.property_dot_nose_ship):
                    new_dot.property_symbol = 'x'
                    ship.property_dot_nose_ship.property_symbol = 'x'
                    ship.property_ship_health -= 1
                    if ship.property_ship_health == 0:
                        self.property_count_alive_ships -= 1
                        print(f'Корабль уничтожен')
                    self.property_list_cells = new_dot
                    self.property_list_cells_hide = new_dot
                    break
                else:
                    if ship.property_dot_nose_ship.property_cord_x == new_dot.property_cord_x \
                            and ship.property_dot_nose_ship.property_cord_y == new_dot.property_cord_y:
                        raise AlreadyMarkDot
                for dot in ship.property_all_dots:
                    if new_dot.__eq__(dot):
                        new_dot.property_symbol = 'x'
                        dot.property_symbol = 'x'
                        ship.property_ship_health -= 1
                        if ship.property_ship_health == 0:
                            self.property_count_alive_ships -= 1
                            print(f'Корабль уничтожен')
                        self.property_list_cells = new_dot
                        self.property_list_cells_hide = new_dot
                        break
                    else:
                        if dot.property_cord_x == new_dot.property_cord_x \
                                and dot.property_cord_y == new_dot.property_cord_y:
                            raise AlreadyMarkDot
                if new_dot.property_symbol == 'x':
                    break
            if new_dot.property_symbol == 'O':
                new_dot.property_symbol = 'm'
                self.property_list_cells = new_dot
                self.property_list_cells_hide = new_dot
        return True if new_dot.property_symbol == 'X' else False


class Player:
    its_board: Board
    enemy_board: Board

    def __init__(self, its_board: Board, board: Board):
        self.property_its_board = its_board
        self.property_enemy_board = board

    def ask(self) -> Dot:
        pass

    def move(self, board: Board):
        try:
            new_dot = self.ask()
            return board.shot(new_dot)
        except OutOfBoardException:
            print('Ход выполняется еще раз выстрел за пределы доски')
            self.move(board)
        except AlreadyMarkDot:
            print('Ход выполняется еще раз. В эту точку уже был выстрел')
            self.move(board)


class AI(Player):
    def ask(self):
        print('Компьютер делает ход\r')
        cord_x = random.choice(range(0, len(its_bord.property_list_cells) - 1))
        cord_y = random.choice(range(0, len(its_bord.property_list_cells) - 1))
        return Dot(x=cord_x, y=cord_y, symbol='o')


class User(Player):
    transliteration = {'A': 0, 'B': 1, 'C': 2,
                       'D': 3, 'E': 4, 'F': 5}

    def ask(self):
        print('Игрок делает ход\r')
        position = ''
        flag_ask = False
        new_dot = Dot()

        while not flag_ask:
            print('Ходите (Введите координату слитно):\r')
            position = input()
            if not re.fullmatch('^[A-Fa-f]\\d|q$', position):
                print('Паттерн строки не совпадает. Введите координаты согласно условию.\r')
            elif position == 'q':
                exit()
            else:
                flag_ask = True
        new_dot.property_cord_x = int(position[1]) - 1
        new_dot.property_cord_y = self.transliteration.get(position[0].upper())
        new_dot.property_symbol = 'o'
        return new_dot


class Game:
    user: User
    its_board: Board
    enemy: AI
    enemy_board: Board
    numbers_ships: dict

    def __init__(self, user: User, enemy: AI, its_board: Board, board: Board):
        self.user = user
        self.its_board = its_board
        self.enemy = enemy
        self.enemy_board = board
        self.numbers_ships = {3: 1, 2: 2, 1: 4}

    def random_board(self, board: Board):
        symbol = 'o'
        list_not_available_dots = []
        lis = []
        j = 0
        for i in range(0, len(board.property_list_cells) - 1):
            for k in range(0, len(board.property_list_cells) - 1):
                temp_list = [j, k]
                lis.append(temp_list)
            j += 1

        for i in range(0, self.numbers_ships.get(3)):
            three_deck_ship = Ship()
            three_deck_ship.property_ship_length = 3
            three_deck_ship.property_ship_health = three_deck_ship.property_ship_length
            three_deck_ship.property_ship_direction = random.choice([0, 1])

            if three_deck_ship.property_ship_direction == 0:
                x = random.choice(range(0, len(board.property_list_cells) -
                                        three_deck_ship.property_ship_length))
                y = random.choice(range(0, len(board.property_list_cells) - 1))
                three_deck_ship.property_dot_nose_ship = Dot(x=x, y=y, symbol=symbol)
                list_not_available_dots.append(Dot(x=x, y=y, symbol=symbol))

                for j in range(1, three_deck_ship.property_ship_length):
                    x = three_deck_ship.property_dot_nose_ship.property_cord_x + j
                    y = three_deck_ship.property_dot_nose_ship.property_cord_y
                    three_deck_ship.property_all_dots = Dot(x=x, y=y, symbol=symbol)
                    list_not_available_dots.append(Dot(x=x, y=y, symbol=symbol))
                board.add_ship(three_deck_ship)
                board.contour(three_deck_ship)
            elif three_deck_ship.property_ship_direction == 1:
                x = random.choice(range(0, len(board.property_list_cells) - 1))
                y = random.choice(range(0, len(board.property_list_cells) -
                                        three_deck_ship.property_ship_length))
                three_deck_ship.property_dot_nose_ship = Dot(x=x, y=y, symbol=symbol)
                list_not_available_dots.append(Dot(x=x, y=y, symbol=symbol))
                for j in range(1, three_deck_ship.property_ship_length):
                    x = three_deck_ship.property_dot_nose_ship.property_cord_x
                    y = three_deck_ship.property_dot_nose_ship.property_cord_y + j
                    three_deck_ship.property_all_dots = Dot(x=x, y=y, symbol=symbol)
                    list_not_available_dots.append(Dot(x=x, y=y, symbol=symbol))
                board.add_ship(three_deck_ship)
                board.contour(three_deck_ship)
            board.property_count_alive_ships += 1

        try:
            for i in range(0, self.numbers_ships.get(2)):
                two_deck_ship = Ship()
                two_deck_ship.property_ship_length = 2
                two_deck_ship.property_ship_health = two_deck_ship.property_ship_length
                two_deck_ship.ship_direction = random.choice([0, 1])
                temp_dots_list = []
                not_available_list_cords = []
                for cord in list_not_available_dots + board.property_list_contour_ships:
                    temp_list = [cord.property_cord_x, cord.property_cord_y]
                    not_available_list_cords.append(temp_list)
                list_available_cords = [i for i in lis if i not in not_available_list_cords]

                if two_deck_ship.property_ship_direction == 0:
                    flag_stop = False
                    while not flag_stop:
                        list_random_cord = random.choice(list_available_cords)
                        x = list_random_cord[0]
                        y = list_random_cord[1]
                        temp_dots_list = [Dot(x=x, y=y, symbol=symbol)]
                        for j in range(1, two_deck_ship.property_ship_length):
                            x = temp_dots_list[0].property_cord_x + j
                            y = temp_dots_list[0].property_cord_y
                            temp_dots_list.append(Dot(x=x, y=y, symbol=symbol))

                        if (temp_dots_list[0] and temp_dots_list[1] not in board.property_list_contour_ships) and \
                                (temp_dots_list[0] and temp_dots_list[1] not in list_not_available_dots) and \
                                (temp_dots_list[1].property_cord_x <= len(board.property_list_cells) - 2):
                            flag_stop = True

                    two_deck_ship.property_dot_nose_ship = temp_dots_list[0]
                    list_not_available_dots.append(temp_dots_list[0])
                    two_deck_ship.property_all_dots = temp_dots_list[1]
                    list_not_available_dots.append(temp_dots_list[1])
                    board.add_ship(two_deck_ship)
                    board.contour(two_deck_ship)
                elif two_deck_ship.property_ship_direction == 1:
                    flag_stop = False
                    while not flag_stop:
                        list_random_cord = random.choice(list_available_cords)
                        x = list_random_cord[0]
                        y = list_random_cord[1]
                        temp_dots_list = [Dot(x=x, y=y, symbol=symbol)]
                        for j in range(1, two_deck_ship.property_ship_length):
                            x = temp_dots_list[0].property_cord_x
                            y = temp_dots_list[0].property_cord_y + j
                            temp_dots_list.append(Dot(x=x, y=y, symbol=symbol))

                        if (temp_dots_list[0] and temp_dots_list[1] not in board.property_list_contour_ships) and \
                                (temp_dots_list[0] and temp_dots_list[1] not in list_not_available_dots) and \
                                (temp_dots_list[1].property_cord_y <= len(board.property_list_cells) - 2):
                            flag_stop = True

                    two_deck_ship.property_dot_nose_ship = temp_dots_list[0]
                    list_not_available_dots.append(temp_dots_list[0])
                    two_deck_ship.property_all_dots = temp_dots_list[1]
                    list_not_available_dots.append(temp_dots_list[1])
                    board.add_ship(two_deck_ship)
                    board.contour(two_deck_ship)
                board.property_count_alive_ships += 1

            for i in range(0, self.numbers_ships.get(1)):
                one_deck_ship = Ship()
                one_deck_ship.property_ship_length = 1
                one_deck_ship.property_ship_health = one_deck_ship.property_ship_length
                temp_dot = Dot()
                not_available_list_cords = []
                for cord in list_not_available_dots + board.property_list_contour_ships:
                    temp_list = [cord.property_cord_x, cord.property_cord_y]
                    not_available_list_cords.append(temp_list)
                list_available_cords = [i for i in lis if i not in not_available_list_cords]

                flag_stop = False
                while not flag_stop:
                    list_random_cord = random.choice(list_available_cords)
                    x = list_random_cord[0]
                    y = list_random_cord[1]
                    temp_dot.property_cord_x = x
                    temp_dot.property_cord_y = y
                    temp_dot.property_symbol = symbol

                    if temp_dot not in board.property_list_contour_ships and \
                            temp_dot not in list_not_available_dots:
                        flag_stop = True

                one_deck_ship.property_dot_nose_ship = temp_dot
                list_not_available_dots.append(temp_dot)
                board.add_ship(one_deck_ship)
                board.contour(one_deck_ship)
                board.property_count_alive_ships += 1
            return board
        except IndexError:
            pass

    @staticmethod
    def greet():
        greetings = """                       Свистать всех наверх! 
                       Добро пожаловать в упрощенную версию игры морской бой: 
                       1) Игровое поле 6x6 
                       2) Корабли расставлются случайным образом
                       3) Вид кораблей только линейный
                       4) Направление кораблей - горизонтальное либо вертикальное 
                       5) На поле может располагаться: 
                          1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку
                       6) Компьютер ходит первый 
                       7) Промахи обозначаются литерой M, попадания - X
                       8) Чтобы выйти из игры введите q"""
        return greetings

    def loop(self):
        try:
            self.random_board(self.its_board)
            self.random_board(self.enemy_board)
        except IndexError:
            self.random_board(self.its_board)
            self.random_board(self.enemy_board)

        while True:
            print('Ваше игровое поле:\r')
            self.its_board.board_hid()
            print('Игровое поле компьютера:\r')
            self.enemy_board.board_hid()
            move_comp = self.enemy.move(its_bord)
            while move_comp:
                print('Компьютер вас подбил! Он ходит еще раз\r')
                print('Ваше игровое поле:\r')
                self.its_board.board_hid()
                print('Игровое поле компьютера:\r')
                self.enemy_board.board_hid()
                if self.its_board.property_count_alive_ships == 0:
                    break
                move_comp = self.enemy.move(its_bord)
                if not move_comp:
                    print('Компьютер промахнулся. Ваш ход.')

            print('Ваше игровое поле:\r')
            self.its_board.board_hid()
            print('Игровое поле компьютера:\r')
            self.enemy_board.board_hid()
            move_user = self.user.move(enemy_board)
            while move_user:
                print('Вы подбили компьютер!\r')
                print('Ваше игровое поле:\r')
                self.its_board.board_hid()
                print('Игровое поле компьютера:\r')
                self.enemy_board.board_hid()
                if self.enemy_board.property_count_alive_ships == 0:
                    break
                move_user = self.user.move(enemy_board)
                if not move_user:
                    print('Вы промахнулись. Ход за компьютером')
            count_alive_its = self.its_board.property_count_alive_ships
            count_alive_enemy = self.enemy_board.property_count_alive_ships
            if count_alive_its == 0 or count_alive_enemy == 0:
                if count_alive_its == 0:
                    print('Компьютер победил\r')
                elif count_alive_enemy == 0:
                    print('Поздравляем, вы победили!\r')
                print('Игра окончена.')
                exit()

    def start(self):
        print(self.greet(), '\r')
        flag_ask = False
        ask = ''

        while not flag_ask:
            print('Начать игру? (введите y - да, n - нет):')
            ask = input()
            if not re.match('^y|n|q$', ask):
                print('Паттерн строки не совпадает.\r')
            elif ask == 'q':
                exit()
            else:
                flag_ask = True
        if ask == 'n':
            exit()
        elif ask == 'y':
            self.loop()
        self.loop()


if __name__ == "__main__":
    its_bord = Board()
    enemy_board = Board()
    enemy_board.property_hid = True

    game = Game(User(its_bord, enemy_board), AI(its_bord, enemy_board), its_bord, enemy_board)
    game.start()
