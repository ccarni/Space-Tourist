import locations.location
import locations.mars
import locations.earth


class Mars(locations.location.Location):
    def __init__(self, state):
        super(Mars, self).__init__(state)

    def draw(self):
        print("I'm on Mars!")

    def update(self):
        options = {}
        options['earth'] = ('take a shuttle to Earth',
                            lambda: self.state.go_to(locations.earth.Earth(self.state)),
                            f'{self.state.player_name} took a shuttle to Earth')
        options['saturn'] = ('take a shuttle to Saturn',
                            lambda: self.state.go_to(locations.saturn.Saturn(self.state)),
                            f'{self.state.player_name} took a shuttle to Saturn')

        return options
