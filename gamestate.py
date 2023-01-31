import locations.pluto
import locations.uranus
import locations.uranus_shop
import locations.rock_encounter


class Gamestate:
    def __init__(self):

        row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        row2 = ["A", "S", "D", "F", "G", "H", "J", "=", "L", " "]
        row3 = ["Z", "X", "C", "V", "B", "N", "M", " ", " ", " "]
        self.rows = [row1, row2, row3]

        self.index = [2, 1]
        self.row = self.rows[self.index[1]]
        self.letter = self.row[self.index[0]]

        self.location = None
        self.inventory = ['strawberry ice cream']
        self.victory = 0
        self.beans = 0
        self.player_name = input("Enter a name for your player: ")
        self.has_rock_friend = False

    def inventory_string(self):
        s = 'Items: \n'
        if len(self.inventory) > 0:
            for item in self.inventory:
                s += item + ', '
            s = s[:-2]
        else:
            s += 'Nothing! :)'

        s += f'\nBeans: {self.beans}'

        return s

    def add_beans(self, num_beans):
        self.beans += num_beans

    def remove_beans(self, num_beans):
        self.beans -= num_beans

    def befriend_rock(self):
        self.has_rock_friend = True

    def move_to(self, location):
        self.location = location

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def update_victory(self, victory):
        self.victory = victory

    def get_option(self, options):
        option = None
        while option not in options.keys():
            print('Your options are:')
            for key, value in options.items():
                print('Type ' + key.upper() + ' to ' + value[0])
            print("-" * 40)
            option = input('What is your selection? ').lower()
        return option

    def draw(self):
        self.location.draw()
        print("-" * 40)
        print(self.inventory_string())

    def use_teleporter(self):
        self.move_to(locations.pluto.Pluto(self))
        self.remove_item('teleporter')

    def get_option_letter(self, options):
        option = None
        while option not in options.keys():
            print('Nearby Letters: ')
            for key, value in options.items():
                print('' + '' + value[0])
            option = input('What is your selection? ').lower()
        return option

    def update(self):
        options = self.location.update()
        if 'teleporter' in self.inventory:
            options['teleport'] = ('use the teleporter.',
                                   self.use_teleporter,
                                   'The teleporter took you to Pluto and exploded!')
        print("-" * 40)
        option = self.get_option(options)
        print('\n'*10)
        options[option][1]()
        print(options[option][2])
        if 'L' in self.inventory:
            self.update_victory(1)
