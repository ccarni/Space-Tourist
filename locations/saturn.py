import locations.location
import locations.saturn
import locations.mars


class Saturn(locations.location.Location):
    def __init__(self, state):
        super(Saturn, self).__init__(state)

    def draw(self):
        print("I'm on Saturn!")

    def update(self):
        options = {}
        options['mars'] = ('take a shuttle to mars',
                           lambda: self.state.move_to(locations.mars.Mars(self.state)),
                           f'{self.state.player_name} took a shuttle to mars')
        options['jupiter'] = ('take a shuttle to Jupiter',
                            lambda: self.state.go_to(locations.jupiter.Jupiter(self.state)),
                            f'{self.state.player_name} took a shuttle to jupiter')

        return options
