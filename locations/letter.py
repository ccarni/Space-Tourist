import locations.location
import locations.neptune


class Letter(locations.location.Location):

    def __init__(self, state):
        super(Letter, self).__init__(state)
        self.state = self.state
        self.state.row = self.state.rows[self.state.index[1]]
        self.state.letter = self.state.row[self.state.index[0]]


    def check_wall(self, char):
        wall_character = "="
        if char == wall_character:
            print(char + " = " + wall_character)
            return True
        return False

    def getChar(self, h, v, state):
        try:
            if self.state.index[1] + v > -1 and self.state.index[1] + v < len(self.state.rows):
                if self.state.index[0] - h > -1 and self.state.index[0] - h < len(self.state.row):
                    char = self.state.rows[self.state.index[1] - v][self.state.index[0] + h]
                else:
                    char = "_"
            else:
                char = "_"
        except:
            char = "_"
        return char

    def up(self, state, get=True):
        newstate = self.state
        newLoc = ""
        if self.state.index[1] - 1 > -1:
            if (get):
                return self.state.rows[self.state.index[1] - 1][self.state.index[0]]
            newLoc = self.state.rows[self.state.index[1] - 1][self.state.index[0]]
            newstate.index[1] = self.state.index[1] - 1
            newstate.row = self.state.rows[self.state.index[1] - 1]
            newstate.letter = newLoc
            if self.check_wall(newLoc):
                newLoc = self.state.letter
                newstate.index[1] = self.state.index[1] + 1
        return newLoc, newstate

    def down(self, state, get=True):
        newstate = self.state
        newLoc = ""
        # print('self.state.index[1] + 1 = ' + str(self.state.index[1] + 1))
        # print('len(self.state.rows) = ' + str(len(self.state.rows)))
        if self.state.index[1] + 1 < len(self.state.rows):
            if (get):
                return self.state.rows[self.state.index[1] + 1][self.state.index[0]]
            newLoc = self.state.rows[self.state.index[1] + 1][self.state.index[0]]
            newstate.index[1] = self.state.index[1] + 1
            newstate.row = self.state.rows[newstate.index[1]]
            newstate.letter = newLoc
            if self.check_wall(newLoc):
                newLoc = self.state.letter
                newstate.index[1] = self.state.index[1] - 1
        return newLoc, newstate

    def right(self, state, get=True):

        newstate = self.state
        newLoc = ""

        if self.state.index[0] + 1 != len(self.state.row):
            if (get):
                return self.state.rows[self.state.index[1]][self.state.index[0] + 1]
            newLoc = self.state.rows[self.state.index[1]][self.state.index[0] + 1]
            newstate.index[0] = self.state.index[0] + 1
            newstate.letter = newLoc
            if self.check_wall(newLoc):
                newLoc = self.state.letter
                newstate.index[0] = self.state.index[0] - 1
                print("You've hit a wall.")
                return "", self.state
        return newLoc, newstate

    def left(self, state, get=True):
        newstate = self.state
        newLoc = ""
        if self.state.index[0] - 1 != -1:
            if (get):
                return self.state.rows[self.state.index[1]][self.state.index[0] - 1]
            newLoc = self.state.rows[self.state.index[1]][self.state.index[0] - 1]
            newstate.index[0] = self.state.index[0] - 1
            newstate.letter = newLoc
            if self.check_wall(newLoc):
                newLoc = self.state.letter
                newstate.index[0] = self.state.index[0] + 1
        return newLoc, newstate

    def draw(self):
        print("I'm on pluto")

    def update(self):
        wall_character = "="

        options = {}
        self.state.row = self.state.rows[self.state.index[1]]
        self.state.letter = self.state.row[self.state.index[0]]

        previous_letter = self.state.letter
        options['up'] = (
        self.getChar(-1, -1, self.state) + ' ' + self.getChar(0, -1, self.state) + ' ' + self.getChar(1, -1, self.state),
        lambda: self.state.move_to(locations.letter.Letter(self.up(self.state, False)[1])),
        'You took a shuttle to ' + self.up(self.state)[0] + '.')
        options['left'] = ('' + self.left(self.state)[0] + ' ' + previous_letter + ' ' + self.right(self.state)[0],
                           lambda: self.state.move_to(locations.letter.Letter(self.left(self.state, False)[1])),
                           'You took a shuttle to ' + self.left(self.state)[0] + '.')
        options['down'] = (
        self.getChar(-1, 1, self.state) + ' ' + self.getChar(0, 1, self.state) + ' ' + self.getChar(1, 1, self.state),
        lambda: self.state.move_to(locations.letter.Letter(self.down(self.state, False)[1])),
        'You took a shuttle to ' + self.down(self.state)[0] + '.')
        options['right'] = ('' + '',
                            lambda: self.state.move_to(locations.letter.Letter(self.right(self.state, False)[1])),
                            'You took a shuttle to ' + self.right(self.state)[0] + '.')
        options['grab'] = ('[grab]',
                           lambda: self.state.add_item(previous_letter),
                           'You took a shuttle to ' + self.right(self.state)[0] + '.')

        options['leave'] = ('leave',
                            lambda: self.state.move_to(locations.jupiter.Jupiter(self.state)),
                            'left')
        return options
