class StopwatchModel:
    def __init__(self):
        self.counter = 0
        self.running = False

    def reset(self):
        self.counter = 0
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def get_counter(self):
        return self.counter

    def increment_counter(self):
        self.counter += 1
