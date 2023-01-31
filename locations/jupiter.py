import locations.location
import locations.jupiter
import locations.ice_cream_shop
import locations.saturn
import locations.letter
import random


class Jupiter(locations.location.Location):
    def __init__(self, state):
        super(Jupiter, self).__init__(state)

    def draw(self):
        print("I'm on Jupiter")

    def update(self):
        options = {}
        options['rock'] = ('observe an interesting rock',
                           lambda: self.state.move_to(locations.rock_encounter.Rock(self.state)),
                           f'{self.state.player_name} observes the rock')

        if random.random() <= 0.3:
            options['pickup'] = ('pickup a strange item in the trash',
                                 lambda: self.state.add_item('gas mask'),
                                 f'{self.state.player_name} got a gas mask!')

        options['shop'] = ('go to the ice cream shop',
                           lambda: self.state.move_to(locations.ice_cream_shop.Shop(self.state)),
                           f'{self.state.player_name} has gone in the ice cream shop')

        if 'gas mask' in self.state.inventory:
            options['saturn'] = ('take a shuttle to saturn with your gas mask',
                                 lambda: self.state.move_to(locations.saturn.Saturn(self.state)),
                                 f'{self.state.player_name} has arrived at saturn')

        options['minigame'] = ('minigame',
                             lambda: self.state.move_to(locations.letter.Letter(self.state)),
                             'you do the minigame')

        return options
