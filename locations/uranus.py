import locations.location
import locations.uranus
import locations.uranus_shop
import locations.jupiter
import random


class Uranus(locations.location.Location):
    def __init__(self, state):
        super(Uranus, self).__init__(state)

    def draw(self):
        print("I'm on uranus")

    def update(self):
        options = {}
        options['neptune'] = ('take a shuttle to Neptune.',
                              lambda: self.state.move_to(locations.neptune.Neptune(self.state)),
                              f'{self.state.player_name} took a shuttle to Neptune.')
        options['pluto'] = ('take shuttle to Pluto.',
                            lambda: self.state.move_to(locations.pluto.Pluto(self.state)),
                            f'{self.state.player_name} took a shuttle to Pluto')
        options['search'] = ('search for stuff.',
                             lambda: self.state.add_beans(10) if self.state.beans <= 12 else self.state.add_beans(0),
                             f'{self.state.player_name} searched around, you may or may not have found some beans')
        options['shop'] = ('go to the shop.',
                           lambda: self.state.move_to(locations.uranus_shop.Shop(self.state)),
                           f'{self.state.player_name} went to the shop')

        random_num = random.randrange(55, 70, 1)
        if self.state.beans >= random_num:

            def buy_ticket():
                self.state.remove_beans(random_num)
                self.state.move_to(locations.jupiter.Jupiter(self.state))

            options['jupiter'] = (f'buy a ticket to Jupiter for {random_num} beans',
                                  buy_ticket,
                                  f'{self.state.player_name} got a ticket to Jupiter')

        return options
