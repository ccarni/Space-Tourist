import locations.location
import locations.uranus_shop


class Shop(locations.location.Location):
    def __init__(self, state):
        super(Shop, self).__init__(state)

    def draw(self):
        print("I'm in a shop")

    def update(self):
        options = {}
        options['leave'] = ('leave the shop',
                            lambda: self.state.move_to(locations.uranus.Uranus(self.state)),
                            f'{self.state.player_name} left the shop and are still on Uranus')

        def decent_pick():
            self.state.add_item('garbage pickaxe')
            self.state.remove_beans(10)

        if self.state.beans >= 10:
            options['pickaxe'] = ('Buy a pickaxe for 10 Beans',
                                  decent_pick,
                                  f'{self.state.player_name} got a garbage pickaxe')

        def buy_ice_cream():
            self.state.add_item('strawberry ice cream')
            self.state.remove_beans(3)

        if self.state.beans >= 3:
            options['cream'] = ('Buy strawberry ice cream for 3 Beans',
                                buy_ice_cream,
                                f'{self.state.player_name} got some tasty ice cream')

        def sell_ice_chunk():
            if 'ice chunk' in self.state.inventory:
                self.state.remove_item('ice chunk')
                self.state.add_beans(60)
                print(f'{self.state.player_name} sold an ice chunk for 60 beans')
            else:
                print(f'{self.state.player_name} has no ice chunks')

        options['ice'] = ('sell an ice chunk',
                          sell_ice_chunk,
                          '')
        return options
