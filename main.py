import tkinter as Tkinter
from model import StopwatchModel
from view import StopwatchView
from controller import StopwatchController


def main():
    root = Tkinter.Tk()
    model = StopwatchModel()
    view = StopwatchView(root)
    controller = StopwatchController(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()
