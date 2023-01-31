import gamestate
from locations.pluto import Pluto

def get_new_state():
    new_state = gamestate.Gamestate()
    new_state.location = Pluto(new_state)
    return new_state


state = get_new_state()

while state.victory == 0:
    state.draw()
    state.update()

if state.victory == 1:
    print('Nice job, you won.')
    state = get_new_state()
elif state.victory == -1:
    print('You lost, rip.')
    state = get_new_state()

