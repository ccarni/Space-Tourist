import locations.location
import locations.mercury


class Mercury(locations.location.Location):
    def __init__(self, state):
        super(Mercury, self).__init__(state)

    def draw(self):
        print("I'm on Mercury!")

    def update(self):
        options = {}

        return options
