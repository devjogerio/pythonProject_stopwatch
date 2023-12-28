import tkinter as Tkinter

class StopwatchView:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.minsize(width=250, height=70)

        self.label = Tkinter.Label(self.root, text='Ready!', fg='black', font='Verdana 30 bold')
        self.label.pack()

        self.frame = Tkinter.Frame(self.root)
        self.start_button = Tkinter.Button(self.frame, text='Start', width=6)
        self.stop_button = Tkinter.Button(self.frame, text='Stop', width=6, state='disabled')
        self.reset_button = Tkinter.Button(self.frame, text='Reset', width=6, state='disabled')

        self.start_button.pack(side='left')
        self.stop_button.pack(side='left')
        self.reset_button.pack(side='left')
        self.frame.pack(anchor='center', pady=5)
