import locations.location
import locations.ice_cream_shop


class Shop(locations.location.Location):
    def __init__(self, state):
        super(Shop, self).__init__(state)

    def draw(self):
        print("I'm in an ice cream shop!")

    def update(self):
        options = {}

        def buy_ice_cream(flavor, cost):
            if self.state.beans >= cost:
                self.state.add_item(f'{flavor} ice cream')
                self.state.remove_beans(cost)
                print(f'{self.state.player_name} got {flavor} ice cream!')
            else:
                print(f'{self.state.player_name} doesn\'t have enough money for that')

        options['vanilla'] = ('buy vanilla ice cream for 15 beans',
                              lambda: buy_ice_cream('vanilla', 15),
                              '')
        options['chocolate'] = ('buy chocolate ice cream for 30 beans',
                                lambda: buy_ice_cream('chocolate', 30),
                                '')
        options['mint'] = ('buy mint chocolate chip ice cream for 90 beans',
                           lambda: buy_ice_cream('chocolate', 90),
                           '')
        options['leave'] = ('leave the store',
                            lambda: self.state.move_to(locations.jupiter.Jupiter(self.state)),
                            f'{self.state.player_name} left the store')

        return options
