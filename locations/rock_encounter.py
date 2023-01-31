import locations.location
import locations.rock_encounter

class Rock(locations.location.Location):
    def __init__(self, state):
        self.state = state

    def draw(self):
        print("A Rock Approaches...\n"
              f"It tells {self.state.player_name} that it likes strawberries")

    def update(self):
        options = {}
        options['avoid'] = ('avoid the rock',
                            lambda: self.state.move_to(locations.jupiter.Jupiter(self.state)),
                            f'{self.state.player_name} avoids this rock')
        if 'strawberry ice cream' in self.state.inventory:
            def give_ice_cream():
                self.state.remove_item('strawberry ice cream')
                self.state.befriend_rock()
                self.state.move_to(locations.jupiter.Jupiter(self.state))

            options['give']  = ('give the rock some strawberry ice cream',
                                give_ice_cream,
                                f'{self.state.player_name} gave the rock some ice cream, it seems happy')

        return options