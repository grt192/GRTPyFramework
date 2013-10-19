import threading
import time

class Sensor:
    def __init__(self):
        self.state = {}  # dict, holding previously read sensor values
        self.listeners = set()  # set of listeners

    def __getattr__(self, name):
        if name in self.state:
            return self.state[name]
        return 0

    def get(self, name):
        '''
        Returns the datum associated with some name.
        '''
        return self.state[name]

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
        Also notifies listeners of state change (on change, not add).
        '''
        if state_id in self.state and self.state[state_id] != datum:
            self.state[state_id] = datum
            for l in self.listeners:
                l(self, state_id, datum)

    def poll(self):
        '''
        Polls the sensor, notifies any listeners if necessary.
        '''
        pass

class SensorPoller:
    '''
    Class that periodically polls sensors.
    '''
    def __init__(self, polltime=0.01, sensors=[]):
        '''
        Sets the polltime (in seconds) and the initial list of sensors.
        '''
        self.sensors = sensors
        self.polltime = polltime

    def add_sensor(sensor):
        '''
        Adds a sensor to poll.
        '''
        sensors.append(sensor)

    def remove_sensor(sensor):
        '''
        Removes a sensor.
        '''
        sensors.remove(sensor)

    def halt(self):
        '''
        Stops this thread from polling.
        '''
        self.running = False

    def start(self):
        '''
        Starts polling.
        '''
        self.running = True
        self.t = threading.Thread(target=self._run)

    def _run(self):
        while self.running:
            for sensor in self.sensors:
                sensor.poll()
            time.sleep(self.polltime)

class Constants(Sensor):
    '''
    Class for reading, and keeping track of, constants in a file.

    File is read line by line, in [key],[number] format.
    Lines starting with '/' are treated as add'l constants files,
    and are read recursively.
    Blank lines, and lines starting with '#' are ignored.

    Behaves more or less like a sensor.
    '''

    def __init__(file_loc='/c/constants.txt'):
        self.file_loc = file_loc

    def poll(self):
        '''
        Reloads file data.
        '''
        self.load_file(self.file_loc)

    def load_file(file_loc):
        '''
        Loads file data from a file.
        If other files are listed inside this file,
        recursively loads them.

        (Beware of "include loops" that will cause a crash)
        '''
        f = open(file_loc)
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('/'):  # is a file, load it!
                self.load_file(line)
                continue
            # continue with getting data
            key, _, value = line.partition(',')
            try:
                self.update_state(key, float(value))
            except ValueError:
                print("Malformed constants file " + file_loc +
                      " with key " + key + " and value " + value)
        f.close()

