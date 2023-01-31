import locations.location
import locations.sun


class Sun(locations.location.Location):
    def __init__(self, state):
        super(Sun, self).__init__(state)

    def draw(self):
        print("I'm on a Sun!")

    def update(self):
        options = {}

        return options
