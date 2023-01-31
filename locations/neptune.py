import locations.location
import locations.crashsite


class Neptune(locations.location.Location):
    def __init__(self, state):
        super(Neptune, self).__init__(state)

    def draw(self):
        print("I'm on Neptune!")

    def update(self):
        options = {}
        options['pluto'] = ('take a shuttle to Pluto.',
                            lambda: self.state.move_to(locations.crashsite.Crashsite(self.state)),
                            f'{self.state.player_name} took a shuttle to Pluto')
        options['uranus'] = ('take a shuttle to Uranus.',
                             lambda: self.state.move_to(locations.uranus.Uranus(self.state)),
                             f'{self.state.player_name} took a shuttle to Uranus')
        if 'teleporter' not in self.state.inventory:
            options['tour'] = ('take a tour.',
                               lambda: self.state.add_item('teleporter'),
                               f'{self.state.player_name} took a cool tour and got a single-use teleporter!')
        return options
