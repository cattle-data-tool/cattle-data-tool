import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class Gui(tk.Tk):
    def __init__(self, data, plotter, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for f in (StartPage, PageOne, PageTwo):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Hello, Gui!", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Visit Page 1",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text = "Visit Page 2",
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page One", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text = "Show Page Two",
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page Two", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text = "Show Page One",
                            command = lambda: controller.show_frame(PageOne))
        button2.pack()
