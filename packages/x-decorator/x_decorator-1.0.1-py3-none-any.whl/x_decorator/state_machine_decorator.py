class StateMachine:
    """
    Finite State Machines (FSMs) are a useful tool for
    modeling complex systems that have different states and
    transitions between those states.

    In this example, we define a StateMachine class that can be used to define a set of states
    and transitions between those states.

    We also define a state decorator that can be used to decorate functions that handle individual states.

    To use the FSM,
    we create an instance of the StateMachine class and add our states and transitions using the add_state method.
    We also specify the start state using the set_start method. Finally, we call the run method with an initial cargo value,
    which is passed to each state handler.

    ------------------------------------------------------------------------------------------------------------------
    Here's an example of how to use the FSM:

        @state("STATE1")
        def state1(cargo):
            print("Processing in state1...")
            return ("STATE2", cargo + 1)


        @state("STATE2")
        def state2(cargo):
            print("Processing in state2...")
            if cargo < 10:
                return ("STATE1", cargo + 1)
            else:
                return ("STATE3", cargo)


        @state("STATE3")
        def state3(cargo):
            print("Processing in state3...")
            return ("STATE4", cargo)


        @state("STATE4")
        def state4(cargo):
            print("Processing in state4...")
            return ("STATE1", cargo)


        machine = StateMachine()
        machine.add_state("STATE1", state1)
        machine.add_state("STATE2", state2)
        machine.add_state("STATE3", state3)
        machine.add_state("STATE4", state4, end_state=True)
        machine.set_start("STATE1")

        machine.run(0)
    ------------------------------------------------------------------------------------------------------------------

    In this example,
     we define four states (STATE1, STATE2, STATE3, and STATE4) and decorate each state handler function using the state decorator.
     We then create an instance of the StateMachine class and add our states and transitions using the add_state method.
     We specify the start state using the set_start method, and then call the run method with an initial cargo value of 0.

    When we run this code, we'll see output that shows us which state we're currently in,
    and how the FSM transitions from state to state.
    The FSM will continue to run until it reaches an end state (STATE4 in this case).

    """

    def __init__(self):
        self.handlers = {}
        self.start_state = None
        self.end_states = []

    def add_state(self, name, handler, end_state=False):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.end_states.append(name)

    def set_start(self, name):
        self.start_state = name.upper()

    def run(self, cargo):
        handler = self.handlers[self.start_state]
        while True:
            (new_state, cargo) = handler(cargo)
            if new_state.upper() in self.end_states:
                print("Reached", new_state)
                break
            else:
                handler = self.handlers[new_state.upper()]


def state(name):
    def decorator(func):
        def wrapper(cargo):
            print("Entering state", name)
            result = func(cargo)
            print("Leaving state", name)
            return result

        return wrapper

    return decorator
