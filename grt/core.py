class Sensor:
    def __init__(self):
        self.state = {}  # dict, holding previously read sensor values
        self.listeners = set()  # set of listeners

    def __getattr__(self, name):
        if name in self.state:
            return self.state[name]
        return 0

    def __dir__(self):
        return sorted(set(dir(type(self) + self.state.keys())))

    def add_listener(self, l):
        '''
        Add a listener, a method that will be called
        when this sensor's state changes.
        Method has format l(sensor, state_id, datum)
        '''
        self.listeners.add(l)

    def remove_listener(self, l):
        '''
        Remove a listener.
        '''
        self.listeners.remove(l)

    def update_state(self, state_id, datum):
        '''
        Updates the state of this sensor.
        Updates state state_id with data datum.
        Also notifies listeners of state change.
        '''
        if state_id not in self.state or self.state[state_id] != datum:
            self.state[state_id] = datum
            for l in self.listeners:
                l(self, state_id, datum)

    def poll(self):
        '''
        Polls the sensor, notifies any listeners if necessary.
        '''
        pass
