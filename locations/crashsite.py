import locations.location


class Crashsite(locations.location.Location):
    def __init__(self, state):
        super(Crashsite, self).__init__(state)

    def draw(self):
        print("The shuttle crashed onto an asteroid! :(")

    def update(self):
        options = {}
        if 'scrap' not in self.state.inventory:
            options['fix'] = ('try to fix the shuttle.',
                              lambda: self.state.add_item('scrap'),
                              f"{self.state.player_name} doesn't have the right tools to fix the shuttle but they did "
                              f"pick up some scrap. :(")

        if 'artifact' not in self.state.inventory:
            options['search'] = ('look around for anything neat.',
                                 lambda: self.state.add_item('artifact'),
                                 f'{self.state.player_name} found a cool artifact!')
        else:
            options['search'] = ('look around for anything neat.',
                                 lambda: None,
                                 "There doesn't seem to be anything else. :(")

        if 'scrap' in self.state.inventory and 'teleporter' not in self.state.inventory:
            
            def alien_abduction():
                if self.state.has_rock_friend:
                    print(f'the rock comes to save {self.state.player_name} and brings you to jupiter')
                    self.state.move_to(locations.jupiter.Jupiter(self.state))
                else:
                    print(f'{self.state.player_name} got abducted by aliens.')
                    self.state.update_victory(-1)

            options['wait'] = ('wait for rescue.',
                               alien_abduction(),
                               '')
        return options
