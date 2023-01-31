import locations.location
import locations.neptune
import locations.uranus_shop


class Pluto(locations.location.Location):
    def __init__(self, state):
        super(Pluto, self).__init__(state)

    def draw(self):
        print("I'm on pluto")

    def update(self):
        options = {}
        options['neptune'] = ('take a shuttle to Neptune.',
                              lambda: self.state.move_to(locations.neptune.Neptune(self.state)),
                              f'{self.state.player_name} took a shuttle to Neptune.')
        options['uranus'] = ('take a shuttle to Uranus.',
                             lambda: self.state.move_to(locations.uranus.Uranus(self.state)),
                             f'{self.state.player_name} took a shuttle to Uranus')
        if 'artifact' in self.state.inventory:
            options['artifact'] = ('show the artifact off.',
                                   lambda: self.state.add_beans(150),
                                   f"Everyone thinks {self.state.player_name} is really cool! Somebody bought the"
                                   f" artifact for 150 beans!")

        def mine():
            self.state.add_item('ice chunk')
            self.state.remove_item('garbage pickaxe')

        if 'garbage pickaxe' in self.state.inventory:
            options['mine'] = ('mine for resources',
                               mine,
                               f'{self.state.player_name} got an ice chunk, but their pickaxe broke')

        return options
