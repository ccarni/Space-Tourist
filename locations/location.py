class Location:
    def __init__(self, state):
        self.state = state
        pass

    def draw(self):
        raise Exception("Encountered Location's draw function rather than a subclasses'.")

    def update(self):
        raise Exception("Encountered Location's update function rather than a subclasses'.")


