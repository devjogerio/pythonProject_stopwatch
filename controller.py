class StopwatchController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.start_button.config(command=self.start)
        self.view.stop_button.config(command=self.stop)
        self.view.reset_button.config(command=self.reset)
        self.update_display()

    def start(self):
        if not self.model.running:
            self.model.start()
            self.update_counter()

    def stop(self):
        if self.model.running:
            self.model.stop()

    def reset(self):
        self.model.reset()
        self.update_display()

    def update_counter(self):
        if self.model.running:
            self.model.increment_counter()
            self.update_display()
            self.view.root.after(1000, self.update_counter)

    def update_display(self):
        display = self.format_time(self.model.counter)
        self.view.label.config(text=display)

    @staticmethod
    def format_time(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"
