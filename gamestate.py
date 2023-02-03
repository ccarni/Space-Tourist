from colorama import Fore, Style
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
        self.options = {}
        self.option = ""

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
    
    def draw_small_border(self):
        print(Fore.BLACK + '-'*50 + Fore.WHITE)
    
    def draw_large_border(self):
        print(Fore.CYAN + "\n" + '-'*50)
        print('*'*50)
        print('-'*50 + "\n" + Fore.WHITE)

    def draw_options(self):
        print('Your options are:')
        for key, value in self.options.items():
            print('Type ' + key.upper() + ' to ' + value[0])


    def draw(self):
        self.draw_large_border()

        if self.option in self.options:
            print(self.options[self.option][2])
        
        self.location.draw()
        self.draw_small_border()
        print(self.inventory_string())
        self.draw_small_border()
        self.draw_options()

        self.draw_large_border()

    def use_teleporter(self):
        self.move_to(locations.pluto.Pluto(self))
        self.remove_item('teleporter')

    def update(self):
        self.options = self.location.update()

        if 'teleporter' in self.inventory:
            self.options['teleport'] = ('use the teleporter.',
                                   self.use_teleporter,
                                   'The teleporter took you to Pluto and exploded!')
        
        if 'L' in self.inventory:
            self.update_victory(1)

    def execute_input(self):
        self.option = None
        while self.option not in self.options.keys():
            self.option = input('What is your selection? ').lower()
            self.draw()
        
        self.options[self.option][1]()
