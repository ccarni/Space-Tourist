import locations.location
import locations.venus

class Venus(locations.location.Location):
    def __init__(self, state):
        super(Venus, self).__init__(state)

    def draw(self):
        print("I'm on Venus!")

    def update(self):
        options = {}
        options['earth'] = ('take a shuttle to Earth',
                            lambda: self.state.go_to(locations.earth.Earth(self.state)),
                            f'{self.state.player_name} took a shuttle to earth')
        options[saturn] = ('take a shuttle to Saturn',
                            lambda: self.state.go_to(locations.saturn.Saturn(self.state)),
                            f'{self.state.player_name} took a shuttle to Saturn')

        return options
