from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from Parser import validInt, parseEquation
from graphPlotter import GraphPlotter

class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("Function Plotter")

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                parent.withdraw()
                quit()
        parent.protocol("WM_DELETE_WINDOW", on_closing)

        # this will create a label widget
        l1 = Label(root, text = "Min X")
        l2 = Label(root, text = "Max X")
        l3 = Label(root, text = "Equation of X")

        # grid method to arrange labels in respective
        # rows and columns as specified
        l1.grid(row = 0, column = 0, sticky = N, pady = 2)
        l2.grid(row = 0, column = 1, sticky = N, pady = 2)
        l3.grid(row = 0, column = 2, sticky = N, pady = 2)

        # entry widgets, used to take entry from user
        minXEntry = Entry(parent)
        maxXEntry = Entry(parent)
        equationEntry = Entry(parent)

        # this will arrange entry widgets
        minXEntry.grid(row = 1, column = 0, pady = 2)
        maxXEntry.grid(row = 1, column = 1, pady = 2)
        equationEntry.grid(row = 1, column = 2, pady = 2 ,ipadx= 40)

        #Graph widget
        graphPlotter= GraphPlotter()
        figure1 = graphPlotter.plott()
        canvas = FigureCanvasTkAgg(figure1, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 2, column = 0,
               columnspan = 4, rowspan = 2, padx = 5, pady = 5)


        def plotAction():
            try:
                graphPlotter.minX = validInt(minXEntry.get())
                graphPlotter.maxX = validInt(maxXEntry.get())
                graphPlotter.equation = parseEquation(equationEntry.get())
                graphPlotter.plottEquation=True

                figure1 = graphPlotter.plott()

                canvas = FigureCanvasTkAgg(figure1, master=parent)
                canvas.draw()
                canvas.get_tk_widget().grid(row=2, column=0,
                                            columnspan=4, rowspan=2, padx=5, pady=5)
            except TypeError as error:
                messagebox.showerror("Error in input",str(error))


        # button widget
        b1 = Button(root, text = "Plot",command=plotAction)
        b1.grid(row = 1, column = 3, sticky = W, columnspan = 2)
        parent.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.title("Function Plotter");

    MainApplication(root).pack(side="top", fill="both", expand=True)


