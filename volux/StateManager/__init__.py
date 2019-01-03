### DEFINE STATE MANAGER
class StateManager:
    def __init__(self,initial_state):
        self.state = initial_state
    def change_state(self,new_state): # request to change states
        self.state().vacate()
        new_state().enter()
        self.state = new_state