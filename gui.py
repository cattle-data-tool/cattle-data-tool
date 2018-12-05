import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import filedialog

from collections import namedtuple

import os

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
        self.controller = controller
        self.parent = parent

        tk.Frame.__init__(self, self.parent)

        self.header = ['ID', 'External ID', 'Internal ID', 'Day', 'Month', 'File Name']
        self.data = []

        self.table = Table(self.header, self.data)

        menubar = tk.Menu(self.controller)

        filemenu = tk.Menu(menubar, tearoff = 0)
        filemenu.add_command(
            label = "Save Workspace",
            command = lambda: self.save_workspace())
        filemenu.add_command(
            label = "Load Workspace",
            command = lambda: self.load_workspace())
        filemenu.add_separator()
        filemenu.add_command(
            label = "Exit",
            command = lambda: self.exit())
        menubar.add_cascade(label = "File", menu = filemenu)

        datamenu = tk.Menu(menubar, tearoff = 0)
        datamenu.add_command(
            label = "Import CSV",
            command = lambda: self.import_csv())
        datamenu.add_command(
            label = "Remove Selected",
            command = lambda: self.remove_selected())
        datamenu.add_command(
            label = "Plot Selected",
            command = lambda: self.plot_selected())
        menubar.add_cascade(label = "Data", menu = datamenu)

        selectmenu = tk.Menu(menubar, tearoff = 0)
        selectmenu.add_command(
            label = "Select All",
            command = lambda: self.select_all())
        selectmenu.add_command(
            label = "Select None",
            command = lambda: self.select_none())
        menubar.add_cascade(label = "Select", menu = selectmenu)

        helpmenu = tk.Menu(menubar, tearoff = 0)
        helpmenu.add_command(
            label = "Open Documentation",
            command = lambda: self.open_documentation())
        menubar.add_cascade(label = "Help", menu = helpmenu)

        tk.Tk.config(self.controller, menu = menubar)

        self.table.container.pack(fill = tk.BOTH, expand = True)

    def save_workspace(self):
        filename =  filedialog.asksaveasfilename(
            title = "Save Workspace", filetypes = (("cattle data file","*.cdf"),))
        self.controller.data.export_db(filename)

    def load_workspace(self):
        filename =  filedialog.askopenfilename(
            title = "Load Workspace", filetypes = (("cattle data file","*.cdf"),))
        self.data = self.controller.data.load_db(filename)
        self.table.update_tree(self.data)

    def exit(self):
        self.controller.destroy()

    def import_csv(self):
        filenames =  filedialog.askopenfilenames(
            title = "Load Workspace", filetypes = (("comma-seperated values file","*.csv"),))
        for filename in filenames:
            self.data.append(self.controller.data.add_csv(filename))
        self.table.update_tree(self.data)

    def remove_selected(self):
        for (iid, id) in self.table.get_selected_ids():
            self.table.tree.delete(iid)
            self.controller.data.remove_by_id(id)

            for data in self.data:
                if data[0] == id:
                    self.data.remove(data)

    def plot_selected(self):
        Curve = namedtuple('Curve', 'x y')
        curve_list = []
        for (iid, id) in self.table.get_selected_ids():
            x, y = self.controller.plotter.plot(id)
            curve_list.append(Curve(x, y))
        display_graph(curve_list)

    def select_all(self):
        iids = self.table.tree.get_children()
        self.table.tree.selection_set(iids)

    def select_none(self):
        iids = self.table.tree.get_children()
        self.table.tree.selection_remove(iids)

    def open_documentation(self):
        popupmsg("Not Implemented Yet")

class Table:
    def __init__(self, header, data):
        self.header = header
        self.data = data
        self.tree = None
        self.setup_widgets()
        self.build_tree()

    def update_tree(self, data):
        self.data = data
        for item in self.tree.get_children():
            self.tree.delete(item)

        for item in self.data:
            self.tree.insert('', 'end', values = item)

    def get_selected_ids(self):
        iids = self.tree.selection()
        list = []
        for iid in iids:
            list.append((iid, int(self.tree.item(iid, 'values')[0])))
        return list

    def setup_widgets(self):
        self.container = ttk.Frame()

        self.tree = ttk.Treeview(columns = self.header, show = "headings", height = 50)
        vertical_scrollbar = ttk.Scrollbar(orient = "vertical",
                                       command = self.tree.yview)
        horizontal_scrollbar = ttk.Scrollbar(orient = "horizontal",
                                             command = self.tree.xview)

        self.tree.configure(yscrollcommand = vertical_scrollbar.set,
                            xscrollcommand = horizontal_scrollbar.set)

        self.tree.grid(column = 0, row = 0, sticky = 'nsew', in_ = self.container)

        vertical_scrollbar.grid(column = 1, row = 0, sticky = 'ns', in_ = self.container)
        horizontal_scrollbar.grid(column = 0, row = 1, sticky = 'ew', in_ = self.container)

        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

    def build_tree(self):
        for col in self.header:
            self.tree.heading(col, text = col.title(),
                              command = lambda c = col: self.sortby(self.tree, c, 0))

            self.tree.column(col,
                             width = tkFont.Font().measure(col.title()))

        for item in self.data:
            self.tree.insert('', 'end', values = item)

        sample = (6081, 2112, 30104665, 21, 21, 'DATA_02_02_Cow_6108.csv')

        for x, val in enumerate(sample):
            col_w = tkFont.Font().measure(val)
            if self.tree.column(self.header[x], width = None) < col_w:
                self.tree.column(self.header[x], width = col_w)

    def sortby(self, tree, col, descending):
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(key = self.tupleToInt, reverse = descending)
        for x, item in enumerate(data):
            tree.move(item[1], '', x)
        tree.heading(col, command = lambda col = col: self.sortby(
            tree, col, int(not descending)))

    def tupleToInt(self, tup):
        try:
            tupInt = (int(tup[0]), tup[1])
            return tupInt
        except:
            return tup
