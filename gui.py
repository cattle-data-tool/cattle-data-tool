import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

from collections import namedtuple

LARGE_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 10)

def popupmsg(msg):
    popup = tk.Tk()

    def leavemini():
        popup.destroy()

    popup.title("Notification")
    label = ttk.Label(popup, text = msg, font = LARGE_FONT)
    label.pack(side = "top", fill = "x", pady = 10, padx = 20)

    b1 = ttk.Button(popup, text = "Okay", command = leavemini)
    b1.pack(pady = 10, padx = 20)
    popup.mainloop()

def display_graph(curve_list):
    graph_page = tk.Toplevel()
    graph_page.title("Movement Graph")
    icon_img = tk.Image("photo", file="icon.png")
    graph_page.tk.call('wm','iconphoto',graph_page._w, icon_img)

    f = Figure()
    a = f.add_subplot(111)

    for curve in curve_list:
        a.plot(curve.x, curve.y)

    canvas = FigureCanvasTkAgg(f, graph_page)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

    toolbar = NavigationToolbar2Tk(canvas, graph_page)
    toolbar.update()
    canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

    graph_page.mainloop()


class Gui(tk.Tk):
    def __init__(self, data, plotter, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.data = data
        self.plotter = plotter

        self.title("Cattle Data Tool")
        icon_img = tk.Image("photo", file="icon.png")
        self.tk.call('wm','iconphoto',self._w, icon_img)

        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        menubar = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(label = "Save Workspace", command = lambda: popupmsg("Not Implemented Yet"))
        filemenu.add_command(label = "Load Workspace", command = lambda: popupmsg("Not Implemented Yet"))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.destroy)
        menubar.add_cascade(label = "File", menu = filemenu)

        datamenu = tk.Menu(menubar, tearoff = 0)
        datamenu.add_command(label = "Import CSV", command = lambda: popupmsg("Not Implemented Yet"))
        datamenu.add_command(label = "Remove Selected", command = lambda: popupmsg("Not Implemented Yet"))
        datamenu.add_command(label = "Plot Selected", command = lambda: popupmsg("Not Implemented Yet"))
        menubar.add_cascade(label = "Data", menu = datamenu)

        selectmenu = tk.Menu(menubar, tearoff = 0)
        selectmenu.add_command(label = "Select All", command = lambda: popupmsg("Not Implemented Yet"))
        selectmenu.add_command(label = "Select None", command = lambda: popupmsg("Not Implemented Yet"))
        menubar.add_cascade(label = "Select", menu = selectmenu)

        helpmenu = tk.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = "Open Documentation", command = lambda: popupmsg("Not Implemented Yet"))
        menubar.add_cascade(label = "Help", menu = helpmenu)

        tk.Tk.config(self, menu = menubar)

        self.frames = {}

        for f in (StartPage,):
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

        # TODO: fix windows file paths
        controller.data.add_csv("DATA_01_05_Cow_42.csv")
        controller.data.add_csv(".xml files/DATA_01_05_Cow_195.csv")
        controller.data.add_csv(".xml files/DATA_01_05_Cow_345.csv")
        controller.data.add_csv(".xml files/DATA_01_05_Cow_407.csv")

        ids = [345, 42, 195, 407]

        Curve = namedtuple('Curve', 'x y')

        curve_list = []

        for id in ids:
            coords_x, coords_y = controller.plotter.plot(id)
            curve_list.append(Curve(coords_x, coords_y))

        button1 = ttk.Button(self, text = "Show Graph",
                                    command = lambda: display_graph(curve_list))
        button1.pack()
