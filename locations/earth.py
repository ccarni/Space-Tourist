import locations.location
import locations.earth
import locations.venus


class Earth(locations.location.Location):
    def __init__(self, state):
        super(Earth, self).__init__(state)

    def draw(self):
        print("I'm on Earth!")

    def update(self):
        options = {}
        options['venus'] = ('take a shuttle to Venus',
                            lambda: self.state.go_to(locations.venus.Venus(self.state)),
                            f'{self.state.player_name} took a shuttle to venus')
        options['mars'] = ('take a shuttle to Mars',
                            lambda: self.state.go_to(locations.mars.Mars(self.state)),
                            f'{self.state.player_name} took a shuttle to Mars')

        return options
