import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

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

        for f in (StartPage, GraphPage):
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

        button1 = ttk.Button(self, text = "Show Graph",
                            command = lambda: controller.show_frame(GraphPage))
        button1.pack()

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Graph Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = "Back to Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

        controller.data.add_csv("DATA_01_05_Cow_42.csv")
        controller.data.add_csv("DATA_01_05_Cow_42.csv")

        accels_x = controller.data.getAccel(42,'acc_x_g')
        accels_y = controller.data.getAccel(42,'acc_y_g')
        coords = controller.plotter.plotter_math(42)

        coords_x = []
        coords_y = []
        for coord in coords:
            coords_x.append(coord[0])
            coords_y.append(coord[1])

        f = Figure()
        a = f.add_subplot(111)

        a.plot(coords_x, coords_y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
