import threading


class AutonomousMode(object):
    """
    Class for executing an autonomous mode. Usually done by executing macros.
    """

    thread = None
    running = False
	
    def __init__(self):
        self.running_macros = set()

    def run_autonomous(self):
        """
        Runs exec_autonomous in a new thread.
        """
        self.thread = threading.Thread(target=self.exec_autonomous)
        self.thread.start()

    def exec_autonomous(self):
        """
        Runs autonomous. This contains exception logic; subclasses
        should override _exec_autonomous.
        """
        self.running = True
        try:
            self._exec_autonomous()
        except StopIteration:
            pass

    def _exec_autonomous(self):
        """
        Runs autonomus. Override this.
        Within this method, don't call macro.run or macro.execute directly, instead,
        call self.run_macro or self.exec_macro in order to keep tabs on them
        and stop the macros when this thread is stopped.
        """
        pass

    def stop_autonomous(self):
        self.running = False
        for macro in self.running_macros:
            macro.kill()
        self.running_macros.clear()

    def exec_macro(self, macro):
        """
        Executes a macro in the current thread.
        Adds macro to self.running_macros when started,
        removes it when finished.

        If autonomous is stopped,
        a StopIteration exception is raised in order to halt
        exec_autonomous.
        """
        if not self.running:
            raise StopIteration()
        self.running_macros.add(macro)
        macro.reset()
        macro.execute()
        if macro in self.running_macros:
            self.running_macros.remove(macro)
        if not self.running:
            raise StopIteration()

    def run_macro(self, macro):
        """
        Runs a macro in a separate thread.
        Returns a handle to the thread.
        """
        thread = threading.Thread(target=self.exec_macro, args=(macro, ))
        thread.start()
        return thread


class MacroSequence(AutonomousMode):
    """
    Class for executing a series of macros sequentially.
    """

    def __init__(self, macros=[]):
        """
        Initializes Controller with an empty list of macros.
        """
        self.macros = macros
        super().__init__()

    def add_macro(self, macro):
        """
        Adds a macro to self.macros.
        """
        self.macros.append(macro)

    def _exec_autonomous(self):
        """
        Iterates through the list of macros, resets them, then runs them sequentially.
        """
        for macro in self.macros:
            self.exec_macro(macro)
